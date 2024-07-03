# PTA输入有严格的标准
# 注意空格数，英文大小写，中文标点
# 变量名cnt count用于计数
# 变量名total sum 用于求和 
# 通过debug（pta上的虫子）来看结果跟编程结果区别





# 6-1 函数的定义
def f(x):
    total = x*x+2
    return total


# 6-2 整数数位和
def digitSum(v):
    lst = [int(i) for i in str(v) ]
    return sum(lst)

# 6-3 编写函数计算f(i) = 1/2 + 2/3 + 3/4 + ... + i/(i+1)
def f(i):
    sum = 0
    for i in range(1,i+1):
        sum += i/(i+1)
    return sum
# 6-3 列表表达式展开写 
def digitSum(v):
    lst = []
    for i in str(v):
        lst.append(int(i))
    return sum(lst)

# 6-3 用循环写
def digitSum(v):
    s = 0
    for i in str(v):
        s += int(i)
    return s

# 6-4 计算工资
# 大于40小时但小于或等于60小时按平时小时薪酬的1.5倍给薪；大于60小时则按平时小时薪酬的2倍给薪。
def pay(salaryHour, hours):
    if hours <= 40:
        total = salaryHour*hours
    elif hours <= 60:
        total = salaryHour*40+salaryHour*1.5*(hours-40)
    else:
        total = salaryHour*40+salaryHour*1.5*20+salaryHour*2*(hours-60)
    return total

# 6-5 求列表中能被3整除的数
def  mult3(lst):
    for i in lst:
        if int(i)%3 == 0:
            print(i)


# 6-6 sdut-利用函数得到缩写词
def acronym(phrase):
    s = ''
    for word in phrase.split():
        a = word[0]
        s += a
    s = s.upper()
    return s

# 6-7 计算阶乘
def factorial(num):
    jiechen = 1
    for i in range(num,0,-1):
# for i in range(1,num+1):
        jiechen *= i
    return jiechen


# 6-8 实现isOdd函数
def isOdd (n):
    flag =True
    if n%2 == 0:
        flag = False
    return flag



# 6-9 求因子之和
def  sum_factor (n):
    total = 0
    for i in range(1,n+1):
        if n%i == 0:
            total += i
    return total


# 7-1 计算BMI并判断
# BMI=weight×703÷height^2
# 当一个人的BMI在18.5与25之间时，其体重被认为是“体重最佳”。
# 如果BMI小于18.5，则被认为是"体重过轻"；
# 如果BMI大于25，则被认为是“体重超重"。
weight = float(input())
height = float(input())
BMI = weight*703/(height**2)
BMI1 = int(BMI*100)/100
print(f'BMI = {BMI1}')
if BMI < 18.5:
    print('体重过轻')
elif BMI <= 25:
    print('体重最佳') 
else:
    print('体重超重')


# 7-2 计算表达式（*，//, %）
exp = list(input().split())
num1 = int(exp[0])
num2 = int(exp[2])
oper = exp[1]
if oper == '*':
    res = num1*num2
    print(f'{num1}*{num2}={res}')
elif oper == '//':
    res = num1//num2
    print(f'{num1}//{num2}={res}')
elif oper == '%':
    res = num1%num2
    print(f'{num1}%{num2}={res}')
else:
    res = 'Invalid operator'
    print(res)


# 7-3 X教授决策成绩评定
score = int(input())
if score < 60:
    level = 'E'
elif score < 70:
    level = 'D'
elif score < 80:
    level = 'C'
elif score < 90:
    level = 'B'
else:
    level = 'A'
print(level)


# 7-4 jmu-python-分段函数1
import math
x = float(input())
x1 = abs(x)
if x1 >= 300:
    fx = -1
else:
    fx = (x**3)/math.log10(x1+2.6)
print(f'f({x:.3f})={fx:.3f}')

# 7-5 jmu-python-汇率兑换
# R60 $10.00 $5 R30.00
s = input()
a_1 = s[0]
b_1 = s[1:]
if a_1 == 'R':
    sum = float(b_1)/6
    print(f'${sum:.2f}')
elif a_1 == '$':
    sum = float(b_1)*6
    print(f'R{sum:.2f}')


