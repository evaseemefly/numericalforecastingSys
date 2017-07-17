def  getArrayInterval(sourceArray):
    """根据传入的数组获取间隔
    """
    # 获取最大值和最小值
    value_max=max(sourceArray)
    value_min=min(sourceArray)
    # 获取长度
    index_len=len(sourceArray)
    # index_count=sourceArray.count()
    # value_first
    # interval
    dict_interval={}
    index=0
    # 获取最小间隔
    for i in sourceArray:
        if index==0:
            
        # 获取两者查的绝对值
        abs_value=abs(value_first-i)
        dict_interval.add(index)
        value_first=i
    return dict_interval

        


     