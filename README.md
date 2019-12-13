# Using the canvas api wrapper (ucfopen/canvasapi) provided by University of Central Florida (UCF) collect data from Canvas LMS.
#grabcourse.py imports the canvas api then with local settings looks up nominated course and returns the full course name and term.

#canvascourselistofusers.py imports the canvas api then with local settings looks up nominated course and returns paginated list of users.

#grabuser.py imports the canvas api then with local settings looks up nominated user and confirms user name and sis_login_id. Then creates a paginated list of all courses for that user with course_id.

#user_active_courses.py canvas api to query Canvas LMS to locate active courses for a user. then creates paginated list of courses.

#settings.py is a file used to control Canvas LMS instance url and the authentication token.  
