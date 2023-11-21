# Instalação do App

Este README fornece instruções sobre como instalar e executar a aplicação Streamlit, além de orientações para configurar o banco de dados MySQL.

## Pré-requisitos

Antes de começar, certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina. Recomendamos o uso do Python 3.7 ou superior.


## Configuração do Banco de Dados

Certifique-se de ter o MySQL Server instalado e em execução em sua máquina. Se ainda não configurou o localhost, recomendamos assistir ao [vídeo tutorial](https://youtu.be/shGezjnGpkU?feature=shared).

1. **Clone o Repositório:**

   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/arthursuzuki/db_project/)
   ```

2. **Navegue até o Diretório do Projeto:**

   ```bash
   cd seu-repositorio
   ```

3. **Acesse o MySQL:**

   - No Windows, abra o prompt de comando do MySQL:

     ```bash
     mysql -u seu-usuario -p
     ```

   - No Linux/Mac, use o seguinte comando:

     ```bash
     mysql -u seu-usuario -p
     ```

   Insira a senha quando solicitado.

4. **Crie o Banco de Dados:**

   ```sql
   CREATE DATABASE nome_do_banco;
   ```

   Substitua `nome_do_banco` pelo nome desejado para o banco de dados.

5. **Selecione o Banco de Dados Criado:**

   ```sql
   USE nome_do_banco;
   ```

6. **Execute o Script SQL:**

   ```sql
   source caminho_completo_para_o_arquivo/rede_social.sql;
   ```

   Certifique-se de substituir `caminho_completo_para_o_arquivo` pelo caminho real onde o arquivo **rede_social.sql** está localizado.

7. **Verifique a Execução Bem-sucedida:**

   Após a execução do script, verifique se as tabelas foram criadas com sucesso. Você pode usar comandos SQL como `SHOW TABLES;` para listar as tabelas no banco de dados.

## Instalação do App

1. **Clone este Repositório:**

   ```bash
   git clone [https://github.com/seu-usuario/NomeDaSuaApp.git](https://github.com/arthursuzuki/db_project/)
   ```

2. **Navegue até o Diretório do Projeto:**

   ```bash
   cd NomeDaSuaApp
   ```

3. **Crie um Ambiente Virtual:**

   ```bash
   python -m venv venv
   ```

4. **Ative o Ambiente Virtual:**

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No Linux/Mac:

     ```bash
     source venv/bin/activate
     
     ```
5. **Streamlit e MySQL Connector:**

Instale as dependências necessárias usando o pip:

```bash
pip install streamlit mysql-connector-python
```


## Executando a Aplicação

Depois de concluir a instalação, você pode iniciar a aplicação Streamlit. Certifique-se de estar no diretório do projeto e com o ambiente virtual ativado.

```bash
streamlit run app.py
```

Isso iniciará o servidor Streamlit e abrirá automaticamente a aplicação no seu navegador padrão. Caso contrário, você pode acessar a aplicação no navegador digitando o seguinte endereço na barra de URL:

```
http://localhost:8501
```

## Encerrando a Aplicação

Para encerrar a aplicação, vá para a janela do terminal onde o Streamlit está sendo executado e pressione `Ctrl+C`.
