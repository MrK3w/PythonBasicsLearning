def pow(number, exponent=2):
    return number**exponent

def sqr_lst(fun, lst):
    ret_lst = []
    for item in lst:
        ret_lst.append(fun(item))
    return ret_lst

sqr = pow
pow(3) #9
sqr(3) #9


sqr_lst(sqr, [1, 2, 3])
#[1, 4, 9]