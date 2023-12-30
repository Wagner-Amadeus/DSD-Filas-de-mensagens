import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='fila_geral')

def callback_geral(ch, method, properties, body):
    dados = body.decode('utf-8')
    temperatura, pressao = dados.split('/t')
    print(f"Temperatura: {temperatura.strip()} Pressão: {pressao.strip()}")

channel.basic_consume(queue='fila_geral', on_message_callback=callback_geral, auto_ack=True)

print('Aguardando dados. Pressione CTRL+C para sair.')
channel.start_consuming()
