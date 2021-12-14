12/14/21 Regrade: 7/7 please plot the logged pvalues for the qqplot 

This looks good! For the first regression, sm.OLS (unlike smf.ols) doesn't automatically include an intercept term, I think. So your p-values are going to be a little bit off. This isn't a huge deal here, though. For your qqplots, the expected distribution of pvalues under the null hypothesis is uniform, not normal. So you're correct that the distribution doesn't match a normal distribution, but nor would we expect it to. (-1). For the second regression, it looks like right now you're actually regressing stage onto expression, rather than vice versa, so I wouldn't trust those p-values. (-0.1). I think the reason your volcano plot looks funky is because you're grabbing mismatching pvalues and beta values. You're grabbing results.pvalues[0] (which I think is the intercept p-value) and results.params[1] (-1)

4.9/7


12/13/21 Changes based on feedback 
  - Changed QQplot to set the x axis distribution to uniform, not normal. 
  - Changed the model to regressing expression onto stage (it was accidentally reversed)
  - Updated models and volcano plot to use proper p values and beta values for regression with sex as a covariate
