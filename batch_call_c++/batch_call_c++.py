import sys, os
import subprocess

program = '/Users/dateng/Developer/python/batch_call_c++/program/atomic'
command_args = ["/dir1", \
                "/dir2"]

command_args_2 = [\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E2_600um_60um_2",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E3_700um_60um",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E4_800um_60um",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E5_900um_60um",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E6_800um_60um_redo",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E6_800um_60um_redo_redo",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E7_900um_60um_redo",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E8_S105-300",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E9_60um",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E9_60um_redo",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E9_R0307-300",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E9_R0307-300_redo",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E10_60um_",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E10_R0406",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E10_R0406-300_redo",\
"C:/Users/Yibo/Desktop/20170224_optimize_chamber/E11_S105-300_redo"]

dev_args = ['/DEVICE_2', '/DEVICE_3']
index_args = ['/000', '/001']

def batch_call_cpp(prog, args, devs, idxs):
	for token in args:
		for dev in devs:
			for idx in idxs:
				p = subprocess.Popen([prog, token+dev+idx], stdout=subprocess.PIPE)
				# print(p.communicate())
				# Grab stdout line by line as it becomes available. This will loop until 
				# p terminates.
				while p.poll() is None:
					l = p.stdout.readline() # This blocks until it receives a newline.
					print(l)
				# When the subprocess terminates there might be unconsumed output 
				# that still needs to be processed.
				# print(p.stdout.read())
		
		
batch_call_cpp(program, command_args_2, dev_args, index_args)