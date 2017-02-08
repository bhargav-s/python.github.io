import heapq

data = [20,3333,34,2200,340,210,12333333,34343]

value = heapq.nlargest(3,data)
print(value)