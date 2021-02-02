def super_print(*p):
    s = " ".join(p)
    print ("-" * len(s))
    print (s)
    print ("-" * len(s))

super_print("Jedna", "dve", "3", "4")