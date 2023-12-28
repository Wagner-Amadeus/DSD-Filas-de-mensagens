import pika

def callback(ch, method, properties, body):
    print(f" [x] Recebido: {body.decode('utf-8')}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_key = input("Digite o seu nome de usuário para receber mensagens (ou 'all' para todas): ")

if binding_key.lower() == 'all':
    binding_key = '#'
else:
    binding_key = f"mensagens.{binding_key}"

channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(f' [*] Aguardando mensagens para {binding_key if binding_key != "#" else "todos"}. Para sair, pressione CTRL+C')
channel.start_consuming()
