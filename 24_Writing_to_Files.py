#write to file will remove all the data and will write only this. You can also create file with this and then write in it.
employee_file = open("employees1.txt", "w")
#append to file will keep all the data and add these to it.
#employee_file = open("employees.txt", "a")
employee_file.write("\nToby - HR")
employee_file.write("\nKelly - Customer service")
#print(employee_file.read())
employee_file.close()