#7-6温度转换
s = input()
a_1 = s[-1]
b_1 = s[:-1]
if a_1 == 'C':
    sum = 1.8*float(b_1)+32
    print(f'{sum}F')
elif a_1 == 'F':
    sum = (float(b_1)-32)/1.8
    print(f'{sum}C')


# 7-7输入数因子
yinzi = []
n = int(input())
for i in range(1,n+1):
    if n%i == 0:
        yinzi.append(i)
print(yinzi) 


# 7-8 累加求5的倍数的和
total = 0
n = int(input())
for i in range(n+1):
    if i%5 == 0:
        total += i
print(total)



# 7-9 1+2+3 = 6
total = 0
a = int(input())
b = int(input())
for i in range(a,b+1):
    total += i
print(total)


# 7-10 编程求一个字符串中有多少个字母和数字字符
# char.isalpha()字母  char.isdigit()数字
char = input()
cnt = 0
for i in char:
    if i.isalpha() or i.isdigit():
        cnt += 1
print(cnt)



# 7-11 编程求1到n的所有奇数之和
total = 0
n = int(input())
for i in range(1,n+1,2):
    total += i
print(f'和为{total}')


# 7-12 分数数列求和，计算1/1+1/2+1/3+...+1/n
total = 0
n = int(input())
for i in range(1,n+1):
    total += 1/i
print(f'和为{total:.6f}')


# 7-13 求前N项和
total = 0
n = int(input())
for i in range(1,n+1):
    total += i
print(total)


# 7-14 求n！
jiechen = 1
n = int(input())
for i in range(n,0,-1):
# range(1,n+1)
    jiechen *= i
print(jiechen)


# 7-15 jmu-python-字符串-统计不同字符个数
# Hi! 天气不错 二十八度 28℃。
# 10 3 2 3
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0 
char = input()
for i in char:
    if i.isalpha():
        cnt1 += 1
    elif i.isspace():
        cnt2 += 1
    elif i.isdigit():
        cnt3 += 1
    else:
        cnt4 += 1
print(cnt1,cnt2,cnt3,cnt4)


# 7-16偶数之积
n = int(input())
ji = 1
for i in range(1,n+1):
    if i%2 == 0:
        ji *= i
print(ji)


# 7-17 s=1+2+3+...+n直到s>=m
# 输入1000   输出1035=1+2+...+45
m = int(input())
total = 3
i = 2
while total < m:
    i += 1 
    total += i
print(f'{total}=1+2+...+{i}')


# 7-18 裁判打分
# 4 
# 100 
# 99 
# 98 
# 97
lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
print(f'{(sum(lst)-max(lst)-min(lst))/(n-2):.2f}')

# 7-19 成绩统计
cnt = 0
num = int(input())
lst = list(map(int,input().split()))
print(f'Max: {max(lst)}')
print(f'Min: {min(lst)}')
print(f'Ave: {sum(lst)/num:.1f}')
for i in lst:
    if int(i) < 60:
        cnt +=1
print(f'Fail: {cnt}')



# 7-20 计算一组数据平均值、最大值、最小值
lst = list(map(int,input().split()))
print(int(sum(lst)/len(lst)),max(lst),min(lst))


# 7-21 求出歌手的得分 
# 输入一个正整数n (n>4)，再输入n个实数，求出歌手的得分（保留2位小数）
# 再去掉1个最高分和1个最低分,计算余下的分数平均值为歌手的得分.
n = int(input())
num = list(map(int,input().split()))
num.remove(max(num))
num.remove(min(num))
num.remove(max(num))
num.remove(min(num))
ave = (sum(num))/len(num)
print(f'aver={ave:.2f}')



# # 7-22 大于身高的平均值
# 143 174 119 127 117 164 110 128
# 143 174 164 
height = list(map(int,input().split()))
ave = sum(height)/len(height)
lst = [i for i in height if i > ave]
print(*lst,end=' ')


# 7-23 水仙花数  （没通过PTA测试，思路是这样的）
# 水仙花数是指一个N位正整数（N≥3），它的每个位上的数字的N次幂之和等于它本身。
# 例如：153=1×1×1+5×5×5+3×3×3。 100-999 1000-9999
N = int(input())
for number in range(10**(N-1),10**N):
    sum = 0
    for i in str(number):
        sum += int(i)**3
        if sum == int(number):
            print(number)



