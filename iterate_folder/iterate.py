import sys, os

rootdir = '/Users/dateng/Developer/python/iterate_folder'

def print_dir(dir, level=1):
"""	dir: directory to print
	level: how much deeper to go into the 'dir' folder
	Explore the folder specified by 'dir' directory. Print out the result
	with structural indentation
"""
	for token in os.listdir(dir):
		if os.path.isdir(os.path.join(dir, token)):
			print(" "*(level-1) + token);
			print_dir(os.path.join(dir, token), level+1)
			
def add_output_dir(dir):
	for token in os.listdir(dir):
		curr = os.path.join(dir, token)
		if os.path.isdir(curr):
			if token == "000" or token == "001":
				if not os.path.exists(curr + "_OUTPUT"):
					os.makedirs(curr + "_OUTPUT")
			else:
				add_output_dir(curr)
				
def remove_output_dir(dir):
	for token in os.listdir(dir):
		curr = os.path.join(dir, token)
		if os.path.isdir(curr):
			if token == "000" or token == "001":
				if os.path.exists(curr + "_OUTPUT"):
					print(curr + "_OUTPUT")
					os.rmdir(curr + "_OUTPUT")
			else:
				remove_output_dir(curr)			
			
# print_dir(rootdir)
# add_output_dir(rootdir)
remove_output_dir(rootdir)
