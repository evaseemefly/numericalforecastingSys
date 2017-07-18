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
    #设定传入的数组的间隔集合（set）
    dict_interval=set([])
    index=0
    value_first=0
    abs_value=0
    # 获取最小间隔
    for i in sourceArray:
        if index==0:            
            # 获取两者查的绝对值
            value_first=i
        else:
            abs_value=abs(value_first-i)
            dict_interval.add(abs_value)
            value_first=i
        index+=1
    return dict_interval

        


     