# _*_ encoding:utf-8 _*_
__author__ = 'youlinux'
__date__ = '2018/1/10 下午6:36'





for i in range(1,101):
    for j in range(2,i):
        if i % j == 0:
            break

    # for j 循环正常结束 就执行  else 语句
    else:
        print(i)













