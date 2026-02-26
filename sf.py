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

''' 例 4.1.1
T = int(input())
for _ in range(T):
    n, *a = map(int, input().split())
    a = list(map(int, a))
    avg = float(sum(a) / len(a))
    sumNum = 0.0
    for i in range(n):
        number = (a[i] - avg) * (a[i] - avg)
        sumNum += number
    S = math.sqrt(sumNum / n)
    print(f"{S:.5f}")'''

''' 例 4.1.2 # 这一题第一版书上的过程太逆天了，第二版还一字不改，真该死
n = int(input())
l = []
for i in range(1,n + 1):
    sumNum = 0 # 用来计算真因子的和
    for j in range(1, i//2 + 1):
        if i % j == 0: # 如果这个数(j)是真因子，就累加起来
            sumNum += j
    if sumNum == i: # 如果真因子加起来是这个数，就加到列表里
        l.append(i)
print(f"{n}:",end = '')
if len(l) != 0: # 把列表里的完数全输出出来
    for i in range(len(l)):
        print(" %d"%l[i], end = '')
else:
    print(" NULL")'''

''' 例 4.2.1
l = list(map(int, input().split())) # 把输入的一行字符串转换成int型的list
l.sort(reverse=True)
print(*l)'''

''' 例 4.2.2
n = input()
l = len(n) # l是数的位数
print(l,end = '')
for i in range(l): # 正向输出
    print(',',n[i],end = '',sep='') # 每个元素之前加个,
for i in range(l-1,-1,-1):
    print(',',n[i],end = '',sep='')'''

''' 例 4.2.3 # 这一题真有点难了，第一次见，去b站学了一会才会
n = int(input()) 
l = [True] * (n + 1) # 索引从1开始，0作废，所以要n + 1个位置
left = n # 剩余人数
times = 1 # 用来判断是不是第三个人，通过模3来判断，只有元素是True才+1
index = 1 # 列表的索引，每次必+1
while(left > 1): # 剩余人数不是1就一直循环
    if l[index] != False: # 如果当前元素尚未出圈
        if times % 3 == 0: # 且正好该被出圈
            l[index] = False # 就给它出圈
            left -= 1 # 剩余人-1
            if left == 1: # 如果只剩一个了，直接找到并输出然后结束
                for i in range(1, n + 1):
                    if l[i] == True:
                        print(i)
                        break
                break
        times += 1 # 判断到未出圈的元素之后，才能继续+1来判断下一个元素该不该出圈，出圈的直接无视掉
    index += 1 # 无论该不该出圈，列表总得往下走
    if index > n: # 如果越界了，就从1开始重新走
        index = 1'''

''' 例 4.2.4
l = list(map(int, input().split()))
n = l[0]
m = l[1]
l = l[2:]
for i in range(m):
    number = l.pop(0)
    l.append(number)
for i in range(len(l)):
    print(f"{l[i]} ",end = '')'''

''' 例 4.2.5
n = int(input())
a = list(map(int, input().split()))
minNum = min(a) # 获取最小的数
idx = a.index(minNum) # 用index函数获得最小数的索引
a[0], a[idx] = a[idx], a[0]
print(*a)'''

''' 例 4.2.6 
n = int(input())
l = list(map(int, input().split()))
for i in range(n-1):
    minidx = i
    for j in range(i + 1,n):
        if l[j] < l[minidx]:
            minidx = j
    l[i], l[minidx] = l[minidx], l[i]
print(*l)'''

''' 例 4.2.7
n = int(input())
l = list(map(int, input().split()))
for i in range(n-1):
    for j in range(n - 1 - i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(*l)'''

''' 例 4.2.8
n = int(input())
l = [True] * (n+1)
l[1] = False
lmt = math.sqrt(n)
for i in range(2, int(lmt+1)):
    if l[i] == False:
        continue
    for j in range(i*i, n+1, i):
        l[j] = False
res = 0
for i in range(1,len(l)):
    if l[i] == True:
        res += 1
        if res > 0:
            print(f"{i} ",end = '')
print()'''

''' 例 4.3.1
m,n = map(int, input().split())
l = [[0] * n for i in range(m)]
for i in range(m):
    l[i] = list(map(int, input().split()))
for i in range(m):
    print(*l[i])'''

