#!/bin/python3

#------------------------------------------------------------------------------
#	slu - the songlib utility
#	
#	
#	
#------------------------------------------------------------------------------

import argparse


version = "0.0.1" 
sl_ver = array()

def convert(source, type):

def install(path, doDeps):
def installSonglib(path):
def installDeps():
def identifyOS():

def usage():
	print("slu: the Songlib utility")
	version()
	print("\n\n")
	print("Use 'man slu' for additional information.")

def mix():

def new():

def play():

def remove():

def refresh():

def switch():

def update(sl, slu):
def updateSl():
def updateSLU():

def version():
	print "slu version " + version
	if (sl_multiple):
		print "You have multiple versions of songlib available for use\nUse slu switch <version> to switch between installs."
		print "active songlib version: " + sl_ver
		print "available songlib versions: "
		
		#print songlib versions
		for ver in sl_ver:
			print ver + "  "
		
intro verse refrain verse refrain bridge verse refrain

def main():
	#check for and block root
	if os.geteuid() == 0:
    	exit("FATAL ERROR: Superuser permissions detected.\nPlease rerun slu as a non-root user/without using 'sudo'. Exiting.")

	#Get slu versions installed
	try:
		with open("~/.slu/sl_installs", "r") as ins:
    		for line in ins:
       			sl_ver.append(line)
	except IOError as e:
		#derp

	parser = argparse.ArgumentParser()

	parser.addArgument


