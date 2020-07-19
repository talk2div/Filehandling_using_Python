# Below are the steps that we will follow:
# 1. Creating a file using write mode
# 2. Create a new file called as random_data
# 3. Writes data in a file
# 4. Close the file

file = open("random_data.txt","w")
file.write("Hello Random World")
file.close()

# Lets Add few lines again using write mode 
# Check the result 
# It will overwrite the previous result and new file 
# will not be created as file is already present 
# with the same name.

file = open("random_data.txt","w")
file.write("Overriding the result using random stuffs\n")
file.close()

# To avoid over overwrite let's using the append mode
# In append mode, new content will be added at the end of the line. 

file = open("random_data.txt","a")
file.write("I am appending new data to avoid overwrite\n")
file.write("Adding few more lines\n")
file.write("Adding more and more lines\n")
file.close()

# Let's start reading the files 
# For reading, files need to open in read mode 

file = open("random_data.txt","r")
print("Reading the file:\n", file.read())

# Will try to again read the file
print("Again Reading the file:\n", file.read())

# Output is blank !!! How ? The file is reached at the end. # For again reading you must reset the file pointer using 
# seek()
file.seek(0)
print("Again Reading the file But after seek(0):\n", file.read())

# Let's read the individual lines using readline() but 
# first do the seek(0)
file.seek(0)
print("Reading individual lines (1st line) of file :\n", file.readline())
print("Reading individual lines (2nd line) of file :\n", file.readline())
print("Reading individual lines (3rd line) of file :\n", file.readline())

# Let's read all the lines using readlines() which 
# returns complete list of lines but first do the seek(0)
file.seek(0)
print("I am reading ALL the lines:\n", file.readlines(), "\n")

# Let's read a file using loop first do the seek(0)
# Using loop is the most simple and gracefull 
# method of accessing the file
file.seek(0)
print("Reading lines using loop:")
for line in file:
  print(line)

file.close()
