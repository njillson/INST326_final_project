""" A tool for managing school assignments"""

from argparse import ArgumentParser
import sys

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
       
    def read_assignment(self, filepath):
        """uses with statement to open and read assignment file
        will open file and use UTF8 encoding to sort through it
	** Madison Diamond"""
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                assignment = line.split(",")
                
            
            
       
    def  assignment_counter (self, assignment_count):
        """use of default parameter to count(int) how many assignments there are
        for each class for the week specific methods like counter +=1 will be 
        used
	** Madison Diamond
        """
        
    counter = 0
    
    
    if assignment_count >= 0:
        counter = counter+1
    print ("counter")
        
    def assignment_overview(self, assignment):
        """uses f string "f”assignment {assignment.name} is due on {assignment.due} 
        at {assignment.time} and is worth {assignment.points} points”" to give an overview of 
        the assignment. This method needs the due date time which is due_time (str),
        and point value which is points (int).
    ** Taylor Tran """  
        
    def sort_assignment(self, due_date, due _time, points):
        """A method that sorts assignments based due_date which is a str. 
        due date cannot be null, and date must be a valid date, due_time (str)
        must be a valid time. Custom list sorting with a key function with 3 
        criteria, first by date, then by time, then by point value
        (being higher)
	** Selina Liu
        """
        
    def late_assignment(self, assignment, due_date):
       """Syntax: ```Expression 1, if some condition, else expression 2```
	    If date => 10:
		print “assignment is late
        Tells us if an assignment is past its due date. Checks to see if the assignment 
        is over the date due, then returns a print statement. Needs assignment_name (str)
        and needs due_date (str) and due_time (str). 
    **Taylor Tran"""" 
        
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
        
    def __add__(self, course):
        """magic method that adds points for a class for the week, course 
        should be a dictionary with the course name as the key(str) and 
        assignment points as the values (int) assignment points can be 0, there 
        is no maximum for points, and there can be 0 assignments in the class
	** Selina Liu
        """
        
def parse_args(args):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
            
    ** Natalie - ArgumentParser
    """
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for assignment in read_assignment(args.file):
        print(f"{assignment!r}\n")
    
