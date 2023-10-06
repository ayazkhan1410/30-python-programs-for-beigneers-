'''Day 13 of '30 days of 30
   Programs challenege '''
   
   
'''
Convert : 🔽
Kilo meter --> Miles
'''

user_input = float(input("Enter Kilometers : "))

miles = 0.621371
result = user_input * miles

x = round(result,2)
print(f"Total Miles : {x}")