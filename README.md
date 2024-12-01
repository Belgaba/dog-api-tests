# Testes de Integração para Dog API

Este projeto contém testes de integração para a Dog API, que fornece informações sobre raças de cães e imagens aleatórias. Os testes foram implementados usando a biblioteca `pytest` e cobrem cenários como requisições bem-sucedidas, erros e validação de dados.

## Estrutura do Projeto

- **test_api.py**: Contém os testes de integração escritos em Python usando `pytest`.
- **requirements.txt**: Lista de bibliotecas necessárias para executar os testes.
- **README.md**: Este arquivo, com instruções para configuração e execução.

## Pré-requisitos

- Python 3.8 ou superior instalado em sua máquina.
- Ambiente virtual configurado (recomendado).

## Como executar os testes

1. Clone o repositório ou copie os arquivos do projeto para sua máquina.
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

## Testes implementados

**Os testes cobrem os seguintes cenários:**

   1.Sucesso ao obter uma imagem aleatória de cachorro: Verifica se a API retorna uma resposta válida ao solicitar uma imagem de cachorro.
   2.Sucesso ao obter imagens de uma raça específica: Confirma que a API responde corretamente com imagens da raça solicitada.
   3.Erro ao acessar um endpoint inválido: Simula o acesso a uma rota inexistente e valida a resposta 404.
   4.Erro ao solicitar imagens de uma raça inexistente: Valida o comportamento da API para uma raça que não existe.
   5.Tempo de resposta da API: Garante que a API responde em um tempo aceitável (menos de 1 segundo).