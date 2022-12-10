""" A tool for managing school assignments"""

from argparse import ArgumentParser
import sys
from datetime import datetime
import re
import seaborn as sns
import pandas as pd

class Assignment:
    """An assignment object
    
    Attributes:
        name(str): name of assignment
        course(str): course code
        duedate(str): date assignment is due
        duetime(str): time assignment is due
        points(int): number of points an assignment is worth
    """
    def __init__(self, line):
        """Initializes assignment object.
        
        Args:
            line(str): line of a text file containing assignment data
            
        Side effects:
            Initializes attributes: name, course, duedate, duetime,
            and points
        
        ** Plan to uses regex
        ** Natalie - RegEx
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
            self.mil_time = self.military_time()
            self.points = int(match.group("Points"))
            
    def __repr__(self):
        return (
        	f"Course:      {self.course}\n"
            	f"Name:        {self.name}\n"
            	f"Due Date:    {self.duedate}\n"
            	f"Due Time:    {self.duetime}\n"
            	f"Points:      {self.points}\n"
       	)
    
    def military_time(self):
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
        return int(m_time)

    
        
def read_assignment(filepath):
    """uses with statement to open and read assignment file
   will open file and use UTF8 encoding to sort through it
	** Madison Diamond"""
    assignments = []
    with open(filepath, "r", encoding = "utf-8") as f:
        for line in f:
            assignment = Assignment(line.strip())
            assignments.append(assignment)
    return assignments
            
            
       
def assignment_counter(filepath, counter = 0):
    """use of default parameter to count(int) how many assignments there are
    for each class for the week specific methods like counter +=1 will be 
    used
	** Madison Diamond"""
    assignments = read_assignment(filepath)
    todays_date = input ("What date would you like to look at? Please insert in MM/DD/YYYY format:")
    
    
    dateregex = r"""(?xm)
    (?P<Month> \d{2})
    \
    (?P<Day>\d{2})
    \
    (?P<Year>\d{4})"""
    matchdate = re. search (dateregex, todays_date)
    if matchdate == None:
        raise ValueError('Not a valid date. Please make sure you entered the date in MM/DD/YYYY format.')
    if int (matchdate.group ("Month")) > 12 or int(matchdate.group("Day")) > 31:
        raise ValueError("Not a valid date.")
    todays_assignments = []
    for assignment in assignments:
        duedate = assignment. duedate
        if todays_date == duedate:
            todays_assignments. append(assignment. _str_())
            counter += 1
    if counter == 0:
        print (f"You have 0 assignments due on {todays_date}.")
    if counter != 0:
        print (f"You have {counter} assignments due on {todays_date}. The are:")
        return todays_assignments 
        
def assignment_overview(assignment):
    """uses f-string to give an overview of the assignment. Accesses state of the assignment object passed in
	Args:
		assignment (Assignment): Assignment object that the overview will be given of
	Returns:
		(str) an overview of the assignment
    	** Taylor Tran """ 
    assignments = read_assignments(filepath)
    somecourse = input ("What course would you like to look at?")
    courseassignments = []
    for assignment in assignments:
        if assignment.course == somecourse:
            courseassignments.append(f"""{assignment.name} is due on {assignment.duedate} 
            at {assignment.duetime} and is worth {assignment.points} points""")
    return courseassignments
        
def late_assignment(assignment, output = True):
	"""Passed an assignment, this method tells us if an assignment is past its due date. Checks to see if the assignment 
        is over the date due using conditional statemetns, then prints a string to the console suggesting appropriate action. 
	Print statement includes ballpark of how long until asssignment is due. Requires that a reference to an Assignment instance is passed.
	Args:
		assignment(Assignment instance): accesses state of assignment object to us due data, due time, and name in logic.
		output(boolean): whether to supress console output. Default is true (prints to console).
	Side Effects:
		prints a string to the console an encouraging statement including the assignment's name and roughly how long there is to complete it,
		unless it is overdue.
	Returns:
		(boolean): returns whether the assignment is late (True) or not (False)
    	***Taylor Tran"""
	cur_date, cur_time = str(datetime.now()).split(" ")
	year, month, day = cur_date.split("-")
	year = int(year)
	month = int(month)
	day = int(day)
	
	#already in military time
	hour, minute, seconds = cur_time.split(":")
	hour = int(hour)
	minute = int(minute)
	
	due_m, due_d, due_y = str(assignment.duedate).split("/")
	due_m = int(due_m)
	due_d = int(due_d)
	due_y = int(due_y)
	due_mtime = str(assignment.mil_time)
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
					message = f"You should probably start working. You only have {due_hour - hour} hours left before {assignment.name} is due"
			else:
				message = f"You have {due_d-day} days to complete {assignment.name}. Do with that what you will."
		else:
			message = f"I wouldn't stress. You have {due_m - month} months to complete {assignment.name}."
	else:
		message = f"Why is this even on your schedule?! You have {due_y - year} years to complete {assignment.name}."
	if(late):
		message = f"Youre assignment, {assignment.name}, is overdue..."
	if(output):
		print(message)
	return late				

def classes_with_work(filename):
    """Takes text file of assignments where each line satisfies intialization of Assignment class. Reads through all assignments and returns a set of all the
     classes that still have work upcoming (not late). Uses error handling.
    Args:
    	filename (str): relative or absolute path to a text file of assignments where each line satisfies intialization of Assignment class
    Side Effects:
    	(junk) creates instances of Assignment class
	(output) exceptions print to console
	
    Returns:
       (set): classes with work upcoming"""
    classes = set()
    try:
        with open(filename, 'r', encoding = 'UTF-8') as f:
            for line in f:
                try:
                    temp_set = set()
                    temp_line = line.replace('\n', '')
                    cur = Assignment(temp_line)
                    if(not(late_assignment(cur, False))):
                        temp_set.add(cur.course)
                except Exception as e:
                    print(e)
                else:
                    classes = classes | temp_set
    except:
        print("Something went wrong with opening the file")
    return classes
    
def visualize_priorities(filename):
	"""Creates a bargraph to compare/visualize the relative importance of assignments according to their point levels. Only considers upcoming assignments.

	Args:
		filename (str): relative or absolute path to a text file of assignments where each line satisfies intialization of Assignment class
	 Side Effects:
    	(junk) creates instances of Assignment class
		(output) displays seaborn bar graph
		***David Greenburg
	"""    
	assignment_points = {
		"Assignment" : [],
		"Point Value" : []
  		}
	df = pd.DataFrame(assignment_points)
	try:
		with open(filename, 'r', encoding = 'UTF-8') as f:
			for line in f:
				try:
					temp_line = line.replace('\n','')
					cur = Assignment(temp_line)
					if(not(late_assignment(cur, False))):
						temp = {"Assignment" : cur.name, "Point Value" : cur.points}
						df = df.append(temp, ignore_index = True)
				except Exception as e:
					print(e)
	except:
		print("Something went wrong with opening the file.")
	else:
		sns.barplot(data = df, x = "Assignment", y = "Point Value")
        
           
def sort_assignments(asgn_list):
    assignments = asgn_list.copy()
    assignments.sort(key = lambda a: (a.duedate, a.mil_time, -(a.points)))
    count = 0
    print("To Do List:")
    for item in assignments:
        count = count + 1
        name = item.name
        print(f"{count}. {name}")
	
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of assignments.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
        
    ** Natalie - ArgumentParser
    """        
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing the details of one assignment per line")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for assignment in read_assignments(args.file):
       		print(f"{assignment!r}\n")
    
