#Scientific Simulator
import random

l = []
#Create an empty list

for i in range(50):
    l.append(random.randint(1, 365))
    #append 30 random numbers within 1 to 365
l.sort() 
print(l)
i = 0
flag = 0 #denotes that there is no repetition
m = []
while(i < (len(l)-1)):
    if(l[i] == l[i+1]):
        flag = 1
        m.append(l[i]) #All occurences of repetition are recorded.
        pass
    i += 1
if(flag == 1):
    print('Repeats')

if(flag == 0):
    print('There is no repetition')
    
print(m)
    
        