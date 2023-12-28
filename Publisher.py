import pika

def publish_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila_teste')

    while True:
        mensagem = input("Digite a mensagem que deseja enviar (ou 'sair' para sair): ")
        
        if mensagem.lower() == 'sair':
            break  # Sai do loop se 'sair' for digitado
        
        channel.basic_publish(exchange='',
                              routing_key='fila_teste',
                              body=mensagem)
        
        print(f" [x] Mensagem enviada: {mensagem}")

    connection.close()

if __name__ == '__main__':
    publish_messages()
