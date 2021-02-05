try:
    f = open('textfile','w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error!")
except:
    print("Unhandled exception")
finally:
    print("I will always run")

