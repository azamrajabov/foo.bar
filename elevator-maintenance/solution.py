def solution(l):
    s = [i for i in sorted(map(f, l), key=lambda x: (x[0], x[1], x[2]))]
    return ['.'.join([str(i) for i in v if i>=0]) for v in s]

def f(i):
    series = i.split('.')
    return [int(x) for x in series + ['-1']*(3-len(series))]

thelist = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
r = solution(thelist)
print(r)
assert r == ['0.1','1.1.1','1.2','1.2.1','1.11','2','2.0','2.0.0']

thelist = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
r = solution(thelist)
print(r)
assert r == ['1.0','1.0.2','1.0.12','1.1.2','1.3.3']
