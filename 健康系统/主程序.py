import datetime
import math
import time
import re
import os
from os import remove
import threading
xi_ton="系统日志.txt"
log_look=threading.Lock()
#边界值
Nian_lin_min,Nian_lin_max=1,200
Ti_zh_min,Ti_zh_max=1,250
She_gao_min,She_gao_max=1,300
Yao_wei_min,Yao_wei_max=1,150
Jin_wei_min,Jin_wei_max=1,100
#表头装饰器
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
                Tool.xi_ton("你输入了错误的值")
    return date_6
#工具类
class Tool:
    #遍历生成器工具
    @staticmethod
    @cw_fz
    def in_tr():
        return (f for f in os.listdir() if f.endswith(".txt") and f != "系统日志.txt")
    #判断是否存在文件，不存在则创建
    @staticmethod
    @cw_fz
    def _init_file(xx):
        for file in [xi_ton, xx]:
            if not os.path.exists(file):
                with open(file, "w+", encoding="utf-8") as f:
                    f.write("")
    #异步处理系统日志
    @staticmethod
    @cw_fz
    def xi_ton(xin_xi:str):
        t = threading.Thread(target=Tool.yi_bu_ji_lu, args=(xin_xi,))
        t.daemon = True
        t.start()
    #系统日志
    @staticmethod
    @cw_fz
    def yi_bu_ji_lu(xin_xi:str):
        with log_look:
            with open(xi_ton, 'a+', encoding='utf-8') as f:
                shi_jiang = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"{shi_jiang},{xin_xi}\n")
    #判断文件是否为空
    @staticmethod
    @cw_fz
    def p_d_lu_jin(xx):
            with open(xx,'r',encoding="utf-8") as f:
                shu_ju=f.readlines()
            return 0 if shu_ju==[] else 1
    #数据存入文件
    @staticmethod
    @cw_fz
    def save_file(a,xx):
            line = (f"{a['时间']}\t\t{a['年龄']}\t{a['体重']}\t{a['身高']}\t{a['腰围']}\t{a['颈围']}\t{a['BMI']}"
                    f"\t{a['BMR']}\t\t{a['体脂率']}\t{a['腰体脂率']}\t{a['基础代谢']}\n")
            with open(xx, 'a', encoding="utf-8") as f:
                f.write(line)
