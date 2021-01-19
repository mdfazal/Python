# r -> allows only to read files
# w -> allows to write files and make changes 
# a -> allows to append in files meaning you can't edit whats in the file only add more to it.
# r+ -> allows to read and write and gives all the power of redaing and writing. 
employee_file = open("employees.txt", "r")

print(employee_file.readable())
#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()