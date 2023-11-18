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

def main():
    st.title("CRUD operações bd da rede social")
    option = st.sidebar.selectbox('Selecione uma operação', ('Visualizar', 'Inserir', 'Alterar', 'Deletar', ))
    table = st.sidebar.selectbox('Selecione uma tabela', ('Professor', 'Aluno', 'Grupo', 'Escola', 'Disciplina', 'Olimpiada', 'Post', 'Comentarios', 'Grupo_Disciplina', 'Prof_Disciplina', 'Leciona', 'Assiste', 'Concorre', 'Olimpiada_Disciplina'))

    if option == "Visualizar":
        st.subheader("Visualizar dados de uma tabela")
        
        sql = f"select * from {table}"
        cursor.execute(sql)
        result = cursor.fetchall()

        st.write(f"Dados da Tabela {table}")
        for row in result:
            st.write(row)

    elif option == "Inserir":
        st.subheader("Inserir um dado a uma tabela")
        st.text_input("Insira um nome")
        st.text_input("Insira o email")

    elif option == "Alterar":
        st.subheader("Alterar dado em tabela")

    elif option == "Deletar":
        st.subheader("Deletar dado(linha) em tabela")



if __name__ == "__main__":
    main()

cursor.close()
mydb.close()