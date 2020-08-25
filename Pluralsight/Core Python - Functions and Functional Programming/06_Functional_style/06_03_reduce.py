from functools import reduce
import operator
# print(reduce(operator.add, [1,2,3,4,5,6])) # 21


#==========================================================================
# numbers = [1,2,3,4,5]
# accumulator = operator.add(numbers[0], numbers[1])
# print(accumulator) # 3



#==========================================================================
# numbers = [1,2,3,4,5]
# accumulator = operator.add(numbers[0], numbers[1])
# for item in numbers[2:]:
#     accumulator = operator.add(accumulator, item)
# print(accumulator) # 15

#==========================================================================
def mul(x, y):
    print('mul {} {}'.format(x, y))
    return x * y
reduce(mul, range(1,10))
# print(reduce(mul, range(1,10)))
"""
mul 1 2
mul 2 3
mul 6 4
mul 24 5
mul 120 6
mul 720 7
mul 5040 8
mul 40320 9
"""
