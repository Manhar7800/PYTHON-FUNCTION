ans=lambda a:a+10

print(ans(10))

#without lambda
def findsqr(num):
    return num*num

print(findsqr(5))

#with lambda

aqr_ans = lambda num : num*num
print(aqr_ans(5))

ans=lambda num:num%2==0
print(ans(12))