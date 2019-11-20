fruits=[('banana',60,30),('apple',80,40),('kiwi',50,99),('melon',200,10),('orange',30,20)]
fruits.sort()
print(fruits)
fruits.sort(key=lambda row:row[0])
print(fruits)
fruits.sort(key=lambda row:row[1])
print(fruits)
fruits.sort(key=lambda row:row[2])
print(fruits)

