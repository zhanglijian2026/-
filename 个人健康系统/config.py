import threading
from date_persistence import DatePersistence
from 健康系统.主程序 import Tool

sys_opt_log="系统操作日志.txt"
sys_err_log="系统异常日志.txt"
log_look=threading.Lock()
#边界值
age_min,age_max=1,200
wt_min,wt_max=1,250
ht_min,ht_max=1,300
waist_min,waist_max=1,150
neck_min,neck_max=1,100
zlj=DatePersistence()
tool_instance=Tool()
