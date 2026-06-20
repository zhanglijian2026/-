
#循环输入并捕获异常装饰器
def lu_ru(func):
    def date_6(*args,**kwargs):
        while True:
            try:
                return func(*args,**kwargs)
            except ValueError:
                print("请输入正确的值")
                from Tool import Tool
                Tool.write_err_log("你输入了错误的值")
    return date_6
#文件异常捕获装饰器
def cw_fz(func):
    def date_7(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except FileNotFoundError:
            print("文件读取失败")
            from Tool import Tool
            Tool.write_err_log("文件读取失败")
    return date_7