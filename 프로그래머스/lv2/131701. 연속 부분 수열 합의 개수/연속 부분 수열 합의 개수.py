def solution(elements):
    answer = 0
    # total = set(elements)
    total = set()
    print('#total :', total)
    for i in range(len(elements)):
        for j in range(len(elements)):
            elements_sub = elements + elements[:j]
            # elements_sub = elements * 2
            case = sum(elements_sub[j:j+i+1])
            total.add(case)
    # print(total)
    
    return len(total)