from flask import Flask, render_template
from flask.templating import render_template_string

app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('home.html')


@app.route('/atualizacao')
def atualizacao():
  return render_template('atualizacao.html')


@app.route('/consulta')
def consulta():
  return render_template('consulta.html')


@app.route('/demo')
def demo():
  return render_template('demo.html')


@app.route('/documentacao')
def documentacao():
  return render_template('documentacao.html')


@app.route('/erros')
def erros():
  return render_template('erros.html')


@app.route('/exclusao')
def exclusao():
  return render_template('exclusao.html')


@app.route('/incersao')
def incersao():
  return render_template('incersao.html')


@app.route('/relatorios')
def relatorios():
  return render_template('relatorios.html')


@app.route('/testes')
def testes():
  return render_template('testes.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
