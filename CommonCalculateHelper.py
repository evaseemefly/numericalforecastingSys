
# 1.如果找到该值就返回
# 2.如果找不到该值就返回该值的上一个Index和下一个Index
# 3.小于List[0] 返回0
# 4.大于len(List)返回该List[-1]
def BinaryInSearch(arr, key):
    """
    """
    # 记录数组的最高位和最低位
    # 数组起始及终止位置下标
    min = 0
    max = len(arr)-1
    if key in arr:
         # 建立一个死循环，直到找到key
         while True:
             # 得到中位数
            # 这里一定要加int，防止列表是偶数的时候出现浮点数据
             center = int((min + max) / 2)
             # key在数组左边
             if arr[center] > key:
                max = center - 1
             # key在数组右边
             elif arr[center] < key:
                 min = center + 1
             # key在数组中间
             elif arr[center] == key:
                 print(str(key) + "在数组里面的第" + str(center) + "个位置")
                 return center
    else:
         print("没有该数字!")
         return -1


def BinarySearch(arr,key):  
    # low = 0  
    value_min=min(arr)
    value_max=max(arr)
    # high = len(List) - 1  
    middle = 0  
      
    while(value_min <= value_max): 
        middle = int((value_min + value_max) / 2)  
        #获取中间数据  
         # 此处以此种方式可能出现的问题：
        # IndexError: list index out of range
        # 换一种思路
        listTime = arr[middle][0]  
        if listTime == key:  
            return listTime  
            break  
        elif listTime < key:  
            value_min = middle + 1  
        elif listTime > key:  
            value_max = middle - 1  
          
        if value_max < value_min:  
            print('不在List范围内'  )
            return 0  
        elif value_min > len(arr) - 1:  
            print('超出List范围'  )
            return len(arr)  
        else:  
            return (value_max,value_min)  