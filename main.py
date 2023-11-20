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

def db_insert_grupo(nome, descricao, fk_professor_id):
    sql_usuario = f"INSERT INTO Usuario (nome) VALUES ('{nome}');"
    cursor.execute(sql_usuario)
    cursor.execute("SELECT LAST_INSERT_ID();")
    usuario_id = cursor.fetchone()[0]
    sql_professor = f"INSERT INTO Professor (id, fk_usuario_id) VALUES (NULL, {usuario_id});"
    cursor.execute(sql_professor)
    cursor.execute("SELECT LAST_INSERT_ID();")
    professor_id = cursor.fetchone()[0]
    sql_grupo = f"INSERT INTO Grupo (nome, descricao, fk_professor_id) VALUES ('{nome}', '{descricao}', {professor_id});"
    cursor.execute(sql_grupo)
    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_escola(nome, tipo):
    sql_usuario = f"INSERT INTO Usuario (nome) VALUES ('{nome}');"
    cursor.execute(sql_usuario)
    cursor.execute("SELECT LAST_INSERT_ID();")
    usuario_id = cursor.fetchone()[0]
    sql_escola = f"INSERT INTO Escola (nome, tipo, fk_usuario_id) VALUES ('{nome}', '{tipo}', {usuario_id});"
    cursor.execute(sql_escola)
    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_disciplina(nome):
    sql_usuario = f"INSERT INTO Usuario (nome) VALUES ('{nome}');"
    cursor.execute(sql_usuario)
    cursor.execute("SELECT LAST_INSERT_ID();")
    usuario_id = cursor.fetchone()[0]
    sql_disciplina = f"INSERT INTO Disciplina (nome, fk_usuario_id) VALUES ('{nome}', {usuario_id});"
    cursor.execute(sql_disciplina)
    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_olimpiada(nome, estado, cidade, rua, numero, edicao):
    sql = f"INSERT INTO Olimpiada (nome, estado, cidade, rua, numero, edicao) VALUES ('{nome}', '{estado}', '{cidade}', '{rua}', '{numero}', {edicao});"
    cursor.execute(sql)
    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_post(conteudo, data_post, fk_usuario_id):
    sql_post = f"INSERT INTO Post (conteudo, data_post, fk_usuario_id) VALUES ('{conteudo}', '{data_post}', {fk_usuario_id});"
    cursor.execute(sql_post)
    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_comentario(conteudo, data_comentario, fk_comentarios_id, fk_post_id, fk_usuario_id):
    sql = f"INSERT INTO Comentarios (conteudo, data_comentario, fk_comentarios_id, fk_post_id, fk_usuario_id) VALUES ('{conteudo}', '{data_comentario}', {fk_comentarios_id}, {fk_post_id}, {fk_usuario_id});"
    cursor.execute(sql)
    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_grupo_disciplina(fk_grupo_id, fk_disciplina_id):
    sql = f"INSERT INTO grupo_disciplina (fk_grupo_id, fk_disciplina_id) VALUES ({fk_grupo_id}, {fk_disciplina_id});"
    cursor.execute(sql)
    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_prof_disciplina(fk_professor_id, fk_disciplina_id):
    sql = f"INSERT INTO Usuario (nome, email) VALUES ('{nome}', '{email}');"
    cursor.execute(sql)
    cursor.fetchall()
    sql = f"INSERT INTO Professor (id) VALUES (LAST_INSERT_ID());"
    cursor.execute(sql)
    sql = f"INSERT INTO prof_disciplina (fk_professor_id, fk_disciplina_id) VALUES ({fk_professor_id}, {fk_disciplina_id});"
    cursor.execute(sql)
    mydb.commit()
    st.success("Record Created Successfully!!!")


