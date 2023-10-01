def calculate(data):
    total = 0
    if data.__len__() == 0:
        return 0
    else:
        for i in data:
            total += i
    return total

def CalProduct(data):
    total = 0
    if data.__len__() == 0:
        return 0
    else:
        for i in data:
            total += i
    return total


def calAvg(data):
    total = 0
    if data.__len__() == 0:
        return 0
    else:
        for i in data:
            total += i
    return total/data.__len__()

def CalMedian(data):
    #total = 0
    if data.__len__() == 0:
        return 0
    else:
        data.sort()
        print(data)

if __name__ == '__main__':
    print(calculate([]) == 0)
    print(calculate([2,4,6,8,10]) == 30)
    print(CalProduct([]) == 0)
    print(CalProduct([1,1,1,1,1]) == 5)
    print(calAvg([]) == 0)
    print(calAvg([2,2,2,2]) == 2)
    print(CalMedian([]) == 0)
    print(CalMedian([8,5,4,89,7045,0,12,34,0]) == 8)