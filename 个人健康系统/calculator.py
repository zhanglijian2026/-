import utils
import config
import time
import datetime
import math
from nemu import YeMian
from Tool import Tool
class Calculator:
    body_date ={'time': "",
                 'age': "",
                 'wt': "",
                 'ht': "",
                 'waist': "",
                 'neck': "",
                 'bmi': "",
                 'bmr': "",
                 'bft': "",
                 'bft_1': "",
                 'meta': ""}
    bmi_eval= ""
    bft_eval= ""
    waist_eval= ""
    def __init__(self,targe,six):
        """初始数据"""
        self.wt=0
        self.age=0
        self.ht=0
        self.waist=0
        self.neck=0
        self.bft=0
        self.bft_1=0
        self.meta=0
        self.bmi=0
        self.bmr=0
        self.date_file=targe
        self.six=six
    def main(self):
        #数据录入
        self.input_basic_data("年龄", "年", config.age_min, config.age_max)
        self.input_basic_data("体重", "kg", config.wt_min, config.wt_max)
        self.input_basic_data("身高", "cm", config.ht_min, config.ht_max)
        self.input_basic_data("腰围", "cm", config.waist_min,config.waist_max)
        self.input_basic_data("颈围", "cm", config.neck_min, config.neck_max)
        #计算
        self.date_computing()
        #保存并上传数据库
        self.__class__.save_temp(self)
        #评价
        self.date_comment()
        YeMian.date_frame(self.__class__.body_date,self.__class__.bft_eval)
        #输出评价
        self.output_evaluation()
        #释放内存
        self.__class__.clear_cache()

    #数据录入
    @utils.lu_ru
    def input_basic_data(self,body_vals:str,units:str,body_date_min:float,body_date_max:float):
        """输入数据"""
        while True:
            body_date= float(input(f'请输入{body_vals}：单位:{units},'))
            if body_date_min <= body_date <= body_date_max:
                print('成功输入')
                Tool.write_sys_opt_log(f"你成功输入了{body_vals}的值{body_date}{units}")
                break
            print(f'请输入正确{body_vals}（范围：{body_date_min}~{body_date_max}）')
        if body_vals=="年龄":
            self.age=body_date
        elif body_vals=="体重":
            self.wt=body_date
        elif body_vals=="身高":
            self.ht=body_date
        elif body_vals=="腰围":
            self.waist=body_date
        else:
            self.neck=body_date
        return
    #数据计算
    def date_computing(self):
        """计算"""
        print("系统正在计算，请稍后")
        time.sleep(0.5)
        print("计算完成")
        bmi = round(self.wt / (self.ht / 100 * self.ht / 100), 2)
        if self.six=="男":
            bmr = round(10 * self.wt + 6.25 * self.ht - 5 * self.age + 5, 1)
            bft = round(1.2 * bmi + 0.23 * self.age - 16.2, 2)
            meta = round(bmr * 1.55, 2)
            if self.neck !=self.waist:
                bft_1=round(495/(1.0324-0.19071*math.log10(abs(self.neck - self.waist))+0.15456*math.log10(self.ht)) - 450)
            else:
                bft_1=bft
        else:
            bmr = round(10 * self.wt + 6.25 * self.ht - 5 * self.age -161, 1)
            bft= round(1.2 * bmi + 0.23 * self.age - 5.4, 2)
            meta = round(bmr * 1.55, 2)
            if self.neck !=self.waist:
                bft_1=round(495/(1.0324-0.19071*math.log10(abs(self.waist-self.neck))+0.15456*math.log10(self.ht)) - 450)
            else:
                bft_1=bft
        self.bmi=bmi
        self.bmr=bmr
        self.bft=bft
        self.meta=meta
        self.bft_1=bft_1
    #赋值类属性
    @classmethod
    def save_temp(cls,date):
        cls.body_date = {'time': datetime.datetime.now().strftime('%Y-%m-%d'),
                     'age': date.age,
                     'wt': date.wt,
                     'ht': date.ht,
                     'waist': date.waist,
                     'neck': date.neck,
                     'bmi': date.bmi,
                     'bmr': date.bmr,
                     'bft': date.bft,
                     'bft_1': date.bft_1,
                     'meta':date.meta}
        config.zlj.add_data(cls.body_date)
    #评价
    def date_comment(self):
        if self.body_date['bmi'] < 18.5:
            bmi_eval = "偏瘦"
        elif self.body_date['bmi'] < 24:
            bmi_eval = "正常"
        elif self.body_date['bmi'] < 28:
            bmi_eval = "偏胖"
        else:
            bmi_eval= "肥胖"
        comp_bft = (self.body_date["bft"] + self.body_date["bft_1"]) / 2
        if self.six == "男":
            if comp_bft <= 10:
                bft_eval= "极低偏瘦"
            elif comp_bft <= 15:
                bft_eval= "完美健身身材"
            elif  comp_bft<= 18:
                bft_eval = "标准身材"
            elif comp_bft <= 22:
                bft_eval= "偏高，腹部有赘肉"
            else:
                bft_eval= "肥胖，脸胖肉松"
            if self.body_date["waist"] < 75:
                waist_eval = "标准苗条"
            elif self.body_date["waist"] < 85:
                waist_eval = "正常"
            else:
                waist_eval = "腹型肥胖，内脏脂肪高"
        else:
            if comp_bft <= 13:
                bft_eval= "极低偏瘦"
            elif comp_bft <= 20:
                bft_eval= "完美健身身材(运动员水平)"
            elif  comp_bft<= 24:
                bft_eval = "标准理想身材"
            elif comp_bft <= 31:
                bft_eval="正常"
            elif comp_bft <= 37:
                bft_eval= "偏高，腹部有赘肉"
            else:
                bft_eval= "肥胖，脸胖肉松"
            if self.body_date["waist"] < 80:
                waist_eval = "标准苗条"
            elif self.body_date["waist"] < 85:
                waist_eval = "正常"
            else:
                waist_eval = "腹型肥胖，内脏脂肪高"
        self.shadow_class_attribute(bmi_eval,bft_eval,waist_eval)
    @classmethod
    def shadow_class_attribute(cls,bmi_eval,bft_eval,waist_eval):
        cls.bmi_eval= bmi_eval
        cls.bft_eval= bft_eval
        cls.waist_eval= waist_eval
    @classmethod
    @utils.lu_ru
    def output_evaluation(cls):
        print("评价生成中。。。")
        time.sleep(0.4)
        print(f"单从bmi来看，你是{cls.bmi_eval},从综合体脂来看你是{cls.bft_eval},从腰围来看你是{cls.waist_eval}")
        print("2秒后自动返回主页面")
        time.sleep(0.3)
    @classmethod
    def clear_cache(cls):
        cls.body_date = {'time': "",
                     'age': "",
                     'wt': "",
                     'ht': "",
                     'waist': "",
                     'nect': "",
                     'bmi': "",
                     'bmr': "",
                     'bft': "",
                     'bft_1': "",
                     'meta': ""}
        cls.bmi_eval= ""
        cls.bft_eval= ""
        cls.waist_eval= ""
    def __del__(self):
        self.wt = 0
        self.age = 0
        self.ht = 0
        self.waist = 0
        self.neck = 0
        self.bft = 0
        self.bft_1 = 0
        self.meta = 0
        self.bmi = 0
        self.bmr = 0
        self.date_file = ""
        self.six = ""
        return

