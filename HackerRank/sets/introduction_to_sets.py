def average(array):
    new_array = set(array)
    average_num = sum(new_array) / (len(new_array))
    return average_num


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
