import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='fila_temperatura')
channel.queue_declare(queue='fila_pressao')

def callback_temperatura(ch, method, properties, body):
    temperatura = body.decode('utf-8')
    print(f"Recebido dado de temperatura: {temperatura}")

def callback_pressao(ch, method, properties, body):
    pressao = body.decode('utf-8')
    print(f"Recebido dado de pressão: {pressao}")

def callback_geral(ch, method, properties, body):
    dados = body.decode('utf-8')
    temperatura, pressao = dados.split('/t')
    print(f"Temperatura: {temperatura.strip()}\tPressão: {pressao.strip()}")

channel.basic_consume(queue='fila_temperatura', on_message_callback=callback_temperatura, auto_ack=True)
channel.basic_consume(queue='fila_pressao', on_message_callback=callback_pressao, auto_ack=True)
channel.basic_consume(queue='fila_geral', on_message_callback=callback_geral, auto_ack=True)

print('Aguardando dados. Pressione CTRL+C para sair.')
channel.start_consuming()
