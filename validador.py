import json
from jsonschema import validate, ValidationError

# 1. Definimos o nosso "Contrato" (Schema)
# Aqui dizemos o que é obrigatório e qual o tipo de cada campo
CONTRATO_SCHEMA = {
    "type": "object",
    "properties": {
        "order_id": {"type": "number"},
        "customer_email": {"type": "string", "format": "email"},
        "total_amount": {"type": "number"},
        "status": {"type": "string"}
    },
    "required": ["order_id", "customer_email", "status"] # Campos obrigatórios
}

def validar_mensagem(mensagem_json):
    try:
        # Tenta validar a mensagem contra o contrato
        mensagem = json.loads(mensagem_json)
        validate(instance=mensagem, schema=CONTRATO_SCHEMA)
        print("✅ Sucesso: A mensagem respeita o contrato!")
    except ValidationError as e:
        print(f"❌ Erro de Contrato: {e.message}")
    except json.JSONDecodeError:
        print("❌ Erro: A mensagem nem sequer é um JSON válido!")

# Exemplo de teste manual
if __name__ == "__main__":
    msg_correta = '{"order_id": 123, "customer_email": "teste@link.com", "total_amount": 50.0, "status": "PAID"}'
    msg_errada = '{"id_errado": 123, "status": "PAID"}' # Falta o email e o id está com nome errado

    print("Testando mensagem correta:")
    validar_mensagem(msg_correta)
    
    print("\nTestando mensagem errada:")
    validar_mensagem(msg_errada)