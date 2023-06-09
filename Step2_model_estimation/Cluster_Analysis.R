# ============================== cluster analysis ==============================

# ============================ 1 load-preprocessing ===================================

# load package
library(readxl)
library(cluster)

library(quantreg)
library(Metrics)

# import
year = 1991
year1990 <- read_excel("pop_3set_90to99.xlsx",
                       sheet = paste0('year', year))
# View(year1990)
# head(year1990)

# tidy data
year1990 =  tidyDF(year1990)
View(year1990)

tidyDF = function(df) {
  print(paste0("Original nrow: ", nrow(df)))
  
  # rename col
  names(df)[4] <- paste0("Grump")
  names(df)[5] <- paste0("GPW")
  names(df)[6] <- paste0("GHS")
  names(df)[7] <- paste0("UN")
  
  # exclude data less than zero
  df = df %>%
    filter((Grump > 0) & (GPW > 0) & (GHS > 0))
  
  print(paste0("Tidy nrow: ", nrow(df)))
  
  return(df)
  
}




# ============================ 2 cluster analysis  =================================

## calculate indicators，normalizaion

getIndex = function(df) {
  df = df %>%
    # APE = （Actual - Predict）/ Actual
    mutate(
      APE_Grump = abs(UN - Grump) / UN,
      APE_GPW = abs(UN - GPW) / UN,
      APE_GHS = abs(UN - GHS) / UN
    ) %>%
    # SE = （Actual - Predict）^2
    mutate(
      SE_Grump = (UN - Grump) ** 2,
      SE_GPW = (UN - GPW) ** 2,
      SE_GHS = (UN - GHS) ** 2
    ) %>%
    # SLE = ( ln(1+x)-ln(1+y))^2
    mutate(
      SLE_Grump = (log(1 + UN) - log(1 + Grump)) ** 2,
      SLE_GPW = (log(1 + UN) - log(1 + GPW)) ** 2,
      SLE_GHS = (log(1 + UN) - log(1 + GHS)) ** 2
    ) %>%
    # Dif = （ Predict - Actual）
    mutate(
      Dif_Grump = (Grump - UN),
      Dif_GPW = (GPW - UN),
      Dif_GHS = (GHS - UN),
    )
  
  return(df)
}

# get the indicators
year1990 = getIndex(year1990)

# normalization
scale1990 = year1990 [, -c(1:7)]
scale1990 = scale(scale1990)

View(scale1990)

# ================================ 3 checking  =================================
z = year1990[, -c(1:7)]  # all pop data
z = year1990[, c(8, 11, 14, 17)]  # grump
z = year1990[, c(9, 12, 15, 18)]  # gpw
z = year1990[, c(10, 13, 16, 19)]  # ghs

means = apply(z, 2, mean) # 2-col data
sds = apply(z, 2, sd)
nor = scale(z, center = means, scale = sds)

#  get the optimal cluster numbers
fviz_nbclust(nor, kmeans, method = "wss")

# check the cluster quality
fviz_nbclust(nor, kmeans, method = "silhouette")


# =========== 4 K-Means Cluster Analysis ===============

set.seed(123)
kc <- kmeans(nor, 2)
kc

# plot the cluster
ot <- nor
datadistshortset <- dist(ot, method = "euclidean")
hc1 <- hclust(datadistshortset, method = "complete")
pamvshortset <- pam(datadistshortset, 3, diss = FALSE)
clusplot(
  pamvshortset,
  shade = FALSE,
  labels = 2,
  col.clus = "blue",
  col.p = "red",
  span = FALSE,
  main = "Cluster Mapping - Grump",
  cex = 1.2
)
