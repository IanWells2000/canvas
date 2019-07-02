# Using the canvas api to query Canvas LMS to locate active courses for a user
# Before using the canvas api instantiate a new canvas object
# Import the Canvas class
from canvasapi import Canvas


# Canvas API URL
API_URL = "https://canvas.instructure.com/"
# Canvas API key
API_KEY = "your access token here"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#grab user xxxxxx
user = canvas.get_user(your user_id here)


# access the user's name
user.name

# confirms user name
print(user)

# list of courses the user is enrolled in
courses = user.get_courses(enrollment_status='active')


# print the list of courses this user is enrolled on
for courses in courses:
	print(courses)
