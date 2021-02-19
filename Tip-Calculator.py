print('Welcome to tip calculator')
bill = float(input('Please enter your bill amount:$ '))
split = int(input('How many people are splitting the bill: '))
tip =int(input('What percentage of tip you want to give 10,12,15?   ')) 
tip_as_percent = tip / 100
total_tip_amount =bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / split
result = round(bill_per_person,2)
print(f"Each person have to pay:  {result}")