# 7-24 字典的应用-找出出现次数最多的字符串
# abc
# abc
# bcd
# xxx
# q
dic = {}
while True:
    char = input()
    if char == 'q':
        break
    elif char not in dic:
        dic[char] = 1
    else:
        dic[char] += 1
for k in dic:
    if dic[k] != 1:
        print(k,dic[k])


# 7-25 jmu-python-最佳身高
# （女方的身高）×1.09 =（男方的身高）
# 输入第一行给出正整数N（≤10），为前来查询的用户数。
# 随后N行，每行按照“性别 身高”的格式给出前来查询的用户的性别和身高
# 其中“性别”为“F”表示女性、“M”表示男性
N = int(input())
lst = []
lst1 = []
for i in range(N):
    lst = list(input().split())
    if lst[0] == 'F':
        height = float(lst[1])*1.09
        lst1.append(height)
    elif lst[0] == 'M':
        height = float(lst[1])/1.09
        lst1.append(height)
for i in lst1:
    print(f'{i:.2f}')



#7-26 求π的近似值 公式π^2/6 = 1+1/2^2+1/3^2+1/4^2+...
t = 1
n = 1
y = 0
wucha = eval(input())
while t >= wucha:  #1e-10
    y += t
    n += 1
    t = 1 / n**2
total = (y * 6)**0.5
print(f'{total:.6f}')


# 7-27 sdut-循环-5-百钱买百鸡
# 一只公鸡五块钱，一只母鸡三块钱，三只小鸡一块钱
# 现在要用一百块钱买一百只鸡，问公鸡、母鸡、小鸡各多少只？
for i in range(0,20):
    for j in range(0,33):
        for k in range(0,300):
            if 5*i + 3*j + (1/3)*k == 100 and i+j+k == 100:
                print(f'公鸡{i:>2}只，母鸡{j:>2}只，小鸡{k:>2}只') 
#输出逗号为中文
# {:>2}右对齐，字符小于两位


# 7-28 计算 11+12+13+...+m
# sum = 4040
m = int(input())
sum  = 11+12+13
i = 13
while i < m:
    i += 1
    sum += i 
print(f'sum = {sum}')


# 7-29 输出星期名缩写
# 输入一个1到7的数字，输出对应的星期名的缩写。
# 1 Mon
# 2 Tue
# 3 Wed
# 4 Thu
# 5 Fri
# 6 Sat
# 7 Sun
day = int(input())
today = {1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat',7:'Sun'}
print(today[day])


# 7-30 找出最大值和最小值
# Max=？
# Min=？
num = list(map(int,input().split()))
print(f'Max={max(num)}')
print(f'Min={min(num)}')


# 7-31 Python-求最大值及其索引
num = list(map(int,input().split()))
max_1 = max(num)
index = num.index(max_1)
print(max_1,index)


# 7-32 jmu-python-逆序输出
# a b  c e   f  gh
# ghfecba
# ['a', 'b', 'c', 'e', 'f', 'gh']
# gh f e c b a
lst = list(input().split())
lst1 = lst[::-1]  #lst[::-1]不改变列表本身 reverse改变
print(*lst1,sep='')
print(lst)
print(*lst1,sep=' ')

# 7-33 计算物体自由下落的距离
h = 1/2*10*(3**2)
print(f'height = {h:.2f}')

# 7-34 输出菱形图案
#   A
# A   A
#   A
print('  A')
print('A   A')
print('  A')


# 7-35 计算存款利息
# interest=money×(1+rate)^year−money
# 其中interest为存款到期时的利息（税前），money是存款金额，year是存期，rate是年利率
# 在一行中按“interest = 利息”的格式输出，其中利息保留两位小数。
lst = list(map(float,input().split()))
money = lst[0] 
year = lst[1]
rate = lst[2]
interest = money*(1+rate)**year-money
print(f'interest = {interest:.2f}')

# 7-36 重要的话说三遍
a = "I'm gonna WIN!"
for i in range(3):
    print(a)

# 7-37 输出星号倒三角
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
print('* * * * *')
print(' * * * *')
print('  * * *')
print('   * *')
print('    *')

# 7-38
print("Hello World!")
