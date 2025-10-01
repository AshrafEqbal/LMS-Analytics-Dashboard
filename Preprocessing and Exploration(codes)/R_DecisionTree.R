library("party")
#column(Class) has been removed from the dataset
#to feed it to decision Tree before loading it in R

data<-read.csv("C:/Users/ashra/OneDrive/Desktop/clean_lms_data.csv")
data[] <- lapply(data, function(x) if(is.character(x)) as.factor(x) else x)
tree<-ctree(performance_score ~ .,data=data)
plot(tree)s