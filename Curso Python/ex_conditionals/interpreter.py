expression=(input('Enter an expression'))
x, y, z = expression.split(" ")
if y=='+':
    print(float(int(x)+int(z)))
elif y=='-':
    print(float(int(x)-int(z)))
elif y=='*':
    print(float(int(x)*int(z)))
elif y=='/':
    print(float(int(x)/int(z)))
else:
    print('Introduce the expression again')
