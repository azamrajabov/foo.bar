"""
31->32->16->8->4->2->1
31->30->15->16->8->4->2->1
"""
def solution(n):
    n = int(n)
    step = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        elif n==3 or (n+1)&n > (n-1)&(n-2):
            n -= 1
        else:
            n += 1
        step += 1
    return step

#print('the number:')
#x = input()
#print(solution(x))
# pow(16, 1.0/4)

r = solution('15')
print(r)
assert r == 5

r = solution('4')
print(r)
assert r == 2
