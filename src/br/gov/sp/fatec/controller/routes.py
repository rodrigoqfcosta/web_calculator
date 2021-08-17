from app import app
from flask import render_template
from model.tabela import Historico


@app.route('/')
def index():
    msg = [ '1. Utilizar linguagem de programação Python (versão 3.6 ou superior) no back end;',
            '2. Utilizar SQLAlchemy (1.2.19 ou superior) para persistência de dados;',
            '3. Utilizar Jinja 2 ou similar para geração de páginas dinâmicas (tipo template);',
            '4. Utilizar o microframework Flask para implantação do sistema web;',
            '5. Utilizar o Gunicorn ou Waitress como servidor de implantação, em conjunto com o Flask;',
            '6. Utilizar o Virtualenv para isolamento de ambiente de desenvolvimento e obtenção de pacotes;',
            '7. Estruturar o sistema seguindo a arquitetura MVC;',
            '8. Sistema Gerenciador de Banco de Dados MariaDB.']
    
    msg2 = ['''1. Exemplificar a utilização de três recursos da linguagem de programação JavaScript, 
            desenvolvendo código-fonte sem fazer uso de bibliotecas ou frameworks de terceiros.
            Além dessas três funcionalidades, utilizar Ajax em alguma funcionalidade do sistema.''',
            '''2. Exemplificar a construção de três regras CSS, sem fazer uso de frameworks ou
            bibliotecas e desconsiderando tamanho e cor de fonte ou cor de plano de fundo. Criar
            mandatoriamente uma regra que controle layout de página ou posicionamento de
            elementos.''',
            '''3. Exemplificar o funcionamento do sistema de integração contínua para pelo menos um
            dos serviços desenvolvidos para o trabalho. Utilizar um sistema de sua escolha (ex.
            GitLab, Jenkins, Trevis CI/CD, etc.).''',
            '''4. Sua aplicação web deve conter um menu para navegação e, no mínimo, duas interfaces
            distintas com o usuário, acessíveis a partir do menu.''']

    return render_template('index.html', hello='Hello, World!', sub_titulo='REQUISITOS E RESTRIÇÕES GERAIS, TECNOLOGIA PYTHON:', 
                            mensagem=msg, sub_titulo2='REQUISITOS E RESTRIÇÕES COMUNS:', mensagem2=msg2)


@app.route('/historico')
def historico():
    lista=[]
    calculos = Historico.query.all()
    for linha in calculos:
        lista.append(linha.calculo)
    return render_template('history.html', list=lista)
