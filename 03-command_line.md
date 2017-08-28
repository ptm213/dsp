# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 1. show current working directory path: $ pwd 
>> 2. creating a directory: $ mkdir, and add -p to create a file path.
>> 3. deleting a directory: $ rmdir , and add -p to remove an entire file path.
>> 4. creating a file using `touch` command: $ touch <filename.ext> , creates an empty file.
>> 5. deleting a file: $ rm <filename> , or $ rm -rf <directory> (-rf recursively deletes directory + all files)
>> 6. renaming a file (i.e. move file): $ mv <filename> <new_filename>.
>> 7. listing hidden files: use command ls -a to list all (hidden and unhidden) contents of current working directory. Hidden files begin with a dot (.)
>> 8. copying a file from one directory to another: $ cp <filename> <directory> , or $ cp -r <directory> <directory>, also $ cp  <filename> <filename> .
>> 9. viewing a file (less, more, cat)
>>  - $ less <filename> to display contents of a file on an in-terminal reader. Press "q" to quit.
>>  - $ more <filename> and cat <filename> will print contents of file directly to terminal.
>> 10. finding multiple files using wildcard (find, *) and performing a command on them (>, <, |): 
>>  - for example: $ cat *.txt > bigfile.txt , which writes all the contents of the .txt files in current working directory to a new file.
>>  - $ rm *.txt removes all .txt files
>>  - $ find <directory or "." for cwd> -name "*.txt" -print > PaulM/ds/metis/temp/somefile.txt , which writes all names of text files found in the directory to a somefile.txt.

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >  - `ls`  - lists files and directories in the current working directory
> >  - `ls -a`  - lists all (hidden and unhidden) files and directories
> >  - `ls -l`  - lists detailed information about directories/files, including: permissions, owner of file and its permissions, size, and last date modified
> >  - `ls -lh`  - adding a '-h' makes the list 'human readable' (e.g. size now has units, B/K/etc.)
> >  - `ls -lah`  - lists all hidden files/directories, in human readable format.
> >  - `ls -t`  - sorted list by most recently modified.
> >  - `ls -Glp`  - '-G' enables color output and '-p' adds a '/' to directory names

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> >  1. ls -m, which displays the names as comma separated lists
> >  2. ls -1, which displays each entry on a line
> >  3. ls -p, which displays directories with a '/' at the end
> >  4. ls -r, displays all contents in reverse order
> >  5. ls -R, displays all subdirectories as well

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs allows you to apply a command on a list of arguments, in one line of code. 
>>  - For example, to find all all .txt files and move them to a directory called "/text_files":
>>   * Type: find -name " \*.txt" -type f -print | xargs -O -I {} mv {} ~/text_files
>>  - This line of code finds all .txt files and then applies the mv command to each item in that list.

 

