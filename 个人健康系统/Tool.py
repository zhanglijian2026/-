import datetime
import threading
import config
import utils
class Tool:
    _instance=None
    _lock=threading.Lock()
    def __new__(cls, *args, **kwargs):
        if Tool._instance is None:
            while cls._lock:
                cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
    #异步处理系统日志
    @staticmethod
    @utils.cw_fz
    def write_sys_opt_log(oper_mode:str):
        t = threading.Thread(target=Tool.write_sys_opt_log_in, args=(oper_mode,))
        t.daemon = True
        t.start()
    #系统日志
    @staticmethod
    @utils.cw_fz
    def write_sys_opt_log_in(oper_mode:str):
        with config.log_look:
            with open(config.sys_opt_log, 'a+', encoding='utf-8') as f:
                mode_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"{mode_time},{oper_mode}\n")
    #异步处理错误日志
    @staticmethod
    @utils.cw_fz
    def write_err_log(err_mode:str):
        t=threading.Thread(target=Tool.write_err_log_in, args=(err_mode,))
        t.daemon=True
        t.start()
    #错误日志
    @staticmethod
    @utils.cw_fz
    def write_err_log_in(err_mode:str):
        with config.log_look:
            with open(config.sys_err_log, 'a+', encoding='utf-8') as f:
                mode_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"{mode_time},{err_mode}\n")

