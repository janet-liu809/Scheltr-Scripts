# Scheltr-Scripts

# Print python test
import random

# Define student class
# name
# school
# distance
# number of roomates
# start month 
# term selections
# gender??
# roomate gender same?
class Student:
	"""docstring for ClassName"""
	def __init__(self):
		self.name = ""
		self.school = ""
		self.distance = ""
		self.roommateNum = ""
		self.startMonth = ""
		self.termSelectionBinary = ""
		self.gender = ""
		self.co_ed = ""

	def Print(self):
		print "**********************"
		print self.name
		print "**********************"
		print "School: " + self.school
		print "Distance: " + self.distance
		print "Number of Roommates: " + self.roommateNum
		print "Start Month: " + self.startMonth
		print "Terms: " + self.termSelectionBinary
		print "Gender: " + self.gender
		print "Co-Ed: " + str(self.co_ed)
		print "\n\n"

def StudentFactory(studentNumber, name):

	# have list of students
	students = []
	# for each studentNumber create a random student
	for x in range(1, studentNumber+1):
		tmp = Student()
		tmp.name = name + str(x)
		tmp.school = str(random.sample(['Waterloo' ,'Laurier'],1))
		#schoolNameNum = random.sample([1,2],1)
		#if schoolNameNum == 1:
		#	tmp.school = 'Waterloo'
		#elsif schoolNameNum == 2:
		#	tmp.school = 'Laurier'


		tmp.distance = str(random.sample([1, 5, 10], 1)) + 'k'
		tmp.roommateNum = str(random.sample([1, 2, 5],1))
		tmp.termSelectionBinary =  random.choice('1234567') 
		tmp.gender = random.choice('MF')
		tmp.co_ed = random.choice('YN')
		students.append(tmp)

	return students

students = StudentFactory(20, "derp")

for student in students:
	student.Print()
  
# mystudent = Student()
# mystudent.name = "frank"
# mystudent.school = "uWaterloo"
# mystudent.distance = "1k"
# mystudent.roommateNum = "5+"
# mystudent.startMonth = "January"
# mystudent.termSelectionBinary = "7"
# mystudent.gender = "M"
# mystudent.co_ed = True

# Create 2000

# factory
# name is variable

# randomizer
# school 70%waterloo 30%laurier

# distance 1k, 5k, 10k
# roomate number 1,2+,5+
# start month Jan, May, Sept
# term selection binary 1-7
# gender 50/50
# gender same 60%same 40%dont care


# Print each student out.
# mystudent.Print()


