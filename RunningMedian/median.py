from __future__ import division
import sys

def openFile(file):
	with open(file) as fp:
		running_edian = runningMedian(fp.readline());
		running_edian.readLines(fp)

class runningMedian:

	def __init__(self, line):
		self.no_of_values = 0
		self.is_first_line = False
		self.values = []
		self.list_length = 0
		self.line = line

	def readLines(self, fp):
		print "\033[1;32;40mOutput \033[1;34;40m \n"
		while self.line:
			if self.is_first_line is False:
				self.no_of_values = int(self.line.strip())
				self.is_first_line = True
			else:
				self.values.append(int(self.line.strip()))
				self.values.sort()
				middle_element = self.findMiddle(self)
				print middle_element
			self.line = fp.readline()
		print "\033[0;37;40m \n"

	@staticmethod
	def getLength(self):
		return len(self.values)

	@staticmethod
	def findMiddle(self):
		self.list_length = self.getLength(self)
		if self.list_length % 2 != 0:
			return float(self.values[int(self.list_length/2)])
		else:
			return ((self.values[int(self.list_length/2)] + self.values[(int(self.list_length/2) - 1)]))/2

print "Choose sample data from below to run the test case with:\n"
print "========"
print "1. Inpunt file 000\n"
print "2. Inpunt file 001\n"
print "2. Inpunt file 002\n"
print "2. Inpunt file 003\n"
print "2. Inpunt file 004\n"

print "Enter your choice and hit enter\n"
sample_input = raw_input("prompt: ")

sample_file = ["./input00.txt", "./input01.txt", "./input02.txt", "./input03.txt", "./input04.txt"]

result = {
  '1': lambda x: openFile(x),
  '2': lambda x: openFile(x)
}[sample_input](sample_file[int(sample_input)-1])
		


