def IntCurrency(n):
    s = [x for x in str(n)]
    l = len(s)
    if l >= 3: 
        s.insert(l-2,".") 
        return(''.join(s))
    else:
        t = ["0","."]
        if l == 2:
            t.extend(s)
        else:
            t.extend(["0", s[0]])
        return(''.join(t))