import sqlite3


class Repository:

    def __init__(self):
        self.database = sqlite3.connect('ch_lessons.sqlite')
        self.cursor = self.database.cursor()
        
    def get_by_oid(self, oid):
        self.cursor.execute(f'SELECT * FROM lessons WHERE oid={oid}')
        return self.cursor.fetchone()
    
    def get_progress(self):
        self.cursor.execute('SELECT * FROM progress')
        return self.cursor.fetchone()[0]

    def add_progress(self):
        progress = self.get_progress()
        self.cursor.execute(f'UPDATE progress SET value={progress + 1}')
        self.database.commit()

    def reset_progress(self):
        self.cursor.execute('UPDATE progress SET value=1')
        self.database.commit()