''' 例 4.3.2
n = int(input())
l = [[0] * n for i in range(n)]
for i in range(n):
    l[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(i):
        l[i][j], l[j][i] = l[j][i], l[i][j]
for i in range(n):
    print(*l[i])'''

''' 例 4.3.3
n = int(input())
l = [[1] * i for i in range(1, n + 1)] # 这里得从1开始，要不然第一行是空的
for i in range(2, n): # 从第三行开始算
    for j in range(1, i): # 每一行中第一个和最后一个不用修改，只要修改中间的数
        l[i][j] = l[i-1][j] + l[i-1][j-1] 
for i in range(n):
    for j in range(i + 1):
        print("%5d"%l[i][j], end = '')
    print()'''

''' 例 4.3.4 # 这一题多了最后一行没有用的输入，在第二版的书中已经修改
m, p, n = map(int,input().split())
a = [[0] * m for i in range(p)]
b = [[0] * p for i in range(n)]
c = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = list(map(int, input().split()))
for i in range(p):
    b[i] = list(map(int, input().split()))

for i in range(m):
    for j in range(n):
        for k in range(p):
            c[i][j] += a[i][k] * b[k][j]
for i in range(m):
    print(*c[i])'''

''' 例 4.3.5
n = int(input())
l = [[0] * (n - i) for i in range(n)]
num = 1
for i in range(n):
    k = 0
    for j in range(i, -1 ,-1): # 列表的行数每次-1，列数每次+1，逐个往右上角
        l[j][k] = num
        num += 1
        k += 1
for i in range(n): print(*l[i])'''

''' 例 4.4.1 # 本来以为是用字典来做题的，没想到还是得用列表
n = int(input())
l = []
for i in range(n):
    a, b = input().split()
    b = int(b)
    l.append({"name":a, "soc":b})
for i in range(n - 1):
    maxidx = i
    for j in range(i + 1, n):
        if l[j]['soc'] > l[maxidx]['soc']:
            maxidx = j
    l[i], l[maxidx] = l[maxidx], l[i]
for i in range(n):
    print(i + 1 , end = ' ')
    print(l[i]['name'], l[i]['soc'])'''

''' 例 4.4.2 # 跟上一题一个样
n = int(input())
l = []
for i in range(n):
    id, soc = input().split()
    l.append({"id":id, "soc":int(soc)})
for i in range(n - 1):
    maxidx = i
    for j in range(i + 1, n):
        if l[j]["soc"] > l[maxidx]["soc"]:
            maxidx = j
        elif l[j]["soc"] == l[maxidx]['soc'] and l[j]['id'] < l[maxidx]['id']:
            maxidx = j
    l[i], l[maxidx] = l[maxidx], l[i]
for i in range(n):
    print(i+1, l[i]['id'], l[i]['soc'])'''

''' 例 4.5.1
string = input()
l = [0] * 10
for i in string:
    l[int(i)] += 1
for i in range(len(l)):
    if l[i] != 0:
        print(i,l[i])
print()'''

''' 例 4.5.2
T = int(input())
isequal = True
for i in range(T):
    n = int(input())
    l = [0 * n for i in range(n)]
    for i in range(n):
        l[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(n // 2):
            if l[i][j] != l[i][n - 1 - j]:
                isequal = False
                break
    for i in range(n // 2):
        for j in range(n):
            if l[i][j] != l[n - 1 - i][j]:
                isequal = False
                break
    if isequal == True:
        print("yes")         
    else:
        print("no")'''

''' 例 4.5.3
T = int(input())
for _ in range(T):
    s = list(input())
    t = list(input())
    s.sort()
    t.sort()

    if s is t:
        print("Yes")
    else:
        print("No")'''

''' 例 4.5.4
n = int(input())
l = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
l.sort()
print(*l)
for i in range(m):
    left = 0
    right = len(l) - 1
    isFind = False
    number = nums[i]
    while(left <= right):
        mid = (left + right) // 2
        if l[mid] < number:
            left = mid + 1
        elif l[mid] > number:
            right = mid - 1
        else:
            isFind = True
            print(mid + 1,end = ' ')
            break
    if isFind == False:
        print(0, end = ' ')'''

''' 例 4.5.5
T = int(input())
for _ in range(T):
    found = False
    m, n = map(int, input().split())
    a = []
    for i in range(m):
        row = list(map(int, input().split()))
        a.append(row)
    for i in range(m):
        ans = min(a[i])  # 每行最小值
        idx = a[i].index(ans)  # 最小值所在列
        isNum = True
        for j in range(m):
            if a[j][idx] > ans:  # 列中有数更大,就不是马鞍点
                isNum = False
                break 
        if isNum:
            print(ans)
            found = True
            break # 找到就直接退出
    if not found:
        print("Impossible")'''

