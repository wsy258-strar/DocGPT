from typing import List
import streamlit as st
ss = st.session_state
from langchain.docstore.document import Document
from tools.parsing import File
import openai
from streamlit.logger import get_logger
from typing import NoReturn
from tools.components.monitor import community_tokens_available_pct

logger = get_logger(__name__)


def wrap_doc_in_html(docs: List[Document]) -> str:
    """Wraps each page in document separated by newlines in <p> tags"""
    text = [doc.page_content for doc in docs]
    if isinstance(text, list):
        # Add horizontal rules between pages
        text = "\n<hr/>\n".join(text)
    return "".join([f"<p>{line}</p>" for line in text.split("\n")])


def is_query_valid(query: str) -> bool:
    if not query:
        st.error("Please enter a question!")
        return False
    return True


def is_file_valid(file: File) -> bool:
    if (
        len(file.docs) == 0
        or "".join([doc.page_content for doc in file.docs]).strip() == ""
    ):
        st.error("Cannot read document! Make sure the document has selectable text")
        logger.error("Cannot read document")
        return False
    return True


def display_file_read_error(e: Exception, file_name: str) -> NoReturn:
    st.error("Error reading file. Make sure the file is not corrupted or encrypted")
    logger.error(f"{e.__class__.__name__}: {e}. Extension: {file_name.split('.')[-1]}")
    st.stop()


@st.cache_data(show_spinner=False)
def is_open_ai_key_valid(openai_api_key, model: str) -> bool:
    if model == "debug":
        return True 
    if not openai_api_key:
        st.error("Please enter your OpenAI API key in the sidebar!")
        return False
    try:
        openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": "test"}],
            api_key=openai_api_key,
        )
    except Exception as e:
        st.error(f"{e.__class__.__name__}: {e}")
        logger.error(f"{e.__class__.__name__}: {e}")
        return False

    return True


def select_openai_api_key():
    pct = community_tokens_available_pct(ss["used"])
      
    if ss['api_key'] :
        openai_api_key = ss.get("api_key")
    if not ss['api_key'] and pct != 0:
        openai_api_key = ss.get("OPENAI_API_KEY")
    if not ss['api_key'] and pct == 0 :
        openai_api_key = None
    return openai_api_key