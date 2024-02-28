import streamlit as st
# from tools.components.faq import faq
from dotenv import load_dotenv
import os
ss = st.session_state
from tools.components  import  monitor
# import streamlit_scrollable_textbox as stx
# from tools.utils import pop_docs_upto_limit



import os
import openai

# get openai keys
from dotenv import load_dotenv, find_dotenv
def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.environ['OPENAI_API_KEY']

openai.api_key = get_openai_key()

load_dotenv()


def ui_api_key():

    if 'community_user' not in st.session_state:
        st.session_state['community_user'] = 'shunyiwang'
    if 'used' not in st.session_state:
        ss['used'] = 0
    if 'debug' not in ss: ss['debug'] = {}
    if ss['community_user']:
        st.write('## Optional - community version enter your OpenAI API key')
        t1,t2 = st.tabs(['community version','enter your own API key'])
        with t1:
            print("ssused_tokens",ss['used'])
            pct = monitor.community_tokens_available_pct(ss['used'])
            st.write(f'Community tokens available: :{"green" if pct else "red"}[{int(pct)}%]')
    
            st.progress(pct/100)
            st.write('Refresh in: ' + monitor.community_tokens_refresh_in())
            st.write('Notice : The community version is provided by the creator and has a limit , you can sign up to OpenAI and/or create your API key [here](https://platform.openai.com/account/api-keys)')
            ss['OPENAI_API_KEY'] = get_openai_key()
            ss['community_pct'] = pct
            ss['debug']['community_pct'] = pct
        with t2:
            st.text_input('OpenAI API key', type='password', key='api_key', label_visibility="collapsed")
    else:
        st.write('## 1. Enter your OpenAI API key')
        st.text_input('OpenAI API key', type='password', key='api_key',  label_visibility="collapsed")
		

        
def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. The default is community version (free!) or you can enter "
            "your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
        )
        
        ui_api_key()
		
        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖DocGPT allows you to ask questions about "
            "your documents and get accurate answers with LLM. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/wsy258-strar/DocGPT) " 
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by [Shunyi Wang](https://twitter.com/wangshunyi_)")
        st.markdown("---")

        # faq()
