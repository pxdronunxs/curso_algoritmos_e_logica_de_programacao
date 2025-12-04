#    L1 = list(range(0, 60, 2))
#    print(L1)
#    L2 = list(range(0, 90, 3))
#    print(L2)

set1 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58}
set2 = {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87}
comun = set1 & set2
print(comun)

somenteSet1 = set1 - set2
print(somenteSet1)

somenteSet2 = set2 - set1
print(somenteSet2)

osdois = set1 | set2
print(osdois)

set1semrepetidosset2 = set1 - set2
print(set1semrepetidosset2)
