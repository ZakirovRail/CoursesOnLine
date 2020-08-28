if __name__ == '__main__':
    nested_list = []
    sorted_list_scores = []
    list_of_second_lowest = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])
        sorted_list_scores.append(nested_list[_][1])

    final_sorted_list_scores = sorted(set(sorted_list_scores))
    second_lowest = final_sorted_list_scores[1]

    for lists in nested_list:
        if second_lowest in lists:
            list_of_second_lowest.append(lists[0])
        list_of_second_lowest = sorted(list_of_second_lowest)
    for i in list_of_second_lowest:
        print(i)


