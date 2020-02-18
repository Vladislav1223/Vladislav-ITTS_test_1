a=[56, 76, 56, 87]#16  Серебренніков Дмитро
b=list(filter(lambda x: x%2==0, a))
for i in a:
    if i in b:
        print('yes')
    else:
        print('no')
print(b)
