from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from api_client import get_sales


def ask_data_analyst(question: str) -> str:
    
    sales_data = get_sales()
    sales = sales_data.get("sales", [])

    # Formatar os dados de forma legível para o modelo
    sales_text = "\n".join([
        f"{s['clientName']} comprou {s['quantity']}x {s['product']['model']} por R$ {s['totalPrice']} em {s['paymentMethod']}"
        for s in sales
    ])

    # Prompt 
    prompt = PromptTemplate.from_template(
        """
    Você é um assistente que responde perguntas sobre vendas. Use os dados fornecidos para responder de forma curta e direta, sem explicações longas.

    Dados das vendas:
    {sales_data}

    Pergunta: {question}
    Resposta (máximo 2 frases, direta e objetiva):
    """
    )

    # configurado para respostas mais enxutas
    # mudar para Ollama2 ou 3...
    llm = OllamaLLM(
        model="mistral",
        temperature=0.1,
        max_tokens=150
    )

    # Montar a cadeia
    chain = prompt | llm

    
    return chain.invoke({"sales_data": sales_text, "question": question})
