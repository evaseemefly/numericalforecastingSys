import sys
import importlib
import pygrib
#import reload
importlib.reload(sys)
#reload(sys)   
sys.setdefaultencoding('utf8') 
grbs=pygrib.open('/usr/testFIles/HTBCG2016120100-006.grb')
grbs.seek(0)
for grb in grbs:
    print(str(grb))