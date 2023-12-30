import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='fila_temperatura')

def callback(ch, method, properties, body):
    temperatura = body.decode('utf-8')
    print(f"Recebido dado de temperatura: {temperatura}")

channel.basic_consume(queue='fila_temperatura', on_message_callback=callback, auto_ack=True)

print('Aguardando dados de temperatura. Pressione CTRL+C para sair.')
channel.start_consuming()
