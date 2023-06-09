# *****************************************
# * file: Compute_adjusted_popCount.py    *
# * Description:                          *
# * Compute the adjusted popCount via     *
# * af*popCount = adjusted popCount.      *
# * The process year is 1990-2020.        *
# *****************************************


# Import the necessary modules

import grass.script as gscript
import timeit 


# Set up the environment

env = gscript.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False
env['GRASS_MESSAGE_FORMAT'] = 'standard'
location = env['LOCATION_NAME']
mapset = env['MAPSET']


# Get the prepared data list

QR_list = gscript.list_grouped('rast',pattern='remain*')[mapset]
AF_list = gscript.list_grouped('rast',pattern='vec_af_more0*')[mapset]
#QR_list = gscript.list_grouped('rast',pattern='qr_clust*')[mapset]
#AF_list = gscript.list_grouped('rast',pattern='vecToR*')[mapset]


# Print the name of data list

for i in range(1990,2020,1):
    start = timeit.default_timer()
    print("Year:",i)
    print("QR_filename:",QR_list[i-1990],"  AF_filename:",AF_list[i-1990],"  Output_filename:",'Af_more0_qr_clust_'+str(i))
    stop = timeit.default_timer()
    print('Running Time: ', stop - start,"seconds")


# Compute the adjusted popCount using for-loop
# Running Time: About 120 seconds per year

for i in range(1990,2020,1):
    start = timeit.default_timer()
    print("Year:",i)
    raster_name= 'Af_more0_qr_clust_'+str(i) # Name of output layer
    input1 = str(QR_list[i-1990]) # name of pop count layer
    input2 = str(AF_list[i-1990]) # name of adjust factor layer
    print("QR_filename:",input1,"  AF_filename:",input2,"  Output_filename:",raster_name)
    gscript.mapcalc('{o}={a}*{b}'.format(o=raster_name,a=input1,b=input2))
    stop = timeit.default_timer()
    print('Running Time: ', stop - start,"seconds.")



# get the name list

AF_remain_list = gscript.list_grouped('rast',pattern='Af_more0*')[mapset]

# get the output filepath

path = "E:/Out_pop/PopCount_more0_afqr/"

# export the adjusted pop>0 Raster Map 1990-2019    
# Running Time: About 70 seconds per year

for i in range(1990,2020,1):
    start = timeit.default_timer()
    print("Year:",i)
    input1 = str(AF_remain_list[i-1990])
    raster_name = path + "Af_more0_qr_clust"+str(i)+"_F32.tiff"
    gscript.run_command('r.out.gdal',input=input1,output=raster_name,format='GTiff',flags='fc',type='Float32',createopt="COMPRESS=LZW,PREDICTOR=3,BIGTIFF=YES")
    stop = timeit.default_timer()
    print('Running Time: ', stop - start,"seconds.")

