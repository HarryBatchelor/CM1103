
test = ("bob",[2,4,1,1,2,5])
def series_score(person, worst=1):
    for i in range(1, worst+1):
        largest = max(person[1])
        found = person[1].index(largest)
        person[1].pop(found)
    return sum(person[1])
print(series_score(test))

testing = [('Alice',[1,2,1,1,1,1]), ('Bob',[3,1,5,3,2,5]), ('Clare', [2,3,2,2,4,2]), ('Dennis', [5,4,4,4,3,4]), ('Eva', [4,5,3,5,5,3])]

def sort_series(sailors):
    unordered = []
    for s in sailors:
        unordered.append((s[0],series_score(s)))
    order = sorted(unordered, key=lambda x: x[1])
    print(order)


sort_series(testing)
