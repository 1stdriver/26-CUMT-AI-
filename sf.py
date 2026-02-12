import math

''' 例3.3.4
n = int(input())
max = 2 * n - 1
for i in range(n):
    spaces = int((max - (2 * (i+1) - 1)) / 2)
    for j in range(spaces):
        print(' ',end = '')
    for j in range(2 * (i+1) - 1):
        print('*', end = '')
    for j in range(spaces):
        print(' ', end = '')
    if(i != n - 1):
        print()
'''

''' 例3.3.5
for i in range(101):
    for j in range(101):
        for k in range(101):
            if (i + j + k == 100 and 5 * i + 3 * j + k / 3 == 100):
                print('公鸡',i,'只,','母鸡',j,'只,','小鸡',k,'只')'''

''' 例3.3.7
n = int(input())
i = 1
sum = 0
while(i != n + 1):
    if (i % 2 != 0):
        sum = sum + i
    i += 1
print(sum)'''

''' 例3.3.8
a = 1
b = 2
t = a / b
total = 0.000001
sum = 0
while(t >= total):
    sum += t
    a += 2
    b *= 2
    t = a / b
    
print("%.6f"%sum)'''

''' 例3.3.10
n = int(input())
flag = True
for i in range(2,n):
    if n % i == 0:
        flag = False
        break;
if n == 1: flag = False
if flag == True:
    print('yes')
else:
    print('no')'''

''' 例3.3.11
import math
n, m = map(int, input().split())
print(math.gcd(n,m))'''

''' 例3.4.1
T = int(input())
i = 0
while(i < T):
    data = list(map(int, input().split()))
    print("%.1f" %(sum(data)/len(data)))
    i += 1'''

''' 例3.4.2
T = int(input())
for i in range(T):
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("YES")
    else:
        print("NO")'''

''' 例3.4.3
T = int(input())
for i in range(T):
    n = int(input())
    sum = 1
    for i in range(1,n + 1):
        sum *= i
    print(sum)'''

''' 例3.4.4
T = int(input())
for i in range(T):
    str = input()
    count = 0
    for s in str:
        if s >= '0' and s <= '9':
            count += 1
    print(count)'''

''' 例3.4.5 
n, m = map(int, input().split())
fm = 1
t = m
while(t > 1):
    fm *= t
    t -= 1
fz = 1
t = n
while(t >= n - m + 1):
    fz *= t
    t -= 1

print(fz // fm)'''

''' 例3.4.6
s = input()
s = s.split()
for i in range(len(s)):
    t = list(s[i])
    t[0] = t[0].upper()
    t = "".join(t)
    if i > 0: print(' ', end = '')
    print(t, end='')'''

''' 例3.4.7
n = int(input())
l = []
isNum = False
for i in range(6, n + 1):
    
    sum = 0
    for j in range(1, i//2 + 1):
        if (i % j == 0):
            sum += j
    if sum == i:
        isNum = True
        l.append(sum)
print(f"{n}:", end="")  
# 第二步：判断是否有完数
if isNum:  
    # 有完数：遍历打印，每个前面加空格
    for pn in l:  
        print(f" {pn}", end="")  
    print()  # 打印完后换行
else:  
    # 无完数：输出NULL（注意冒号后有一个空格）
    print(" NULL")'''

''' OJ 1
T = int(input())
for i in range(T):
    n, *a = map(int, input().split())
    print(sum(a))'''

''' OJ 2
n, *a = map(int,input().split())
print(sum(a))'''

''' OJ 3
data = input().split()
while(data != '0'):
    a = data[1:]
    a = [int(s) for s in a]
    print(sum(a))
    data = input().strip()'''

''' OJ 4
T = int(input())
l = []
for i in range(T):
    n, *a = map(int, input().split())
    l.append(sum(a))
for i in range(0,len(l)):
    print(l[i])
    if i != len(l) - 1:
        print()'''     

''' OJ 5
T = int(input())
for i in range(T):
    pow = float(input())
    chg = 0.0
    if pow <= 150:
            chg = 0.4463 * pow
    elif pow >= 151 and pow <= 400:
        chg = 0.4463 * 150 + 0.4663 * (pow-150.0)
    else:
        chg = 0.4463 * 150 + 0.4663 * 250 + 0.5663 * (pow - 400.0)
    print(f"电费为chg:{chg:.1f}元")'''

''' OJ 6
T = int(input())
for i in range(T):
    n, *a = map(int, input().split())
    sm = sum(a)
    if sm % 5 == 0 and sm % 7 == 0 and sm % 3 == 0:
        print("YES")
    else:
        print("NO")'''

''' OJ 7
T = int(input())
l = []
maxNum = -1.0
item = ""
for i in range(T):
    n, price = input().split()
    price = float(price)
    if price > maxNum:
        item = n
        maxNum = price
    l.append(price)
l = list(map(float, l))
avg = sum(l) / len(l)
print(f"{item} {avg:.1f}")'''

