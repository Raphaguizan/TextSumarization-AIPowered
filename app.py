from langchain_anthropic import ChatAnthropic
from langchain_deepseek import ChatDeepSeek
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
import os

# carregar variáveis de ambiente
load_dotenv(find_dotenv())
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
DEEPSEEK_API_KEY = os.environ["DEEPSEEK_API_KEY"]


llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=DEEPSEEK_API_KEY
    # outros parâmetros conforme necessário
)
#criar modelo IA
#llm = ChatAnthropic(
#    model="claude-3-opus-20240229",
#    temperature=0,
#    anthropic_api_key=ANTHROPIC_API_KEY
#)

text = "Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter, and his friends, Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harry's conflict with Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic, and subjugate all wizards and Muggles (non-magical people)." 

#split text: fatiamento de texto
text_splitter = CharacterTextSplitter()
texts = text_splitter.split_text(text)


# Criar prompts personalizados para map e reduce
map_prompt = PromptTemplate(
    input_variables=['text'],
    template="Resuma o seguinte texto de forma clara e objetiva em português:\n\n{text}"
)

combine_prompt = PromptTemplate(
    input_variables=['text'],
    template="Aqui estão vários resumos de trechos de um texto maior:\n\n{text}\n\n"
             "Com base nesses resumos, forneça um resumo final claro e objetivo em português."
)


docs = [Document(page_content=text)for tex in texts]

# Criar a cadeia de sumarização com prompts personalizados
chain = load_summarize_chain(
    llm, 
    chain_type="map_reduce", 
    verbose=True, 
    map_prompt=map_prompt, 
    combine_prompt=combine_prompt
)


summary = chain.invoke(docs)
print(summary['output_text'])


#print (resp)


