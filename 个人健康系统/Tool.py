import datetime
import threading
import os
import config
import utils
class Tool:
    #遍历生成器工具
    @staticmethod
    @utils.cw_fz
    def traverse_folders():
        return [f for f in os.listdir() if f.endswith(".txt") and f != config.sys_err_log and config.sys_opt_log]
    #异步处理系统日志
    @staticmethod
    @utils.cw_fz
    def write_sys_opt_log(xin_xi:str):
        t = threading.Thread(target=Tool.write_sys_opt_log_in, args=(xin_xi,))
        t.daemon = True
        t.start()
    #系统日志
    @staticmethod
    @utils.cw_fz
    def write_sys_opt_log_in(xin_xi:str):
        with config.log_look:
            with open(config.sys_err_log, 'a+', encoding='utf-8') as f:
                shi_jiang = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"{shi_jiang},{xin_xi}\n")
    #判断文件是否为空
    @staticmethod
    @utils.cw_fz
    def p_d_lu_jin(xx):
            with open(xx,'r',encoding="utf-8") as f:
                shu_ju=f.readlines()
            return 0 if shu_ju==[] else 1
    #数据存入文件
    @staticmethod
    @utils.cw_fz
    def save_file(a,xx):
            line = (f"{a['时间']}\t\t{a['年龄']}\t{a['体重']}\t{a['身高']}\t{a['腰围']}\t{a['颈围']}\t{a['BMI']}"
                    f"\t{a['BMR']}\t\t{a['体脂率']}\t{a['腰体脂率']}\t{a['基础代谢']}\n")
            with open(xx, 'a', encoding="utf-8") as f:
                f.write(line)