# coding= utf-8 

# gapfill raster
# --------------------------------------------

#!/usr/bin/env python3

import sys
import copy
import grass.script as gscript
import grass.temporal as tgis
from datetime import datetime

# -------------------settings-----------------
env = gscript.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False  
env['GRASS_MESSAGE_FORMAT'] = 'standard'
location = env['LOCATION_NAME']
mapset = env['MAPSET']

#------------------------------Gap Filling---------

# % description: Replaces gaps in a space time raster dataset with interpolated raster maps.
# % keyword: temporal
# % keyword: interpolation
# % keyword: raster
# % keyword: time
# % keyword: no-data filling
# %end

def main():
    import grass.pygrass.modules as pymod

    # Get the options
    #input = 'GHS_'
    #base = 'GHS_'
    input = 'Grump_'
    base = 'Grump_'
    where = None
    nprocs = 4
    tsuffix = 'gran'

    # mapset shoule be preset

    # Make sure the temporal database exists

    tgis.init()

    # We need a database interface

    dbif = tgis.SQLDatabaseInterfaceConnection()

    dbif.connect()

    sp = tgis.open_old_stds(input, "strds")

    maps = sp.get_registered_maps_as_objects_with_gaps(where=None, dbif = None)

    num = len(maps)


    # Configure the r.to.vect module

    gapfill_module = pymod.Module(

        "r.series.interp",

        overwrite=gscript.overwrite(),

        quiet=True,

        run_=False,

        finish_=False,



    )


    process_queue = pymod.ParallelModuleQueue(int(nprocs))

    gap_list = []

    overwrite_flags = {}


    # Identify all gaps and create new names

    count = 0

    for _map in maps:

        if _map.get_id() is None:

            count += 1

            if sp.get_temporal_type() == "absolute" and tsuffix in ["gran", "time"]:

                _id = "{ba}@{ma}".format(ba=base, ma=mapset)

            else:

                map_name = tgis.create_numeric_suffix(base, num + count, tsuffix)

                _id = "{name}@{ma}".format(name=map_name, ma=mapset)

            _map.set_id(_id)


            gap_list.append(_map)



    if len(gap_list) == 0:

        gscript.message(_("No gaps found"))

        return


    # Build the temporal topology

    tb = tgis.SpatioTemporalTopologyBuilder()

    tb.build(maps)



    # Do some checks before computation

    for _map in gap_list:

        if not _map.get_precedes() or not _map.get_follows():

            gscript.fatal(_("Unable to determine successor " "and predecessor of a gap."))

        if len(_map.get_precedes()) > 1:

            gscript.warning(

                _("More than one successor of the gap found. " "Using the first found.")

            )


        if len(_map.get_follows()) > 1:

            gscript.warning(

                _(
                    "More than one predecessor of the gap found. "

                    "Using the first found."
                )

            )


    # Interpolate the maps using parallel processing


    result_list = []


    for _map in gap_list:

        predecessor = _map.get_follows()[0]
        successor = _map.get_precedes()[0]

        gran = sp.get_granularity()

        tmpval, start = predecessor.get_temporal_extent_as_tuple()

        end, tmpval = successor.get_temporal_extent_as_tuple()

        # Now resample the gap

        map_matrix = tgis.AbstractSpaceTimeDataset.resample_maplist_by_granularity(

            (_map,), start, end, gran

        )


        map_names = []

        map_positions = []

        increment = 1.0 / (len(map_matrix) + 1.0)

        position = increment

        count = 0

        for intp_list in map_matrix:

            new_map = intp_list[0]

            count += 1

            if sp.get_temporal_type() == "absolute" and tsuffix == "gran":

                suffix = tgis.create_suffix_from_datetime(

                    new_map.temporal_extent.get_start_time(), sp.get_granularity()
                )

                new_id = "{ba}_{su}@{ma}".format(

                    ba=new_map.get_name(), su=suffix, ma=mapset

                )

            elif sp.get_temporal_type() == "absolute" and tsuffix == "time":

                suffix = tgis.create_time_suffix(new_map)

                new_id = "{ba}_{su}@{ma}".format(

                    ba=new_map.get_name(), su=suffix, ma=mapset
                )


            else:

                map_name = tgis.create_numeric_suffix(

                    new_map.get_name(), count, tsuffix

                )

                new_id = "{name}@{ma}".format(name=map_name, ma=mapset)



            new_map.set_id(new_id)

            overwrite_flags[new_id] = False

            if new_map.map_exists() or new_map.is_in_db(dbif):

                if not gscript.overwrite():

                    gscript.fatal(

                        _(

                            "Map with name <%s> already exists. "

                            "Please use another base name." % (_id)

                         )

                    )


                else:

                    if new_map.is_in_db(dbif):

                        overwrite_flags[new_id] = True


            map_names.append(new_map.get_name())

            map_positions.append(position)

            position += increment

            result_list.append(new_map)



        mod = copy.deepcopy(gapfill_module)


        mod(

            input=(predecessor.get_map_id(), successor.get_map_id()),

            datapos=(0, 1),

            output=map_names,

            samplingpos=map_positions,

        )


        sys.stderr.write(mod.get_bash() + "\n")

        process_queue.put(mod)




    # Wait for unfinished processes

    process_queue.wait()




    # Insert new interpolated maps in temporal database and dataset

    for _map in result_list:

        id = _map.get_id()

        if overwrite_flags[id]:

            if _map.is_time_absolute():

                start, end = _map.get_absolute_time()

                if _map.is_in_db():

                    _map.delete(dbif)

                _map = sp.get_new_map_instance(id)

                _map.set_absolute_time(start, end)

            else:

                start, end, unit = _map.get_relative_time()

                if _map.is_in_db():

                    _map.delete(dbif)

                _map = sp.get_new_map_instance(id)

                _map.set_relative_time(start, end, unit)

        _map.load()

        _map.insert(dbif)

        sp.register_map(_map, dbif)



    sp.update_from_registered_maps(dbif)

    sp.update_command_string(dbif=dbif)

    dbif.close()



###############################################################################


def run_interp(inputs, dpos, output, outpos):

    """Helper function to run r.series.interp in parallel"""

    return gscript.run_command(

        "r.series.interp",

        input=inputs,

        datapos=dpos,

        output=output,

        samplingpos=outpos,

        overwrite=gscript.overwrite(),

        quiet=True,

    )




if __name__ == "__main__":

    options, flags = gscript.parser()

    main()