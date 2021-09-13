This looks really great! No need to change anything, just wanted to make one small point:
1. In your third code cell, you shouldn't actually need to "remove the header" by doing `x = df_male_14[1:]`. When you did `.loc` to generate `df_male_14A`, it should already remove the header.
