# _*_ encoding:utf-8 _*_
__author__ = 'youlinux'
__date__ = '2018/1/11 上午11:55'

for i in range(1,10):
    for j in range(1,i+1):
        # print(i*j,end="\t")
        print("%d * %d = %d" %(j,i,i*j),end='\t')
    print()
