# GlobPOP
A 31-year (1990-2020) global gridded population dataset generated by cluster analysis and statistical learning.
https://doi.org/10.5281/zenodo.8019391

## Usage Notes
The input datasets and census data are all available on their official website. The programs used to generate and validate the gridded population dataset were GRASS GIS (8.2), Python(3.9) and RStuido (2022.07.2). The zonal statistics were performed at QGIS (3.22). All software needs to be installed in Windows 10.

## Data Records
The continuous global gridded population product (GlobPOP 1990-2020) in the WGS84 coordinate system with a spatial resolution of 30 arcseconds (approximately 1km in equator) can be freely accessed on Zenodo at https://doi.org/10.5281/zenodo.7813301, which is stored as the GeoTIFF format for each year.   
There are two population formats, one is the 'Count'(Population count per grid) and another is the 'Density'(Population count per square kilometer each grid). The current version of the product spans the globe from 90N latitude to 90S.

Each GeoTIFF filename has 5 fields that are separated by an underscore "_". A filename extension follows these fields. 

The fields are described below with the example filename: GlobPOP_Count_30arc_1990_I32.

Field 1: GlobPOP(Global gridded population)  
Field 2: Pixel unit is population "Count" or population "Density"  
Field 3: Spatial resolution is 30 arc seconds  
Field 4: Year "1990"  
Field 5: Data type is I32(Int 32) or F32(Float32)  

## GlobPOP for time-series analysis
To validate the temporal accuracy of GlobPOP at the country level, we have developed an interactive web application, accessible at https://globpop.shinyapps.io/GlobPOP/, where data users can explore the country level population time-series curves of interest and compare them with census data.
