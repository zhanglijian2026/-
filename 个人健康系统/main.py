import time
from Tool import Tool
from nemu import YeMian
from  calculator import Calculator
import date_persistence
import datetime
import config
def main(file,sex_3):
        """主程序"""
        while True:
            YeMian.ye_mian()
            while True:
                try:
                    opt_3=int(input('请输入1~5的操作数字'))
                    if opt_3<=0 or opt_3>5:
                        print("请输入1~5的操作")
                        Tool.write_err_log("你输入了错误操作")
                        continue
                    else:
                        print("操作成功")
                        Tool.write_sys_opt_log(f"你输入了{opt_3}操作")
                    break
                except ValueError:
                    Tool.write_err_log_in("你输入了错误的操作")
                    print('请输入正确操作')
            if opt_3==1:
                work_out=Calculator(file,sex_3)
                work_out.main()
            elif opt_3==2:
                while True:
                    try:
                        YeMian.fen_ye_mian()
                        opt_2=int(input())
                        if opt_2==1:
                            median=config.zlj.get_data()
                            YeMian.fen_date_frame(median)
                            Tool.write_sys_opt_log("你直接查看了历史数据")
                        elif opt_2==2:
                            config.zlj.get_data_one()
                            Tool.write_sys_opt_log("你用单条模式遍历了数据")
                        elif opt_2==3:
                            a,e=day_input()
                            config.zlj.day_get_data(a,e)
                            Tool.write_sys_opt_log("你用日期查看了数据")
                        else:
                            print("请输入正确操作")
                            Tool.write_err_log("你输入了错误的操作数据")
                    except ValueError:
                        print("请返回主页面操作")
                        Tool.write_err_log("你输入了错误的操作")
                        time.sleep(0.4)
            elif opt_3==3:
                print("操作会清空历史数据，且无法恢复,是否确定要如此操作,1.是，2,否")
                config.zlj.get_data()
                Tool.write_sys_opt_log("你清空了历史数据")
            elif opt_3==4:
                Tool.write_sys_opt_log(f"你想要删除{file}文件")
                opt_4=int(input("请确定是否要删除档案，是则输入1").strip())
                if opt_4==1:
                    config.zlj.delete_file()
                    break
            else:
                print('成功退出档案')
                Tool.write_sys_opt_log("成功退出档案")
                break
def day_input():
    while True:
        try:
            start_date = input("请输入开始日期(格式YYYY-MM-DD)：")
            end_date = input("请输入结束日期(格式YYYY-MM-DD)：")
            s = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            e = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            return s,e
        except ValueError:
            print("请输入正确日期")
            Tool.write_err_log("你输入了错误的日期")
def input_name():
    while True:
        try:
            name = input("请输入档案名").strip()
            if name=="":
                continue
            return name
        except ValueError:
            print("请输入正确的档案名")
def input_sex():
    while True:
        try:
            sex_1=int(input("请输入性别，1.男，2.女").strip())
            if sex_1==1:
                sex_2= "男"
                return sex_2
            elif sex_1==2:
                sex_2="女"
                return sex_2
            else:
                print("请输入正确数字")
                continue
        except ValueError:
            print("请输入数字")
#登陆页面
def run():
    date_persistence.create_database()
    while True:
        YeMian.zhu_cai_dan()
        try:
            opt = int(input("请输入操作数字"))
            if opt == 1:
                date_file = input_name()
                sex = input_sex()
                opt_1 = config.zlj.login(date_file, sex)
                if opt_1 == 1:
                    continue
                Tool.write_sys_opt_log(f"你登陆了{date_file}档案")
                main(date_file, sex)
                config.zlj.delete_file()
            elif opt == 2:
                date_file = input_name()
                sex = input_sex()
                opt_1 = config.zlj.create_table(date_file, sex)
                Tool.write_sys_opt_log(f"你创建了{date_file}档案")
                if opt_1 == 1: continue
                main(date_file, sex)
                config.zlj.close_data()
            elif opt == 3:
                print("成功退出系统")
                Tool.write_sys_opt_log("退出了系统")
                break
            else:
                print("请输入正确数字")
                Tool.write_err_log("你输入了不存在的操作数字")
        except ValueError:
            print("请输入有效值")
            Tool.write_err_log("你输入了错误的值")
if __name__ == '__main__':
    run()
