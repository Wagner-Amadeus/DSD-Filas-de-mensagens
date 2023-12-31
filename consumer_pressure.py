import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='fila_pressao')

def callback_pressao(ch, method, properties, body):
    pressao = body.decode('utf-8')
    print(f"Recebido dado de pressão: {pressao}")

channel.basic_consume(queue='fila_pressao', on_message_callback=callback_pressao, auto_ack=True)

print('Aguardando dados de pressão. Pressione CTRL+C para sair.')
channel.start_consuming()
