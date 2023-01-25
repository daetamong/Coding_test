from collections import Counter

def compare(l1, l2):
    if l1 == l2:
        return True
    else:
        return False

def solution(want, number, discount):
    wants = {want[i] : number[i] for i in range(len(want))}
    answer = 0
    
    for i in range(0, len(discount) - 9):
        shop = discount[i:i+10]
        shop_dic = Counter(shop)
        if compare(shop_dic, wants):
            answer += 1
    return answer