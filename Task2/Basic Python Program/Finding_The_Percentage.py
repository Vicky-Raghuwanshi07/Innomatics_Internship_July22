if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum_of_student= sum(student_marks.get(query_name))/len(student_marks.get(query_name))
    print(f"{sum_of_student:.2f}")