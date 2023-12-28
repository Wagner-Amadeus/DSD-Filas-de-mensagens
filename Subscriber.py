import pika

def callback(ch, method, properties, body):
    print(f" [x] Recebido: {body}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila_teste')

channel.basic_consume(queue='fila_teste',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')
channel.start_consuming()
