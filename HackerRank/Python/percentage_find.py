if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    relevant_student_marks = student_marks[query_name]
    
    avg_grade = sum(relevant_student_marks) / len(relevant_student_marks)
    formatted_grade = "{:.2f}".format(avg_grade)
    print(formatted_grade)
    

