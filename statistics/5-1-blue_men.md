[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 

```python

import scipy.stats
import pandas as pd
import numpy as np

# Import data
import brfss
df = brfss.ReadBrfss()


# Step 1: Filter dataset - select males only
males = df[df['sex']==1]
mu = males.htm3.mean()
std = males.htm3.std()

print("The observed data is normally distributed. \
      \nThe normal distribution summary statistics are: mu = {}, std = {}".format(mu, std)) # confirmed, correct dataset

#Note: scipy.stats.norm.cdf() is essentially the Percentile Rank function, which uses a Z score. 
#Input is a value and output is % of population below the given value 


# Step 2: Use scipy to find the percentile ranks of 5'10" (70 inches) and 6'1" (73 inches). 

# Convert inches to cm
def inch_to_cm(inch):
    cm = inch*2.54
    return cm

# Create normal distribution given mu and std
male_norm_dist = scipy.stats.norm(loc=mu, scale=std)

upperlim = male_norm_dist.cdf(inch_to_cm(73))
lowerlim = male_norm_dist.cdf(inch_to_cm(70))

# Step 3: Calculate the difference, which equals the percentage of US male population that is in the given range. 
diff = upperlim-lowerlim
diff*100
```
