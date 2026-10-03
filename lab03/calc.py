f,s,q = float(input('Введите первое число: ')),float(input('Введите второе число: ')),input('Введите символ операции(+,-,*,/): ')
if q == '+':
    print(f+s)
elif q == '-':
    print(f-s)
elif q == '*':
    print(f*s)
elif q == '/':
    if s == 0:
        print('На ноль делить нельзя!')
    else:
        print(f/s)