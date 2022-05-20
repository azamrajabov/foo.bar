import numpy as np
from fractions import Fraction

def solution(m):
    if len(m) < 2:
        return [1,1]
    r_subm, q_subm = split_martix(m)
    f_subm = calc_f(q_subm)
    fr_subm = np.dot(f_subm, r_subm)
    return dec_to_frac_with_lcm(fr_subm[0])

def split_martix(m):
    absorbing = set()
    for row_i in range(len(m)):
        if sum(m[row_i]) == 0:
            absorbing.add(row_i)
    r_subm = []
    q_subm = []
    for row_i in range(len(m)):
        if row_i not in absorbing:
            row_total = float(sum(m[row_i]))
            r_temp = []
            q_temp = []
            for col_i in range(len(m[row_i])):
                if col_i in absorbing:
                    r_temp.append(m[row_i][col_i]/row_total)
                else:
                    q_temp.append(m[row_i][col_i]/row_total)
            r_subm.append(r_temp)
            q_subm.append(q_temp)
    return r_subm, q_subm

def calc_f(q_subm):
    return np.linalg.inv(np.subtract(np.identity(len(q_subm)), q_subm))

def dec_to_frac_with_lcm(l):
    ret_arr = []
    denoms = []
    for num in l:
        frac = Fraction(num).limit_denominator()
        ret_arr.append(frac.numerator)
        denoms.append(frac.denominator)
    lcd = 1
    for denom in denoms:
        lcd = compute_lcm(lcd,denom)
    for num_i in range(len(ret_arr)):
        ret_arr[num_i] *= int(lcd/denoms[num_i])
    ret_arr.append(lcd)
    return ret_arr

def compute_lcm(x, y):
    greater = x if x > y else y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

thelist = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
r = solution(thelist)
print(r)
assert r == [7, 6, 8, 21]

thelist = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
r = solution(thelist)
print(r)
assert r == [0, 3, 2, 9, 14]

