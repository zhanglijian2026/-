import sqlite3
def connect_database():
    conn = sqlite3.connect("database.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
def create_database():
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
class DatePersistence:
    def __init__(self):
        self.conn = connect_database()
        self.cursor = self.conn.cursor()
        self.name = None
        self.sex=None
        self.data_id = None
    def create_table(self,name:str,sex:str):
        self.cursor.execute("SELECT data_id FROM data_base WHERE name=? and sex=?",(name,sex))
        if  self.cursor.fetchone():
            print("用户已存在")
            return
        sql = "INSERT INTO data_base(name,sex) VALUES(?,?)"
        self.cursor.execute(sql,[name,sex])
        self.conn.commit()
        self.data_id= self.cursor.lastrowid
        self.name= name
        self.sex=sex
        sql=f"""CREATE TABLE IF NOT EXISTS {self.name}( (
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
    def login(self,input_name:str,input_sex:str):
        user_id=self.cursor.execute("SELECT data_id,name,sex FROM data_base WHERE name=? and sex=?", (input_name, input_sex))
        if  not self.cursor.fetchone():
            print("用户不存在")
        self.data_id,self.name,self.sex=user_id
        print("登陆成功")
    def add_data(self,data:dict):
        sql=f"insert into {self.name}(time,age,wt,ht,waist,neck,bmi,bmr,bft,bft_1,meta) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
        self.cursor.execute(sql,data)
        self.conn.commit()
