Hi Brad, 

- In the future, please upload code snippets (including even just your notes on what you did) as a .txt file (e.g., made in textmate, which should be on your bootcamp computer) rather than a word document 
- For the Manhattan plot, you correctly labeled the most significant snps (e.g., rs934755). However, we also want you to plot only those significant SNPs in a different color. On both your Manhattans, I see random red dots at the bottom of the chromosomes.
I think this is an artifact of the qmplot manhattanplot package and while it’s great to use packages when appropriate, the packages you use need to generate figures that meet the specifications of exactly what you want. 
Unless you can figure out how to color only those significant SNPs using this package, you shouldn’t use it. In general, plotting a manhattan by hand is a generalizable skill for you - so it would be a worthwhile exercise to try to learn it here.
(Hint: try doing it as a regular scatter plot) (-0.25)
- Your qq plot looks a bit out of whack. Look up some papers (e.g., fig 4 here: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1181913/) for what they should look like. 
Again I think this is an artifact of the package you're using; and again, plotting it manually is a generalizable skill worth learning. I recommend plotting it as a scatter as well. (-1)
- Please label the boxplot more clearly - I'm left wondering which SNP we're visualizing 

5.75/7
