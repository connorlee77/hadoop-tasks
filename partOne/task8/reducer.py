#!/usr/bin/python

import sys

currStudentId = -1
currStudentGrades = ''
for line in sys.stdin:
    line = line.strip().split('.')
    
    #line is a student
    if len(line) == 3 and line[1] == 'student':
        currStudentId, _, name = line
        if currStudentGrades[-3:] != '-->':
            print currStudentGrades  
        currStudentGrades = str(name) + ' -->'
    
    #line is a mark
    elif len(line) == 4 and line[1] == 'mark':
        studentId, _, course, grade = line 
        if(studentId == currStudentId):
            currStudentGrades += ' (' + str(course) + ',' + str(grade) + ')'

if currStudentGrades[-3:] != '-->':
    print currStudentGrades
        
