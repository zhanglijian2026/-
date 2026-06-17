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
    def date_frame(body_date,bft):
        """"个人数据"""
        print(f'你的BMI为：{body_date["BMI"]}')
        print(f'你的BMR为；{body_date["BMR"]}')
        print(f'你的体脂率为：{body_date["体脂率"]}%')
        print(f'你的体脂率2为：{body_date["腰体脂率"]}%')
        print(f'你的综合体脂率为：{bft}%')
        print(f'你的基础代谢为{body_date["基础代谢"]}')
    #查看数据页面
    @staticmethod
    def fen_ye_mian():
        print("\n请输入查看数据方式")
        print("1.直接查看所有数据")
        print("2.自动逐条遍历所有数据")
        print("3.手动逐条遍历所有数据")
        print("4.查看某天的数据")