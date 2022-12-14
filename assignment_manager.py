""" A tool for managing school assignments"""

from argparse import ArgumentParser
import sys
from datetime import datetime
import re
import pandas as pd
import matplotlib.pyplot as plt

 
class Assignment:
    """An assignment object
    
    Attributes:
        name(str): name of assignment
        course(str): course code
        duedate(str): date assignment is due
        duetime(str): time assignment is due
        points(int): number of points an assignment is worth
        mil_time(int): value for military tme sorting
	    late(boolean): whether the due date for an assingment has passed or not
    """
    def __init__(self, line):
        """Initializes assignment object.
        
        Args:
            line(str): line of a text file containing assignment data
            
        Side effects:
            Initializes attributes: name, course, duedate, duetime,
            and points
        
        *** Natalie Jillson (Technique: Regular Expressions)
        """
        regex = r"""(?xm)
        ^(?P<Course>[A-Z]{4}\d{3}(?:\w?))
        ,\s
        (?P<AssignmentName>.*?)
        ,\s
        (?P<DueDate>\d{2}/\d{2}/\d{4})
        ,\s
        (?P<DueTime>\d{1,2}:\d{2}\s(?:am|pm))
        ,\s
        (?P<Points>\d*)
        """

        line = line.strip()
        match = re.search(regex, line)
        if match == None:
            raise ValueError('Your assignment information could not be parsed')
        else:
            self.assignment = line
            self.course = match.group("Course")
            self.name = match.group("AssignmentName")
            self.duedate = match.group("DueDate")
            self.duetime = match.group("DueTime")
            self.points = int(match.group("Points"))
            self.mil_time = self.military_time()
            self.late = self.late_assignment(False)
            
    def __repr__(self):
        """Formal representation of Assignment object

        Returns:
            string: formal representation of course, name, duedate, duetime, and points attributes
        *** Selina Liu (Technique: magic methods other than __init__())
        """        
        return (
        	f"""
         Course:      {self.course}\n
         Name:        {self.name}\n
         Due Date:    {self.duedate}\n
         Due Time:    {self.duetime}\n
         Points:      {self.points}\n"""
       	)
    
    def __str__(self):
        """Informal representation of an Assignment object

        Returns:
            string: informal representation of an assignment's name and due date
            ** Natalie Jillson
        """        
        return f"{self.name} for {self.course}"
    
    def military_time(self):
        """Creates a value for self.duetime that can be compared and sorted

        Returns:
            int: value for self.duetime tha can be compared and sorted
        *** Selina Liu
        """        
        hour, minute = self.duetime.strip().split(":")   
        if "pm" in minute:
            hour = int(hour)
            minute = int(minute.strip("pm"))  
            hour = 12 + hour
            if minute < 10:
                hour = hour * 10
        else:
            minute = int(minute.strip("am"))
            if minute < 10:
                hour = 10 * int(hour)
        
        m_time = f"{hour}{minute}"
        mil_time = int(m_time)
        return mil_time
    
    def late_assignment(self, output = True):
        """Passed an assignment, this method tells us if an assignment is past its due date. Checks to see if the assignment 
        is over the date due using conditional statements, then prints a string to the console suggesting appropriate action. 
	Print statement includes ballpark of how long until asssignment is due.
	Args:
		assignment(Assignment instance): accesses state of assignment object to us due data, due time, and name in logic.
		output(boolean): whether to supress console output. Default is true (prints to console).
	Side Effects:
		prints a string to the console an encouraging statement including the assignment's name and roughly how long there is to complete it,
		unless it is overdue.
	Returns:
		(boolean): returns whether the assignment is late (True) or not (False)
    Side Effects: 
        Prints messages to remind user the due date and how much time they have left to complete their assignment 
    	*** Taylor Tran (Technique: Conditional Expressions)
        """
        cur_date, cur_time = str(datetime.now()).split(" ")
        year, month, day = cur_date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        
        hour, minute, seconds = cur_time.split(":")
        hour = int(hour)
        minute = int(minute)
        
        due_m, due_d, due_y = str(self.duedate).split("/")
        due_m = int(due_m)
        due_d = int(due_d)
        due_y = int(due_y)
        due_mtime = str(self.mil_time)
        due_hour = int(due_mtime[:2])
        due_minute = int(due_mtime[2:])
        
        late = False
        
        if(year > due_y):
            late = True
        elif(year == due_y):
            if(month > due_m):
                late = True
            elif(month == due_m):
                if(day > due_d):
                    late = True
                elif(day == due_d):
                    if(hour>due_hour):
                        late = True
                    elif(hour == due_hour):
                        if(minute >= due_minute):
                            late = True
                        else:
                            message = f"GET GOING! You only have {due_minute-minute} minutes left!"
                    else:
                        message = f"You should probably start working. You only have {due_hour - hour} hours left before {self.name} is due"
                else:
                    message = f"You have {due_d-day} days to complete {self.name}. Do with that what you will."
            else:
                message = f"I wouldn't stress. You have {due_m - month} months to complete {self.name}."
        else:
            message = f"Why is this even on your schedule?! You have {due_y - year} years to complete {self.name}."
        if(late):
            message = f"Your assignment, {self.name}, is overdue..."
        if(output):
            print(message)
            return late
    
        
