def solution(xs):
	max_value = xs.pop(xs.index(max(xs)))
	negatives = list(filter(lambda x: x<0, xs))
	if len(negatives) % 2:
		xs.pop(xs.index(max(negatives)))
	for i in xs:
		if i:
			max_value *= i
	return str(max_value)



#print('the number:')
#x = input()
print(solution([-2, -3, 4, -5]))



"""
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17
				9
				i
				  10
				  i+1
"""