import time
from Tool import Tool
from nemu import YeMian
from export import GonNen
from  calculator import Calculator
def main(file,six):
        """主程序"""
        while True:
            YeMian.ye_mian()
            while True:
                try:
                    print('请输入1~5的操作数字')
                    opt_1=int(input())
                    if opt_1<=0 or opt_1>5:
                        print("请输入1~5的操作")
                        Tool.xi_ton("你输入了错误操作")
                        continue
                    else:
                        print("操作成功")
                        Tool.xi_ton(f"你输入了{opt_1}操作")
                    break
                except ValueError:
                    Tool.xi_ton("你输入了错误的操作")
                    print('请输入正确操作')
            if opt_1==1:
                zlj=Calculator(file,six)
                zlj.main()
            elif opt_1==2:
                sys_opt=Tool.p_d_lu_jin(file)
                if sys_opt==0:
                    print("无历史数据")
                    Tool.xi_ton("你查看了历史数据，但是发现没有")
                else:
                    try:
                        YeMian.fen_ye_mian()
                        opt_2=int(input())
                        if opt_2==1:
                           GonNen.ton_jia(file)
                        elif opt_2==2:
                            print("请输入逐条遍历的速度,建议0.1")
                            GonNen.zhu_tia_bian_li(file)
                        elif opt_2==3:
                            GonNen.shou_d_bian_li(file)
                            print("按回车健为下一条")
                        elif opt_2==4:
                            GonNen.re_qi_bian_li(date_file)
                        else:
                            print("请输入正确操作")
                    except ValueError:
                        print("请返回主页面操作")
                        Tool.xi_ton("你输入了错误的操作")
                        time.sleep(0.4)
            elif opt_1==3:
                print("操作会清空历史数据，且无法恢复,是否确定要如此操作,1.是，2,否")
                GonNen.clear_date(file)
                Tool.xi_ton("你清空了历史数据")
            elif opt_1==4:
                Tool.xi_ton(f"你想要删除{file}文件")
                GonNen.san_chu(file)
                break
            else:
                print('成功退出档案')
                Tool.xi_ton("成功退出档案")
                break
def login_rec(date_file):
    if not date_file:
        print("档案名不能为空,或者档案名不能为空格")
        time.sleep(0.5)
        Tool.xi_ton("你在登陆中没有输入档案名就回车了，或者输入了空格")
        return
    if date_file.endswith(".txt"):
        date_file = date_file[:-4]
    exists = GonNen.six_qr(date_file)
    if exists.endswith(".man.txt"):
        six = "男"
        main(exists, six)
    elif exists.endswith(".gril.txt"):
        six = "女"
        main(exists, six)
    else:
        print("档案不存在，返回主页")
        Tool.xi_ton("你输入了不存在的档案名")
        time.sleep(0.5)
def create_rec(date_file):
    if not date_file:
        print("档案名不能为空")
        time.sleep(0.5)
        Tool.xi_ton("你在创建中没有输入档案名就回车了，或者输入了空格")
        return
    six = GonNen.six_pd()
    if date_file.endswith(".txt"):
        date_file_new = date_file[:-4]
        if six == 1:
            target = date_file_new + ".man.txt"
        else:
            target = date_file_new + ".girl.txt"
    else:
        if six == 1:
            target = date_file + ".man.txt"
        else:
            target = date_file + ".girl.txt"
    exists = target in Tool.in_tr()
    if not exists:
        print("创建成功,正在为你打开档案")
        main(target, six)
        Tool.xi_ton(f"你成功创建了名为{target}的档案")
        time.sleep(0.8)
    else:
        print("档案已存在,返回主页面中")
        Tool.xi_ton("你在创建中输入了已经存在的档案名")
        time.sleep(0.5)
if __name__ == '__main__':
    #主页面的登陆等
    while True:
        YeMian.zhu_cai_dan()
        try:
            opt=int(input("请输入操作数字"))
            if opt==1:
                print("请输入要登陆的档案名字")
                date_file = input().strip()
                login_rec(date_file)
            elif opt==2:
                print("请输入要创建的档案名称")
                date_file = input().strip()
                create_rec(date_file)
            elif opt==3:
                print("成功退出系统")
                Tool.xi_ton("退出了系统")
                break
            else:
                print("请输入正确数字")
                Tool.xi_ton("你输入了不存在的操作数字")
        except ValueError:
            print("请输入有效值")
            Tool.xi_ton("你输入了错误的值")