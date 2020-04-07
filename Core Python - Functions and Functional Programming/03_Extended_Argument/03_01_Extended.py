# print("{a}========{b}".format(a = "Oslo", b = "Stavanger"))
#================================================================

# def hypervolume(*args):
#     print(args)
#     print(type(args))

# hypervolume()
# hypervolume(3,4)  # (3, 4)      <class 'tuple'>

# hypervolume(3,4, 5)   # (3, 4, 5)     <class 'tuple'>

#================================================================
# def hypervolume(*lenghts):
#     i = iter(lenghts)
#     v = next(i)
#     for lenght in i:
#         v *= lenght
#     return v

# print(hypervolume(2,4))   # 8
# print(hypervolume(2,4,6))  # 48
# print(hypervolume(2,4,6, 8))  # 384
#================================================================


def hypervolume(lenght, *lenghts):
    v = lenght
    for item in lenghts:
        v *= item
    return v

# print(hypervolume(3,5,7,9))  #945
# print(hypervolume(3,5,7))   # 105
# print(hypervolume(3,5))     # 15
# print(hypervolume(3))       # 3
print(hypervolume())    # TypeError: hypervolume() missing 1 required positional argument: 'lenght'












