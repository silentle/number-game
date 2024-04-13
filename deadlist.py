for i in range(10,99):
    i1=i//10
    i2=i%10
    list=[]
    list2=[]
    while True:
        if i1+i2==10:
            list=[]
            break
        if [i1,i2] in list:
            print(i)
            list2.append(i)
            list=[]
            break
        list.append([i1,i2])
        i1=(i1+i2)%10
        i2=(i1+i2)%10
        #print(i1,i2)
        

        
        
    