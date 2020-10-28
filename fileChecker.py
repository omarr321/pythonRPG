#!/usr/bin/env python3

import os
import shutil

tempDir = os.path.join(os.getcwd(), "temp") 

# This def will search for the files that you give it
# and move them to the destinationDir.
# If notFlAG = True, it will move all files but the files
# you spicfie.
def moveFileList(searchDir, fileList, destinationDir, notFlag = False):
	if not os.path.isdir(os.path.join(os.getcwd(), searchDir)):
		return False

	(_, _, files) = next(os.walk(searchDir))
	for f in files:
		if notFlag:
			flag = True
			for fi in fileList:
				if f == fi:
					flag = False
			if flag:
				shutil.move(os.path.join(searchDir, f), os.path.join(destinationDir, f))
		else:
			for fi in fileList:
				if f == fi:
					shutil.move(os.path.join(searchDir, f), os.path.join(destinationDir, f))
					break

def movefList(stepCounter, searchDir, fileList, notFlag=False):
	print("(%d/%d) Moving files in %s..." % (stepCounter[0], stepCounter[1], searchDir), end="")
	moveFileList(searchDir, fileList, "temp", notFlag=notFlag)
	print("Done!")

# This will search the directory for the directory name
# and move those directory to the destination folder.
# if notFlAG = True, it will move all directory but the
# ones listed
def moveDirs(searchDir, dirList, destinationDir, notFlag = False):
	if not os.path.isdir(os.path.join(os.getcwd(), searchDir)):
		return False

	(_, dirs, _) = next(os.walk(searchDir))

	for d in dirs:
		if notFlag:
			flag = True
			for di in dirList:
				if d == di:
					flag = False
			if flag:
				shutil.move(os.path.join(searchDir, d), destinationDir)
		else:
			for di in dirList:
				if d == di:
					shutil.move(os.path.join(searchDir, d), destinationDir)
					break
	return True

# This def will call moveDirs with the prams and print out a nice output to terminal
# see moveDirs
def moveDir(stepCounter, printString, searchDir, dirList, notFlag=False):
	print("(%d/%d) Moving directories in %s..." % (stepCounter[0], stepCounter[1], printString), end="")
	moveDirs(searchDir, dirList, "temp", notFlag=notFlag)
	print("Done!")

# This will search the directory for the file extension
# and move those files to the destination folder.
# if notFlAG = True, it will move all files but the file extension
def moveFiles(searchDir, fileExtension, destinationDir, notFlag = False):
	if not fileExtension.startswith("."):
		fileExtension = "." + fileExtension

	if not os.path.isdir(os.path.join(os.getcwd(), searchDir)):
		return False

	(_, _, files) = next(os.walk(searchDir))
	for f in files:
		if notFlag:
			if not f.endswith(fileExtension):
				shutil.move(os.path.join(searchDir, f), os.path.join(destinationDir, f))
		else:
			if f.endswith(fileExtension):
				shutil.move(os.path.join(searchDir, f), os.path.join(destinationDir, f))
	return True

# This def will call moveFiles withtn he prms and print out a nice output to terminal
# see moveFiles
def moveFile(stepCounter, printString, searchDir, fileExtension, notFlag=False):
	print("(%d/%d) Moving %s files..." % (stepCounter[0], stepCounter[1], printString), end="")
	moveFiles(searchDir, fileExtension, "temp", notFlag=notFlag)
	print("Done!")

def main():
	totalSteps = 0

	print("(0/%d) Starting file check...Error: Fuck off it is not done!" % totalSteps)
	
	#os.mkdir(tempDir, mode=0o777)

if __name__ == "__main__":
	raise NotImplementedError("This file is not done yet!")

	if (os.path.isdir(tempDir)):
		shutil.rmtree(tempDir)
	main()