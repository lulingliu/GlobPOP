# coding=utf-8

# Calculate the pop count, by density * landarea

#!/usr/bin/env python3


import grass.script as gscript
import timeit 

# -------------------settings-----------------
env = gscript.gisenv()


overwrite = True


env['GRASS_OVERWRITE'] = overwrite


env['GRASS_VERBOSE'] = False

env['GRASS_MESSAGE_FORMAT'] = 'standard'

location = env['LOCATION_NAME']

mapset = env['MAPSET']

# ------------Raster Maps Calculation------------


start = timeit.default_timer()


# list rasters in mapset

raster_list = gscript.list_grouped('rast',pattern='GlobPOP_*')[mapset]


for raster in raster_list[0:20]:

        raster_name= str(raster)

        year=raster_name[8:12]

        print(raster_name," year:",year)

    # landarea layer

    landarea = gscript.list_grouped('rast',pattern='Area*')[mapset]
    

    ## Pop Count = pop density * landarea    
 
    for i in range(2001,2021,1):
      start = timeit.default_timer()
      raster_name= 'GlobPOP_'+str(i) # Name of pop count layer
      input1 = str(raster_list[i-2001]) # Year of pop density layer
      input2 = str(landarea[0]) 

      gscript.mapcalc('{o}={a}*{b}'.format(
      	o=raster_name,
      	a=input1,
      	b=input2))
      stop = timeit.default_timer()
      print('Time: ', stop - start) 



stop = timeit.default_timer()

print('Time: ', stop - start)  
