# Projeto de Sumarização de Texto com LangChain e DeepSeek

Este projeto implementa uma ferramenta de sumarização de texto em português utilizando as bibliotecas LangChain e DeepSeek. A aplicação recebe um texto como entrada e fornece um resumo claro e objetivo.

## Pré-requisitos

- Python 3.8 ou superior  
- Virtualenv (recomendado)  
- [LangChain](https://github.com/langchain-ai/langchain)  
- [DeepSeek](https://deepseek.ai/)  

## Instalação

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. **Crie e ative um ambiente virtual:**

  ```bash
  python -m venv .venv
  source .venv/bin/activate  # No Windows, use '.venv\Scripts\activate'
  ```

3. **Instale as dependências:**

  ```bash
  pip install -r requirements.txt
  ```

4. **Configure a chave da API do DeepSeek:**

-Renomeie o arquivo .env.example para .env:

  ```bash
  mv .env.example .env
  ```
-Abra o arquivo .env e adicione sua chave da API do DeepSeek:

  ```bash
  DEEPSEEK_API_KEY=sua_chave_aqui
  ```
## Uso
1. **Execute o script principal:**
  
  ```bash
  python app.py
  ```

2. **Insira o texto que deseja resumir quando solicitado.**

## Estrutura do Projeto
-app.py: Script principal que executa a aplicação.
-requirements.txt: Lista de dependências Python.
-.env.example: Exemplo de arquivo de configuração para variáveis de ambiente.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a MIT License.
