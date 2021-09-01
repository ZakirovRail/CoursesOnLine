def find_runner_up(n: int, arr: list):
    if n in range(2, 11):
        sorted_list = sorted(set(arr))
        # print(sorted_list)
        runner_up = sorted_list[-2]
        # print(runner_up, "Is the current runner-up value")
        return runner_up
    else:
        print('Error, the entered value is out of acceptable length')


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(find_runner_up(n, arr))
