from flask import Flask, request
import pika

app = Flask(__name__)

@app.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    mensagem = request.get_json().get('mensagem')

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='fila_teste')
    channel.basic_publish(exchange='',
                          routing_key='fila_teste',
                          body=mensagem)

    connection.close()

    return "Mensagem enviada com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
