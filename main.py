import streamlit as st
import pandas as pd
import mysql.connector

#rodar com:  streamlit run "C:<path>\main.py"

#conexão com o banco
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", #inserir a senha!
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
    table = st.sidebar.selectbox('Selecione uma tabela', ('Professor', 'Aluno', 'Grupo', 'Escola', 'Disciplina', 'Olimpiada', 'Post', 'Comentarios', 'Participa', 'Grupo_Disciplina', 'Prof_Disciplina', 'Leciona', 'Assiste', 'Concorre', 'Olimpiada_Disciplina'))

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
        # cursor = mydb.cursor()

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

        if table == "Professor":
            id = st.number_input("Id do Professor")
            if st.button("Deletar"):
                sql = f"DELETE FROM Professor WHERE Professor.id = {int(id)};"
                cursor.execute(sql)

                cursor.fetchall()

                sql = f"DELETE FROM Usuario WHERE Usuario.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

        elif table == "Aluno":
            id = st.number_input("Id do Aluno")
            if st.button("Deletar"):
                # sql = f"DELETE FROM Usuario INNER JOIN Aluno ON Usuario.id = Aluno.id WHERE Aluno.id = {int(id)};"

                sql = f"DELETE FROM Aluno WHERE Aluno.id = {int(id)};"
                cursor.execute(sql)

                cursor.fetchall()

                sql = f"DELETE FROM Usuario WHERE Usuario.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

        elif table == "Grupo":
            id = st.number_input("Id do Grupo")
            if st.button("Deletar"):
                sql = f"DELETE FROM Grupo WHERE Grupo.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

        elif table == "Disciplina":
            id = st.number_input("Id da Disciplina")
            if st.button("Deletar"):
                sql = f"DELETE FROM Disciplina WHERE Disciplina.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")      

        elif table == "Escola":
            id = st.number_input("Id da Escola")
            if st.button("Deletar"):
                sql = f"DELETE FROM Escola WHERE Escola.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Olimpiada":
            id = st.number_input("Id da Olimpiada")
            if st.button("Deletar"):
                sql = f"DELETE FROM Olimpiada WHERE Olimpiada.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Post":
            id = st.number_input("Id da Post")
            if st.button("Deletar"):
                sql = f"DELETE FROM Post WHERE Post.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Comentarios":
            id = st.number_input("Id do comentario")
            if st.button("Deletar"):
                sql = f"DELETE FROM Comentarios WHERE Comentarios.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Participa":
            id_user = st.number_input("Id do usuário")
            id_group = st.number_input("Id do grupo")
            if st.button("Deletar"):
                sql = f"DELETE FROM Participa WHERE fk_usuario_id = {int(id_user)} AND fk_grupo_id = {int(id_group)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Grupo_Disciplina":
            id_group = st.number_input("Id do grupo")
            id_subject = st.number_input("Id da disciplina")
            if st.button("Deletar"):
                sql = f"DELETE FROM grupo_disciplina WHERE fk_disciplina_id = {int(id_subject)} AND fk_grupo_id = {int(id_group)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!") 

        elif table == "Prof_Disciplina":
            id_user = st.number_input("Id do professor")
            id_subject = st.number_input("Id da disciplina")
            if st.button("Deletar"):
                sql = f"DELETE FROM Prof_Disciplina WHERE fk_disciplina_id = {int(id_subject)} AND fk_professor_id = {int(id_user)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!") 

######
    
        elif table == "Leciona":
            fk_professor_id = st.number_input("Id do professor")
            fk_escola_id = st.number_input("Id da escola")
            if st.button("Deletar"):
                sql = f"DELETE FROM leciona WHERE fk_professor_id = {int(fk_professor_id)} AND fk_escola_id = {int(fk_escola_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

    
        elif table == "Assiste":
            fk_aluno_id = st.number_input("Id do aluno")
            fk_professor_id = st.number_input("Id do professor")
            fk_escola_id = st.number_input("Id da escola")
            if st.button("Deletar"):
                sql = f"DELETE FROM assiste WHERE fk_aluno_id = {int(fk_aluno_id)} AND fk_professor_id = {int(fk_professor_id)} AND fk_escola_id = {int(fk_escola_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

    
        elif table == "Concorre":
            fk_aluno_id = st.number_input("Id do aluno")
            fk_olimpiada_id = st.number_input("Id da olimpíada")
            if st.button("Deletar"):
                sql = f"DELETE FROM concorre WHERE fk_aluno_id = {int(fk_aluno_id)} AND fk_olimpiada_id = {int(fk_olimpiada_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")


        elif table == "Olimpiada_Disciplina":
            fk_olimpiada_id = st.number_input("Id da olimpíada")
            fk_disciplina_id = st.number_input("Id da disciplina")
            if st.button("Deletar"):
                sql = f"DELETE FROM olimpiada_disciplina WHERE fk_olimpiada_id = {int(fk_olimpiada_id)} AND fk_disciplina_id = {int(fk_disciplina_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")


if __name__ == "__main__":
    main()

cursor.close()
mydb.close()