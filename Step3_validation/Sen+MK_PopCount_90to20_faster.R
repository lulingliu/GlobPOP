## ---------------------------- Load-libraries --------------------------

# Load required packages
library(terra)
library(zyp)
library(raster)
## --------------------------- Set working directory --------------------
wd <- ("E://")
setwd(wd)

## -------------------------- set file path  --------------------------

in_path = paste0(wd,"Out_pop/GlobPOP_Count/")
out_path = paste0(wd,"Out_pop/GlobPop_Trend/")
Orig_GlobPop <- list.files(in_path,
                           full.names = TRUE,
                           pattern = ".tiff$")

# Read the raster file as a SpatRaster object
Pop_rast <- rast(Orig_GlobPop)



##----------------------------Trend calculation - 31 years-----------------------

Pop_rast <- brick(Pop_rast)


# Create a function to apply zyp.sen to each pixel

# Define the calc_sen function
calc_sen <- function(x) {
  
  # Check if all values in the raster are NA
  if (all(is.na(x))) {
    return(NA)
  }
  
  # Otherwise, compute the Sen slope using the zyp.sen function
  result <- zyp.sen(x, time=1990:2020)
  
  # Extract the slope value
  slope <- result$estimate
  
  # Check if the slope is statistically significant
  pval <- result$p.value
  if (pval <= 0.05) {
    # If the slope is significant, return it as a RasterLayer object
    return(raster(slope))
  } else {
    # Otherwise, return NA as a RasterLayer object
    return(raster(NA))
  }
}

# Apply calc_sen to each pixel in the raster stack
sen_slope <- calc(Pop_rast, fun = calc_sen)


# Calculate the Sen's slope for each pixel in the spatRaster
sen_slope <- apply(Pop_rast, MARGIN=1:2, FUN=zyp.sen, time=1990:2020)

# Extract the slope and p-value layers
slope <- sen_slope$slope
p_value <- sen_slope$p.value

# Set a significance threshold (e.g., 0.05)
alpha <- 0.05

# Create a binary layer indicating significant trends
significant <- ifelse(p_value < alpha, 1, 0)

# Export the slope, p-value, and significant trend layers as separate TIFF files
writeRaster(slope, "slope.tif", format="GTiff", overwrite=TRUE)
writeRaster(p_value, "p_value.tif", format="GTiff", overwrite=TRUE)
writeRaster(significant, "significant.tif", format="GTiff", overwrite=TRUE)


