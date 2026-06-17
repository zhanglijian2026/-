import utils
import time
from Tool import Tool
import datetime
import re
from os import remove
class GonNen:
    #评价输出
    @utils.date
    @utils.cw_fz
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
    @utils.lu_ru
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
    @utils.date
    @utils.cw_fz
    @utils.lu_ru
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
    @utils.date
    @utils.cw_fz
    @utils.lu_ru
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
    @utils.date
    @utils.cw_fz
    def shou_d_bian_li(self,xx):
            with open(xx, 'r', encoding="utf-8") as f:
                print("按回车键为下一条")
                for line in f:
                    print(line)
                    ss = input()
                print("已查看完所有数据")
            Tool.xi_ton("你手动遍历了历史数据")
    #删除档案
    @utils.lu_ru
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
    @utils.lu_ru
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