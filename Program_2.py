Mon = input("Enter the amount of money: ")
Money = int(Mon)
num_hun  = Money/100
Money =  Money%100
num_fif = Money/50
Money =  Money%50
num_ten = Money/10
Money = Money%10
num_five = Money/5
Money = Money%5
num_two = Money/2
Money = Money%2
num_one = Money/1
Money = Money%1
print("Number of Hundred notes : "+ str(int(num_hun)))
print("Number of Fifty notes :"+ str(int(num_fif)))
print("Number of Ten notes: "+ str(int(num_ten)))
print("Number of five notes: "+ str(int(num_five)))
print("Number of two notes: "+ str(int(num_two)))
print("Number of one notes: "+ str(int(num_one)))

