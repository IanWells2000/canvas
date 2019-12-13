#Using the canvas lms api to locate assignments from three courses in canvas lms

#Import the Canvas class
from canvasapi import Canvas

#import settings from separate python file
from settings import API_URL, API_KEY
import requests
import json
import csv
import pandas as pd
import numpy as np
import xlsxwriter
from datetime import datetime

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#grab course using canvas course code
course = canvas.get_course(XXXXXX)

#PRINTS TO SCREEN FOR DEVELOPMENT ERROR CHECKING ONLY
# prints name of course and course id
print("Course name is ...",course)

#list given assignment numbers using named variable for three assignments
assignment = course.get_assignment(123456)
assignment1 = course.get_assignment(123789)
assignment2 = course.get_assignment(123999)

#get a list of submissions for these assignments using named variables again
submissions = course.list_submissions(123456)
submissions1 = course.list_submissions(123789)
submissions2 = course.list_submissions(123999)
  
      
#OPENS A CSV FILE STORED LOCALLY e.g. 'alpha.csv', THEN WRITES TO CSV writer.writerow contains list of headers for data
with open('ENTER FULL PATH OF CSV FILE TO WRITE DATA TO ', 'w', newline = '')as f:
   writer = csv.writer(f)
   writer.writerow(["COURSE", "SUBMISSION - ASSIGNMENT CODE AND USER ID", "ASSIGNMENT ID", "SUBMISSION SCORE","SUBMISSION ATTEMPS", "SUBMISSION DUE DATE", "SUBMISSION LATE", "SUBMISSION SECONDS LATE", "SUBMISSION SUBMITTED AT",
   "SUBMISSION TYPE","SUBMISSION GRADED DATE", "SUBMISSION GRADER ID", "SUBMISSION PREVIEW URL" ])

#STARTS A LOOP AND WRITES TO THE FILE THE DATA SPECIFIED
#write the list of assignment scores, 
   for submission in submissions:
      writer.writerow([course,submission, submission.assignment_id, submission.score, submission.attempt, submission.cached_due_date,  
       submission.late, submission.seconds_late, submission.submitted_at,submission.submission_type, submission.graded_at, submission.grader_id, submission.preview_url])

#after writing this data close the workbook
f.close()

#OPENS A CSV FILE STORED LOCALLY, THEN WRITES TO CSV e.g. 'beta.csv', THEN WRITES TO CSV writer.writerow contains list of headers for data
with open('ENTER FULL PATH OF CSV FILE TO WRITE DATA TO', 'w', newline = '')as f:
    writer = csv.writer(f)
    writer.writerow(["COURSE", "SUBMISSION - ASSIGNMENT CODE AND USER ID", "ASSIGNMENT ID", "SUBMISSION SCORE","SUBMISSION ATTEMPS", "SUBMISSION DUE DATE", "SUBMISSION LATE", "SUBMISSION SECONDS LATE", "SUBMISSION SUBMITTED AT",
   "SUBMISSION TYPE","SUBMISSION GRADED DATE", "SUBMISSION GRADER ID", "SUBMISSION PREVIEW URL" ])

    #write submissions data 
    for submission in submissions1:
      writer.writerow([course, submission, submission.assignment_id, submission.score, submission.attempt, submission.cached_due_date,  
       submission.late, submission.seconds_late, submission.submitted_at,submission.submission_type, submission.graded_at, submission.grader_id, submission.preview_url])

#after writing this data close the workbook
f.close()

#OPENS A CSV FILE STORED LOCALLY e.g. delta.csv, THEN WRITES TO CSV writer.writerow contains list of headers for data
with open('ENTER FULL PATH OF CSV FILE TO WRITE DATA TO', 'w', newline = '')as f:
   writer = csv.writer(f)
   writer.writerow(["COURSE", "SUBMISSION - ASSIGNMENT CODE AND USER ID", "ASSIGNMENT ID", "SUBMISSION SCORE","SUBMISSION ATTEMPS", "SUBMISSION DUE DATE", "SUBMISSION LATE", "SUBMISSION SECONDS LATE", "SUBMISSION SUBMITTED AT",
   "SUBMISSION TYPE","SUBMISSION GRADED DATE", "SUBMISSION GRADER ID", "SUBMISSION PREVIEW URL" ])

#STARTS A LOOP AND WRITES TO THE FILE THE DATA SPECIFIED
#write the list of assignment scores, 
   for submission in submissions2:
      writer.writerow([course,submission, submission.assignment_id, submission.score, submission.attempt, submission.cached_due_date,  
       submission.late, submission.seconds_late, submission.submitted_at,submission.submission_type, submission.graded_at, submission.grader_id, submission.preview_url])

#after writing this data close the workbook
f.close()

#PRINTS A SUCCESS MESSAGE TO SCREEN
print('SUCCESS! THIS ROUTINE HAS EXECUTED')

