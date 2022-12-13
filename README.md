# INST326_final_project
Assignment manager

## Team "Team"
Madison Diamond  
David Greenberg  
Natalie Jillson  
Selina Liu  
Taylor Tran

## Files in our repository:
README.md: Project submission documentation  

assignments.txt: An example text file to use in our program. Each line of the 
file contains what is parsed as an Assignment object within our script.  

assignment_manager.py: Our final project script. Takes 1 argument: the path to a
text file.

## How to run the program from the command line:
python3 assignment_manager.py textfilename.txt 

To run it using our example file:  
python3 assignment_manager.py assignments.txt


## Instructions on how to use the program/interpret output:  
Upon running it in the terminal, the user will be presented with menu options:   
Option 1: Displays all of the assignments and their details.  
Option 2: Sorts and displays the assignments based on priority (duedate, duetime, then by ascending point value).    
Option 3: Counts and displays the assignments on a given date.    
Option 4: Asks the user what assignment they would like the program to check if it is late or not. Prints a message corresponding with the assignment's lateness.  
Option 5: Asks user for a course, and displays the assignments for that course.  
Option 6: Displays classes that still have work given the current date. (Should only return courses that have assignments due after the current date). 
Option 7: Uses plt module to visualize priorities. (Shows bar graph of assignments and their point value so you can visualize how many points are associated with each assignment)  
 

## Attribution:

```__init__:```: Natalie Jillson - Regular Expressions

```__repr___```: Selina Liu - Magic methods other than ```__init__```

```str```: Natalie Jillson - N/A (extra)

```military_time```: Selina Liu - N/A (extra)

```late_assignment```: Taylor Tran - Conditional Expressions

```read_assignments```: Madison Diamond - ```with``` statement

```assignment_counter```: Madison Diamond - Optional parameters

```course_overview```: Taylor Tran - F-strings

```classes_with_work```: David Greenberg - Set operations

```visualize_priorities```: David Greenberg - Visualizing data with pyplot

```sort_assignments```: Selina Liu - Custom list sorting with a key function

```late```: Selina Liu - N/A (extra)

```parse_args```: Natalie Jillson - ArgumentParser class
