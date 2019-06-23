import sys
import re
import json

with open("./key-words.json") as f:
	key_words = json.load(f);

def openFile(file):
	with open(file) as fp:
		mouse_vs_mouse = mouseVsMouse(fp.readline());
		mouse_vs_mouse.readLines(fp)

class mouseVsMouse:

	def __init__(self, line):
		self.no_of_values = ""
		self.is_first_line = False
		self.line = line

	def readLines(self, fp):
		print "\033[1;32;40mOutput \033[1;34;40m \n"
		while self.line:
			if self.is_first_line is True:
				self.no_of_values = (re.sub(r'[^\w\s]','',self.line.lower().strip())).split(" ")
				result =  any(elem in key_words["computer_vocab"]  for elem in self.no_of_values)
				if result:
   					print 'Computer-Mouse'
   				result =  any(elem in key_words["animal_vocab"]  for elem in self.no_of_values)
   				if result:
   					print 'Animal'			
			else:
				self.is_first_line = True
			self.line = fp.readline()
		print "\033[0;37;40m \n"
		

print "Choose sample data from below to run the test case with:\n"
print "========"
print "1. Inpunt file 001\n"
print "2. Inpunt file 002\n"

print "Enter your choice and hit enter\n"
sample_input = raw_input("prompt: ")

sample_file = ["./input00.txt", "./input01.txt"]

result = {
  '1': lambda x: openFile(x),
  '2': lambda x: openFile(x)
}[sample_input](sample_file[int(sample_input)-1])
		


 






