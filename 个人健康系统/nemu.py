class YeMian:
    def __new__(cls, *args, **kwargs):
        pass
    # 主页面
    @staticmethod
    def zhu_cai_dan():
        print("*" * 50)
        print("\t\t男性身体数据分析")
        print("*" * 50)
        print("1.登陆档案")
        print("2.创建档案")
        print("3.退出系统")
        print("请输入1~3的有效数字")
        print("补充，如果输入无效值，可能回到主页面")
    #档案页面
    @staticmethod
    def ye_mian():
        """主页面"""
        print("\t\t男性个人身体健康数据计算统计\t\t")
        print("="*40)
        print('请输入操作')
        print('1.录入数据')
        print('2.查看所有数据记录')
        print("3.清空历史数据")
        print("4.删除档案")
        print("5.退出档案")
        print("="*40)
    #个人数据页面
    @staticmethod
    def date_frame(body_date,bft_r):
        """"个人数据"""
        print(f'你的BMI为：{body_date["bmi"]}')
        print(f'你的BMR为；{body_date["bmr"]}')
        print(f'你的体脂率为：{body_date["bft"]}%')
        print(f'你的体脂率2为：{body_date["bft_1"]}%')
        print(f'你的综合体脂率为：{bft_r}%')
        print(f'你的基础代谢为{body_date["meta"]}')
    #查看数据页面
    @staticmethod
    def fen_ye_mian():
        print("\n请输入查看数据方式")
        print("1.直接查看所有数据")
        print("2.手动逐条遍历所有数据")
        print("3.查看某天的数据")
    #全部数据
    @staticmethod
    def fen_date_frame(data):
        for i in data:
            print(f"{i}")
    #单条数据
    @staticmethod
    def fen_date_frame2(data):
        for i in data:
            print(f"{i}")