def read_assignments(filepath):
    """uses with statement to open and read assignment file
   will open file and use UTF8 encoding to sort through it
	** Madison Diamond

    Args:
        filepath (str): file containing user data based on their classes and
        assignments 

    Returns:
        (str): string of sorted data
    """
    assignments = []
    with open(filepath, "r", encoding = "utf-8") as f:
        for line in f:
            assignment = Assignment(line.strip())
            assignments.append(assignment)
    return assignments
                       
       
def assignment_counter(asgn_list, counter = 0):
    """use of default parameter to count(int) how many assignments there are
    for each class for the week specific methods like counter +=1 will be 
    used
	*** Madison Diamond (Technique: Optional Parameter)
    
    Args:
        assignments (int): Assignment object that is sorted through and tells the 
        user information about the count of their assignments
    Returns (string):
        returns a string to the user where they can see a count of the assignments 
        due on todays date
    Side effects: prints message regarding if the user has assignments due on a given day  
    """
      
    assignments = asgn_list.copy()
    todays_date = input("What date would you like to look at? Please insert in MM/DD/YYYY format:")
    
    
    dateregex = r"""(?xm)
    (?P<Month>\d{2})
    /
    (?P<Day>\d{2})
    /
    (?P<Year>\d{4})"""
    matchdate = re.search(dateregex, todays_date)
    if matchdate == None:
        raise ValueError('Not a valid date. Please make sure you entered the date in MM/DD/YYYY format.')
    if int (matchdate.group ("Month")) > 12 or int(matchdate.group("Day")) > 31:
        raise ValueError("Not a valid date.")
    todays_assignments = []
    for assignment in assignments:
        duedate = assignment.duedate
        if todays_date == duedate:
            todays_assignments.append(assignment.__str__())
            counter += 1
    if counter == 0:
        print (f"You have 0 assignments due on {todays_date}.")
    if counter != 0:
        print (f"You have {counter} assignments due on {todays_date}. They are:") 
        print (f"{todays_assignments}")
        
def course_overview(asgn_list):
    """uses f-string to give an overview of the assignment. Accesses state of the assignment object passed in
	Args:
		assignments (Assignment): Assignment object that the overview will be given of
	Returns:
		(str) an overview of the assignment including due date, due time, and amount of points 
    Side Effects: 
        Prints overview of assignment, includes due date, time it is due, and point value 
    	** Taylor Tran
        F-strings""" 
    assignments = asgn_list.copy()
    somecourse = input ("What course would you like to look at?")
    for assignment in assignments:
        if assignment.course == somecourse:
            print(f"""\n{assignment.name} is due on {assignment.duedate} at {assignment.duetime} and is worth {assignment.points} points""")


