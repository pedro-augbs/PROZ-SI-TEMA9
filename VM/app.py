from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para armazenar os registros de comandos e saídas
command_log = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global command_log
    if request.method == 'POST':
        command = request.form['command']
        if command.lower() == 'stop':
            command_log = []  # Limpa o log de comandos
            return render_template('index.html', command_log=command_log)
        output = execute_command_on_cloud(command)
        # Adiciona o comando e a saída ao registro
        command_log.append({'command': command, 'output': output})
    return render_template('index.html', command_log=command_log)

def execute_command_on_cloud(command):
    # Simulando a execução de comandos fictícios relacionados a serviços de nuvem
    if command == 'vm':
        output = 'Máquina virtual iniciada'
    elif command == 'sgbd':
        output = 'Banco de dados disponível'
    elif command == 'nodejs':
        output = 'Plataforma Node.js iniciada'
    elif command == 'ftp':
        output = 'Serviço de transferências de arquivos habilitado'
    else:
        output = f"Comando '{command}' não reconhecido."
    
    # Imprime o output na tela de saída
    print(output)
    
    return output

if __name__ == '__main__':
    app.run(debug=True)
