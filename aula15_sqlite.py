import sqlite3

config = 'aula15.db'
s = sqlite3.connect(config)
c = s.cursor()

sql = """
    create table if not exists t(
    id integer not null primary key autoincrement,
    nome text not null,
    idade integer
    );
"""

sql = """
    insert into t(nome, idade)
    values(?, ?);
"""
nome = 'Andre Ricardo'
idade = 50
#c.execute(sql, (nome, idade))
#s.commit()

sql = 'select * from t;'
resultado = c.execute(sql)
print(resultado.fetchall())

sql = """
    update t
    set nome = ?, idade = ?
    where id = ?;
"""

id = 1
c.execute(sql, (nome, idade, id))
s.commit()

sql = 'select * from t;'
resultado = c.execute(sql)
print(resultado.fetchall())

sql = '''
    delete from t
    where id = ?;
'''
c.execute(sql, (id,))
s.commit()

s.close()