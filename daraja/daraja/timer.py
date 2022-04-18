import time
t = 1 * 10
while t:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins, secs)

    

    time.sleep(1)
    t -=1
    print(t)

num1 = 9
num2 = 4
ans = num1 + num2
print("The answer is " + str(ans))