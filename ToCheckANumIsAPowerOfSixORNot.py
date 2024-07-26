'''Power of 6,, Given an integer n,return true if it is a power of six.otherwise
,return false.An integer n is a power of six,if there exists an integer x such that
n==6^x.example: I/P:36 O/P:True'''


#n = int(input())

#Without recursion

'''while(True):
    if n < 1:
        print(False)
        break
    if n == 1:
        print(True)
        break
    if n % 6 != 0:
        print(False)
        break
    n = n // 6

while n!=1:
    if n%6==0:
        n//=6
    else:
        print("false")
        break
else:
    print("true")'''


#With recursion
    
def six(n):
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 6 != 0:
        return False
    return six(n // 6)

n = int(input())
print(six(n))

