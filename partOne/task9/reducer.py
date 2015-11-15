#!/usr/bin/python

import sys

currStudentId = -1
currStudentAvg = 0
currStudentName = ''
numGrades = 0
for line in sys.stdin:
    line = line.strip().split('.')
    
    #line is a student
    if len(line) == 3 and line[1] == 'student':
        currStudentId, _, newName = line
        
        if currStudentAvg != 0 and numGrades > 4:
            print("{0}.{1}".format(currStudentName, int(round(float(currStudentAvg) / numGrades))))    
       
        currStudentName = newName
        numGrades = 0
        currStudentAvg = 0 
    #line is a mark
    elif len(line) == 4 and line[1] == 'mark':
        studentId, _, course, grade = line 
        if(studentId == currStudentId):
            currStudentAvg += int(grade)
            numGrades += 1
if currStudentAvg != 0 and numGrades > 4:
    print("{0}.{1}".format(currStudentName, int(round(float(currStudentAvg) / numGrades))))
        
