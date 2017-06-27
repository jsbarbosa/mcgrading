from grading import *

desired = ['cargas.py', 'integral.py']

def convertAll(files):
    for file in files:
        convert2to3(file)

def testCargas():
    importFile('cargas')
    if not fileExists('cargas.pdf'):
        raise FileMissing('Cargas.pdf')

def testIntegral():
    importFile('integral')
    if not fileExists('num_integral.pdf'):
        raise FileMissing('num_integral.pdf')
    if not fileExists('err_integral.pdf'):
        raise FileMissing('err_integral.pdf')

cleanFiles(getTxtFiles())

convertTask = Task(convertAll, args=(desired, ))
cargasTask = Task(testCargas, timeout=120)
integralTask = Task(testIntegral, timeout=120)

tasks = [convertTask, cargasTask, integralTask]

students = Classroom(getZipFiles(), tasks)
students.undesired(desired)
students.addStudentsTasks()
students.runTasks()
students.saveResults('hw1.csv')

cleanMACOS()
