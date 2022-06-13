import random

tester = str(random.randint(0000, 9999))
if len(tester) == 3:
    tester = "0" + tester
count = 0
number = ""
for ret in range(4):
    for i in range(10):
        if str(i) == tester[ret]:
            number = number + str(i)
            count += 1
            break
        else:
            count += 1

print("number ",number," tester ",tester)
print(count)