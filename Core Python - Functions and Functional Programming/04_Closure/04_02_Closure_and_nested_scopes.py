#Closure
# def enclosing():
#     x = 'closed over'
#     def local_func():
#         print(x)
#     return local_func()
# lf = enclosing() # closed over
# lf  # closed over


#================================================================
# Function Factories
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

# sqaure = raise_to(2)
# print(sqaure(5)) #25
# print(sqaure(9)) #81
# print(sqaure(10)) # 100

square = raise_to(3)
print(square(5)) #125
print(square(9)) #729
print(square(10)) # 1000




#================================================================





#================================================================




#================================================================







#================================================================
