import random
t1 = tuple(range(1,49))
t2 = tuple(range(1,19))
# I use tuples so I can get fresh unmuted lists out of them every time

def fiveNum(lt):
   """this function gives me set of 5 random numbers, they cannot all be
even or odd"""
   lst4 = []
   lst5 = []
   for i in range(5):
      x = lt[random.randint(0,len(lt)-1)]
      lst4.append(x)
      lt.remove(x)
   for a in lst4:
      lst5.append(a%2)
   if sum(lst5)==0 or sum(lst5)==5:
      fiveNum(list(t1))
   """this is how I fix scenerio when they are all odd or even"""
   return (lst4)

def oneNum(lt1):
   """this gives me a list of five numbers which are used as lucky ball numbers,
one per set of 5 numbers. They cannot be repited per set of five five digits combos"""
   lst6 =[]
   for i in range(5):
      x = lt1[random.randint(0,len(lt1)-1)]
      lst6.append(x)
      lt1.remove(x)
      print
   return(lst6)
   
lst7 = oneNum(list(t2))  
for i in range(5):
   print(fiveNum(list(t1))," ",lst7[i])
