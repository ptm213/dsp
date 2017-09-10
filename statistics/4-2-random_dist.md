[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 

```python
# Step 1: Generate data, i.e. random list of numbers
nums = np.random.random(1000)

# Step 2: Create the Probability Mass Function (pmf), which is a normalized freqency (dictionary) table.
import collections

def EvalPmf(sample):
    pmf = collections.Counter(sample) # freq dictionary
    for key in pmf:
        pmf[key] = pmf[key]/len(pmf)
    return pmf
    
#Step 2a: Plot the PMF
pmf = EvalPmf(nums)

plt.bar(range(len(pmf)), pmf.values())
plt.xticks(range(len(pmf)), pmf.keys())
plt.xlabel('Random Variable btwn 0-1000')
plt.ylabel('PMF')
plt.show()


# Step 3: Create the Cumulative Density Function (cdf)
def EvalCdf(sample, x):
    count = 0
    for item in sample:
        if item <= x:
            count += 1
    
    PercentileRank = count/len(sample)*100
    
    return PercentileRank
    

# Step 4: Plot CDF
x_values = nums # set of values (i.e. random numbers)
x_values = sorted([x for x in x_values if not np.isnan(x)]) # clean dataset: remove nan values and sort
y_values = [EvalCdf(x_values, x) for x in x_values] # percentile rank of random values

plt.plot(x_values, y_values, 'k')
plt.title('CDF of 1000 Random Numbers')
plt.xlabel('Random Numbers')
plt.ylabel('Percentile Rank')
plt.show()

```
