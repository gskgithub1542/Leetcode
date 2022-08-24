n = 19
sum1 = 0
lst = []
while True:
    m = str(n)
    for i in m:
        sum1 += int(i) ** 2
    if sum1 in lst:
        print(False)  # originally we use return instead of print, so it works fine also in line 13
    lst.append(sum1)
    if sum1 == 1:
        print(True)
    n = sum1
    sum1 = 0

