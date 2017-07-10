# coding=UTF-8
# print('测试')
import sys
import importlib
import pygrib
import os
#import reload
# 具体步骤：
# 1 获取文件的一些信息（传入参数）
# 2 找到对应文件——目前先根据预报要素、时间、时效
# 3 读取文件
# 4 根据经纬度二维数组以及层级获取指定的gribmessage
# 5 根据经纬度找到对应的区域并取出对应的结果一维数组
importlib.reload(sys)

#reload(sys)   
#sys.setdefaultencoding('utf8') 
# 2 找到对应文件——目前先根据预报要素、时间、时效
forecastType='HTBCG'
targetDateTime='201612010000'
aging=6
grbname_array=[forecastType,targetDateTime,'-',aging,'.grb']
targetName=''.join(grbname_array)
targetPath='/usr/testFIles/'
targetFullName=targetPath+targetName
# 判断指定路径及是否存在指定文件
if not os.path.exists(targetPath):
    print('路径'+targetName+'不存在')    
elif os.path.exists(targetFullName):
    print('指定文件'+targetFullName+'不存在')
else:       
    print('文件：'+targetName+'存在')

# 读取文件
# grbs=pygrib.open(targetFullName)
grbs=pygrib.open('')
grbs.seek(0)

# 4 根据经纬度二维数组以及层级获取指定的gribmessage
# for grb in grbs:       
    # print(grb)
    # print(grb.values)
    # grb.get_count()
grbs
data= grbs[1].values
print(grbs[1].latlons)
# for temp in  len(data[0]):
#     for 

print(grbs[1][1].values)
print(data)
# 获取数组的长度
lenghth=grbs.messagenumber

# 获取数组中每个对象的长度
count_temp=len(grbs[1])
temp=grbs[1]
latlon=grbs[1].latlons()[0]
print(latlon)
# print(type(data))
print(data.shap,data.min(),data.max())
lat=grb.latlons()
print(lat)

#通过grbs[1].values的方式可以读取文件
# grb = grbs.select(name='regular_ll')[0]
# data = grb.values
# print(data)
print('测试')

