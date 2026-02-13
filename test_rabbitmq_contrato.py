import pika
import json
import pytest
from jsonschema import validate, ValidationError

# Mesmo contrato de antes
CONTRATO_SCHEMA = {
    "type": "object",
    "properties": {
        "order_id": {"type": "number"},
        "customer_email": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["order_id", "customer_email", "status"]
}

def test_validar_mensagem_da_fila():
    # 1. Conecta ao RabbitMQ para pegar uma mensagem real
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    # Pega apenas uma mensagem da fila
    method_frame, header_frame, body = channel.basic_get(queue='order_notifications', auto_ack=True)

    if body is None:
        pytest.fail("A fila está vazia! Rode o produtor.py primeiro.")

    # 2. Transforma a mensagem em JSON
    mensagem_real = json.loads(body)
    print(f"\nValidando mensagem recebida: {mensagem_real}")

    # 3. VALIDAÇÃO REAL DO CONTRATO
    # Se você mudou o nome do campo no produtor, isso aqui vai falhar!
    validate(instance=mensagem_real, schema=CONTRATO_SCHEMA)
    
    connection.close()