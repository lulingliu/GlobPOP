# coding=utf-8
#!/usr/bin/env python3


# Extrapolate Gpwv4 from 1990 to 2000



import grass.script as gscript


def main():


    # -------------------settings-----------------



    env = gscript.gisenv()



    overwrite = True



    env['GRASS_OVERWRITE'] = overwrite



    env['GRASS_VERBOSE'] = False



    env['GRASS_MESSAGE_FORMAT'] = 'standard'



    location = env['LOCATION_NAME']



    mapset = env['MAPSET']







    # ------------Raster Maps Calculation------------

    # list rasters in mapset

    #raster_list = gscript.list_grouped('rast',pattern='GHS_POP*')[mapset]
    raster_list= gscript.list_grouped('rast',pattern='gpw_v4_pop*')[mapset]

    for raster in raster_list[1:3]:

        raster_name= str(raster)

        year=raster_name[9:13]

        print(raster_name," year:",year)

    # Delta Y -average pop growth


    output_raster='gpw_Delta_Y_05_00'


    input1 = str(raster_list[1]) # Year of 2005

    input2 = str(raster_list[0]) # Year of 2000

    gscript.mapcalc('{o}=({a}-{b})/5'.format(o=output_raster,a=input1,b=input2))

    gscript.read_command('r.info',map=output_raster,flags='g')



    # --------------------------- Gpw  Extrapolatetion ----------------------
    def num_to_string(num):
        numbers = {
            1999:"{o}={a}- {b}*1",
            1998:"{o}={a}- {b}*2",
            1997:"{o}={a}- {b}*3",
            1996:"{o}={a}- {b}*4",
            1995:"{o}={a}- {b}*5",
            1994:"{o}={a}- {b}*6",
            1993:"{o}={a}- {b}*7",
            1992:"{o}={a}- {b}*8",
            1991:"{o}={a}- {b}*9",
            1990:"{o}={a}- {b}*10",
        }
        return numbers.get(num,None)

    # Calculate Every year pop : 1990-2000
    for i in range(1990,2000,1):

      raster_name= 'Gpw_Expop_'+str(i)

      #print(raster_name)

      expr = num_to_string(i)
      print(expr)

      gscript.mapcalc(
        expr.format(
            o=raster_name,
            a=input2,
            b=output_raster))




if __name__ == "__main__":
    #options, flags = grass.parser()
    main()








