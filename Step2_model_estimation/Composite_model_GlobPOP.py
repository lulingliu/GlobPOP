# coding=utf-8




#*

 # * File: Composite_model_GlobPOP.py

 # * Note: this products have to be adjusted later.

# */



import grass.script as gscript




def main():

# --------------------- settings --------------------



    env = gscript.gisenv()

    overwrite = True

    env['GRASS_OVERWRITE'] = overwrite

    env['GRASS_VERBOSE'] = False

    env['GRASS_MESSAGE_FORMAT'] = 'standard'

    location = env['LOCATION_NAME']

    mapset = env['MAPSET']



# ----- Input Raster : Pop Count -----


    GPW_list = gscript.list_grouped('rast',pattern='GPWv4_*')[mapset]

    LS_list = gscript.list_grouped('rast',pattern='landscan_*')[mapset]

    WP_list = gscript.list_grouped('rast',pattern='ppp_*')[mapset]


# --------- 2001-2020 : model(LS,WP,GPWv4) --------


# -- Raster Maps Calculation : 2001 --


    year = 2001

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])

    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.504)*{a}+{b}*0.558-{c}*0.051'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2002 --



    year = 2002

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])



    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.519)*{a}+{b}*0.434+{c}*0.056'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2003 --


    year = 2003

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.479)*{a}+{b}*0.406+{c}*0.123'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2004 --



    year = 2004

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.446)*{a}+{b}*0.402+{c}*0.159'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2005 --



    year = 2005

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.428)*{a}+{b}*0.415+{c}*0.165'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2006 --



    year = 2006


    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.388)*{a}+{b}*0.6-{c}*0.024'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2007 --



    year = 2007

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.342)*{a}+{b}*0.63+{c}*0.041'.format(o=raster_name,a=input1,b=input2,c=input3))


# -- Raster Maps Calculation : 2008 --



    year = 2008

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])



    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.432)*{a}+{b}*0.671-{c}*0.087'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2009 --



    year = 2009

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])

    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.409)*{a}+{b}*0.857-{c}*0.246'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2010 --



    year = 2010

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.476)*{a}+{b}*0.532+{c}*0.007'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2011 --


    year = 2011

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.481)*{a}+{b}*0.439+{c}*0.093'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2012 --



    year = 2012

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])



    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.47)*{a}+{b}*0.497+{c}*0.048'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2013 --



    year = 2013

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])



    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.439)*{a}+{b}*0.535+{c}*0.041'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2014 --



    year = 2014

    # input pop layer



    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])



    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.45)*{a}+{b}*0.553+{c}*0.013'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2015 --



    year = 2015

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])



    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.556)*{a}+{b}*0.217+{c}*0.238'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2016 --



    year = 2016

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.841)*{a}+{b}*0.107+{c}*0.072'.format(o=raster_name,a=input1,b=input2,c=input3))


# -- Raster Maps Calculation : 2017 --



    year = 2017

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])

    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}={a}+{b}*0.088-{c}*0.063'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2018 --



    year = 2018

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])

    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.787)*{a}+{b}*0.988-{c}*0.73'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2019 --



    year = 2019

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.933)*{a}+{b}*0.533-{c}*0.433'.format(o=raster_name,a=input1,b=input2,c=input3))



# -- Raster Maps Calculation : 2020 --



    year = 2020

    # input pop layer

    input1 = str(LS_list[year-2000])  

    input2 = str(WP_list[year-2000])

    input3 = str(GPW_list[year-1990])


    # qr_clust_year

    raster_name= 'qr_clust_'+str(year)

    gscript.mapcalc('{o}=(0.942)*{a}+{b}*0.339-{c}*0.252'.format(o=raster_name,a=input1,b=input2,c=input3))





if __name__ == '__main__':



    main()

