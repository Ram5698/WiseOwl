Prime_Numbers =[]
Numbers =""
First = True
for i in range (2,100,1):
    prime_Number=True
    # print(i)
    if i==2:
        # print(i)
        continue
    for j in range(2,i,1):
        if i%j==0: 
            # print("Not Prime Number ",i,j)
            prime_Number = False
            break

    if prime_Number ==True:
        if First==True:
            Numbers=Numbers+str(2)+","+str(i)
            First=False
        else:
            Numbers=Numbers+","+str(i)
        #print(i) 

print(Numbers)
List=Numbers.split(",")

for i in List:
    print(i)
            
            
 
    