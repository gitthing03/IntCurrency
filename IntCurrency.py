def IntCurrency(n):
    s = [x for x in str(n)]
    if len(s) >= 3: 
        s.insert(len(s)-2,".") 
        return(''.join(s))
    else:
        t = ["0","."]
        if len(s) == 2:
            for n in s: t.append(n)
        else:
            t.append("0")
            t.append(s[0])
        return(''.join(t))