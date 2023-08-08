import mysql.connector
con = mysql.connector.connect(host = "localhost",user = "root",passwd = "Aniruddh#123",database = "db1")
class sql:
    def __init__(self) -> None:
        global con
        self.con = con.cursor()
        
    def viewjojo(self):
        self.con.execute("SELECT * FROM JoJo")
        data = self.con.fetchall()
        for i in data:
            print(i)
            
    def add(self,guild,id,amount):
        l = guild.split()

        self.con.execute(f"SELECT Coins FROM {str(l[0])} WHERE id = {id}")
        a = self.con.fetchall()   
        for i in a:
            for j in i:
                b = int(j)
        b += int(amount)

                
        self.con.execute(f'UPDATE {guild} SET Coins = {b} WHERE id = {id};')
        con.commit()

    
    def register(self,guild_name):
        try:
            l = guild_name.split()
            self.con.execute("CREATE TABLE "+str(l[0])+" (Name varchar(100),id BIGINT PRIMARY KEY,Coins int);")
            con.commit()
        except:
            return True
    
    def register_user(self,guild,id,name):
        l = guild.split()
        self.con.execute(f"SELECT * FROM "+l[0])
        a = self.con.fetchall()
        for i in a:
            if id in i:
                return True
        else:
            self.con.execute(f'INSERT INTO {l[0]} VALUES("'+ name +f'",{id},999);')
            self.add(guild,id,1)
        
    def subtract(self,guild,id,amount):
        l = guild.split()

        self.con.execute(f"SELECT Coins FROM {l[0]} WHERE id = {id}")
        a = self.con.fetchall()   
        for i in a:
            for j in i:
                b = j
        b = int(b)
        b -= int(amount)
                
        self.con.execute(f'UPDATE {l[0]} SET Coins = {b} WHERE id = {id};')
        con.commit()
        
    def balance(self,guild,id):
        b = 0
        l = guild.split()
        self.con.execute(f"SELECT Coins FROM {l[0]} WHERE id = {id}")
        a = self.con.fetchall()
        for i in a:
            for j in i:
                b = j
        return int(b)

    
    def leaderboard(self,guild):
        l = guild.split()
        self.con.execute(f"SELECT * FROM {l[0]} ORDER BY Coins DESC")
        a = self.con.fetchall()
        return a
    

