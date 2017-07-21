# coding=UTF-8
import sys
import importlib
import os
import pygrib
import ArrayOper
import QuickPositioning
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
# 测试文件名为：HTBCG2016120100-006.grb
forecastType='HTBCG'
targetDateTime='2016120100'
# 注意此处需要手动将6转换为str类型,并向前填充0，保持三位数字
aging=str(6).zfill(3)
grbname_array=[forecastType,targetDateTime,'-',aging,'.grb']
targetName=''.join(grbname_array)
targetPath='/usr/testFIles/'
targetFullName=targetPath+targetName
# 判断指定路径及是否存在指定文件
#/usr/testFIles/HTBCG2016120100-006.grb
if not os.path.exists(targetPath):
    print('路径'+targetName+'不存在')    
elif not os.path.exists(targetFullName):
    print('指定文件'+targetFullName+'不存在')
else :       
    print('文件：'+targetName+'存在')

# 读取文件
# grbs=pygrib.open(targetFullName)
grbs=pygrib.open(targetFullName)
grbs.seek(0)

#根据高度，预报时效以及起始时间获取指定片区的所在位置（数组中的位置）
def getTargetArea(grbs,level,aging,fromDate):
    index=0
    isExist=False
    index_final=-1
    #遍历grbs
    for grb in grbs:
        area_name=str(grb)
        print(area_name)
        index+=1
        # 当当前片区的名字满足条件时
        # fromDate:'from 201612010000'
        if level in area_name and aging in area_name and fromDate in area_name:            
            isExist=True
            index_final=index
            break
    return index_final

# 4 根据经纬度二维数组以及层级获取指定的gribmessage

level=100

# 获取满足条件的片区编号

index=getTargetArea(grbs,'level 1000','fcst time 6 hrs','from 201612010000')
# 根据经纬度找到对应的区域并取出对应的结果一维数组

def getLatLonValues(latlon_array,index):
    # 获取纬度二维数组
    # 纬度二维数组    
    # 纬度只需要取出第一列即可
    lat_array= [x[0] for x in grbs[index].latlons()[0]]
    # 取出经度——取出第一行即可
    lon_array=grbs[index].latlons()[1][0].tolis()
    return lat_array,lon_array

lat_array,lon_array= getLatLonValues(latlon_array,index)

# 此种方式的思路，现在已经拥有lat和lon这两个数组了
# lat,lon分别代表经度和纬度
# latlon_array是一个经纬度信息的二维数组
# [经度... ]
# [纬度... ]
# 思路：
    #    计算lat与lon的间隔，与最大值与最小值
    #    根据latlon_array数组中的值计算其在lat与lon数组中的位置，定位后获取该值
values=grbs[index].values

latlon_array_value=[[90,80],[0,1]]
for temp in latlon_array_value:
    latlon_array_index.append(QuickPositioning.getPosition(temp[0],temp[1],lat_array,lon_array)) 

# 获取了经纬度的数组
final_array=[]
#for lat_temp in latlon_array[0]:
#    for lon_temp in latlon_array[1]:
#        index_lat=lat.index(lat_temp)
#        index_lon=lon.indexOf(lat_temp)
#        final_array.push(values[index_lat][index_lon])
    



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

