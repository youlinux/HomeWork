# _*_ encoding:utf-8 _*_
__author__ = 'youlinux'
__date__ = '2018/1/11 下午12:00'


char = "*"
num = input("请输入行号 : ")



num = int(num)


if num % 2 == 0:
    print("不能为偶数")
    num = input("请输入行号 : ")
    num = int(num)

for i in range(1,num,2):
    print(" "*((num+1)//2-(i+1)//2) + i*char)

for j in range(num,0, -2):
    print(" " *((num + 1) // 2 - (j + 1) // 2) + j * char)




