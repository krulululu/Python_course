for x in range(56,101):
    print(2*x**2+2*x+2)

print('-'*30)

#print("Insert your value here:")
try:
    x = int(input("Your value:"))
except ValueError:
    print("It isn't a int")
def factorial(x):
    if x < 0:
        return ("Insert positive number")
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
print("Factorial value is:", factorial(x))

print('-'*30)

#list1 = [1, 42, 1, 1]
print("Insert values:")
arr = list(map(int, input().split()))
print("min value:", min(arr))
min_element = min(arr)
indexes = []
for i in range(len(arr)):
    if arr[i] == min_element:
        indexes.append(i)
print("Indexess:", indexes)
#print("min value:", min(list1))

print('-'*30)

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-20,20,100)
y = (2*x-2)**3
plt.plot(x,y, color="darkblue", lw=2)
plt.xlabel("oś x")
plt.ylabel("oś y")
plt.title("plot", fontsize=20)
plt.show()














