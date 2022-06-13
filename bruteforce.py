test = [0, 7, 4, 9]
count = 0
answer = []

for i in range(len(test)):
    while count <= 9:
        print("Angka ke",i, ": ", count)
        if count == test[i]:
            print("----------------------------")
            print("Angka ke",i, "ketemu, yaitu", count)
            print("----------------------------")
            answer.append(count)
            break
        count += 1
    count = 0

for j in answer:
    print(j, end="")