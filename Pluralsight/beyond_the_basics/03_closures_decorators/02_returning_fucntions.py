# def counter():
#     def inner():
#         print("inner")
#
#     inner()


# print(counter())
# counter()

# i = counter()
# i()
# ================
def enclosing():
    def local_func():
        print('local func')
    return local_func

lf = enclosing()
lf()






