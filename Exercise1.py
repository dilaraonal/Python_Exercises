### QUESTION 1
    
my_str = 'TR29abcdqxw10Casd1923yhdf23askdjl04ajdfguj19akflk05ssfýj30lkhu08akdf'
sum_numbers = 0 # for sum  of numbers in my_str
num_count = 0 # for average calculation

for i in my_str:
    if i.isdigit(): #isdigit() # method returns True when it finds a number in the string.
        sum_numbers += int(i)   # when adding these numbers, turned integer numbers that in my_str
        num_count += 1    # Finds how many numbers are in the string
        
# turned float data type because result of divide may be decimal
average = float(sum_numbers / num_count)
#display results of calculation
print("The sum of the numbers in the string: ", sum_numbers)        
print("Average of numbers in the string: ", average)
