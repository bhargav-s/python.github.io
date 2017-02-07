marks = {
    'bhargav' : 40,
    'ajay' : 34,
    'karthik' : 33,
    'nandan' : 45
}

Max = max(zip(marks.values(),marks.keys()))
Min = min(zip(marks.values(),marks.keys()))
Sort = sorted(zip(marks.values(),marks.keys()))

print(Max)
print(Min)
print(Sort)