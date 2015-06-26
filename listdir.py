import os

def run(**args):

	print "[*] In listdir module."
	files = os.listdir(".")

	return str(files)