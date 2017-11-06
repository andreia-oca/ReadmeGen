#!/usr/bin/python3

"""

Readme template generator

"""
import sys, getopt

#Default values
title = "Homework 1"
height = 5
width = 70
character = '='
subtitle = "Task"
no_subtitle = 5	

#Command Arguments
options = "hT:t:n:"
long_options = ["help", "title=", "subtitle=", "height=", "width=", \
		"character="]

#Parsing command line arguments
try:
	opts, args = getopt.getopt(sys.argv[1:], options, long_options)
except getopt.GetoptError:
	print("Unrecognized option.\nTry --help for more information.")
	sys.exit(2)
for opt, arg in opts:
	if opt in ("-h", "--help"):
		print("Usage: ")
		sys.exit()
	elif opt in ("-T", "--title"):
		title = ' ' + arg + ' ' 
	elif opt in ("-t", "--subtitle"):
		subtitle = ' ' + arg + ' '
	elif opt in ("-n"):
		no_subtitle = int(arg)
	elif opt in ("--height"):
		height = int(arg)
	elif opt in ("--width"):
		width = int(arg)
	elif opt in ("--character"):
		character = arg

#Template
for i in range(int(height/2)):
	print(''.center(width, character))

print(title.center(width, character))

for i in range(int(height/2)):
	print(''.center(width, character))

for i in range(1, no_subtitle + 1):
	print('')
	print((' ' + subtitle + ' ' + str(i) + ' ').center(width, character))
	print('')


