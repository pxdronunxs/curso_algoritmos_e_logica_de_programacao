string1 = "CTA"
string2 = "ABC"
string3 = ""

for e in string1:
    if e in string1 and e not in string2:
        string3 += e
        for x in string2:
            if x in string2 and x not in string1:
                string3 += x
                print(string3)

