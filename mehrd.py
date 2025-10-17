import json
numbers=[0,1,2,3,4,5,6,7,8,9,]
#numbers.extend([12])
#print(numbers)


"""numbers2=[10,11,12,13,14,15,]
numbers+=numbers2
print(numbers)
for item in  (4,5,6) :
    numbers.append(item)
print(numbers)"""
 


#numbers+=numbers2*1
#print(numbers)

#numbers[len(numbers): ] = [10,11,12]
print (numbers) 
import operator 
operator.iadd(numbers,[6,7,8])
print(numbers)