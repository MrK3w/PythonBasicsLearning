def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("yes that's it")
            break
        finally: 
            print("End of try/except/finally")
    return result

result = ask_for_int()
print(result)