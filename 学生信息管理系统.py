import sqlite3
#表头装饰器
def biao_tou(funes):
    def date_er(*args,**kw):
        print("序号\t\t名字\t\t学号\t\t年龄\t\t性别")
        return funes(*args,**kw)
    return date_er
#连接内置数据库
def c_j():
    conn=sqlite3.connect("xiu_sen.db")
    return conn
#创建表
def jian_biao ():
    conn=c_j()
    cursor=conn.cursor()
    try:
        sql="""CREATE TABLE IF NOT EXISTS student(
        student_id   integer   primary key autoincrement,
        name     text   not null, 
        stu_id int   unique not null,  
        age    int   not null,
        gander   text   not null
        )
        """
        cursor.execute(sql)
        conn.commit()
    except sqlite3.Error :
        print("你已经创建了表格")
    finally:
        cursor.close()
        conn.close()
#页面
def ye_mian():
    print("==========学生信息管理系统=========")
    print("1.录入数据")
    print("2.查看数据")
    print("3.修改数据")
    print("4.删除数据")
    print("5.退出系统")
#分也面
def cha_xun():
    while True:
        try:
            print("1,查询学生数据")
            print("2.查看所有学生数据")
            c_z=int(input())
            if c_z<0 or c_z>2:
                continue
            return c_z
        except ValueError:
            print("请输入正确数字")
#增删查改
class SQL:
    #创建游标
    def __init__(self):
        self.conn=c_j()
        self.cursor=self.conn.cursor()
    #增加操作的数据输入
    @staticmethod
    def date_computing():
        xin_bie=""
        while True:
                shu_ju1=input("请输入名字")
                break
        while True:
            try:
                shu_ju2=int(input("请输入学号"))
                break
            except ValueError:
                print("请输入正确学号")
        while True:
            try:
                shu_ji3=int(input("请输入年龄"))
                break
            except ValueError:
                print("请输入正确年龄")
        while True:
            try:
                print("请输入性别序号：1，男，2.女")
                shu_ji4=int(input())
                if shu_ji4<1 or shu_ji4>2:
                    continue
                if shu_ji4==1:
                    xin_bie="男"
                    break
                if shu_ji4==2:
                    xin_bie="女"
                    break
            except ValueError:
                print("请输入正确序号")
        return [shu_ju1,shu_ju2,shu_ji3,xin_bie]
    #增加数据
    def zheng_jia(self,date):
        try:
            sql="INSERT INTO student(name,stu_id,age,gander) VALUES(?,?,?,?)"
            self.cursor.execute(sql,date)
            self.conn.commit()
            print("录入成功")
        except sqlite3.IntegrityError:
            print("学号已存在")
            print("录入失败")
        except sqlite3.Error:
            print("录入失败")
    #查找数据
    def show(self):
        try:
            sql="SELECT * FROM  student"
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
            self.hua_bian(res)
        except sqlite3.Error:
            print("查看数据失败")
    #删除数据
    def dell(self):
        try:
            del_id=int(input("请输入要删除的学生学号："))
            sql="DELETE FROM student WHERE stu_id =?"
            self.cursor.execute(sql,(del_id,))
            if self.cursor.rowcount==0:
                print("未找到该生")
            else:
                self.conn.commit()
                print("删除成功")
        except ValueError:
            print("学号必须是数字")
        except sqlite3.Error:
            print("数据删除失败")
    #数据查询的输出
    @biao_tou
    def hua_bian(self,res):
        if not res:
            print("暂无学生数据")
            return
        for stu in res:
            sid,name,stu_id,age,gander=stu
            print(f"{sid}\t\t{name}\t\t{stu_id}\t\t{age}\t\t{gander}")
    #数据修改
    def gai_jia(self):
        while True:
            try:
                edit_sql=int(input("请输入要修改的学生学号："))
                self.cursor.execute("SELECT * FROM student  WHERE stu_id=?",(edit_sql,))
                if not self.cursor.fetchone():
                    print("该学号不存在")
                    return
                break
            except ValueError:
                print("请输入正确数字")
        while True:
            try:
                print("可修改的选项，1，姓名，2.年龄，3，性别")
                opq=int(input("请选择要修改的选项："))
                new_opq=input("请输入新内容：").strip()
                sql=""
                param=()
                if opq==1:
                    sql="update student set name=? where stu_id=?"
                    param=(new_opq,edit_sql)
                elif opq==2:
                    new_opq=int(new_opq)
                    sql="update student set age=? where stu_id=?"
                    param=(new_opq,edit_sql)
                elif opq==3:
                    if new_opq not in ["男","女"]:
                        print("如果要改性别，请输入男/女")
                        return
                    sql="update student set gander=? where stu_id=?"
                    param=(new_opq,edit_sql)
                else:
                    print("请输入1~3的数字")

                self.cursor.execute(sql,param)
                self.conn.commit()
                print("修改成功")
                break
            except ValueError:
                print("输入数字格式错误")
            except sqlite3.Error:
                print("数据修改失败")
    #单个学生的查询
    def cha_xiu(self):
        while True:
            try:
                print("请输入要查询的学生学号")
                x_h=int(input())
                if x_h<0 :
                    continue
                break
            except ValueError:
                print("请输入数字")
            except sqlite3.Error as e:
                print(e)
        try:
            sql_text="SELECT * FROM student WHERE stu_id =?"
            self.cursor.execute(sql_text,(x_h,))
            res=self.cursor.fetchall()
            self.dan_re(res)
        except sqlite3.Error as e:
            print(e)
    ##单个学生数据的输出
    @biao_tou
    def dan_re(self,res):
        if not res:
            print("没有查询到该生学号")
            return
        row=res[0]
        sid,name,stu_id,age,gander=row
        print(f"{sid}\t\t{name}\t\t{stu_id}\t\t{age}\t\t{gander}")
    #关闭链接和游标
    def xxx(self):
        self.cursor.close()
        self.conn.close()
        print("数据库连接已关闭")
    #主交互窗口
    def main(self):
        while True:
            ye_mian()
            try:
                c_z=int(input("请输入操作数字"))
                if c_z==1:
                    date=tuple(SQL.date_computing())
                    self.zheng_jia(date)
                elif c_z==2:
                    chao_xun=cha_xun()
                    if chao_xun==1:
                        self.cha_xiu()
                    else:
                       self.show()
                elif c_z==3:
                    self.gai_jia()
                elif c_z==4:
                    self.dell()
                elif c_z==5:
                    self.xxx()
                    print("退出系统成功")
                    break
                else:
                    print("请输入正确数字")
                    continue
            except ValueError:
               print("请输入正确操作数字")
if __name__ == "__main__":
    jian_biao()
    zl =SQL()
    zl.main()