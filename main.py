import streamlit as st
import pandas as pd
import mysql.connector

#rodar com:  streamlit run "C:<path>\main.py"

#conexão com o banco
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", #inserir a senha!
    database="rede_social"
)

cursor = mydb.cursor()
print("conexão efetivada com sucesso")

def db_insert_prof(nome, email):
    sql = f"INSERT INTO Usuario (nome, email) VALUES ('{nome}', '{email}');"
    cursor.execute(sql)

    cursor.fetchall()

    sql = f"INSERT INTO Professor (id) VALUES (LAST_INSERT_ID());"
    cursor.execute(sql)

    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_aluno(nome, email, ano_escolar):
    sql = f"INSERT INTO Usuario (nome, email) VALUES ('{nome}', '{email}');"

    cursor.execute(sql)

    cursor.fetchall()

    sql = f"INSERT INTO Aluno (id, ano_escolar) VALUES ((SELECT LAST_INSERT_ID()), {ano_escolar});"
    cursor.execute(sql)

    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_select_prof(table):
    sql = f"SELECT Usuario.id, Usuario.email, Usuario.nome FROM USUARIO INNER JOIN {table} ON Usuario.id = {table}.id"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def db_select_aluno(table):
    sql = f"SELECT Usuario.id, Usuario.email, Usuario.nome, {table}.ano_escolar FROM USUARIO INNER JOIN {table} ON Usuario.id = {table}.id"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def db_select(table):
    sql = f"select * from {table}"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def main():
    
    st.title("CRUD operações bd da rede social")
    option = st.sidebar.selectbox('Selecione uma operação', ('Visualizar', 'Inserir', 'Alterar', 'Deletar', ))
    table = st.sidebar.selectbox('Selecione uma tabela', ('Professor', 'Aluno', 'Grupo', 'Escola', 'Disciplina', 'Olimpiada', 'Post', 'Comentarios', 'Grupo_Disciplina', 'Prof_Disciplina', 'Leciona', 'Assiste', 'Concorre', 'Olimpiada_Disciplina'))

    if option == "Visualizar":
        st.subheader("Visualizar dados de uma tabela")
        
        if table == 'Professor':
            result = db_select_prof(table)
        elif table == "Aluno":
            result = db_select_aluno(table)
        else:   
            result = db_select(table)

        st.write(f"Dados da Tabela {table}")
        for row in result:
            st.write(row)
        cursor = mydb.cursor()

    elif option == "Inserir":
        st.subheader("Inserir um dado a uma tabela")
        if table == "Professor":
            nome = st.text_input("Nome do Professor")
            email = st.text_input("Email do Professor")
            
            if st.button("Inserir"):
                db_insert_prof(nome, email)
        
        elif table == "Aluno":
            nome = st.text_input("Nome do Aluno")
            email = st.text_input("Email do Aluno")
            ano_escolar = st.number_input("Ano Escolar")

            if st.button("Inserir"):
                db_insert_aluno(nome, email, ano_escolar)


            

    elif option == "Alterar":
        st.subheader("Alterar dado em tabela")

    elif option == "Deletar":
        st.subheader("Deletar dado(linha) em tabela")



if __name__ == "__main__":
    main()

cursor.close()
mydb.close()