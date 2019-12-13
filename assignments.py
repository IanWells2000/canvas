#Using the canvas api to query canvas beta to locate courses in canvas
# Before using the canvas api instantiate a new canvas object
#Import the Canvas class
from canvasapi import Canvas
import requests
import json
import csv
import datetime

# Canvas API URL
API_URL = "ADD YOUR CANVAS INSTANCE URL HERE"
# Canvas API key
API_KEY = "ADD YOUR CANVAS LMS TOKEN HERE"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#grab course using your course code located from canvas and place as argument
course = canvas.get_course(XXXXX)

#access the course's name
#course.name

# prints name of course and course id
print("Course name is ...",course)
print('#############################################')

#list students ONLY for a given course
#users = course.get_users(enrollment_type=['student'])

#print the list of students ONLY for this course
#for user in users:
    #print("Student in this course...",user)
    
#list of assignments for a given course
assignments = course.get_assignments(submission_type=['true'])

#target a specific assignment using the assignment indiocator code from canvas
#assignmentscores = course.get_assignments(XXXXXX)

#print the list of assignments for this course also used string formatting on the canvas date stamp
for assignment in assignments:
    print("Assignment associated with this course",assignment,"Assignment due date",assignment.due_at_date.strftime("%d/%m/%Y"))

#create a csv file and declare as variable 'f' then initialise writer as the csv writer
with open('CSV/34058/assignments.csv', 'w', newline = '')as f:
    writer = csv.writer(f)
            
#print the list of assignments for a course using a 'for loop' use string formatting for canvas date stamp
    for assignment in assignments:
        writer.writerow([assignment, assignment.due_at_date.strftime("%d/%m/%Y")])
        
f.close()
   
