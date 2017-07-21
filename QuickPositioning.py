import ArrayOper
import CommonCalculateHelper

def getPosition(lat,lon,lat_array,lon_array):
    """根据传入的经纬度数组获取在lat与lon两个数组中的序号
    """
    value_max_lat=max(lat_array)
    value_min_lat=max(lat_array)
    totallen=abs(value_max_lat-value_min_lat)
     #获取lat数组的间隔
    set_lat_interval= ArrayOper.getArrayInterval(lat_array)
    # 获取长度
    #index_len=len(lat_array)
    #if len(set_lat_interval)<=0:
    isdesc_lat=lat_array[0]<lat_array[1]
    isdesc_lon=lon_array[0]<lon_array[1]
    index_lat=CommonCalculateHelper.BinaryInSearch(lat_array,lat,isdesc_lat)
    index_lon=CommonCalculateHelper.BinaryInSearch(lon_array,lon,isdesc_lon)
    return index_lat,index_lon
        
        
