import ArrayOper
import CommonCalculateHelper
import QuickPositioning

# def main():
#     #初始化测试的数据
#     list_test=[0,10,20,30]
#     ArrayOper.getArrayInterval(list_test)
list_test=[0,10,20,30,40,50,60,70,80,90]
# 获取传入的数组的间距的集合
# ArrayOper.getArrayInterval(list_test)
# 获取数组中的最大值与最小值

# 使用二分法获取指定数值所在的位置
# 不使用此种方法
# CommonCalculateHelper.BinarySearch(list_test,70)
index=CommonCalculateHelper.BinaryInSearch(list_test,70)

# 测试快速定位
lat=87.25
lon=39
lat_array=[80,80.25,81,81.25,82,87,87.25,87.5]
lon_array=[30,31,32,33,34,35,36,37,38,39,40]
index_lat,index_lon=QuickPositioning.getPosition(lat,lon,lat_array,lon_array)