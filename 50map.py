income = [10,40,60]

def total(dollars):
    return dollars * 2

new_data = list(map(total,income))
print(new_data)