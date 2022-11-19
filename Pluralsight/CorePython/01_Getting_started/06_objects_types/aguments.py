def add_spam(menu=[]):
    menu.append('spam')
    return menu

breakfast = ['bacon', 'eggs']
print(add_spam(breakfast))  #

lunch = ['backed beans']
print(add_spam(lunch))  # ['backed beans', 'spam']
print(add_spam())  # ['spam']
print(add_spam())  # ['spam', 'spam']
print(add_spam())  # ['spam', 'spam', 'spam']
# ============================
print('*'* 50)
def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

print(add_spam())  # ['spam']
print(add_spam())  # ['spam']
print(add_spam())  # ['spam']
