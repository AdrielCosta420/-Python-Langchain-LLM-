# Data Analyst Agent - Agente de Análise de Dados com LLM

Este repositório contém o código do **Data Analyst Agent**, um agente inteligente construído com **LangChain** e integrado a modelos locais via **Ollama** ou modelos em Cloud. Ele consome dados de vendas fornecidos por uma API backend em **Node.js + Fastify + Prisma + MongoDB**, realiza análises, interpretações e recomendações, e responde perguntas em linguagem natural.

---

## Objetivo

Criar um agente conversacional para responder perguntas estratégicas sobre dados de vendas, fornecendo insights rápidos, recomendações e interpretações contextuais para auxiliar a tomada de decisões em um MVP de aplicação.

---

## Tecnologias

- **Backend:** Node.js + Fastify + Prisma + MongoDB  
- **Agente LLM:** Python + LangChain + Ollama (modelos locais como Llama2:7b)  ou Modelos em Cloud (OpenAI, Deepseek etc) - use o OpenRouter para acessar o Hub de modelos gratuitos
- **Frontend:** Flutter com gerenciamento nativo usando ChangeNotifier, injeção de dependência via GetIt, arquitetura modular

---

## Funcionalidades

- Consumo dinâmico de dados de vendas da API Node.js  
- Análise e resumo dos dados com linguagem natural  
- Respostas objetivas em 3 categorias:  
  - Análise e Insights  
  - Recomendações e Estratégias  
  - Interpretação Contextual (termo ajustável para facilitar compreensão)  
- Configuração e escolha de modelo local Ollama para respostas rápidas e de qualidade  

---

## Como usar (Visão geral)

1. Configure suas variáveis sensíveis no arquivo `.env` (não versionado).  
2. Execute o backend Node.js com conexão ao banco de dados.  
3. Rode o agente Python, que consulta a API do backend e processa as respostas via LangChain + Ollama ou Modelos em Cloud.  
4. Integre com o frontend Flutter para consulta via botões pré-definidos, evitando perguntas genéricas e otimizando custo computacional.  

---

## Estrutura do repositório

- `data_analyst_agent.py` — script principal do agente  
- `api_client.py` — cliente para consumir a API Node.js  
- `.env` — variáveis de ambiente (excluído do versionamento)  
- `README.md` — documentação do projeto  

---

## Próximos passos

- Versão do agente em nuvem (OpenAI API) como fallback.
- Ajustar termos e categorias para melhorar usabilidade no app  
- Implementar cache para reduzir chamadas e acelerar respostas  
- Expandir modelos e estratégias de análise conforme feedback do usuário  