def db_insert_leciona(fk_professor_id, fk_escola_id):
    sql = f"INSERT INTO Usuario (nome, email) VALUES ('{nome}', '{email}');"
    cursor.execute(sql)
    cursor.fetchall()

    sql = f"INSERT INTO Professor (id) VALUES (LAST_INSERT_ID());"
    cursor.execute(sql)

    sql = f"INSERT INTO leciona (fk_professor_id, fk_escola_id) VALUES ({fk_professor_id}, {fk_escola_id});"
    cursor.execute(sql)

    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_assiste(fk_aluno_id, fk_professor_id, fk_escola_id):
    sql = f"INSERT INTO Usuario (nome, email) VALUES ('{nome}', '{email}');"
    cursor.execute(sql)
    cursor.fetchall()

    sql = f"INSERT INTO Aluno (id) VALUES (LAST_INSERT_ID());"
    cursor.execute(sql)

    sql = f"INSERT INTO assiste (fk_aluno_id, fk_professor_id, fk_escola_id) VALUES ({fk_aluno_id}, {fk_professor_id}, {fk_escola_id});"
    cursor.execute(sql)

    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_concorre(fk_aluno_id, fk_olimpiada_id):
    sql = f"INSERT INTO Usuario (nome, email) VALUES ('{nome}', '{email}');"
    cursor.execute(sql)
    cursor.fetchall()

    sql = f"INSERT INTO Aluno (id) VALUES (LAST_INSERT_ID());"
    cursor.execute(sql)

    sql = f"INSERT INTO concorre (fk_aluno_id, fk_olimpiada_id) VALUES ({fk_aluno_id}, {fk_olimpiada_id});"
    cursor.execute(sql)

    mydb.commit()
    st.success("Record Created Successfully!!!")

