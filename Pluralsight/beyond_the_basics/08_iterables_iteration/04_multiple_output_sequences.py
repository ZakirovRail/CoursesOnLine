
size = ['small', 'medium', 'large']
colors = ['lavender', 'teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamander']


def combine(size, color, animals):
    return '{} {} {}'.format(size, color, animals)

 
print(list(map(combine, size, colors, animals)))  # ['small lavender koala', 'medium teal platypus', 'large burnt orange salamander']



# ==============================================================================================================================





# ==============================================================================================================================





