marks = [12,34,56,20,9]
extend_marks = [23,43,67,30]

# print(marks)
marks.append(67)
print(marks)    
marks.pop()
print(marks)

marks.extend(extend_marks)
print(marks)

marks.insert(13,9)
print(marks)