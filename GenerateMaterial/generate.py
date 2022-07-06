from AssignmentNotebook import IDSCourse
def checkPython():
    import sys
    print("Python version")
    print (sys.version)
    print("Version info.")
    print (sys.version_info)
    import sys
    print(sys.executable)

course = IDSCourse()
course.to_nb()
#course.makeAssignmentNotebook(assignment_number = 5,notebook_type='problem_solution')
