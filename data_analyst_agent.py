import os
from langchain_core.prompts import PromptTemplate
# from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from api_client import get_sales


def ask_data_analyst(question: str) -> str:
    
    sales_data = get_sales()
    sales = sales_data.get("sales", [])

 
    sales_text = "\n".join([
        f"{s['clientName']} comprou {s['quantity']}x {s['product']['model']} por R$ {s['totalPrice']} em {s['paymentMethod']}"
        for s in sales
    ])

    # Prompt 
    prompt = PromptTemplate.from_template(
     "Dados das vendas:\n{sales_data}\n\nPergunta: {question}\nResposta (máximo 2 frases, direta e objetiva):"
    )

    # configurado para respostas mais enxutas
    # mudar para Ollama2 ou 3...
    llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENAI_API_KEY"),
        model="deepseek/deepseek-prover-v2:free",
        max_tokens=150,
        temperature=0.1,
        # cache=True,
    )
    # OllamaLLM(
    #     model="mistral",
    #     temperature=0.1,
    #     max_tokens=150
    # )

    # Montar a cadeia
    chain = prompt | llm

    
    response = chain.invoke({"sales_data": sales_text, "question": question})
    return str(response.content).strip()
