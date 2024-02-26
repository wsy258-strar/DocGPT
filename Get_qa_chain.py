
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate



def get_qa_chain(vector_store):
    prompt_template = """基于以下已知内容，简洁和专业的来回答用户的问题。
                                            如果无法从中得到答案，清说"根据已知内容无法回答该问题"
                                            答案请使用中文。
                                            已知内容:
                                            {context}
                                            问题:
                                            {question}"""
 
    prompt = PromptTemplate(template=prompt_template,
                            input_variables=["context", "question"])
 
    return RetrievalQA.from_llm(llm=ChatOpenAI(model_name='gpt-3.5-turbo-16k'), retriever=vector_store.as_retriever(), prompt=prompt)