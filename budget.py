from itertools import zip_longest
class Category:
      ledger = []
      deposit  = '1000.00'
      groceries = -10.15
      restaurant = -15.89
      Transfer =  '-50.00'
      Total = float(deposit) + groceries + restaurant + float(Transfer)
      print('*'*13 + 'Food' + '*'*13)
      print('initial deposit','{:>14}'.format(deposit))
      print('groceries','{:>20}'.format(groceries))
      print('restaurant and more foo','{:>2}'.format(restaurant))
      print('Transfer to Clothing','{:>9}'.format(Transfer))
      print('Total:',Total)
      print('Percentage spent by category')
      sum_spent = (-1*(float(groceries))) + (-1*(float(restaurant)))  + (-1*(float(Transfer)))
      round1 = ((-1*(float(Transfer)))*100)/sum_spent
      round2 = ((-1*(float(restaurant)))*100)/sum_spent
      round3 = ((-1*(float(groceries)))*100)/sum_spent
      if (round1 % 10) < 10:
           r1 = '{:.0f}'.format(round1 - (round1 % 10))
      if (round2 % 10) < 10:
           r2 = '{:.0f}'.format(round2 - (round2 % 10))    
      if (round3 % 10) < 10:
           r3 = '{:.0f}'.format(round3 - (round3 % 10))
      food = []
      clothing = []
      auto = []
      for i in range(0,int(r1) + 10,10):
           food.append(i)  
      for i in range(0,int(r2) + 10,10):
           clothing.append(i) 
      for i in range(0,int(r3) + 10,10):
           auto.append(i)        
      i = 100
      while i >= 0: 
            a = '{:3}'.format(i)
            b = '|'
            space1 = ' '
            space2 = ' '
            space3 = ' '
            for n in food:
                if n == i:
                    space1 += 'o'
            for n in clothing:
                if n == i:
                    space2 += 'o' 
            for n in auto:
                 if n == i:
                     space3 += 'o'             
            print(a,b,space1,' ',space2,' ',space3,sep = '') 
            i -= 10

object1 = Category()
Category()     
 
print(' '*3,'{:>10}'.format('-'*10)) 

str = 'Food'   
str1 = 'Clothing'        
str2 = 'Auto'

for x in zip_longest(str,''*2,str1,''*2,str2, fillvalue = ''):
    print(' '*4,'{:>6}'.format(' '.join(x)))
    