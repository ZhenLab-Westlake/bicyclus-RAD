library(ggplot2)

df <- read.table("./depth_vcftools.txt",header = T,sep = "\t")

View(df)

pdf("sample_mean_depth_distribution.pdf",height = 5, width = 5)
p <- ggplot(df,aes(x=MEAN_DEPTH))+
  geom_histogram(binwidth = 5,color="black",fill="white")+
  labs(x="Mean depth per sample",y="Count")+
  theme_bw()+
  coord_cartesian(xlim = c(0,85))

print(p)
dev.off()
