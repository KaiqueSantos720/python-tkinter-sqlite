import sqlite3
from sqlite3 import Error


def conexao_banco():
    return sqlite3.connect('C:\\Users\\Windows 10 Pro\\PycharmProjects\\pythonProject1\\Python\\times.db')


def query(sql):  # dml
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()  # atualizar a base de dados com as devidas atualizações
        print('\nOperação Realizada com Sucesso')
    except Error as er:
        print(er)


def consulta(sql):  # dql
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute(sql)
    return cursor.fetchall()  # retorna o resultado da consulta


conexao_banco().close()
