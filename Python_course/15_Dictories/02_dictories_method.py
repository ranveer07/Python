marks = {"Ranveer" : 94,"Ganesh" : 54,"Ayush":35}
print(marks.keys())
print(marks.values())
print(marks.items())


marks.pop("Ayush")
print(marks)
marks.clear()
print(marks)