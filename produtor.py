from flask import Flask, render_template, request
import pika

app = Flask(__name__)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='fila_temperatura')
channel.queue_declare(queue='fila_pressao')
channel.queue_declare(queue='fila_geral')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    temperatura = request.form['temperatura']
    pressao = request.form['pressao']

    if temperatura:
        channel.basic_publish(exchange='', routing_key='fila_temperatura', body=temperatura)
    if pressao:
        channel.basic_publish(exchange='', routing_key='fila_pressao', body=pressao)
    
    if temperatura and pressao:
        dados_gerais = f"{temperatura} /t {pressao}"
        channel.basic_publish(exchange='', routing_key='fila_geral', body=dados_gerais)

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
