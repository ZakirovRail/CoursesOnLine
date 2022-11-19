# def sort_by_last_letter(strings):
#     def last_letter(s):
#         return s[-1]
#     return sorted(strings, key=last_letter)
#
# print(sort_by_last_letter(['hello', 'from', 'a', 'local', 'function']  ))

# ================
g = 'global'


def outer(p="param"):
    l = 'local'

    def inner():
        print(g, p, l)

    inner()

outer()