def db_insert_olimpiada_disciplina(fk_olimpiada_id, fk_disciplina_id):
    sql = f"INSERT INTO Olimpiada (id) VALUES (LAST_INSERT_ID());"
    cursor.execute(sql)

    sql = f"INSERT INTO olimpiada_disciplina (fk_olimpiada_id, fk_disciplina_id) VALUES ({fk_olimpiada_id}, {fk_disciplina_id});"
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

        # Exibindo a tabela no Streamlit
        st.table(result)

    elif option == "Inserir":
        st.subheader("Inserir um dado a uma tabela")
        if table == "Professor":
            nome = st.text_input("Nome do Professor")
            email = st.text_input("Email do Professor")
            
            if st.button("Inserir"):
                db_insert_prof(nome, email)
        
        elif table == "Aluno":
            st.subheader("Inserir um dado a uma tabela")
            nome = st.text_input("Nome do Aluno")
            email = st.text_input("Email do Aluno")
            ano_escolar = st.number_input("Ano Escolar")

            if st.button("Inserir"):
                db_insert_aluno(nome, email, ano_escolar)
                
        elif table == "Escola":
            st.subheader("Inserir um dado a uma tabela")
            nome = st.text_input("Nome da Escola")
            tipo = st.text_input("Tipo de Escola")
            
            if st.button("Inserir"):
                db_insert_escola(nome, tipo)

        elif table == "Disciplina":
            st.subheader("Inserir um dado a uma tabela")
            nome_disciplina = st.text_input("Nome da Disciplina")
            
            if st.button("Inserir"):
                db_insert_disciplina(nome_disciplina)

        elif table == "Olimpiada":
            nome_olimpiada = st.text_input("Nome da Olimpiada")
            estado = st.text_input("Estado")
            cidade = st.text_input("Cidade")
            rua = st.text_input("Rua")
            numero = st.text_input("Número")
            edicao = st.number_input("Edição")
            
            if st.button("Inserir"):
                db_insert_olimpiada(nome_olimpiada, estado, cidade, rua, numero, edicao)

        elif table == "Post":
            conteudo = st.text_area("Conteúdo do Post")
            data_post = st.date_input("Data do Post")
            # Assuming you have a user ID for the post, you can replace 'user_id' with the actual user ID
            fk_usuario_id = st.number_input("ID do Usuário (para vincular ao post)")

            if st.button("Inserir"):
                db_insert_post(conteudo, data_post, fk_usuario_id)
        
        elif table == "Comentarios":
            conteudo_comentario = st.text_area("Conteúdo do Comentário")
            data_comentario = st.date_input("Data do Comentário")
            fk_comentarios_id = st.number_input("ID do Comentário Pai (opcional)")
            fk_post_id = st.number_input("ID do Post (para vincular ao comentário)")
            fk_usuario_id_comentario = st.number_input("ID do Usuário (para vincular ao comentário)")

            if st.button("Inserir"):
                db_insert_comentario(conteudo_comentario, data_comentario, fk_comentarios_id, fk_post_id, fk_usuario_id_comentario)

        elif table == "grupo_disciplina":
            fk_grupo_id = st.number_input("ID do Grupo")
            fk_disciplina_id_grupo = st.number_input("ID da Disciplina")

            if st.button("Inserir"):
                db_insert_grupo_disciplina(fk_grupo_id, fk_disciplina_id_grupo)

        elif table == "prof_disciplina":
            fk_professor_id_disciplina = st.number_input("ID do Professor")
            fk_disciplina_id_professor = st.number_input("ID da Disciplina")

            if st.button("Inserir"):
                db_insert_prof_disciplina(fk_professor_id_disciplina, fk_disciplina_id_professor)

        elif table == "leciona":
            fk_professor_id_leciona = st.number_input("ID do Professor")
            fk_escola_id_leciona = st.number_input("ID da Escola")

            if st.button("Inserir"):
                db_insert_leciona(fk_professor_id_leciona, fk_escola_id_leciona)

        elif table == "assiste":
            fk_aluno_id_assiste = st.number_input("ID do Aluno")
            fk_professor_id_assiste = st.number_input("ID do Professor")
            fk_escola_id_assiste = st.number_input("ID da Escola")

            if st.button("Inserir"):
                db_insert_assiste(fk_aluno_id_assiste, fk_professor_id_assiste, fk_escola_id_assiste)

        elif table == "concorre":
            fk_aluno_id_concorre = st.number_input("ID do Aluno")
            fk_olimpiada_id_concorre = st.number_input("ID da Olimpiada")

            if st.button("Inserir"):
                db_insert_concorre(fk_aluno_id_concorre, fk_olimpiada_id_concorre)

        elif table == "olimpiada_disciplina":
            fk_olimpiada_id_olimpiada_disciplina = st.number_input("ID da Olimpiada")
            fk_disciplina_id_olimpiada_disciplina = st.number_input("ID da Disciplina")

            if st.button("Inserir"):
                db_insert_olimpiada_disciplina(fk_olimpiada_id_olimpiada_disciplina, fk_disciplina_id_olimpiada_disciplina)



    elif option == "Alterar":
        st.subheader("Alterar dado em tabela")
        if table == "Professor":
            id = st.number_input("Id do professor", min_value= 1)
            nome = st.text_input("nome do professor")
            email = st.text_input("email do professor")
            if st.button("Alterar"):
                slq = f"UPDATE Usuario SET Usuario.nome = '{nome}', Usuario.email = '{email}' WHERE Usuario.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Aluno":
            id = st.number_input("Id do Aluno", min_value= 1)
            nome = st.text_input("nome do Aluno")
            email = st.text_input("email do Aluno")
            ano_escolar = st.number_input("Ano escolar do Aluno", min_value= 1)
            if st.button("Alterar"):
                slq = f"UPDATE Usuario SET Usuario.nome = '{nome}', Usuario.email = '{email}' WHERE Usuario.id = {int(id)};"
                cursor.execute(sql)

                cursor.fetchall()

                slq = f"UPDATE Aluno SET Aluno.ano_escolar = {int(ano_escolar)} WHERE Aluno.id = {int(id)};"
                cursor.execute(sql)

                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == 'Grupo':
            id = st.number_input("Id do Grupo", min_value =1)
            nome = st.text_input("nome do Usuário")
            descricao = st.text_input("Descrição do grupo")
            fk_professor_id = st.number_input("Id do Professor Responsável", min_value =1)
            if st.button("Alterar"):
                sql = f"UPDATE Grupo SET Grupo.nome = '{nome}', Grupo.descricao = '{descricao}', Grupo.fk_professor_id = {int(fk_professor_id)} WHERE Grupo.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

