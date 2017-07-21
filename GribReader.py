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


class GribReader:
	"""grib读取类
	"""      
	def __init__(self,sourcePath,fileName,forecastType,targetDateTime):
		"""
		构造函数需传入：
		1 文件路径（不含文件名）
		2 文件路径
		3 类型
		4 预报时间
		"""
		# 所有变量均设置为私有变量
		self.__sourcePath=sourcePath
		self.__fileName=fileName
		self.__forecastType=forecastType
		self.__targetDateTime=targetDateTime
        

	def display(self):
		print("")

	def __str__(self):
		return "读取的grib的文件路径为:%s"%self.filePath   		
    		
	def test(self):
		print('test func')

	def getLatLonValues(self,grbs,latlon_array,index):  
		"""privte
		根据传入的grbs对象以及经纬度信息以及片区gribmessage获取经纬度数组
		"""  		
		# 获取纬度二维数组
		# 纬度二维数组    
		# 纬度只需要取出第一列即可
		lat_array= [x[0] for x in grbs[index].latlons()[0]]
		# 取出经度——取出第一行即可
		lon_array=grbs[index].latlons()[1][0].tolist()
		return lat_array,lon_array

	def getTargetArea(self,grbs,level,aging,fromDate):
		"""privte
		根据grbs对象，等级，预报时效以及预报时间获取片区所在位置（下标）
		根据高度，预报时效以及起始时间获取指定片区的所在位置（数组中的位置）
		"""
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

	def read(self,level,latlon_array_value):
		"""根据等级读取文件，并根据传入的经纬度数组（根据该两个数组获取对应的值）
		   返回这些经纬度在grbs[index].values中的对应值的数组
		"""
		# 1 找到对应文件——目前先根据预报要素、时间、时效
		# 测试文件名为：HTBCG2016120100-006.grb
		forecastType=self.__forecastType
		targetDateTime=self.__targetDateTime
		#使用此种方式会出错，注释掉
		#targetForecastDate="from "+str(self.targetDateTime)
		targetForecastDate=""
		targetForecastDate="from 2016120100"
		agingForecast="fcst time 6 hrs"
		# 注意此处需要手动将6转换为str类型,并向前填充0，保持三位数字
		aging=str(6).zfill(3)
		grbname_array=[forecastType,targetDateTime,'-',aging,'.grb']
		targetName=''.join(grbname_array)
		targetPath=self.__sourcePath
		targetFullName=targetPath+targetName        
		# 判断指定路径及是否存在指定文件
		#/usr/testFIles/HTBCG2016120100-006.grb
		if not os.path.exists(targetPath):
			print('路径'+targetName+'不存在') 
			return   
		elif not os.path.exists(targetFullName):
			print('指定文件'+targetFullName+'不存在')
			return
		else :       
			print('文件：'+targetName+'存在')
		
		# 2 读取文件
		# 使用Pygrib打开文件		
		grbs=pygrib.open(targetFullName)
		grbs.seek(0)

		self.test()
		# 3 根据经纬度二维数组以及层级获取指定的gribmessage
		str_level='level '+str(level)
		# 获取满足条件的片区编号
		index=self.getTargetArea(grbs,str_level,agingForecast,targetForecastDate)
		# 根据经纬度找到对应的区域并取出对应的结果一维数组
		lat_array,lon_array= self.getLatLonValues(grbs,latlon_array_value,index)

		# 3 获取传入的经纬度数组在values中对应的值
		# 此种方式的思路，现在已经拥有lat和lon这两个数组了
		# lat,lon分别代表经度和纬度
		# latlon_array是一个经纬度信息的二维数组
		# [经度... ]
		# [纬度... ]
		# 思路：
			#    计算lat与lon的间隔，与最大值与最小值
			#    根据latlon_array数组中的值计算其在lat与lon数组中的位置，定位后获取该值
		values=grbs[index].values
		latlon_array_index=[]	#经纬度所在位置（下标）
		# 作为参数传入——以下注释
		# latlon_array_value=[[90,80],[0,1]] 
		for temp in latlon_array_value:
			latlon_array_index.append(QuickPositioning.getPosition(temp[0],temp[1],lat_array,lon_array)) 

		# 4 根据下标获取对应的值
		latlon_value=[]
		for temp in latlon_array_index:
			latlon_value.append(values[temp[0],temp[1]])
		return latlon_value
		

	# def readGrib(self,level):		
	# 	"""
	# 	"""
	# 	# 1 找到对应文件——目前先根据预报要素、时间、时效
	# 	# 测试文件名为：HTBCG2016120100-006.grb
	# 	forecastType=self.forecastType
	# 	targetDateTime=self.targetDateTime
    #     #使用此种方式会出错，注释掉
    #     #targetForecastDate="from "+str(self.targetDateTime)
	# 	targetForecastDate=""
    #     targetForecastDate="from 2016120100"
    # 	agingForecast="fcst time 6 hrs"
	# 	# 注意此处需要手动将6转换为str类型,并向前填充0，保持三位数字
	# 	aging=str(6).zfill(3)
	# 	grbname_array=[forecastType,targetDateTime,'-',aging,'.grb']
	# 	targetName=''.join(grbname_array)
	# 	targetPath=self.sourcePath
	# 	targetFullName=targetPath+targetName        
	# 	# 判断指定路径及是否存在指定文件
	# 	#/usr/testFIles/HTBCG2016120100-006.grb
	# 	if not os.path.exists(targetPath):
	# 		print('路径'+targetName+'不存在') 
	# 		return   
	# 	elif not os.path.exists(targetFullName):
	# 		print('指定文件'+targetFullName+'不存在')
	# 		return
	# 	else :       
	# 		print('文件：'+targetName+'存在')
		
	# 	# 2 读取文件
	# 	# 使用Pygrib打开文件		
	# 	grbs=pygrib.open(targetFullName)
	# 	grbs.seek(0)

	# 	# 3 根据经纬度二维数组以及层级获取指定的gribmessage
	# 	str_level='level '+level
	# 	# 获取满足条件的片区编号
	# 	index=getTargetArea(grbs,str_level,agingForecast,targetForecastDate)
	# 	# 根据经纬度找到对应的区域并取出对应的结果一维数组
	# 	lat_array,lon_array= getLatLonValues(grbs,latlon_array,index)

	# 	# 此种方式的思路，现在已经拥有lat和lon这两个数组了
	# 	# lat,lon分别代表经度和纬度
	# 	# latlon_array是一个经纬度信息的二维数组
	# 	# [经度... ]
	# 	# [纬度... ]
	# 	# 思路：
	# 		#    计算lat与lon的间隔，与最大值与最小值
	# 		#    根据latlon_array数组中的值计算其在lat与lon数组中的位置，定位后获取该值
	# 	values=grbs[index].values

	# 	latlon_array_value=[[90,80],[0,1]]
	# 	for temp in latlon_array_value:
	# 		latlon_array_index.append(QuickPositioning.getPosition(temp[0],temp[1],lat_array,lon_array)) 

		
	