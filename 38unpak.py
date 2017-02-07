def unpacking(grades):
    first, *middle = grades
    total = sum(middle) / len(middle)
    total = total + first
    print (total)

unpacking([12,13,14,15,16,17])