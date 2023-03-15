library(ggplot2)

df <- read.table("./loci_length.txt",header = T,sep = "\t")

View(df)

pdf("Loci_length_distribution.pdf",height = 5, width = 5)
p <- ggplot(df,aes(x=length))+
  geom_histogram(binwidth = 30,color="black",fill="white")+
  labs(x="Loci length",y="Count")+
  theme_bw()+
  coord_cartesian(xlim = c(0,1000))
print(p)
dev.off()
