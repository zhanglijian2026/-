
def date(func):
    def date_8(*args,**kwargs):
        print("=" * 110)
        print("\t\t时间\t\t\t\t年龄\t\t体重\t\t身高\t\t腰围\t\t颈围\t\tBMI\t\tBMR\t\t\t体脂率\t腰体脂率\t基础代谢")
        print("=" * 110)
        return func(*args,**kwargs)
    return date_8
#文件异常捕获装饰器
def cw_fz(func):
    def date_7(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except FileNotFoundError:
            print("文件读取失败")
            from Tool import Tool
            Tool.xi_ton("文件读取失败")
    return date_7
#循环输入并捕获异常装饰器
def lu_ru(func):
    def date_6(*args,**kwargs):
        while True:
            try:
                return func(*args,**kwargs)
            except ValueError:
                print("请输入正确的值")
                from Tool import Tool
                Tool.xi_ton("你输入了错误的值")
    return date_6