#Filter - lazy
# filter(function, sequence)

# positives = filter(lambda x:x > 0, [1,-5,0,6,-2,8])
# print(list(positives)) # [1, 6, 8]

#==========================================================================

trues = filter(None, [0,1, False, True,[], [1,2,3], '', ' ', 'hello'])
print(list(trues)) # [1, True, [1, 2, 3], ' ', 'hello']
