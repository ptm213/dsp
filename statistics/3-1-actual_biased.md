[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> 
```python
from __future__ import print_function, division

%matplotlib inline

import nsfg
import first
import thinkstats2
import thinkplot

import numpy as np
import pandas as pd
import collections
import matplotlib.pyplot as plt

resp = nsfg.ReadFemResp()


# Part 1: Actual (unbiased) Distribution of Children per Household

# Step 1: Create frequency table
freq = collections.Counter(resp.numkdhh)

# Step 2: Create pmf table (divide freq table by n)
n = sum(freq.values())
pmf = {key: freq[key]/n for key in freq}

# Step 3: Plot pmf data w/ plt.hist
plt.bar(list(pmf.keys()) , list(pmf.values()))
plt.title('Actual: Number of Children per Household')
plt.xlabel('Number of Children')
plt.ylabel('PMF')
plt.show()


# Calculate the unbiased mean
total = 0
for key in freq:
    total += key*freq[key]
mean = total/sum(freq.values()) # Actual "unbiased" mean


# Part 2: Biased Distribution of Children per Household

# function to produce Biased PMF
def BiasPmf(pmf):
    new_pmf = pmf.copy()

    for x, p in pmf.items():
        new_pmf[x] = x*p
        
    #new_pmf.Normalize()
    return new_pmf
    
    
# Plot biased PMF
biased_pmf = BiasPmf(pmf)

plt.bar(list(biased_pmf.keys()) , list(biased_pmf.values()))
plt.title('Observed: Number of Children per Household')
plt.xlabel('Number of Children')
plt.ylabel('PMF')
plt.show()


# Calculate the biased mean
total = 0
for key in biased_pmf:
    total += key*biased_pmf[key]
mean = total/sum(biased_pmf.values()) # Actual "unbiased" mean

```
