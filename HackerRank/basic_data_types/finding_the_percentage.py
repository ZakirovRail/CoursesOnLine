if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    length_list_name = len(student_marks[query_name])
    required_scores = student_marks[query_name]
    sum_marks = 0
    for i in required_scores:
        sum_marks += i
    final_result = sum_marks / length_list_name
    print("{:.2f}".format(final_result))