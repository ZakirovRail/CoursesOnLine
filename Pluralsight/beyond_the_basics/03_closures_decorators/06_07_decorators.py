def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap

def capitalise_symbols(f:str):
    def wrap(*args, **kwargs):
        y = f(*args, **kwargs)
        return y.capitalize()
    return wrap


@escape_unicode
def northern_city():
    return "Ȩ Ç Ḑ Ģ Ḩ Ķ Ļ Ņ Ŗ Ş Ţ"

@capitalise_symbols
def lower_case():
    return "hello, i should be capitalised"


print(northern_city())
print(lower_case())




