# 基础镜像
FROM python:3.11-slim


#安装依赖
RUN pip install --upgrade pip
RUN pip install streamlit-scrollable-textbox 
RUN pip install langchain==0.0.220 
RUN pip install PyPDF2==3.0.1
RUN pip install python-dotenv==0.21.1 
RUN pip install streamlit==1.25.0 
RUN pip install faiss-cpu==1.7.4 
RUN pip install openai==0.28.0
RUN pip install aiohttp==3.8.5 
RUN pip install aiosignal==1.3.1 
RUN pip install altair==5.0.1 
RUN pip install async-timeout==4.0.2 
RUN pip install attrs==23.1.0 
RUN pip install blinker==1.6.2 
RUN pip install cachetools==5.3.1 
RUN pip install certifi==2023.7.22 
RUN pip install charset-normalizer==3.2.0 
RUN pip install click==8.1.6 
RUN pip install cohere==3.10.0 
RUN pip install colorama==0.4.6 
RUN pip install dataclasses-json==0.5.9 
RUN pip install decorator==5.1.1 
RUN pip install docx2txt==0.8 
RUN pip install faiss-cpu==1.7.4 
RUN pip install filelock==3.12.3 
RUN pip install frozenlist==1.4.0 
RUN pip install fsspec==2023.9.0 
RUN pip install gitdb==4.0.10 
RUN pip install gitpython==3.1.32 
RUN pip install greenlet==2.0.2 
RUN pip install huggingface-hub==0.16.4 
RUN pip install idna==3.4 
RUN pip install importlib-metadata==6.8.0 
RUN pip install jinja2==3.1.2 
RUN pip install jsonschema-specifications==2023.7.1 
RUN pip install jsonschema==4.18.4 
RUN pip install langchainplus-sdk==0.0.20 
RUN pip install markdown-it-py==3.0.0 
RUN pip install markupsafe==2.1.3 
RUN pip install marshmallow-enum==1.5.1 
RUN pip install marshmallow==3.20.1 
RUN pip install mdurl==0.1.2 
RUN pip install multidict==6.0.4 
RUN pip install mypy-extensions==1.0.0 
RUN pip install numexpr==2.8.4 
RUN pip install numpy==1.25.1 
RUN pip install openapi-schema-pydantic==1.2.4 
RUN pip install packaging==23.1 
RUN pip install pandas==2.0.3 
RUN pip install pillow==9.5.0 
RUN pip install protobuf==4.23.4 
RUN pip install pyarrow==12.0.1 
RUN pip install pycryptodome==3.18.0 
RUN pip install pydantic==1.10.11 
RUN pip install pydeck==0.8.0 
RUN pip install pygments==2.15.1 
RUN pip install pympler==1.0.1 
RUN pip install pymupdf==1.22.5 
RUN pip install python-dateutil==2.8.2
RUN pip install pytz-deprecation-shim==0.1.0.post0 
RUN pip install pytz==2023.3 
RUN pip install pyyaml==6.0.1 
RUN pip install referencing==0.30.0 
RUN pip install regex==2023.6.3 
RUN pip install requests==2.31.0 
RUN pip install rich==13.4.2 
RUN pip install rpds-py==0.9.2 
RUN pip install safetensors==0.3.3 
RUN pip install six==1.16.0 
RUN pip install smmap==5.0.0 
RUN pip install sqlalchemy==2.0.19 
RUN pip install tenacity==8.2.2 
RUN pip install tiktoken==0.4.0 
RUN pip install tokenizers==0.13.3
RUN pip install toml==0.10.2 
RUN pip install toolz==0.12.0 
RUN pip install tornado==6.3.2 
RUN pip install tqdm==4.65.0 
RUN pip install transformers==4.33.1 
RUN pip install typing-extensions==4.7.1 
RUN pip install typing-inspect==0.9.0 
RUN pip install tzdata==2023.3 
RUN pip install tzlocal==4.3.1 
RUN pip install urllib3==1.26.16 
RUN pip install validators==0.20.0 
RUN pip install watchdog==3.0.0 
RUN pip install yarl==1.9.2 
RUN pip install zipp==3.16.2 

# 设置工作目录为
WORKDIR /app

COPY . /app

# ENV OPENAI_API_KEY = "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"

COPY . /DocGPT

# 安装requirments.txt中列举的包

# 向容器外暴露一个端口
EXPOSE 8501
# 在容器启动时运行main.py
CMD ["python", "-m", "streamlit", "run", "main.py", "--server.port=8501"]

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt --verbose