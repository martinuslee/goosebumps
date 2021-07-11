setRepositories(ind=1:8)

setwd('../../../../disk1/bijh/10.Circadian_Transcriptome/')

degSetFile <- function(path){
  
  filenames <- list.files(path, pattern = "*.txt$", full.names = TRUE)
  basenames <- list.files(path, pattern = "*.txt$")
  
  fileList <-  list()
  geneId <- c()
  
  for(i in filenames){
    fileList[[i]] <- read.table(i, header=T)
    geneId <- fileList[[i]][1]
    fileList[[i]] <- fileList[[i]][7]
  }
  fc_res <- as.data.frame(fileList)
  rownames(fc_res) <- geneId$Geneid
  colnames(fc_res) <- basenames
  return(fc_res)
}

result <- degSetFile('./FeatureCounts')

view(result)


x <- nearZeroVar(result, saveMetrics = TRUE);x
