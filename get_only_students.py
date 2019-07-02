# Using the canvas api to query Canvas LMS to locate courses in canvas
# Before using the canvas api instantiate a new canvas object
# Import the Canvas class
from canvasapi import Canvas


# Canvas API URL
API_URL = "https://canvas.instructure.com/"
# Canvas API key
API_KEY = "your access token here"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#grab course xxxxxx
course = canvas.get_course(your course_id here)

#access the course's name
course.name

# prints name of course and course id
print(course)

#list students ONLY for a given course
users = course.get_users(enrollment_type=['student'])

#print the list of students ONLY for this course
for user in users:
	print(user)
	
