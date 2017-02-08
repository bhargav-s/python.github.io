from collections import Counter

text = "we are who we are . First tel them who I am ok. so how was your day.Please call me"

words  = text.split()
counter = Counter(words)
cmmn = counter.most_common(3)
print(cmmn)