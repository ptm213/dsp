[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> 
```python
# Import modules
from __future__ import print_function, division

import numpy as np
import nsfg
import first
import collections
import matplotlib.pyplot as plt
import random

%matplotlib inline

def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.

    group1: Series or DataFrame
    group2: Series or DataFrame

    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

# Import data
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.pregordr==1]
others = live[live.pregordr!=1]

# Create 2 Series for total weights firsts and others
firsts_totalwgt_lb = firsts.totalwgt_lb
others_totalwgt_lb = others.totalwgt_lb

# Plot total weight for firsts and others on histogram

firsts_vals = [vals for vals in firsts_totalwgt_lb if not np.isnan(vals)] #remove nans
others_vals = [vals for vals in others_totalwgt_lb if not np.isnan(vals)] #remove nans


firsts_vals
plt.subplot(211)
plt.hist(firsts_vals, bins=range(int(max(firsts_vals))), rwidth=0.45, align='left')
plt.hist(others_vals, bins=range(int(max(others_vals))), rwidth=0.45)
plt.xlabel('Total Weight (lbs)')
plt.ylabel('Count')
plt.show()

# Compute and compare means of firsts vs. others

firsts_totalwgt_lb.mean()
others_totalwgt_lb.mean()
print("Difference between total weight means of firsts and others;", firsts_totalwgt_lb.mean() - others_totalwgt_lb.mean())

# Computer Cohen d of firsts vs. others

CohenEffectSize(firsts_totalwgt_lb, others_totalwgt_lb)
```
