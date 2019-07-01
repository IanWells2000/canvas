#using the canvas api to query Canvas LMS (see ucfopen/canvasapi)
#Before using the canvas api need to instatiate a new canvas object
#Import the canvas class

#Canvas API URL put your own url here where indicated using instructure as an example only
API_URL = "https://instructure.com/"

API_KEY = (place your token here) See documentation how to locate token

#Initiate a new Canvas object (place your own particular course_id as the argument)
canvas = canvas.get_course(xxxxxx)

#print name and course id of canvas course
print(course)
