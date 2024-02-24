import streamlit as st
ss = st.session_state

from tools.components.sidebar import sidebar
# from knowledge_gpt.components.sidebar import sidebar, ui_api_key

from ui import (
    wrap_doc_in_html,
    is_query_valid,
    is_file_valid,
    is_open_ai_key_valid,
    display_file_read_error,
    select_openai_api_key,
)

from tools.caching import bootstrap_caching

from tools.parsing import read_file
from tools.chunking import chunk_file
from tools.embedding import embed_files
from tools.qa import query_folder
from tools.utils import get_llm,pop_docs_upto_limit
import streamlit_scrollable_textbox as stx
# from tools.llm import LlmEngine
# from tools.components.monitor import community_tokens_available_pct



EMBEDDING = "openai"
VECTOR_STORE = "faiss"
MODEL_LIST = ["gpt-3.5-turbo", "gpt-4"]

# Uncomment to enable debug mode
# MODEL_LIST.insert(0, "debug")


st.set_page_config(page_title="DocGPT", page_icon="📖", layout="wide")
st.header("📖DocGPT")

# Enable caching for expensive functions
bootstrap_caching()

sidebar()

openai_api_key = ss.get("api_key")
# #select 
openai_api_key = select_openai_api_key()
print("select_keys:",openai_api_key)

if not openai_api_key:
    st.warning(
        "Enter your OpenAI API key in the sidebar. You can get a key at"
        " https://platform.openai.com/account/api-keys."
    )


uploaded_file = st.file_uploader(
    "Upload a pdf, docx, or txt file",
    type=["pdf", "docx", "txt"],
    help="Scanned documents are not supported yet!",
)

model: str = st.selectbox("Model", options=MODEL_LIST)  # type: ignore

with st.expander("Advanced Options"):
    return_all_chunks = st.checkbox("Show all chunks retrieved from vector search")
    show_full_doc = st.checkbox("Show parsed contents of the document")


if not uploaded_file:
    st.stop()

try:
    file = read_file(uploaded_file)
except Exception as e:
    display_file_read_error(e, file_name=uploaded_file.name)


chunked_file = chunk_file(file, chunk_size=300, chunk_overlap=0)

if not is_file_valid(file):
    st.stop()


if not is_open_ai_key_valid(openai_api_key, model):
    st.stop()


with st.spinner("Indexing document... This may take a while⏳"):
    folder_index = embed_files(
        files=[chunked_file],
        embedding=EMBEDDING if model != "debug" else "debug",
        vector_store=VECTOR_STORE if model != "debug" else "debug",
        openai_api_key=openai_api_key,
    )

print("your API keys:",openai_api_key)

with st.form(key="qa_form"):
    query = st.text_area("Ask a question about the document")
    submit = st.form_submit_button("Submit")


if show_full_doc:
    with st.expander("Document"):
        # Hack to get around st.markdown rendering LaTeX
        st.markdown(f"<p>{wrap_doc_in_html(file.docs)}</p>", unsafe_allow_html=True)



if submit:
    if not is_query_valid(query):
        st.stop()

    # Output Columns
    answer_col, sources_col = st.columns(2)

    llm =  get_llm(model=model, openai_api_key=openai_api_key, temperature=0)
    result = query_folder(
        folder_index=folder_index,
        query=query,
        return_all=return_all_chunks,
        llm=llm,
    )
    # print(token_dict)
    if openai_api_key == ss["OPENAI_API_KEY"]:
        ss['used'] = result.total_tokens


    
    # total_used_token += used_token  # 累加 used_token
    # # 调用另一个函数并传递 total_used_token
    # # total = get_community_usage_cost(total_used_token)
    # community_tokens_available_pct.userd = total_used_token
    # ui_api_key()
    
    with answer_col:
        st.markdown("#### Answer")
        st.markdown(result.answer)
        st.markdown("### Already Used Tokens")
        st.markdown(result.total_tokens)
        print("markdown total tokens:",result.total_tokens)


    with sources_col:
        docs_show =''
        st.markdown("#### Sources")
        for source in result.sources:
            docs_show = docs_show +'\n'+source.page_content+'\n'+source.metadata["source"]+'\n'+"--------------------------------------------------------"
        stx.scrollableTextbox(text = docs_show,height = 300)