####sss

        elif table == "Escola":
            id = st.number_input("Id da Escola", min_value=1)
            nome = st.text_input("nome da Escola")
            tipo = st.text_input("tipo da Escola")
            if st.button("Alterar"):
                sql = f"UPDATE Escola SET Escola.nome = '{nome}', Escola.tipo = '{tipo}' WHERE Escola.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Disciplina":
            id = st.number_input("Id da Disciplina", min_value=1)
            nome = st.text_input("nome da Disciplina")
            if st.button("Alterar"): 
                sql = f"UPDATE Disciplina SET Disciplina.nome = '{nome}' WHERE Disciplina.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Olimpiada":
            id = st.number_input("Id da Olimpíada", min_value=1)
            nome = st.text_input("nome da Olimpíada")
            estado = st.text_input("estado da Olimpíada")
            cidade = st.text_input("cidade da Olimpíada")
            rua = st.text_input("rua da Olimpíada")
            numero = st.text_input("número da Olimpíada")
            edição = st.number_input("edição da Olimpíada")
            if st.button("Alterar"):
                sql = f"UPDATE Olimpiada SET Olimpiada.nome = '{nome}', Olimpiada.estado = '{estado}', Olimpiada.cidade = '{cidade}', Olimpiada.rua = '{rua}', Olimpiada.numero = '{numero}', Olimpiada.edicao = {int(edição)} WHERE Olimpiada.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Post":
            id = st.number_input("Id do Post", min_value=1)
            conteúdo = st.text_input("conteúdo do Post")
            data_post = st.date_input("data de publicação do Post")
            if st.button("Alterar"):
                sql = f"UPDATE Post SET Post.conteúdo = '{conteúdo}', Post.data_post = '{data_post}' WHERE Post.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Comentários":
            id = st.number_input("Id do Comentário", min_value=1)
            conteúdo = st.text_input("conteúdo do Comentário")
            data_comentario = st.date_input("data do Comentário")
            if st.button("Alterar"):
                sql = f"UPDATE Comentários SET Comentários.conteúdo = '{conteúdo}', Comentários.data_comentario = '{data_comentario}' WHERE Comentários.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")


        elif table == "Participa":
            id_user = st.number_input("Antigo Id do usuário", min_value=1)
            id_group = st.number_input("Antigo Id do grupo", min_value=1)
            id_user_new = st.number_input("Novo Id do usuário", min_value=1)
            id_group_new = st.number_input("Novo Id do grupo", min_value=1)
            if st.button("Alterar"):
                sql = f"UPDATE Participa SET Participa.fk_usuario_id = {int(id_user_new)}, Participa.fk_grupo_id = {int(id_group_new)} WHERE Participa.fk_usuario_id = {int(id_user)} AND Participa.fk_grupo_id = {int(id_group)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Grupo_Disciplina":
            fk_grupo_id = st.number_input("Antigo Id do Grupo", min_value=1)
            fk_disciplina_id = st.number_input("Antigo Id da Disciplina", min_value=1)
            fk_grupo_id_new = st.number_input("Novo Id do Grupo", min_value=1)
            fk_disciplina_id_new = st.number_input("Novo Id da Disciplina", min_value=1)
            if st.button("Alterar"):
                sql = f"UPDATE Grupo_Disciplina SET Grupo_Disciplina.fk_grupo_id = {int(fk_grupo_id_new)}, Grupo_Disciplina.fk_disciplina_id = {int(fk_disciplina_id_new)} WHERE Grupo_Disciplina.fk_grupo_id = {int(fk_grupo_id)} AND Grupo_Disciplina.fk_disciplina_id = {int(fk_disciplina_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")
