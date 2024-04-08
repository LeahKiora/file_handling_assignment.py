#open file for writing
file = open("my_file.txt", 'w')

#write some text to the file
file.write("Hello, there!\n")
file.write("First file handling.\n")
file.write("2024.\n")

#close the file
file.close()

#Open file for reading
file = open("my_file.txt", 'r')

#read contents of file
content = file.read()

#Print the contents of the file
print(content)

#close the file
file.close()

#append the file
file = open("my_file.txt", 'a')

file.write("Hey,\n")
file.write("I'm getting better\n")
file.write("at file handling\n")
file.close()

#Implementing error handling using try, except and blocks to manage potential file_related exceptions
try:
    # Open file for reading
    file = open("my_file.txt", 'r')
    
    # Read contents of file
    content = file.read()
    
    # Print the contents of the file
    print(content)
    
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
finally:
    # Close the file
    file.close()
