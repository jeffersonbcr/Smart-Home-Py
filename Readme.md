# Smart Home Automation API

## Descrição do Projeto

Este projeto implementa uma **API de Automação Residencial** utilizando o framework **FastAPI**. O sistema é responsável por gerenciar dispositivos inteligentes, permitindo o registro, controle e agrupamento de dispositivos por ambientes. Ele simula um sistema no qual dispositivos como cortinas, TVs e lâmpadas podem ser controlados por comandos enviados através da API. O projeto é modular e facilmente expansível, permitindo adicionar novos tipos de dispositivos e funcionalidades no futuro.

### Funcionalidades

- Registro de dispositivos inteligentes com suas operações (ex: abrir/fechar cortinas, ligar/desligar lâmpadas).
- Agrupamento de dispositivos por ambientes (ex: "Sala", "Quarto").
- Envio de comandos para dispositivos ou para todos os dispositivos de um ambiente.
- Sistema intermediado por um servidor, onde todas as mensagens do cliente para os dispositivos são processadas.

### Dependências

O projeto utiliza as seguintes dependências:

- Python 3.7+
- FastAPI: Framework utilizado para construir a API.
- Uvicorn: Servidor ASGI para rodar o FastAPI.
- Pydantic: Utilizado para validação de dados.
- pytest: Framework para testes automatizados.
- httpx: Cliente HTTP utilizado nos testes do FastAPI.

### Execução do projeto

Criar um ambiente virtual:

```bash
python3 -m venv venv
```

Ativar o ambiente virtual:

```bash
source venv/bin/activate
```

Executar testes para validação da API.

```bash
pytest
```

Ver documentação:

```bash
uvicorn app.main:app --reload
```

Acessar :http://127.0.0.1:8000/docs