''' OJ 8
r = float(input())
s = math.sqrt(3)/4 * r * r # 四分之根3 * 边长的平方
print(f"{s:.2f}")'''

''' OJ 9
T = int(input())
for i in range(T):
    isNum = False
    n, a = map(int, input().split())
    for j in range(n, a + 1):
        if j % 3 == 2 and j % 7 == 1:
            print(f"{j} ", end = '')
            isNum = True
    if isNum == False: print('none')'''

''' OJ 10
Sg = 0
Gs = 0
T = int(input())
for i in range(T):
    sg,gs = map(int, input().split())
    Sg += sg
    Gs += gs
if Sg > gs:
    print("Sg")
elif Gs > Sg:
    print("Gs")
else:
    print("CONTINUE")'''

''' OJ 11
nums, strs = input().split()
string = ''
nums = list(map(int, nums))
for i in range((len(nums))):
    ordNum = ord(strs[i])
    ordNum += nums[i]
    string += chr(ordNum)
print(string)''' 

''' OJ 12
string = input()
f = 0
m = 0
for i in range(len(string)):
    if string[i] == 'f' or string[i] == 'F':
        f += 1
    elif string[i] == 'm' or string[i] == 'M':
        m +=1
sumNums = f + m
fp = f / sumNums * 100
mp = m / sumNums * 100
print(f"{mp:.1f} {fp:.1f}")'''

''' OJ 13
maxNums = 0
psb = 0
p = int(input())
for i in range(p):
    if i % 7 == 5 and i % 5 == 3 and i % 3 == 2:
        maxNums = i
        psb +=1
print(psb, maxNums)'''

''' OJ 14 
暂时不会
'''

''' OJ 15
T = int(input())
for i in range(T):
    l = []
    a, b, c = map(int, input().split())
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    print(l[0] * l[1] // 2)'''

''' OJ 16
T = int(input())
for i in range(T):
    num = int(input())
    for j in range(1, 2 * num):
        if j > 5:
            for k in range(2 * num - j):
                print(2 * num - j, end = '')
            print()
        else:
            for k in range(j):
                print(j, end = '')
            print()'''

''' OJ 17
n, a = map(int, input().split())
sum = a
string = str(a)
for i in range(n - 1):
    string += str(a)
    sum += int(string)
print(sum)'''

''' OJ 18
T = int(input())
for i in range(T):
    m, n = map(int, input().split())
    for j in range(m, n + 1):
        for k in range(j):
            print(j, end = '')
        print()'''

''' OJ 19
n = int(input())
line = 2 * n - 1
for i in range(1, 2 * n):
    if i < 6:
        stars = 2 * i - 1
        for j in range(line - stars // 2):
            print(' ', end = '')
        for j in range(stars):
            print('*', end = '')
        for j in range(line - stars // 2):
            print(' ', end = '')
        print()
    else:
        stars = line - (i - n) * 2
        for j in range(line - stars // 2):
            print(' ', end = '')
        for j in range(stars):
            print('*', end = '')
        for j in range(line - stars // 2):
            print(' ', end = '')
        print()'''

''' OJ 20
m, n = map(int, input().split())
isNum = False
for i in range(m, n + 1):
    ge = int(i % 10)
    shi = int(i / 10 % 10)
    bai = int(i / 100)
    number = ge * ge * ge + shi * shi * shi + bai * bai * bai
    if i == number:
        isNum = True
        print(f"{i}={bai} * {bai} * {bai}+{shi} * {shi} * {shi}+{ge} * {ge} * {ge}")
if isNum == False:
    print("none")'''

''' OJ 21
T = int(input())
for i in range(T):
    n, k = map(int, input().split())
    d = n - 1
    for j in range(d):
        k = 3 * (k + 1)
    print(k)'''
    
''' OJ 22
T = int(input())
for _ in range(T):
    item = input()
    number = int(item)
    while(1):
        l = len(item)
        isFind = True
        for i in range(l // 2):
            if item[i] != item[l - 1 - i]:
                isFind = False
                break
        if isFind == True:
            print(number)
            break
        number += 1
        item = str(number)'''

''' OJ 23
暂时不会
'''

''' OJ 24
n = int(input())
fm = 1.0
fz = 2.0
sum = fz / fm
for i in range(n - 1):
    temp = fz
    fz += fm
    fm = temp
    sum += fz / fm
print(f"{sum:.6f}")'''

''' OJ 25
n = int(input())
for i in range(n // 3):
    for j in range(n // 2):
        for k in range(n * 2):
            if 3 * i + 2 * j +  k // 2 == n and i + j + k == n and k % 2 == 0:
                print(i, j, k)'''