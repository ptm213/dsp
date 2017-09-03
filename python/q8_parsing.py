# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# Change directory
import os
os.chdir('/Users/PaulM/ds/metis/metisgh/prework/dsp/python')
os.getcwd()

# Import and format data
football = open('football.csv').read() 
data = football.split('\n')
data = [x.split(',') for x in data] # List of football data lists

# Calculate new variable and sort
goal_diff = [[x[0], abs(int(x[5])- int(x[6]))] for x in data[1:]] # Relevant information only
ascending_teams = sorted(goal_diff, key = lambda x: x[1]) # Sort teams by goal differential
least_diff = ascending_teams[0][0] # Team w/ smallest goal differential

print("The team with the smallest goal differential is {}".format(least_diff))
