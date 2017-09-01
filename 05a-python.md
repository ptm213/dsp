# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are similar in the sense that they are both sequences and they can both store information. The main difference bewteen the two is that lists are mutable (they can be changed) and tuples are not. Dictionaries keys must be immutable, therefore tuples will work as keys for dictionaries but lists will not. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both collections of data, but sets (similar to dictionaries) are hashable, unordered, and do not support indexing. For example, a list can be used to store data about patients' weights if you'd like to sort them from greatest to smallest and access to the list's index is important. Sets can be used to store gym membership data, where simply being able to tell if a gym member ID# is in set of paid gym members. Elements can be searched and found much faster with sets because sets are hashable; lists on the other hand, must be iterated on through each value - which takes much longer.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda operator is a way to create annonymous "throw away" functions. A lambda function consists of an argument list and an expression. It is used with the map() and filter() functions. For example, if you have a list of integers, lst = \[1,2,3,4], you can multiple each element in that list by simply using lambda: list(map(lambda x : x\*2, lst). 

>> The lambda function can also be used as the key to the sorted() function. This means that you can specify how a sequence is sorted based on some lambda criteria. For example, if you had the sequence: 

>> student_tuples = \[
>>        ('john', 'A', 15),
>>        ('jane', 'B', 12),
>>        ('dave', 'B', 10)
>> ]

>> You could sort on age (i.e. the 3rd item): sorted(student_tuples, key = lambda student : student\[2]). In this line of code, the lambda function tells the key to refer to the item in index position 2 of the list student_tuples. 


---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





