def solve(a,b):
    return b if a ==0 else solve(b%a,a)

print(solve(20,50))

a=3
b=1
print(a,b)
print('\r')
a,b=b,a
print(a,b)

def check(a):
    print("EVEN" if a%2==0 else "ODD")

check(12)

example = ["Sunday","Monday","Tuesday","Wednesday"]
print(example[-3:-1])

def is_even(number):
    message = f"{number} is an even number" if number%2==0 else f"{number} is an odd number"
    return message

print(is_even(54))

dict1 ={'first':'sunday','second':'monday'}
dict2 = {1:3,2:4}
dict1.update(dict2)
print(dict1)

a= {'Hello':'World','First':1}
b= {val:k for k, val in a.items()}
print(b)

a="4,5"
nums=a.split(',')
x,y =nums
int_prod = int(x)*int(y)
print(int_prod)


def tester(**kwargs):
    for key, value in kwargs.items():
        print(key, value, end=" ")

tester(Sunday = 1, Monday=2, Tuesday=3, Wednesday=4)

set1={1,3,5}
set2={2,4,6}
print(len(set1) +len(set2))

a= (2**3 +5**2)
print(a)






