""" A tool for managing school assignments"""

class Assignment:
    """An assignment object
    
    Attributes:
        name(str): name of assignment
        course(str): course code
        date(str): date assignment is due
        time(str): time assignment is due
    """
    def __init__(self, assignment):
        """uses regex to parse through each line in the file and determine class, due date, due time, point value fore each assignment"""
       
    def read_assignment(self, filepath):
        """uses with statement to open and read assignment file""""
       
    def  assignment_counter (self, count = 0):
        """use of default parameter to count(int) how many assignments there are for each class for the week"""
        
    def assignment_overview(self, assignment):
        """prints to the user with the use of an fstring a message in regards to the assignments"""
        
    def sort_assignment(self, schedule):
        """A method that sorts assignments based on which class its for
        Custom list sorting with a key function with 2 criteria, first by date, then by point value""" 
        
    def late_assignment(self, assignment, due_date):
        """uses conditional expression to print whether or not an assignment will be late"""
        
    def __add__(self, course):
        """magic method that adds points for a class for the week"""
        
    def parse_args(args):
        """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
        