## ate aqui ta tudo ok

        elif table == "Prof_Disciplina":
            fk_professor_id = st.number_input("Antigo Id do Professor", min_value=1)
            fk_disciplina_id = st.number_input("Antigo Id da Disciplina", min_value=1)
            new_fk_professor_id = st.number_input("Novo Id do Professor", min_value=1)
            new_fk_disciplina_id = st.number_input("Novo Id da Disciplina", min_value=1)
            if st.button("Alterar"):
                sql = f"UPDATE Prof_Disciplina SET Prof_Disciplina.fk_professor_id = {int(new_fk_professor_id)}, Prof_Disciplina.fk_disciplina_id = {int(new_fk_disciplina_id)} WHERE Prof_Disciplina.fk_professor_id = {int(fk_professor_id)} AND Prof_Disciplina.fk_disciplina_id = {int(fk_disciplina_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Leciona":
            fk_professor_id = st.number_input("Antigo Id do Professor", min_value=1)
            fk_escola_id = st.number_input("Antigo Id da Escola", min_value=1)
            new_fk_professor_id = st.number_input("Novo Id do Professor", min_value=1)
            new_fk_escola_id = st.number_input("Novo Id da Escola", min_value=1)
            if st.button("Alterar"):
                sql = f"UPDATE Leciona SET Leciona.fk_professor_id = {int(new_fk_professor_id)}, Leciona.fk_escola_id = {int(new_fk_escola_id)} WHERE Leciona.fk_professor_id = {int(fk_professor_id)} AND Leciona.fk_escola_id = {int(fk_escola_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Assiste":
            fk_aluno_id = st.number_input("Antigo Id do Aluno", min_value=1)
            fk_professor_id = st.number_input("Antigo Id do Professor", min_value=1)
            fk_escola_id = st.number_input("Antiga Id da Escola", min_value=1)
            fk_aluno_id_new = st.number_input("Novo Id do Aluno", min_value=1)
            fk_professor_id_new = st.number_input("Novo Id do Professor", min_value=1)
            fk_escola_id_new = st.number_input("Nova Id da Escola", min_value=1)
            if st.button("Alterar"):
                sql = f"UPDATE Assiste SET Assiste.fk_aluno_id = {int(fk_aluno_id_new)}, Assiste.fk_professor_id = {int(fk_professor_id_new)}, Assiste.fk_escola_id = {int(fk_escola_id_new)} WHERE Assiste.id = {int(id)} AND Assiste.fk_aluno_id = {int(fk_aluno_id)} AND Assiste.fk_professor_id = {int(fk_professor_id)} AND Assiste.fk_escola_id = {int(fk_escola_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Concorre":
            fk_aluno_id = st.number_input("Antigo Id do Aluno", min_value=1)
            fk_olimpiada_id = st.number_input("Antiga Id da Olimpíada", min_value=1)
            fk_aluno_id_new = st.number_input("Novo Id do Aluno", min_value=1)
            fk_olimpiada_id_new = st.number_input("Nova Id da Olimpíada", min_value=1)
            if st.button("Alterar"):   
                sql = f"UPDATE Concorre SET Concorre.fk_aluno_id = {int(fk_aluno_id_new)}, Concorre.fk_olimpiada_id = {int(fk_olimpiada_id_new)} WHERE Concorre.id = {int(id)} AND Concorre.fk_aluno_id = {int(fk_aluno_id)} AND Concorre.fk_olimpiada_id = {int(fk_olimpiada_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif table == "Olimpiada_Disciplina":
            fk_olimpiada_id = st.number_input("Antigo Id da Olimpíada", min_value=1)
            fk_disciplina_id = st.number_input("Antiga Id da Disciplina", min_value=1)
            fk_olimpiada_id_new = st.number_input("Novo Id da Olimpíada", min_value=1)
            fk_disciplina_id_new = st.number_input("Nova Id da Disciplina", min_value=1)
            if st.button("Alterar"):
                sql = f"UPDATE Olimpiada_Disciplina SET Olimpiada_Disciplina.fk_olimpiada_id = {int(fk_olimpiada_id_new)}, Olimpiada_Disciplina.fk_disciplina_id = {int(fk_disciplina_id_new)} WHERE Olimpiada_Disciplina.id = {int(id)} AND Olimpiada_Disciplina.fk_olimpiada_id = {int(fk_olimpiada_id)} AND Olimpiada_Disciplina.fk_disciplina_id = {int(fk_disciplina_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Updated Successfully!!!")



    elif option == "Deletar":
        st.subheader("Deletar dado(linha) em tabela")

        if table == "Professor":
            id = st.number_input("Id do Professor", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM Professor WHERE Professor.id = {int(id)};"
                cursor.execute(sql)

                cursor.fetchall()

                sql = f"DELETE FROM Usuario WHERE Usuario.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

        elif table == "Aluno":
            id = st.number_input("Id do Aluno", min_value= 1)
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
            id = st.number_input("Id do Grupo", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM Grupo WHERE Grupo.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

        elif table == "Disciplina":
            id = st.number_input("Id da Disciplina", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM Disciplina WHERE Disciplina.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")      

        elif table == "Escola":
            id = st.number_input("Id da Escola", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM Escola WHERE Escola.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Olimpiada":
            id = st.number_input("Id da Olimpiada", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM Olimpiada WHERE Olimpiada.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Post":
            id = st.number_input("Id da Post", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM Post WHERE Post.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Comentarios":
            id = st.number_input("Id do comentario", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM Comentarios WHERE Comentarios.id = {int(id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Participa":
            fk_usuario_id = st.number_input("Id do usuário", min_value= 1)
            fk_grupo_id = st.number_input("Id do grupo")
            if st.button("Deletar"):
                sql = f"DELETE FROM Participa WHERE fk_usuario_id = {int(fk_usuario_id)} AND fk_grupo_id = {int(fk_grupo_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")  

        elif table == "Grupo_Disciplina":
            fk_grupo_id = st.number_input("Id do grupo", min_value= 1)
            id_subject = st.number_input("Id da disciplina", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM grupo_disciplina WHERE fk_disciplina_id = {int(id_subject)} AND fk_grupo_id = {int(fk_grupo_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!") 

        elif table == "Prof_Disciplina":
            fk_usuario_id = st.number_input("Id do professor", min_value= 1)
            id_subject = st.number_input("Id da disciplina", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM Prof_Disciplina WHERE fk_disciplina_id = {int(id_subject)} AND fk_professor_id = {int(fk_usuario_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!") 

######
    
        elif table == "Leciona":
            fk_professor_id = st.number_input("Id do professor", min_value= 1)
            fk_escola_id = st.number_input("Id da escola", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM leciona WHERE fk_professor_id = {int(fk_professor_id)} AND fk_escola_id = {int(fk_escola_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

    
        elif table == "Assiste":
            fk_aluno_id = st.number_input("Id do aluno", min_value= 1)
            fk_professor_id = st.number_input("Id do professor", min_value= 1)
            fk_escola_id = st.number_input("Id da escola", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM assiste WHERE fk_aluno_id = {int(fk_aluno_id)} AND fk_professor_id = {int(fk_professor_id)} AND fk_escola_id = {int(fk_escola_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

    
        elif table == "Concorre":
            fk_aluno_id = st.number_input("Id do aluno", min_value= 1)
            fk_olimpiada_id = st.number_input("Id da olimpíada", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM concorre WHERE fk_aluno_id = {int(fk_aluno_id)} AND fk_olimpiada_id = {int(fk_olimpiada_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")


        elif table == "Olimpiada_Disciplina":
            fk_olimpiada_id = st.number_input("Id da olimpíada", min_value= 1)
            fk_disciplina_id = st.number_input("Id da disciplina", min_value= 1)
            if st.button("Deletar"):
                sql = f"DELETE FROM olimpiada_disciplina WHERE fk_olimpiada_id = {int(fk_olimpiada_id)} AND fk_disciplina_id = {int(fk_disciplina_id)};"
                cursor.execute(sql)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")


if __name__ == "__main__":
    main()

cursor.close()
mydb.close()
