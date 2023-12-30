import pika

def publish_message(message, recipient):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    routing_key = f"mensagens.{recipient}" if recipient.lower() != 'all' else 'todos'

    channel.basic_publish(exchange='topic_logs',
                          routing_key=routing_key,
                          body=message)

    print(f" [x] Mensagem enviada para {recipient if recipient.lower() != 'all' else 'todos'}: {message}")

    connection.close()

if __name__ == '__main__':
    while True:
        recipient = input("Digite o nome do subscriber para o qual deseja enviar a mensagem (ou 'all' para todos, 'exit' para sair): ")

        if recipient.lower() == 'exit':
            break

        message = input("Messagem: ")

        publish_message(message, recipient)
