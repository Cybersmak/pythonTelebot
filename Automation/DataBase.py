import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self,User_ID):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`User_ID`) VALUES (?)",(User_ID,))

    def user_exists(self,User_ID):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `User_ID` = ?",(User_ID,)).fetchall()
            return bool(len(result))

    def set_name(self,User_ID,Name):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `Name` = ? WHERE `User_ID` = ?",(Name,User_ID,))

    def get_signup(self,User_ID):
        with self.connection:
            result = self.cursor.execute("SELECT `signup` FROM `users` WHERE `User_ID` = ?",(User_ID,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup
    def get_name(self,User_ID):
        with self.connection:
            result = self.cursor.execute("SELECT `Name` FROM `users` WHERE `User_ID` = ?",(User_ID,)).fetchall()
            for row in result:
                Name = str(row[0])
            return Name

    def set_signup(self,User_ID,signup):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `signup` = ? WHERE `User_ID` = ?",(signup,User_ID,))
            

    def set_phone(self,User_ID,Phone):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `Phone` = ? WHERE `User_ID` = ?",(Phone,User_ID,))

    def set_key(self,User_ID,Key):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `Key` = ? WHERE `User_ID` = ?",(Key,User_ID,))

        
    def get_phone(self,User_ID):
        with self.connection:
            result = self.cursor.execute("SELECT `Phone` FROM `users` WHERE `User_ID` = ?",(User_ID,)).fetchall()
            for row in result:
                Phone = str(row[0])
            return Phone
            
    def get_key(self,User_ID):
        with self.connection:
            result = self.cursor.execute("SELECT `Key` FROM `users` WHERE `User_ID` = ?",(User_ID,)).fetchall()
            for row in result:
                Key = str(row[0])
            return Key   
                    
    def get_key1(self,User_ID):
        with self.connection:
            result = self.cursor.execute("SELECT `Key` FROM `users` WHERE `User_ID` = ?",(User_ID,)).fetchone()
            return result