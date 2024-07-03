# Documentação do Projeto BGPHe

## Visão Geral

Este projeto é uma aplicação web desenvolvida com FastAPI, projetada para interagir com o site bgp.he.net. Ele permite aos usuários obter informações detalhadas sobre endereços IP e redes, incluindo dados IRR, informações de rede e dados WHOIS. A aplicação oferece uma interface RESTful para consulta dessas informações de forma programática.

## Funcionalidades

- **Consulta de Informações de Rede**: Permite aos usuários obter informações detalhadas sobre uma rede específica, usando o endpoint `/net?address={address}`.
- **Consulta do Meu IP**: Fornece informações sobre o IP do usuário que está fazendo a requisição, acessível através do endpoint [`/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fse7e%2FDocumentos%2Fcode%2FL7-Looking-Glass%2FTest-BGPhe%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/se7e/Documentos/code/L7-Looking-Glass/Test-BGPhe/").

## Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- FastAPI
- Uvicorn
- Requests

### Instalação

1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias usando o seguinte comando:

```bash
pip install fastapi uvicorn requests
```

3. Inicie o servidor com o seguinte comando:

```bash
python bgphe.py
```

### Endpoints

#### Consulta de Informações de Rede

- **URL**: `/net`
- **Método**: `GET`
- **URL Params**: [`address=[IPv4/IPv6 ou prefixo de rede]`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Fse7e%2FDocumentos%2Fcode%2FL7-Looking-Glass%2FTest-BGPhe%2Fbgphe.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A14%2C%22character%22%3A15%7D%5D "bgphe.py")
- **Resposta de Sucesso**:
  - **Código**: 200
  - **Conteúdo**: JSON contendo dados IRR, informações de rede e dados WHOIS.

#### Consulta do Meu IP

- **URL**: [`/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fse7e%2FDocumentos%2Fcode%2FL7-Looking-Glass%2FTest-BGPhe%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/se7e/Documentos/code/L7-Looking-Glass/Test-BGPhe/")
- **Método**: `GET`
- **Resposta de Sucesso**:
  - **Código**: 200
  - **Conteúdo**: JSON contendo informações sobre o IP do usuário.

## Exemplos de Uso

### Consulta de Informações de Rede

```bash
curl http://localhost:8000/net?address=8.8.8.8
```

### Consulta do Meu IP

```bash
curl http://localhost:8000/
```

## Desenvolvimento

Este projeto foi desenvolvido com as seguintes tecnologias:

- **FastAPI**: Para a criação da API RESTful.
- **Uvicorn**: Como servidor ASGI para hospedar a aplicação.
- **Requests**: Para fazer requisições HTTP ao site bgp.he.net.

## Contribuições

Contribuições são sempre bem-vindas! Para contribuir, por favor:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`).
3. Faça commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`).
4. Faça push para a branch (`git push origin feature/AmazingFeature`).
5. Abra um Pull Request.


## Contato

Se7e - [Instagram](https://www.instagram.com/eliashenriquesh/)

Projeto Link: [https://github.com/elias-henrique/BGPhe-api.git](https://github.com/elias-henrique/BGPhe-api.git)