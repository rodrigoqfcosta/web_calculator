from app import app
from flask import render_template
from model.tabela import Log


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
    
    msg3 = ['''Desenvolver um sistema simples que se comporte como uma calculadora orientada a serviços.''',
            '''A calculadora deve ser provida, pelo menos de 3 operações, divididas em duas categorias:''',
            '''1. Operações Elementares (e.g.: soma, subtração);''',
            '''2. Operações envolvendo funções transcendentes (e.g.: seno, cosseno, tangente, exponencial, tangente hiperbólica) ''',
	        '''ou computação composta de uma fórmula que faça uso de uma operação elementar (e.g.: x3 + x2). ''',
            '''''',
            '''Essa operação deverá ser única para cada trabalho e especificada no canal “Tema trabalho prático”.''',
            '''''',
            '''Para cada operação realizada, um log é criado informando qual operação foi realizada, em qual horário. ''',
            '''Esse log é armazenado em um banco de dados que deve conter:''',
            '''	- Data da operação;''',
            '''	- Tipo de operação;''',
            '''	- Operação específica;''',
            '''	- Argumentos utilizados;''',
            '''''',
            '''A calculadora deve ser estruturada utilizando orientação a serviços (service oriented architecture - SOA). ''',
            '''Mais especificamente, por serem serviços simples, são chamados de microsserviços.''',
            '''1. As operações elementares devem ser implementadas por um serviço independente de qualquer outro serviço.''',
            '''2. As operações transcendentes ou de fórmulas, devem ser implementadas de modo''',
            '''independente (e.g: seno) ou consumindo o serviço das funções elementares ''',
	        '''(e.g: x3 + x2 calcula isoladamente o cubo, o quadrado e, depois, consome o serviço de cálculo de soma).''',
            '''3. O log deve ser implementado em um serviço totalmente independente.''',
            '''4. O log não deve possuir persistência em tabela única. Deve haver, no mínimo uma''',
            '''associação à uma tabela que classifica a operação como “elementar” ou “transcendente”.''',
            '''''',
            '''O sistema para a internet deve possuir ao menos 2 interfaces totalmente distintas:''',
            '''	1. Interface para execução das operações.''',
            '''	2. Interface para exibição do log de operações, podendo filtrar os logs, para exibição, por data e por tipo de operação.''']

    return render_template('index.html', titulo='Hello, World!', 
                            sub_titulo='REQUISITOS E RESTRIÇÕES GERAIS - TECNOLOGIA PYTHON:', mensagem=msg, 
                            sub_titulo2='REQUISITOS E RESTRIÇÕES COMUNS:', mensagem2=msg2,
                            sub_titulo3='CALCULADORA ORIENTADA A SERVIÇOS:', mensagem3=msg3)


@app.route('/calculadora')
def calculadora():
        return render_template('calculadora.html')


@app.route('/log')
def log():
    """ lista=[]
    calculos = Log.query.all()
    for linha in calculos:
        lista.append(f'Data e hora: {linha.data_oper} - Tipo da operação: {linha.tipo_oper} - Operação: {linha.operacao} - Argumento utilizado: {linha.args}') """
    return render_template('log.html')
