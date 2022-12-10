""" A tool for managing school assignments"""

from argparse import ArgumentParser
import sys
from datetime import datetime
import re

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
    
        
def read_assignments(filepath):
"""uses with statement to open and read assignment file
   will open file and use UTF8 encoding to sort through it
	** Madison Diamond"""
	assignments = []
   	with open(filepath, "r", encoding="utf-8") as f:
       		assignments = [Assignment(line) for line in f]
  	return (assignments)	
            
            
       
def assignment_counter(filepath, todays_date, counter = 0):
        """use of default parameter to count(int) how many assignments there are
        for each class for the week specific methods like counter +=1 will be 
        used
	** Madison Diamond
        """
	assignments = read_assignments(filepath)
        for assignment in assignments:
           	duedate = assignment.duedate
           	if todays_date == duedate:
               		counter += 1
        return counter
        
def assignment_overview(assignment):
        """uses f-string to give an overview of the assignment. Accesses state of the assignment object passed in
	Args:
		assignment (Assignment): Assignment object that the overview will be given of
	Returns:
		(str) an overview of the assignment
    	** Taylor Tran 
    	""" 
	return f"Assignment {assignment.name} is due on {assignment.due} at {assignment.time} and is worth {assignment.points} points” 
        
def late_assignment(assignment):
       """Passed an assignment, this method tells us if an assignment is past its due date. Checks to see if the assignment 
        is over the date due using conditional statemetns, then prints a string to the console suggesting appropriate action. 
	Print statement includes ballpark of how long until asssignment is due. Requires that a reference to an Assignment instance is passed.
	Args:
		assignment(Assignment instance): accesses state of assignment object to us due data, due time, and name in logic.
	Side Effects:
		prints a string to the console an encouraging statement including the assignment's name and roughly how long there is to complete it,
		unless it is overdue.
	Returns:
		(boolean): returns whether the assignment is late (True) or not (False)
    	**Taylor Tran"""" 
	#current
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
						print(f"GET GOING! You only have {due_minute-minute} minutes left!")
				else:
					print(f"You should probably start working. You only have {due_hour - hour} hours left before {assignment.name} is due")
			else:
				print(f"You have {due_d-day} days to complete {assignment.name}. Do with that what you will.")
		else:
			print(f"I wouldn't stress. You have {due_m - month} months to complete {assignmnet.name}.")
	else:
		print(f"Why is this even on your schedule?! You have {due_y - year} years to complete {assignment.name}.")
	if(late):
		print(f"You're assignment, {assignment.name}, is overdue...")
	return late
					
        
def shared_tasks(self, other):
     """Not sure if you want to incorporate into class but if so then person1 wil be self
    takes two people objects/ task sets and compares the tasks using a set operation
    so that the shared tasks are listed (You get a companion!)
    **Maybe display their email at the end so that you can connect - could run this function through
    data base of people so that it gives you email and classes for every person that you match
    tasks with

    Args:
        person1 (set): unordered list of all the activities person1 has in their object
        person2 (set): unordered list of all the activities person2 has in their object

    Returns:
        rlist(set): list of activities/ tasks that the two people share
    """
    """
    #will require additional code to build set from people(task) objects
    tasks = {}
    return self.tasks.intersection(other.tasks)
    #or assignments on the same day
    **david greenburg"""
    
def visualize_priorities(Assignment, person):
     """creates a bargraph with each task in an object's task list graphed against their priority level/ urgency
    
    Args:
        person object
        
    Side Effects:
        seaborn bar plot is displayed"""

    """
    x = []
    y = []
    for task in person.tasks:
        x.append(task)
        y.append(person.get_priority(task))
    data = {'task':x, 'priority':y}
    sb.barplot(data, x= 'task', y = 'priority')
    ** david greenburg"""
        


    
def sort_assignments(asgn_list):
	assignments = assgn_list.copy()
	assignments.sort(key = lambda a: (a.duedate, a.mil_time, -(a.points)))
	count = 0
	print("To Do List:")
	for item in assignments:
        	count = count + 1
        	name = item.name
        print(f"{count}. {name}")
	
def parse_args(args):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of assignments.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
            
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing the details of one assignment per line")
    return parser.parse_args(arglist)
    
    ** Natalie - ArgumentParser
    """

if __name__ == "__main__":
   	args = parse_args(sys.argv[1:])
   	for assignment in read_assignment(args.file):
       		print(f"{assignment!r}\n")
    
