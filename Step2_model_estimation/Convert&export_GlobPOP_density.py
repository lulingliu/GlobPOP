# ************************************************
# * file: Convert&export_remain_pop_QrClust_density.py *
# * Desciption：                                       *
# *             1990-2020:Pop Count convert to density *
# ******************************************************


# import the necessary modules

import grass.script as gscript
import timeit


# set up environment

env = gscript.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False
env['GRASS_MESSAGE_FORMAT'] = 'standard'
location = env['LOCATION_NAME']
mapset = env['MAPSET']


# get the name list

PopCount_list = gscript.list_grouped('rast',pattern='Af_more0_qr_clust*')[mapset]
Area_list = gscript.list_grouped('rast',pattern='Area*')[mapset]


# Convert the pop>0 1990-2020 Count Map as density Map 
# Running Time: About 100 seconds per year

for i in range(1990,2021,1):
    start = timeit.default_timer()
    print("Year:",i)
    print("PopCount_list filename:",PopCount_list[i-1990])
    input1 = str(PopCount_list[i-1990])
    input2 = str(Area_list[0])
    raster_name= 'Density_af_qr_more0_'+str(i)
    print("Output_filename:",raster_name)
    gscript.mapcalc('{o}={a}/{b}'.format(o=raster_name,a=input1,b=input2))
    stop = timeit.default_timer()
    print('Running Time: ', stop - start,"seconds.")


# get the name list

Density_list = gscript.list_grouped('rast',pattern='Density_*')[mapset]


# get the output filepath

path = "E:/"

# export the pop>0 Density Map 1990-2019    
# Note : Export raster as Int32
# Running Time: About 70 seconds per year
# COMPRESS=LZW,PREDICTOR=3,BIGTIFF=YES --- PREDICTOR=3 for float point data can further reduce file size
for i in range(1990,2021,1):
    start = timeit.default_timer()
    print("Year:",i)
    input1 = str(Density_list[i-1990])
    raster_name = path + "GlobPOP_Density_"+str(i)+"_F32.tiff"
    gscript.run_command('r.out.gdal',input=input1,output=raster_name,format='GTiff',flags='fc',type='Float32',
    	createopt="COMPRESS=LZW,PREDICTOR=3,BIGTIFF=YES")
    stop = timeit.default_timer()
    print('Running Time: ', stop - start,"seconds.")



# get the output filepath

path = "E:/"

# export the pop>0 Raster Map 1990-2019
# COMPRESS=LZW,PREDICTOR=2,BIGTIFF=YES --- PREDICTOR=2 for integer data can further reduce file size    
for i in range(1990,2021,1):
    start = timeit.default_timer()
    print("Year:",i)
    input1 = str(PopCount_list[i-1990])
    raster_name = path + "GlobPOP_"+str(i)+"_I32.tiff"
    gscript.run_command('r.out.gdal',input=input1,output=raster_name,format='GTiff',flags='fc',type='Int32',createopt="COMPRESS=LZW,PREDICTOR=2,BIGTIFF=YES")
    stop = timeit.default_timer()
    print('Running Time: ', stop - start,"seconds.")

