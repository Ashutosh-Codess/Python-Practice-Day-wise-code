#Exam Result Processor
def exam_result(marks: list[int]) -> str:
    if not marks:
        raise ValueError("marks list cannot be empty")
    if any(mark < 35 for mark in marks):
        return "FAIL"
    average = sum(marks) / len(marks)
    if average >= 75:
        return "DISTINCTION"
    return "PASS"