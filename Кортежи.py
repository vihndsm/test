# кортеж не меняемый, но можно использовать список внутри картежа
# A=(1, 2, 3, [])
# A[3].append(4)
# B=list(A)
# print(B)
# print(tuple(B)) 

# В Python можно использовать кортежи, чтобы присваивать значение несколь- ким переменным сразу:
# a=('f', 5, True)
# (x, y, z)=a
# print(x,y,z)

# B=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY)=range(1,8)
# print(MONDAY)

# a=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print([i[:-1]+(100,) for i in a])