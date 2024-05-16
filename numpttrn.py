
for i in range(1,6) :

      for j in range(1,i+1) :
          print(j,end=' ')
          j+=1
      print()

# 

rows=6
for i in range(rows):
    for j in range(i):
        print(i,end=' ')
    print('')    

# rows=6
# for i in range(rows):
#      for j in range(i):
#           print(i,end=' ')  
#      print('')

for i in range(1,6):
    for j in range(6-i):
        print(i,end=' ')
          
    print('')