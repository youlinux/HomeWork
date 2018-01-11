# _*_ encoding:utf-8 _*_
__author__ = 'youlinux'
__date__ = '2018/1/11 下午1:53'


'''
 1,1,2,3,5,8,13,21,34,55,89,
'''
sum = 2
li = [1,1,]
num = input("请输入第n个数 : ")

num = int(num)

first = 1
second = 1
third = ""

if num == 1 or num == 2:
    print("第%d个数的值为 : 1" %num )

else:

    for i in range(3,num+1):
        third = first + second
        first = second
        second = third
        li.append(third)

        sum  += third

    print("fib数列为 : ".format(0) , li)
    print("第%d个数的值为 : %d" %(num,third))
    print("前%d个的和为 : %d" %(num,sum))


