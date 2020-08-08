data <- read.csv("input/train.csv")
data$image_name <- paste0(data$image_name,".jpg")

malig <- data %>% filter(target == 1)
benign <- data %>% filter(target == 0)

split.data <- function(data, train.prop, set.seed=4583) {
  set.seed(set.seed)
  data <- data[sample(1:dim(data)[1]),]
  train.set <- data[1:as.integer(train.prop*dim(data)[1]),]
  test.set <- data[(as.integer(train.prop*dim(data)[1])+1):dim(data)[1],]
  return(list(train=train.set, test=test.set))
}

train.prop <- 0.80
train.split.seed <- 7294

split <- split.data(newdf, train.prop, set.seed=train.split.seed)
train.set <- split$train; test.set <- split$test

write.csv(train.set, "input/new/train.csv")
write.csv(test.set, "input/new/test.csv")

