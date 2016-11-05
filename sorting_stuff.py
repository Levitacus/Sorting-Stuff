import random
from datetime import datetime

class MyList():
	def __init__(self, list):
		self.list = list
		
	def fill_list(self, elements):
		for element in range(0, elements):
			i = int(random.random() * 100000)
			self.list.append(i)
		return self.list
			
	def shuffle_list(self):
		random.shuffle(self.list)
		return self.list
	
	def insertion_sort(self):
		for index in range(1, len(list)):
			value = list[index]
			position = index
			while position > 0 and list[position-1]>value:
				list[position] = list[position-1]
				position = position-1
				
			list[position] = value
			
	def selection_sort(self):
		for index in range(0, len(list)):
			for i in range(index, len(list)):
				value = list[index]
				if list[i]<list[index]:
					list[index] = list[i]
					list[i] = value
	
	def bubble_sort(self):
		for index in range(0, len(list)):
			for i in range(len(list)-1, index, -1):
				value = list[index]
				if list[i]<list[index]:
					list[index] = list[i]
					list[i] = value
					
	def shell_sort(self):
		for index in range(int((len(list)/4)+1)):
			top = list[index]
			bottom = list[len(list)-index-1]
			if top>bottom:
				list[index] = bottom
				list[len(list)-index-1] = top
		self.insertion_sort()
		
		#Add in more sorting algorthms.
		
		
					
list = []			
my_list = MyList(list)

print "Choose an amount of numbers you want in your list."
my_list.fill_list((int)(raw_input("> ")))
print my_list.list

def f(input):
	while True:
		print "Which sorting type do you want?"
		input = raw_input("> ")
		input = input.lower()
		start = datetime.now()
		try:
			sorting_method = {
				"insertion": my_list.insertion_sort(),
				"selection": my_list.selection_sort(),
				"bubble": my_list.bubble_sort(),
				"shell": my_list.shell_sort()
			}[input]
			time = (datetime.now() - start).total_seconds()
			print time
			return(sorting_method)
		except KeyError:
			print "Oops! That wasn't a valid sort type. Try again!"
		
f(input)