print("Welcome to our Python calculator")
print("--------------------------------")

n1 = int(input('Please enter first number: '))

n2 = int(input('Please enter second number: '))

sum = n1+n2
sub = n1-n2
mul = n1*n2
divide = n1/n2

print(f'{n1} + {n2} = {sum}')
print(f'{n1} - {n2} = {sub}')
print(f'{n1} * {n2} = {mul}')
print(f'{n1} / {n2} = {divide}')
