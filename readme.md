# Instalação do App

Este README fornece instruções sobre como instalar e executar a aplicação Streamlit.

## Pré-requisitos

Antes de começar, certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina. Recomendamos o uso do Python 3.7 ou superior.

## Instalação

1. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/NomeDaSuaApp.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd NomeDaSuaApp
   ```

3. Crie um ambiente virtual para isolar as dependências do projeto:

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No Linux/Mac:

     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
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

## Personalizando a Aplicação

Sinta-se à vontade para personalizar a aplicação de acordo com suas necessidades. O arquivo `app.py` contém o código principal da aplicação, e você pode modificar o layout, os gráficos e outros elementos conforme desejado.

---

Esperamos que essas instruções sejam úteis para instalar e executar a sua aplicação Streamlit. Se você encontrar problemas ou tiver dúvidas, consulte a [documentação oficial do Streamlit](https://docs.streamlit.io/) para obter mais informações.
