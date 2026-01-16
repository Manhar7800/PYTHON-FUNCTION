l1=["python","java","flutter","php"]

l2=list(map(lambda sub:len(sub),l1))

print(l2)

print("------------------------------------------------")
d1=dict(map(lambda sub:(sub,len(sub)),l1))
print(d1)

print("--------------------------------------------------")
l1=[12,2,6,78,90,45]

def myfun(num):
    if num%2==0:
        return True
    else:
        return False
print("---------------------------------------------------")
    
l2=list(map(myfun,l1))
print(l2)


l2=list(map(lambda num:num%2==0,l1))
print(l2)