Question 1c
	cp /Users/cmdb/qbb2021/data/{K27me3.bed,K4me3.bed,K9me3.bed,LADs_Kc.bed,S2_9state.bed,dm6.chrom.sizes,fbgenes.bed} ~/qbb2021-answers/day1-lunch/
	
2B
	wc -l *.bed > feature_count.txt
2C
	Lads_Kc has the smallest number of features (412)
	fbGenes has the highest number of features (30718)

3B
	cut -f 1 fbgenes.bed | sort | uniq -c > fbgenes.info

3C
	ChrM has the smallest number of features at 13
	Chr3R has the largest number of features at 7246	

4C
	bedtools intersect -wb -a K9me3.bed -b *.bed | cut -f 1 | uniq -c > chr-with-fbgenes-k9.txt
4D
	ChrY has the lowest number of overlapping features at 36
	ChrX has the highest number of overlapping features at 6387
