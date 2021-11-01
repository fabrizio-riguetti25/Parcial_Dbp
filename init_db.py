import sqlite3

con = sqlite3.connect('curriculums.db')

cur = con.cursor()

cur.execute('''CREATE TABLE users(
               nombre text, 
               cargo text, 
               centro_estudio text, 
               telefono text, 
               direccion text,
               email text, 
               password text, 
               experiencia json,
               educacion json,
               competencias json)''')


con.commit()

con.close()