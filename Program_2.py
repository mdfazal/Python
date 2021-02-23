Money = input("Enter the amount of money: ")
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
print("Number of Hundred notes :"+ num_hun)
print("Number of Fifty notes :"+ num_fif)
print("Number of Ten notes: "+num_ten)
print("Number of five notes: "+ num_five)
print("Number of two notes: "+ num_two)
print("Number of one notes: "+ num_one)

