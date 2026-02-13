import pytest
from jsonschema import validate, ValidationError

# O Contrato (o "gabarito" da prova)
CONTRATO_SCHEMA = {
    "type": "object",
    "properties": {
        "order_id": {"type": "number"},
        "customer_email": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["order_id", "customer_email", "status"]
}

# Caso de Teste 1: Mensagem Perfeita
def test_contrato_mensagem_valida():
    mensagem = {
        "order_id": 123,
        "customer_email": "teste@email.com",
        "status": "PAID"
    }
    # Se não der erro, o teste passa
    validate(instance=mensagem, schema=CONTRATO_SCHEMA)

# Caso de Teste 2: Mensagem com campo faltando (Deve falhar)
def test_contrato_falta_campo_obrigatorio():
    mensagem_errada = {
        "order_id": 123,
        # Falta o email aqui
        "status": "PAID"
    }
    # Aqui dizemos ao Pytest que ESPERAMOS um erro ValidationError
    with pytest.raises(ValidationError):
        validate(instance=mensagem_errada, schema=CONTRATO_SCHEMA)

# Caso de Teste 3: Mensagem com tipo errado (ID como texto em vez de número)
def test_contrato_tipo_de_dado_errado():
    mensagem_tipo_errado = {
        "order_id": "ID_EM_TEXTO", 
        "customer_email": "teste@email.com",
        "status": "PAID"
    }
    with pytest.raises(ValidationError):
        validate(instance=mensagem_tipo_errado, schema=CONTRATO_SCHEMA)