def classes_with_work(assignments):    
    """Takes text file of assignments where each line satisfies intialization of Assignment class. Reads through all assignments and returns a set of all the
     classes that still have work upcoming (not late). Uses error handling.
    Args:
    	assignments (list of Assignment objects): used to iterate over all assignment instances
    Side Effects:
    	(junk) creates instances of Assignment class
	(output) exceptions print to console
	calls read_asssignment & late_assignment methods
	
    Returns:
       (set): classes with work upcoming
       **David Greenberg"""
    
    classes = set()
    for task in assignments:
        temp_set = {f"{task.course}"}
        classes = classes.union(temp_set)
    return classes
    
def visualize_priorities(assignments):
    """Creates a bargraph to compare/visualize the relative importance of assignments according to their point levels. Only considers upcoming assignments.
	Args:
		filename (str): relative or absolute path to a text file of assignments where each line satisfies intialization of Assignment class
	 Side Effects:
    		(junk) creates instances of Assignment class
		(output) displays seaborn bar graph
		calls read_assignments && late_assignment methods
		***David Greenberg
	"""  
    assignment_points = {
		"Name of Assignment" : [],
		"Point Value" : []
  		}
    for task in assignments:
        if(task.points > 0):
            assignment_points["Name of Assignment"].append(task.name)
            assignment_points["Point Value"].append(task.points)
            
    df = pd.DataFrame(assignment_points)
    df = df.set_index("Name of Assignment")
    df.plot(kind = 'bar', linewidth = 4)
    plt.xticks(rotation = 45, ha = 'right')
    plt.subplots_adjust(bottom = 0.6)
    plt.title("Point Values of All Assignments")
    plt.show()
        
           
def sort_assignments(asgn_list):
    """Sorts assignments based off of nearest due date and due time, then by highest points

    Args:
        asgn_list (list): list of Assignment objects
        
    Side Effects: Prints to do list
    *** Selina Liu (Technique: custom list sorting with a key function (possibly a lambda expression))
    """    
    assignments = asgn_list.copy()
    assignments.sort(key = lambda a: (a.duedate, a.mil_time, -(a.points)))
    count = 0
    print("To Do List:")
    for item in assignments:
        count = count + 1
        name = item.name
        print(f"{count}. {name}")

def late(assignment, assgnlist):
    """function to run late_assignment method, checks if assignment is in list of objects, and if it is it finds that Assignment 
    object associated with the assignment name

    Args:
        assignment (str): assignment name
        assgnlist (list): list of Assignment objects
    Returns:
        Reference: Assignment object
        NoneType: None 
    *** Selina Liu    
    """    
    alist = assgnlist.copy()
    for item in alist:
        if item.name == assignment:
            return(item)
    return None
	
def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of assignments.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
        
    *** Natalie Jillson (Technique: ArgumentParser)
    """        
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing the details of one assignment per line")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])   
    a = read_assignments(args.file)
    print("Welcome to the Assignment Manager, if you would like to stop at any time type 'STOP'")
    check = True
    while check == True:
        command = input(f"""
    What would you like to do?
                        
    1. Check all assignments
    2. Sort assignments by priority (date, time, points)
    3. Count and view the assignments due on a given day
    4. See if an assignment is late or not
    5. View assignments for a chosen course
    6. See what courses you still have assignments in
    7. Visualize assignment priorities by point value
                    
    Type the number of the command you would like me to do:""")
        if command == "STOP":
            check = False
            print ("See you next time!")
        if command == "1":
                print (a)
        if command == "2":
            sort_assignments(a)
        if command == "3":
            assignment_counter(a)
        if command == "4":
            check4 = True
            while check4 == True:
                assignment = input("What assignment would you like to check?")
                cur = late(assignment, a)
                if cur != None:
                    cur.late_assignment()
                    check4 = False
                else:
                    print("You don't have that assignment, try again!")

        if command == "5":
            course_overview(a)
        if command == "6":
            print(f"You have assignments in: \n\t{classes_with_work(a)}")
        if command == '7':
            visualize_priorities(a)
            print("You will need to close the figure before entering any new commands")
		
            

    
