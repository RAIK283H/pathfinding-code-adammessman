import heapq

list = []
heapq.heapify(list)
heapq.heappush(list, (4, 'A'))
heapq.heappush(list, (3, 'B'))
heapq.heappush(list, (1, 'C'))
for element in list:
    if element[1] == "B":
        list.remove(element)
print(heapq.heappop(list))


