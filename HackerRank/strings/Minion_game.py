def minion_game(string):
    vowels = 'AEIOU'
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    print(length)
    for i in range(length):
        print('it is i = ', i)
        if string[i] in vowels:
            print('it is string from i', string[i])
            Kevin_score += (length - i)
            print('this is kevins score', Kevin_score)
        else:
            Stuart_score += (length - i)
            print('this is Stuarts score', Stuart_score)
    print('The winner is: ')
    if Kevin_score > Stuart_score:
        print('Kevin', Kevin_score)
    elif Kevin_score < Stuart_score:
        print('Stuart', Stuart_score)
    else:
        print('Draw')

minion_game('BANANA')