#功能类
class GonNen:
    #评价输出
    @staticmethod
    @lu_ru
    def pin_jia_shu_chu(ji):
        cz2 = int(input("请问是否允许我们进行评价，1.是，2.否"))
        if cz2 == 1:
            print("评价生成中。。。")
            time.sleep(0.8)
            print(f"单从bmi来看，你是{ji[0]},从综合体脂{ji[3]}来看你是{ji[1]},从腰围来看你是{ji[2]}")
            Tool.xi_ton("你允许了评价操作")
            print("2秒后自动返回主页面")
            time.sleep(0.8)
        elif cz2 == 2:
            print("好的")
            Tool.xi_ton("你拒接了评价操作")
            print("2秒后自动返回主页面")
            time.sleep(0.8)
        else:
            print("请填写正确操作")
        return
    #查看所有数据
    @date
    @cw_fz
    def ton_jia(self,xx):
        """统计"""
        shu_zi, ping_ju1, ping_ju2 = 0, 0, 0
        with open(xx, 'r', encoding="utf-8") as f:
            for b in f:
                if b == "":
                    continue
                print(b)
        with open(xx, 'r', encoding="utf-8") as f:
            for line in f:
                lines = re.findall(r'(\d+\.\d+)', line)
                shu_zi += 1
                ping_ju1 += float(lines[7])
                ping_ju2 += float(lines[8])
            if shu_zi == 0:
                print("无法计算")
            else:
                print(f"你的平均bmi体脂率为{round(ping_ju1 / shu_zi, 2)}%,你的专业标准体脂平均为{round(ping_ju2 / shu_zi, 2)}%", )
        print("2秒后自动返回主页面")
        time.sleep(1)
    #清空历史数据
    @lu_ru
    def clear_date(self,xx):
        pan_duan = int(input())
        if pan_duan == 1:
            with open(xx, 'w', encoding="utf-8") as f:
                f.write('')
            Tool.xi_ton("您清空了历史数据")
            print("数据清理中")
            time.sleep(0.8)
            print("数据清理完毕，正在自动为你跳转到主页面")
            time.sleep(0.7)
            return
        elif pan_duan == 2:
            print("正在为您取消此操作")
            time.sleep(0.8)
            print("取消成功，自动返回主页面")
            time.sleep(0.5)
            return
        else:
            print("请输入正确操作数字")
    #按日期查看数据
    @date
    @cw_fz
    @lu_ru
    def re_qi_bian_li(self,xx):
            start_date = input("请输入开始日期(格式YYYY-MM-DD)：")
            end_date = input("请输入结束日期(格式YYYY-MM-DD)：")
            s = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            e = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            with open(xx, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    time_str = line.split("\t")[0]
                    record_date = datetime.datetime.strptime(time_str[:10], "%Y-%m-%d")
                    if s <= record_date <= e:
                        print(line)
                print("自动返回主页面")
                Tool.xi_ton(f"你查找了{s}到{e}的历史数据")
                time.sleep(1)
                return
    #自动遍历数据
    @date
    @cw_fz
    @lu_ru
    def zhu_tia_bian_li(self,xx):
        time1 = float(input())
        if time1 <=0 :
            time1=1
            print("感觉你。。。。,系统自动为你把倍速改为1s一条。")
        with open(xx, 'r', encoding="utf-8") as f:
            for line in f:
                if not line == "":
                    print(line)
                    time.sleep(time1)
        Tool.xi_ton(f"你用{time1}倍速度自动遍历了历史数据")
        return
    #手动遍历数据
    @date
    @cw_fz
    def shou_d_bian_li(self,xx):
            with open(xx, 'r', encoding="utf-8") as f:
                print("按回车键为下一条")
                for line in f:
                    print(line)
                    ss = input()
                print("已查看完所有数据")
            Tool.xi_ton("你手动遍历了历史数据")
    #删除档案
    @lu_ru
    def san_chu(self,xx):
        if not xx:
            print("不存在此文件")
            return
        else:
            print("请确认是否要删除档案，1，是 2，否")
            sss = int(input())
            if sss==1:
                remove(xx)
                print("你已经成功删除，正在返回主页面")
                time.sleep(0.8)
                Tool.xi_ton("你成功删除了文件")
                return
            elif sss==2:
                print("你已经取消操作，2s后自动回页面")
                time.sleep(0.8)
                Tool.xi_ton("你取消了这个操作")
                return
            else:
                print("请输入正确数字")
    @staticmethod
    @lu_ru
    def six_pd():
        print("请确认您的性别,输操作数字即可")
        print("1.男")
        print("2.女")
        six_1=int(input())
        if six_1<0 or six_1>2:
            pass
        else:
            return six_1
    @staticmethod
    def six_qr(a):
        b=a+".man.txt"
        c = b in Tool.in_tr()
        if c:
            return b
        else:
            j = a + ".gril.txt"
            d = j in Tool.in_tr()
            if d:
                return j
            else:
                return None
#页面类
class YeMian:
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
    def date_frame(shu_gu1, ji):
        """"个人数据"""
        print(f'你的BMI为：{shu_gu1["BMI"]}')
        print(f'你的BMR为；{shu_gu1["BMR"]}')
        print(f'你的体脂率为：{shu_gu1["体脂率"]}%')
        print(f'你的体脂率2为：{shu_gu1["腰体脂率"]}%')
        print(f'你的综合体脂率为：{ji[3]}%')
        print(f'你的基础代谢为{shu_gu1["基础代谢"]}')
        SenNiShuGuJiangCe.pin_jia_shu_chu(ji)
    #查看数据页面
    @staticmethod
    def fen_ye_mian():
        print("\n请输入查看数据方式")
        print("1.直接查看所有数据")
        print("2.自动逐条遍历所有数据")
        print("3.手动逐条遍历所有数据")
        print("4.查看某天的数据")
#业务类
class SenNiShuGuJiangCe(Tool,YeMian,GonNen) :
    def __init__(self,targe,six):
        """初始数据"""
        self.ti_zh=0
        self.nian_lin=0
        self.sen_gao=0
        self.yao_wei=0
        self.jin_wei=0
        self.date_file=targe
        self.six=six
        Tool._init_file(self.date_file)
    #数据录入
    @lu_ru
    def input_basic_data(self,shu_jiang:str,dan_wei:str,xian_xian:int,san_xian:int):
        """输入数据"""
        while True:
            nian_lin = float(input(f'请输入{shu_jiang}：单位{dan_wei}'))
            if xian_xian < nian_lin <= san_xian:
                print('成功输入')
                Tool.xi_ton(f"你成功输入了{shu_jiang}的值{nian_lin}{dan_wei}")
                break
            print(f'请输入正确{shu_jiang}（范围：{xian_xian}~{san_xian}）')
        if shu_jiang=="年龄":
            self.nian_lin=nian_lin
        elif shu_jiang=="体重":
            self.ti_zh=nian_lin
        elif shu_jiang=="身高":
            self.sen_gao=nian_lin
        elif shu_jiang=="腰围":
            self.yao_wei=nian_lin
        else:
            self.jin_wei=nian_lin
        return
    #数字评价
    @staticmethod
    def date_comment(shu_gu1):
        """评价分析"""
        if shu_gu1['BMI'] < 18.5:
            bmi3 = "偏瘦"
        elif shu_gu1['BMI'] < 24:
            bmi3 = "正常"
        elif shu_gu1['BMI'] < 28:
            bmi3 = "偏胖"
        else:
            bmi3 = "肥胖"
        zhon_he_tiz = (shu_gu1["体脂率"] + shu_gu1["腰体脂率"]) / 2
        if zhon_he_tiz <= 10:
            ti_zi1 = "极低偏瘦"
        elif zhon_he_tiz <= 15:
            ti_zi1 = "完美健身身材"
        elif zhon_he_tiz <= 18:
            ti_zi1 = "标准身材"
        elif zhon_he_tiz <= 22:
            ti_zi1 = "偏高，腹部有赘肉"
        else:
            ti_zi1 = "肥胖，脸胖肉松"
        if shu_gu1["腰围"] < 75:
            yao_bu1 = "标准苗条"
        elif shu_gu1["腰围"] < 85:
            yao_bu1 = "正常"
        else:
            yao_bu1 = "腹型肥胖，内脏脂肪高"
        return [bmi3, ti_zi1, yao_bu1, zhon_he_tiz]
    #数据计算
    @cw_fz
    def date_computing(self):
        """计算"""
        print("系统正在计算，请稍后")
        time.sleep(0.5)
        print("计算完成")
        bmi = round(self.ti_zh / (self.sen_gao / 100 * self.sen_gao / 100), 2)
        if self.six==1:
            bmr = round(10 * self.ti_zh + 6.25 * self.sen_gao - 5 * self.nian_lin + 5, 1)
            ti_zi = round(1.2 * bmi + 0.23 * self.nian_lin - 16.2, 2)
            dai_xie = round(bmr * 1.55, 2)
            if self.jin_wei !=self.yao_wei:
                ti_zi2=round(495/(1.0324-0.19071*math.log10(abs(self.jin_wei - self.yao_wei))+0.15456*math.log10(self.sen_gao)) - 450)
            else:
                ti_zi2=ti_zi
        else:
            bmr = round(10 * self.ti_zh + 6.25 * self.sen_gao - 5 * self.nian_lin + 5, 1)
            ti_zi = round(1.2 * bmi + 0.23 * self.nian_lin - 5.4, 2)
            dai_xie = round(bmr * 1.55, 2)
            if self.jin_wei !=self.yao_wei:
                ti_zi2=round(495/(1.0324-0.19071*math.log10(abs(self.yao_wei-self.jin_wei))+0.15456*math.log10(self.sen_gao)) - 450)
            else:
                ti_zi2=ti_zi
        shu_gu1 = {'时间': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                   '年龄': self.nian_lin,
                   '体重': self.ti_zh,
                   '身高': self.sen_gao,
                   '腰围': self.yao_wei,
                   '颈围': self.jin_wei,
                   'BMI': bmi,
                   'BMR': bmr,
                   '体脂率': ti_zi,
                   '腰体脂率': ti_zi2,
                   '基础代谢': dai_xie}
        ji = SenNiShuGuJiangCe.date_comment(shu_gu1)
        YeMian.date_frame(shu_gu1, ji)
        Tool.save_file(shu_gu1,self.date_file)
    #功能页面
    def main(self):
        """主程序"""
        while True:
            YeMian.ye_mian()
            while True:
                try:
                    print('请输入1~5的操作数字')
                    chao_zuo=int(input())
                    if chao_zuo<=0 or chao_zuo>5:
                        print("请输入1~5的操作")
                        Tool.xi_ton("你输入了错误操作")
                        continue
                    else:
                        print("操作成功")
                        Tool.xi_ton(f"你输入了{chao_zuo}操作")
                    break
                except ValueError:
                    Tool.xi_ton("你输入了错误的操作")
                    print('请输入正确操作')
            if chao_zuo==1:
                self.input_basic_data("年龄","年",Nian_lin_min,Nian_lin_max)
                self.input_basic_data("体重","kg",Ti_zh_min,Ti_zh_max)
                self.input_basic_data("身高","cm",She_gao_min,She_gao_max)
                self.input_basic_data("腰围","cm",Yao_wei_min,Yao_wei_max)
                self.input_basic_data("颈围","cm",Jin_wei_min,Jin_wei_max)

                self.date_computing()
            elif chao_zuo==2:
                p_d=Tool.p_d_lu_jin(self.date_file)
                if p_d==0:
                    print("无历史数据")
                    Tool.xi_ton("你查看了历史数据，但是发现没有")
                else:
                    try:
                        YeMian.fen_ye_mian()
                        c_z2=int(input())
                        if c_z2==1:
                           self.ton_jia(self.date_file)
                        elif c_z2==2:
                            print("请输入逐条遍历的速度,建议0.1")
                            self.zhu_tia_bian_li(self.date_file)
                        elif c_z2==3:
                            self.shou_d_bian_li(self.date_file)
                            print("按回车健为下一条")
                        elif c_z2==4:
                            self.re_qi_bian_li(self.date_file)
                        else:
                            print("请输入正确操作")
                    except ValueError:
                        print("请返回主页面操作")
                        Tool.xi_ton("你输入了错误的操作")
                        time.sleep(0.4)
            elif chao_zuo==3:
                print("操作会清空历史数据，且无法恢复,是否确定要如此操作,1.是，2,否")
                self.clear_date(self.date_file)
                Tool.xi_ton("你清空了历史数据")
            elif chao_zuo==4:
                Tool.xi_ton(f"你想要删除{self.date_file}文件")
                self.san_chu(self.date_file)
                break
            else:
                print('成功退出档案')
                Tool.xi_ton("成功退出档案")
                break
if __name__ == '__main__':
    #主页面的登陆等
    while True:
        YeMian.zhu_cai_dan()
        try:
            c_z=int(input())
            if c_z==1:
                print("请输入要登陆的档案名字")
                date_file = input().strip()
                if not date_file:
                    print("档案名不能为空,或者档案名不能为空格")
                    time.sleep(0.5)
                    Tool.xi_ton("你在登陆中没有输入档案名就回车了，或者输入了空格")
                    continue
                if date_file.endswith(".txt"):
                    date_file=date_file[:-4]
                exists=GonNen.six_qr(date_file)
                if exists.endswith(".man.txt"):
                    six=1
                    zlj = SenNiShuGuJiangCe(exists,six)
                    zlj.main()
                elif exists.endswith(".gril.txt"):
                    six=2
                    zlj = SenNiShuGuJiangCe(exists,six)
                    zlj.main()
                else:
                    print("档案不存在，返回主页")
                    Tool.xi_ton("你输入了不存在的档案名")
                    time.sleep(0.5)
            elif c_z==2:
                print("请输入要创建的档案名称")
                date_file = input().strip()
                if not date_file:
                    print("档案名不能为空")
                    time.sleep(0.5)
                    Tool.xi_ton("你在创建中没有输入档案名就回车了，或者输入了空格")
                    continue
                six=GonNen.six_pd()
                if date_file.endswith(".txt"):
                    date_file=date_file[:-4]
                    if six==1:
                       target=date_file+".man.txt"
                    else:
                        target=date_file+".girl.txt"
                else:
                    if six==1:
                        target = date_file + ".man.txt"
                    else:
                        target = date_file + ".girl.txt"
                exists = target in Tool.in_tr()
                if not exists:
                    zlj = SenNiShuGuJiangCe(target,six)
                    print("创建成功")
                    Tool.xi_ton(f"你成功创建了名为{target}的档案")
                    time.sleep(0.8)
                    zlj.main()
                else:
                    print("档案已存在,返回主页面中")
                    Tool.xi_ton("你在创建中输入了已经存在的档案名")
                    time.sleep(0.5)
            elif c_z==3:
                print("成功退出系统")
                Tool.xi_ton("退出了系统")
                break
            else:
                print("请输入正确数字")
                Tool.xi_ton("你输入了不存在的操作数字")
        except ValueError:
            print("请输入有效值")
            Tool.xi_ton("你输入了错误的值")