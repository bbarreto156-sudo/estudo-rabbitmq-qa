import pika
import json

def send_order():
    # Conexão com o RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declaração da fila
    channel.queue_declare(queue='order_notifications')

    # Mensagem seguindo o contrato
    order_data = {
        "order_id": 123456,
        "customer_email": "dev@teste.com",
        "total_amount": 150.00,
        "status": "False"
    }

    channel.basic_publish(
        exchange='',
        routing_key='order_notifications',
        body=json.dumps(order_data)
    )
    
    print(f" [x] Mensagem enviada: {order_data}")
    connection.close()

if __name__ == "__main__":
    send_order()