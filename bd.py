import mysql.connector
import datetime as dt


def conecta():
    return mysql.connector.connect( host="localhost",
                                    user="root",
                                    password="admin",
                                    database="bd_chamados")



def abre_chamado(nome, local, setor, comentario):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into chamados(nome, local, setor, data_abertura, comentario) values (%s, %s, %s, %s, %s)"
    valores = (nome, local, setor, dt.datetime.now(), comentario)

    cursor.execute(sql, valores)
    bd.commit()

    return 'Inserido com sucesso!!!'


def listar_chamados():
    bd = conecta()
    cursor = bd.cursor()

    sql = "select * from chamados"
    cursor.execute(sql)

    return cursor.fetchall()


def atualiza_chamados(id_chamado):
    bd = conecta()
    cursor = bd.cursor()
    sql = 'update chamados set status = false, data_fechamento =  %s where id = %s'
    valor = (dt.datetime.now(),id_chamado,)

    cursor.execute(sql, valor)
    bd.commit()

    return 'Chamado concluído com Sucesso!!'     


