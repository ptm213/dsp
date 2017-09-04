# Part 1 - Regular Expressions

## Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

import os
#os.getcwd()
os.chdir('/Users/PaulM/ds/metis/metisgh/prework/dsp/python')
data = open('faculty.csv').read()
data = data.split('\n')
data = [x.split(',') for x in data] # Create master dataset by individual

# Create and clean list of degrees
degrees = [x[1].strip() for x in data[1:]] # degrees only by individual
degrees = [x.split(' ') for x in degrees] # Some individuals have multiple degrees
degrees = [x for row in degrees for x in row] # flatten list

for i in degrees: # Recode raw data value of '0'
    if i == '0':
        degrees.remove('0')
        degrees.append('phd')

degrees = [x.upper() for x in degrees] # recode values to all capital letters to prevent double counting

# Remove punctuation ('.')
deg_upper = []
new_row = []

for row in degrees:
    for char in row:
        if char not in '.':
            new_row.append(char)
    deg_upper.append(''.join(new_row))
    new_row = []

# Store degree names and frequencies in dictionary
degreehist = {}
for i in deg_upper:
    if i not in degreehist:
        degreehist[i] = 1
    else:
        degreehist[i] += 1

unique_degs = len(degreehist)

print("The following dataset shows the different UPenn CCEB faculty degrees ({}) and frequencies:\n"
      .format(unique_degs), degreehist)

## Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor

titles_full = [x[2] for x in data[1:]] # Scrape titles from master dataset

# Titles only
titles = []
for row in titles_full:
    i = row.index(' Biostatistics')-3
    #print(row[:i])
    titles.append(row[:i])

# Store titles and frequencies in dictionary
titlehist = {}

for i in titles:
    if i not in titlehist:
        titlehist[i] = 1
    else:
        titlehist[i] += 1

unique_titles = len(titlehist)

print("The following dataset shows the different UPenn CCEB faculty titles ({}) and frequencies:\n"
      .format(unique_titles), titlehist)

# Q3. Search for email addresses and put them in a list. Print the list of email addresses.

emails = [x[3] for x in data[1:]] # scrape emails from master dataset
print(emails)

# Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.

domains = []
for row in emails: # domain = right side of full email address
    i = row.index('@')
    domains.append(row[i+1:])

unique_domains = set(domains)

print("There are {} unique domains: ".format(len(unique_domains)), unique_domains)
