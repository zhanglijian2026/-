import sqlite3
#建立连接
def connect_database():
    conn = sqlite3.connect("database.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
#创建总表
def create_database():
    try:
        conn = connect_database()
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS data_base (
               data_id  integer PRIMARY KEY AUTOINCREMENT,
               name     text NOT NULL,
               sex   text NOT NULL
               )
               """
        cursor.execute(sql)
        conn.commit()
    except sqlite3.connect :
        print("已成功连接数据库")
class DatePersistence:
    def __init__(self):
        self.conn = connect_database()
        self.cursor = self.conn.cursor()
        self.name = None
        self.sex=None
        self.data_id = None
    #创建用户
    def create_table(self,name:str,sex:str):
        self.cursor.execute("SELECT data_id FROM data_base WHERE name=? and sex=?",(name,sex))
        if  self.cursor.fetchone():
            print("用户已存在")
            return 1
        try:
            sql = "INSERT INTO data_base(name,sex) VALUES(?,?)"
            self.cursor.execute(sql,[name,sex])
            self.conn.commit()
            self.data_id= self.cursor.lastrowid
            self.name= name
            self.sex=sex
            sql=f"""CREATE TABLE IF NOT EXISTS {self.name}( 
            id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, 
            data_id INTEGER NOT NULL,
            time  TEXT NOT NULL ,
            age INTEGER NOT NULL,
            wt   REAL NOT NULL,
            ht   REAL NOT NULL,
            waist REAL NOT NULL,
            neck REAL NOT NULL,
            bmi REAL NOT NULL,
            bmr REAL NOT NULL,
            bft REAL NOT NULL,
            bft_1 REAL NOT NULL,
            meta REAL NOT NULL,
            FOREIGN KEY (data_id) REFERENCES data_base (data_id)
            ON UPDATE CASCADE
            ON DELETE CASCADE
            )"""
            self.cursor.execute(sql)
            self.conn.commit()
        except sqlite3.connect :
            self.conn.rollback()
            print("创建失败")
    #登陆用户
    def login(self,input_name:str,input_sex:str):
        self.cursor.execute("SELECT name,sex FROM data_base WHERE name=? and sex=?", (input_name, input_sex))
        user_id=self.cursor.fetchone()
        if  not user_id:
            print("用户不存在")
            return 1
        self.data_id,self.name,self.sex=user_id
        print("登陆成功")
        return None
    #删除用户
    def delete_file(self):
        try:
            self.conn.execute("SELECT date_id,name,sex From data_base WHERE name=? and sex=?",(self.name,self.sex))
            res=self.cursor.fetchone()
            if not res:
                print("用户不存在")
                return 1
            self.cursor.execute(f"drop table data_base if exists `{self.name}`")
            self.cursor.execute(f"delete from data_base where name=? and sex=?",(self.name,self.sex))
            self.conn.commit()
            self.data_id=None
            self.name=None
            self.sex=None
        except sqlite3.connect :
            self.conn.rollback()
            print("删除失败")
    #增加数据
    def add_data(self, data: dict):
        try:
            sql = f"insert into {self.name}(time,age,wt,ht,waist,neck,bmi,bmr,bft,bft_1,meta) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            self.cursor.execute(sql, data)
            self.conn.commit()
        except sqlite3.connect :
            self.conn.rollback()
            print("录入失败")
    #清空数据
    def drop_data(self):
        try:
            sql=f"delete from {self.name}"
            self.cursor.execute(sql)
            self.conn.commit()
        except sqlite3.connect :
            self.conn.rollback()
            print("清空数据失败")
    #查看所有数据
    def get_data(self):
        try:
            sql=f"select * from {self.name}"
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
            if not res:
                print("没有数据")
                return None
            return res
        except sqlite3.connect :
            self.conn.rollback()
            print("查看失败")
    #查看单条数据
    def get_data_one(self,):
        try:
            sql=f"select * from {self.name}"
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
            if not res:
                print("没有发现数据")
                return None
            class Reset:
                def __init__(self):
                    yield from res
            return Reset()
        except sqlite3.connect :
            self.conn.rollback()
            print("查看失败")
    #按日期查找
    def day_get_data(self,start,end):
        try:
            day_data=[]
            sql=f"select * from {self.name}"
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
            if not res:
                print("没有数据")
                return None
            for i in res:
                if start<=i[1]<=end:
                    day_data.append(i)
            if not day_data:
                print("当前日期没有数据")
                return None
            return day_data
        except sqlite3.connect :
            self.conn.rollback()
            print("查看失败")
    #关闭连接
    def close_data(self):
        self.cursor.close()
        self.conn.close()








