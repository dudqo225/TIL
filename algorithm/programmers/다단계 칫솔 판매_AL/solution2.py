def solution(enroll, referral, seller, amount):
    answer = []
    
    rev = dict()
    parent = dict()
    for i in range(len(enroll)):
        rev[enroll[i]] = 0
        parent[enroll[i]] = referral[i]
        
    def find_ref(seller_name, cost):
        ref = parent[seller_name]

        if ref == "-":
            rev[seller_name] += (cost - cost // 10)
            return

        if cost * 0.1 < 1:
            rev[seller_name] += cost
        else:
            rev[seller_name] += (cost - cost // 10)
            find_ref(ref, cost // 10)

        return

    for i in range(len(seller)):
        benefit = amount[i] * 100
        find_ref(seller[i], benefit)
        
    for r in rev:
        answer.append(rev[r])

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))