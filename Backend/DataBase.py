import sqlite3
import json
class DatabaseIndex:
    """creates connection to database and sets the database up if it is empty."""
    def __init__(self, database):
        self.__database = database
        self.__database_to_edit = sqlite3.connect(self.__database)
        self.__cursor_obj = self.__database_to_edit.cursor()
        self.database_setup()


    def add_new_image(self, ):
        added_element = "INSERT INTO Images (Image_Path, Image_Name) VALUES (?, ?) "
       
    
    
    

    
    
   


    #TODO: Modify this code base so that it can store games instead of images. Keep in mind that the appid is the only thing that should be not null

    """Sets up database if it has not already been set up."""
    def database_setup(self):
        self.__cursor_obj.execute("""CREATE TABLE IF NOT EXISTS Games(
            AppID INT PRIMARY KEY NOT NULL,
            Game_Name VARCHAR(255) NOT NULL
            
         ); """)
        
        self.__database_to_edit.commit()
    
    """close the connection if it is open"""
    def close_connection(self):
        if self.__database_to_edit is not None:
            self.__database_to_edit.close()
            self.__database_to_edit = None

    def reopen_connection(self):
        if self.__database_to_edit is None:
            self.__database_to_edit = sqlite3.connect(self.__database)
    
    def get_cursor(self):
        return self.__cursor_obj

    
database = DatabaseIndex("database.db")