''' 例 4.5.6
lct = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]] # 这是所有能走的位置
T = int(input())
for _ in range(T):
    cnt = 0
    loc = input()
    string = loc[0]
    num = loc[1]
    for i in range(len(lct)):
        s = chr(ord(string) + lct[i][0]) # 把字母转为对应的ascii数字再加上位移量，再变为字母(字母 -> 数字 -> 字母)
        l = int(num) + lct[i][1] # 数字就直接加
        if s >= 'a' and s <= 'h' and l >= 1 and l <= 8: # 如果字母和数字都在正常范围内，cnt加1
            cnt += 1
    print(cnt)'''

''' 例 4.5.7 # 这一题答案k很抽象，写得不太好，可以通过提前计算每一行和每一列的和，再用双重循环来更新最大值，时间复杂度能降到O(n^2)
T = int(input())
for _ in range(T):
    n = int(input())
    maxNum = 0
    r, c = 0, 0
    a = [[0] * (n) for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            num = 0
            for k in range(n):
                num += a[i][k]
                num += a[k][j]
            num -= a[i][j]
            if num > maxNum:
                maxNum = num
                r = i + 1
                c = j + 1
    print(r, c, maxNum)'''

''' 例 4.5.8 # 这一题忘了还能直接遍历字典的key
n = int(input())
dic = {}
for i in range(n):
    string = input()
    if string in dic.keys():
        dic[string] += 1
    else:
        dic[string] = 1
Value = max(dic.values())
Key = max(dic.keys())
for i in dic.keys():
    if dic[i] == Value and i < Key:
        Key = i
print(Key)'''

''' OJ 1 # 要善于利用python的特性，能省不少事
T = int(input())
for _ in range(T):
    a = []
    n, i, j, *a = map(int, input().split())
    a[1:6] = a[1:6][::-1]
    print(*a)'''

''' OJ 2 # 同上
a = []
n, x, *a = map(int, input().split())
a.append(x)
a.sort()
print(*a)'''

''' OJ 3
T = int(input())
for _ in range(T):
    m, *a = map(int, input().split())
    n, *b = map(int, input().split())
    c = a + b
    c.sort()
    print(*c)'''

''' OJ 4
T = int(input())
for _ in range(T):
    n, *a = map(int, input().split())
    a.sort()
    for i in range(n):
        num = a.pop(0)
        a.append(num)
    print(*a)'''

''' OJ 5
n, *a = map(int, input().split())
a.sort()
l = 0
if len(a) % 2 == 1:
    l = len(a) // 2 + 1
else:
    l = len(a) // 2
p = 0
for i in range(l):
    if a[i] % 2 == 1:
        p += a[i] // 2 + 1
    else:
        p += a[i] // 2
print(p)'''

''' OJ 6
T = int(input())
for _ in range(T):
    n, m, *a = map(int, input().split())
    A = a[:n]
    B = a[n:]
    for i in B:
        if A.count(i) > 0:
            A.remove(i)
    if len(A) > 0:
        A.sort()
        print(*A)
    else:
        print("NULL")'''

''' OJ 7
a, b = input().split()
match(a):
    case('one'):
        a = 1
    case('two'):
        a = 2
    case('three'):
        a = 3
    case('four'):
        a = 4
    case('five'):
        a = 5
    case('six'):
        a = 6
    case('seven'):
        a = 7
    case('eight'):
        a = 8
    case('nine'):
        a = 9
    case('ten'):
        a = 10
match(b):
    case('one'):
        b = 1
    case('two'):
        b = 2
    case('three'):
        b = 3
    case('four'):
        b = 4
    case('five'):
        b = 5
    case('six'):
        b = 6
    case('seven'):
        b = 7
    case('eight'):
        b = 8
    case('nine'):
        b = 9
    case('ten'):
        b = 10
print(a+b)'''

