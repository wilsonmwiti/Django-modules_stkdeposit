def fun(x):
    try:
        return x * 20
    finally:
        print("Yay! I still got executed, even though my function has already returned!")

print(fun(5))