def function(list):
    i=0
    a=[]
    while i<len(list):
        if list[i]%2==0:
            a.append(list[i])
        i+=1
    print(a)
list=[1,2,3,4,5,6,7,8,9]
function(list)