''' OJ 8 # 有点难,得多看几遍
T = int(input())
for _ in range(T):
    n = int(input())
    res = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    tmin, tmax = 0, n - 1
    qmin, qmax = 0, n - 1
    while(tmin <= tmax):
        if a[tmax] > b[qmax]:
            res += 1
            tmax -= 1
            qmax -= 1
        elif a[tmin] > b[qmin]:
            res += 1
            qmin += 1
            tmin += 1
        else:
            if a[tmin] < b[qmax]:
                res -= 1
            tmin += 1
            qmax -= 1
    print(res * 200)'''

''' OJ 9 # 这一题输入有问题，应该是XYYXXYYX，第一版是错的，第二版中已经修改
s = input()
n = len(s)
minLen = n
while(True):
    if minLen % 2 != 0:
        print(minLen)
        break
    half = minLen // 2
    first_half = s[:half]
    second_half = s[half:]
    print(first_half)
    print(second_half)
    print()
    if second_half == first_half[::-1]:
        s = first_half
        minLen = half
    else:
        print(minLen)
        break'''

''' OJ 10
n, *a = map(int, input().split())
res = 0
heapVal = 0
while(len(a) > 1):
    a.sort()
    heapVal = a[0] + a[1]
    res += heapVal
    a.append(heapVal)
    a.pop(0)
    a.pop(0)
print(res)'''

''' OJ 11
T = int(input())
for _ in range(T):
    s1 = input().strip()
    s2 = list(''.join(s1))
    s3 = list(''.join(s1))
    s2.reverse()
    if s3 == s2:
        print("YES")
    else:
        print("NO")'''

''' OJ 12
T = int(input())
for _ in range(T):
    n = int(input())
    a = input().strip().split()
    res = 0
    for i in range(len(a)):
        if len(a[i]) == n:
            res += 1
    print(res)'''

''' OJ 13
T = int(input())
for _ in range(T):
    n, *a = map(int, input().split())
    a = list(set(a))
    print(*a)'''

''' OJ 14
T = int(input())
for _ in range(T):
    a = input().split()
    for i in range(len(a)):
        a[i] = a[i].lower()
        if len(a[i]) > 4:
            a[i] = a[i][:4]
            a[i] += '.'
    print(*a)'''

''' OJ 15
N = int(input())
a = []
for i in range(N):
    s = input()
    if s == '0':
        break
    a.append(s)
for i in range(N - 1):
    idx = i
    for j in range(i + 1, N):
        if len(a[j]) < len(a[idx]):
            idx = j
        elif len(a[j]) == len(a[idx]):
            if int(a[j]) < int(a[idx]):
                idx = j
    a[i], a[idx] = a[idx], a[i]
for i in range(N):
    print(a[i])'''

''' OJ 16
s = input().strip()
dic = {}
for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1
for i in dic:
    print(i, dic[i])'''

''' OJ 17
m = int(input())
print(pow(2,m*8-1)-1)'''

''' OJ 18'''

''' OJ 19
T = int(input())
for _ in range(T):
    n = int(input())
    a = [[0] * n] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    isDc = True
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                isDc = False
    if isDc:
        print("YES")
    else:
        print("NO")'''

''' OJ 20
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    a = [[0] * m] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    Avsc = [0] * n
    for i in range(n):
        Avsc[i] = sum(a[i]) / len(a[i])
        for j in range(m):
            if a[i][j] < 60:
                Avsc[i] = -1.0'''
    
''' OJ 21
T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    a = [[0] * m] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    sumScore = [0] * n
    for i in range(n):
        sumScore[i] = sum(a[i])
    sumScore.sort()
    sumScore.reverse()
    for i in range(n):
        if sum(a[i]) == sumScore[k - 1]:
            for j in range(m):
                print(a[i][j], end = ' ')'''

''' OJ 22
n, m = map(int, input().split())
a = [[0] * m] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
minv = a[0][0]
maxv = a[0][0]
mini = 0
minj = 0
maxi = 0
maxj = 0
for i in range(n):
    for j in range(m):
        if a[i][j] < minv:
            minv = a[i][j]
            mini = i
            minj = j
        if a[i][j] > maxv:
            maxv = a[i][j]
            maxi = i
            maxj = j
a[mini][minj], a[maxi][maxj] = a[maxi][maxj], a[mini][minj]
for i in range(n):
    for j in range(m):
        print(a[i][j],end = ' ')
    print()'''

''' OJ 23'''
T = int(input())
for _ in range(T):
    n = int(input())
    val = 1
    a = [[1] * n] * n
    for i in range(n):
        for j in range(n - 1, -1):
            a[i][j] = val
            val += 1
