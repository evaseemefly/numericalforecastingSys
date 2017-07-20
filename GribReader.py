
class GribReader:
	"""grib文件读取类
	"""
	def __init__(self):
		self.filePath=''

	def display(self):
		print("")

	def __str__(self):
		return "读取的grib文件所在路径为:%s"%self.filePath
