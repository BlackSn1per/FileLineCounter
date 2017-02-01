import os
print("This script counts the non-empty lines of a particular file")
print("Version 1.0")
print("By BlackSn1per \n")

print("Files in directory: ")
print(os.listdir())
print("\n\n\n")

while True:
	print("Write the file name (It has to be writted as shown in the list above. For example: 'one test.py'. Write it whithout quotation marks. It has to be in the list above)")
	file = input("")
	os.system('cls')
	try:
		with open(file) as myfile:
			count = sum(1 for line in myfile if line.rstrip('\n'))
			print ("File: " + file)
			print ("\n\nNumber of no empty-lines in file: " + str(count))
			break
	except:
		os.system('cls')
		print ("File: " + file)
		print("Invalid file name")
		print("")

input("Press any key to end the program")