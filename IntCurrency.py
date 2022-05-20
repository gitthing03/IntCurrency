def IntCurrency(n):
    s = [x for x in str(n)]
    if len(s) >= 3: 
        s.insert(len(s)-2,".") 
        return(''.join(s))
    else:
        t = ["0","."]
        if len(s) == 2:
            t.extend(s)
        else:
            t.extend(["0", s[0]])
        return(''.join(t))