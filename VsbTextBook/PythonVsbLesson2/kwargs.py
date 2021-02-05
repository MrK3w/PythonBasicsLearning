def filtruj_mesta(mesta, **kw):
    flt = []
    lim = 0
    #pokud je gt v kw preda se do limitu hodnota slovniku kw['gt']
    if 'gt' in kw:
        lim = kw['gt']
    flt = [ key for key in mesta if mesta[key] > lim ]
    if 'lt' in kw:
        lim = kw['lt']
        flt += [ key for key in mesta if mesta[key] < lim ]
    return flt

mesta = {"Ostrava": 336000, "Praha": 1249000,
"Brno": 405000, "Olomouc": 101000,
"Karvina": 63000, "Havirov": 82000}
#gt a lt jako slovnik
print(filtruj_mesta(mesta, gt=100000, lt=70000))