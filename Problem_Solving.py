import random
NAMES = ["Azzarano","Babcock","Bubb","Ciminelli","Faluotico","Falus","Houseal","Iusupova","Jenkins-Culver","Ke","Kovalczik", "Kragalott","Lewkowicz","Lopez-Martinez","McMaster","Mendes","Mercedes","Mohan","Morgan","Patel","Picciano","Porter","Rodriguez","Santiago","Saunders","Silverman","Soto","Tolossa","Zheng"]
def create_random_groups():
    groups = []
    for i in range(9):
        groups.append([])
        for j in range(3):
            groups[i].append(NAMES.pop(random.randint(0,len(NAMES)-1)))
    while(len(NAMES) != 0):
        num = random.randint(0,len(groups)-1)
        if(len(groups[num]) < 4):
            groups[num].append(NAMES.pop(0))
    return groups


def main():
    groups = create_random_groups()
    for group in groups:
        print(group)

main()