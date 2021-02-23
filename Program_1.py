#Write a program to input temperature in Celsius and Fahrenheit scale and convert the temperature to theother scale. Display the results .
cel = input("Input temperature in Celsius: ")
fah = input("Input Temperature in Fahrenheit: ")
fah1 = (float(cel) * 9/5) + 32
cel1 = (float(fah) - 32) * 5/9
print("The temperature in fahrenheit is :"+ str(fah1))
print("The temperature in Celsius is :"+ str(cel1))
