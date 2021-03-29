import sqlite3
from urllib.request import urlopen
import json

db = sqlite3.connect('ch_lessons.sqlite')
cursor = db.cursor()

cursor.execute('CREATE TABLE "progress" ("value" INTEGER)')
cursor.execute('INSERT INTO progress VALUES (0)')

cursor.execute('''CREATE TABLE "lessons" (
     "id" INTEGER UNIQUE,
     "oid" INTEGER DEFAULT 0 UNIQUE,
     "character" TEXT,
     "translation" TEXT,
     "stroke_count" UNSIGNED INTEGER,
     PRIMARY KEY("id" AUTOINCREMENT));
     '''
)


data = urlopen("https://gist.githubusercontent.com/branneman/f93d596ac236f0dbd9fb5b1a5099122f/raw/35510b58615c506c81b45551a500bc06ec11478a/radicals.json").read().decode('utf-8')

data = json.loads(data)

for item in data:
    cursor.execute(f'INSERT INTO lessons (oid, character, translation, stroke_count) VALUES ({item["id"]},\'{item["radical"]}\',\'{item["english"]}\',{item["strokeCount"]})')

db.commit()
cursor.close()
db.close()