#at this stage you should have written three files in csv format containing data
print('#############################################')

#READ THE INPUT FILE TO CREATE DATAFRAMES USING PANDAS
dg = pd.read_csv('FULL PATH TO  alpha.csv')

#CREATE DATAFRAME TO CHANGE DATE TIME FORMATS FOR SUBMISSION DUE DATE, SUBMITTED AND GRADED DATE USING STRING FORMATTING
dg['SUBMISSION DUE DATE'] = pd.to_datetime(dg['SUBMISSION DUE DATE']).dt.strftime('%d/%m/%Y')
dg['SUBMISSION SUBMITTED AT'] = pd.to_datetime(dg['SUBMISSION SUBMITTED AT']).dt.strftime('%d/%m/%Y')
dg['SUBMISSION GRADED DATE'] = pd.to_datetime(dg['SUBMISSION GRADED DATE']).dt.strftime('%d/%m/%Y')

##Prints a confirmation for checking
print(dg)

#CREATE WRITER OBJECT AND DEFINE OUTPUT FILE USING XLSXWRITER  
writer = pd.ExcelWriter('FULL PATH TO first assignment worksheet 123456.xlsx', engine = 'xlsxwriter')
dg.to_excel(writer, sheet_name = '123456')

workbook = writer.book

#worksheet = workbook.add_worksheet('Data')
#worksheet = writer.sheets['123456']
#worksheet.write_formula()

writer.save()

print("123456 complete *****************************")

#READ THE INPUT FILE
df = pd.read_csv('FULL PATH TO  beta.csv')

#CREATE DATAFRAME TO CHANGE DATE TIME FORMATS FOR SUBMISSION DUE DATE, SUBMITTED AND GRADED DATE
df['SUBMISSION DUE DATE'] = pd.to_datetime(df['SUBMISSION DUE DATE']).dt.strftime('%d/%m/%Y')
df['SUBMISSION SUBMITTED AT'] = pd.to_datetime(df['SUBMISSION SUBMITTED AT']).dt.strftime('%d/%m/%Y')
df['SUBMISSION GRADED DATE'] = pd.to_datetime(df['SUBMISSION GRADED DATE']).dt.strftime('%d/%m/%Y')

#print(dg)

#CREATE WRITER OBJECT AND DEFINE OUTPUT FILE
writer = pd.ExcelWriter('FULL PATH TO first assignment worksheet 123789.xlsx', engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = '123789')

workbook = writer.book

#worksheet = workbook.add_worksheet('Data')
#worksheet = writer.sheets['123789']
#worksheet.write_formula()

writer.save()
print("123789 complete *****************************")

#READ THE INPUT FILE
df = pd.read_csv('FULL PATH TO  delta.csv')

#CREATE DATAFRAME TO CHANGE DATE TIME FORMATS FOR SUBMISSION DUE DATE, SUBMITTED AND GRADED DATE
df['SUBMISSION DUE DATE'] = pd.to_datetime(df['SUBMISSION DUE DATE']).dt.strftime('%d/%m/%Y')
df['SUBMISSION SUBMITTED AT'] = pd.to_datetime(df['SUBMISSION SUBMITTED AT']).dt.strftime('%d/%m/%Y')
df['SUBMISSION GRADED DATE'] = pd.to_datetime(df['SUBMISSION GRADED DATE']).dt.strftime('%d/%m/%Y')

#print(dg)

#CREATE WRITER OBJECT AND DEFINE OUTPUT FILE
writer = pd.ExcelWriter('FULL PATH TO first assignment worksheet 123999.xlsx', engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = '123999')

worksheet = writer.sheets['123999']
#worksheet.write_formula()

writer.save()
print("123999 complete *****************************")

#create three variables to hold the dat from the three worksheets
dr = pd.read_excel('C:/Users/wellsi/My Scripts/Chemistry/content/final/123456.xlsx')
ds = pd.read_excel('C:/Users/wellsi/My Scripts/Chemistry/content/final/123789.xlsx')
dt = pd.read_excel('C:/Users/wellsi/My Scripts/Chemistry/content/final/123999.xlsx')

#where we collate these three into one worksheet
writer = pd.ExcelWriter('FULL PATH TO the final report worksheet_totals.xlsx', engine = 'xlsxwriter')

#these are the three that we then write to excel worksheets within a workbook
dr.to_excel(writer, sheet_name = '123456')
ds.to_excel(writer, sheet_name = '123789')
dt.to_excel(writer, sheet_name = '123999')

#save the workbook after writing
writer.save()

#PRINTS A SUCCESS MESSAGE TO SCREEN
print('SUCCESS! THIS ROUTINE HAS EXECUTED, GO TO THE FILE worksheet_totals.xlsx TO SEE THE RESULTS')

