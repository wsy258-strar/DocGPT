from typing import List
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from tools.prompts import STUFF_PROMPT
from langchain.docstore.document import Document
from tools.embedding import FolderIndex
from pydantic import BaseModel
from langchain.chat_models.base import BaseChatModel
from typing import Tuple, List
import re
# 跟踪token使用情况
from langchain.callbacks import get_openai_callback
from tools.llm import LlmEngine
# from langchain_openai import OpenAI
#全局变量，存储总的token


class AnswerWithSources(BaseModel):
    answer: str
    sources: List[Document]
    total_tokens: int  # 添加一个 total_tokens 属性


def query_folder(
    query: str,
    folder_index: FolderIndex,
    llm : BaseChatModel,
    return_all: bool = False,
) -> AnswerWithSources:
# -> Tuple[AnswerWithSources, int]:
    """Queries a folder index for an answer.

    Args:
        query (str): The query to search for.
        folder_index (FolderIndex): The folder index to search.
        return_all (bool): Whether to return all the documents from the embedding or
        just the sources for the answer.
        model (str): The model to use for the answer generation.
        **model_kwargs (Any): Keyword arguments for the model.

    Returns:
        AnswerWithSources: The answer and the source documents, 
        along with the length of query, answer, and sources combined.
    """

    chain = load_qa_with_sources_chain(
        llm=llm, 
        chain_type="stuff",
        prompt=STUFF_PROMPT,
    )

    relevant_docs = folder_index.index.similarity_search(query, k=5)
    with get_openai_callback() as cb:
    
        result = chain(
            {"input_documents": relevant_docs, "question": query}, return_only_outputs=True
        )
        total_tokens = cb.total_tokens
        print(f"Total Tokens: {total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Cost (USD): ${cb.total_cost}")

    total_tokens += total_tokens
    total_tokens = get_community_usage_cost(total_tokens)

    sources = relevant_docs

    if not return_all:
        sources = get_sources(result["output_text"], folder_index)

    answer = result["output_text"].split("SOURCES: ")[0]

    print("result:",len(result["output_text"]))


    return AnswerWithSources(answer=answer, sources=sources, total_tokens=total_tokens) 




def get_sources(answer: str, folder_index: FolderIndex) -> List[Document]:
    """Retrieves the docs that were used to answer the question the generated answer."""

    source_keys = [s for s in answer.split("SOURCES: ")[-1].split(", ")]

    source_docs = []
    for file in folder_index.files:
        for doc in file.docs:
            if doc.metadata["source"] in source_keys:
                # 移除 source.metadata["source"] 中单词之间的多余空格和换行
                clean_source = re.sub(r'\s+', ' ', doc.metadata["source"]).strip()
                doc.metadata["source"] = clean_source  # 更新源字符串
                source_docs.append(doc)  # 将匹配的文档对象添加到列表中
    return source_docs

def get_community_usage_cost(total_used_token):
    # 在这个函数中进行对 total_used_token 的操作
    # 假设这里是统计每次的 used_token 的和并返回
    return total_used_token