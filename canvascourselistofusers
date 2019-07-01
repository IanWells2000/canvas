# Using Using the Canvas api to query canvas and locate courses in Canvas LMS
# Before using the canvas api I need to instantiate a new canvas object

# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.instructure.com/"
# Canvas API key
API_KEY = "Enter your access token here"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#grab the canvas course
course = canvas.get_course(course_id here)

# Retieve a list of users enrolled in this specific course

users = course.get_users()

#print the list of users in the course identified in course_id
for user in users:
	print(user)
