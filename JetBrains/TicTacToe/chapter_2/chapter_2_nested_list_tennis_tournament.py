n = int(input())

winners_list = []


for i in range(n):
    name, result = input().split(' ')
    if result == 'win':
        winners_list.append([name, result])
print([i[0] for i in winners_list])
print(len(winners_list))


# =====================================================================================================================
# players = int(input())
# player_names = []
# player_wins = []
# for _ in range(players):
#     name = input()
#     name_result = name.split()
#     player_names.append(name_result)
# for win in player_names:
#     if win[1] == 'win':
#         player_wins.append(win[0])
# print(player_wins)
# print(len(player_wins))
# =====================================================================================================================
# test_list = []
# for _ in range(int(input())):
#     wins_or_loses = input().split()
#     if wins_or_loses[1] == "win":
#         test_list.append(wins_or_loses[0])
#
# print(test_list)
# print(len(test_list))
# =====================================================================================================================

# n = int(input())
# won = [word[0] for word in [input().split() for _ in range(n)] if word[1] == 'win']
#
# print(won)
# print(len(won))















