# GlobPOP: A 33-year (1990-2022) global gridded population dataset generated by cluster analysis and statistical learning.

**Article citation**: Liu, L., Cao, X., Li, S. et al. A 31-year (1990–2020) global gridded population dataset generated by cluster analysis and statistical learning. Sci Data 11, 124 (2024). https://doi.org/10.1038/s41597-024-02913-0.    

**Code citation**：Liu, L. (2023). GlobPOP: A 31-year (1990-2020) global gridded population dataset generated by cluster analysis and statistical learning. Zenodo. https://doi.org/10.5281/zenodo.10098366.    

**Dataset citation**：Liu, L., Cao, X., Li, S., & Jie, N. (2024). GlobPOP: A 33-year (1990-2022) global gridded population dataset generated by cluster analysis and statistical learning (3.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11071404

## Data Update Notice
We are pleased to announce that the GlobPOP dataset, originally encompassing the years from 1990 to 2020, has now been updated to include data for 2021 and 2022.    
Following the established methodology that ensures the high precision and reliability, the latest update allows for even more comprehensive time-series analysis. The updated GlobPOP dataset remains available in GeoTIFF format for easy integration into your existing workflows.

## Usage Notes
The input datasets and census data are all available on their official website. The programs used to generate and validate the gridded population dataset were GRASS GIS (8.2), Python(3.9) and RStuido (2022.07.2). The zonal statistics were performed at QGIS (3.22). All software needs to be installed in Windows 10.

## Data Records
The continuous global gridded population product (GlobPOP 1990-2022) in the WGS84 coordinate system with a spatial resolution of 30 arcseconds (approximately 1km in equator) can be freely accessed on Zenodo at https://doi.org/10.5281/zenodo.7813301, which is stored as the GeoTIFF format for each year.   
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
