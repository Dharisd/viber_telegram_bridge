import sqlite3
import settings
import tempfile, shutil, os



class SQLTools():
        
    def __init__(self):
        #load everything fron .env file
        #print(f"inital path:{settings.db_location}")
        self.db_file = os.path.join(settings.db_location,"viber.db")
        
        
        

    
    def create_db_copy(self):            
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, 'viber.db')
        shutil.copy2(self.db_file, temp_path)
        self.db_file = temp_path
        
        
        
        
    def create_connection(self):
        try:
            #self.create_db_copy()
            #print(self.db_file)
            self.conn = sqlite3.connect(self.db_file)
            return self.conn
        
        #handle locked db
        except Exception as e:
            #please do logging later
            print(e) 


            

        return None




    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)



        return cur.fetchall()