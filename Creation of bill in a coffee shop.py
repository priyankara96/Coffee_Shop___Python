
#ceylon      A.H.M.C.P.ATHAPATHTHU   {  IT 18 302 486  } 


na={1:'Espress',2:'Cafe Americano',3:'Cafe Latte',4:'Vanilla Latte',
    5:'Hazelnut Latte',6:'Butterscotch Latte',7:'Ice Coffee',8:'Ice Americano',
    9:'Frio Cappuccino',10:'Fri Caramel Coffee',11:'Macha Chocolate Marathon',
    12:'Frio Choco - Nut Blaste'}
price={1:250.0,2:250.0,3:300.0,4:330.0,5:330.0,6:330.0,7:330,8:330.0,9:350.0,10:350.0,
       11:400.0,12:400}

print(" ")
print(" **************************************************************************** ")
print(" ***************************                    ***************************** ")
print(" *************************         WELCOME        *************************** ")
print(" ************************            to            ************************** ")
print(" ************************     THE COFFEE HOUSE     ************************** ")
print(" *************************     --------------     *************************** ")
print(" ***************************                    ***************************** ")
print(" **************************************************************************** ")
print("\n")
print("        Item",' '*28,"Item Price")
print(" ")
print("        HOT COFFEE ")
print("     {0:2} {1:32}  Rs.250.00  ".format(1,na[1]))
print("     {0:2} {1:32}  Rs.250.00  ".format(2,na[2]))
print("     {0:2} {1:32}  Rs.300.00  ".format(3,na[3]))
print("     {0:2} {1:32}  Rs.330.00  ".format(4,na[4]))
print("     {0:2} {1:32}  Rs.330.00  ".format(5,na[5]))
print("     {0:2} {1:32}  Rs.330.00  ".format(6,na[6]))
print(" ")
print("        COOL COFFEE ")
print("     {0:2} {1:32}  Rs.330.00  ".format(7,na[7]))
print("     {0:2} {1:32}  Rs.330.00  ".format(8,na[8]))
print("     {0:2} {1:32}  Rs.350.00  ".format(9,na[9]))
print("     {0:2} {1:32}  Rs.350.00  ".format(10,na[10]))
print("     {0:2} {1:32}  Rs.400.00  ".format(11,na[11]))
print("     {0:2} {1:32}  Rs.400.00  ".format(12,na[12]))
print(" ")
print( "_"*78)
print(" ")

while True:
    opt=[]
    cnt=[]
    n=0
    while n>-1:
        opt.append(int(input('            Enter Item Code : ')))
        if opt[n]==0 :
            break
        else:
            m=opt[len(opt)-1]
            print(' Item :  {0:27} Enter Quantity :   '.format(na[m]),end="")
            cnt.append(int(input()))
            n+=1
            print("\n")
        
    pr=[]
    n=0
    for num in cnt:
        pr.append(float(num*price[opt[n]]))
        n+=1
    print(' ')
    x=0
    tot=0.0
    for n in opt:
        if n>0:
            print('  {0:25}   Rs.{1:.7}'.format(na[n],pr[x]))
            tot+=pr[x]
            x+=1
    print("\n")
    print('  {0:25}   Rs.{1:.7}'.format('Total = ',tot))
    print("_"*78)
    print("\n")


