scientists = ['Marie Curie', 'Albert Einstein', 'Rosalind Franklin',
              'Niels Bohr', 'Dian Fossey', 'Isaac Newton',
              'Grace Hopper', 'Charles Darwin', 'Lise Meither']

# for name in scientists:
#     print(name.split()[-1])

print(sorted(scientists, key=lambda name: name.split()[-1]))
# ['Niels Bohr', 'Marie Curie', 'Charles Darwin', 'Albert Einstein', 'Dian Fossey', 'Rosalind Franklin',
# 'Grace Hopper', 'Lise Meither', 'Isaac Newton']
