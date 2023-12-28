import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila_teste')

channel.basic_publish(exchange='',
                      routing_key='fila_teste',
                      body='Mensagem de exemplo')
print(" [x] Mensagem enviada")

connection.close()
