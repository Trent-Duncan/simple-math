# Trent Duncan
# 9/25/24
# basic math practice1

num1=float (5)

num2= float (2)
sum= num1 + num2
diffrence= num1 - num2
product= num1 * num2
quotient= num1 / num2

print(f'{num1} plus {num2} = {sum}')
print(f'{num1} minus {num2} = {diffrence}')
print(f' {num1} * {num2} = {product}')
print(f'{num1} devided by {num2} = {quotient}')


# Area Calculation

length=float( input('please enter the length of the rectangular room (in feet)\n'))
width= float(input('now please enter the width of the rectangular room (in feet)\n'))


area= length * width 
print(f'the area of the rectangular room is {area}sq feet')





# Formatting Numeric Output

name= 'Trent'
age= "16"
favorite_color= "blue"
message= "Hello my name is {0} and i am {1} years old my favorite color is {2}." .format(name,age,favorite_color)
print(message)



# Grocery Store Calculation

SALES_TAX_RATE = 0.06

# INPUT
apple = 1.19
chips = 4.99
pop = .89




# PROCESS (Do the math/calculation(s))
# Find the sum of the three items we want to buy (subtotal)
subtotal = apple + chips + pop

sales_tax = subtotal * SALES_TAX_RATE

grand_total = subtotal + sales_tax

# OUTPUT

