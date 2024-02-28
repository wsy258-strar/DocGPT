# 基础镜像
FROM python:3.11-slim


#安装依赖
RUN pip install --upgrade pip
RUN pip install --no-cache-dir streamlit-scrollable-textbox 
RUN pip install --no-cache-dir langchain==0.0.220 
RUN pip install --no-cache-dir PyPDF2==3.0.1
RUN pip install --no-cache-dir python-dotenv==0.21.1 
RUN pip install --no-cache-dir streamlit==1.25.0 
RUN pip install --no-cache-dir faiss-cpu==1.7.4 
RUN pip install --no-cache-dir openai==0.28.0
RUN pip install --no-cache-dir aiohttp==3.8.5 
RUN pip install --no-cache-dir aiosignal==1.3.1 
RUN pip install --no-cache-dir altair==5.0.1 
RUN pip install --no-cache-dir async-timeout==4.0.2 
RUN pip install --no-cache-dir attrs==23.1.0 
RUN pip install --no-cache-dir blinker==1.6.2 
RUN pip install --no-cache-dir cachetools==5.3.1 
RUN pip install --no-cache-dir certifi==2023.7.22 
RUN pip install --no-cache-dir charset-normalizer==3.2.0 
RUN pip install --no-cache-dir click==8.1.6 
RUN pip install --no-cache-dir cohere==3.10.0 
RUN pip install --no-cache-dir colorama==0.4.6 
RUN pip install --no-cache-dir dataclasses-json==0.5.9 
RUN pip install --no-cache-dir decorator==5.1.1 
RUN pip install --no-cache-dir docx2txt==0.8 
RUN pip install --no-cache-dir faiss-cpu==1.7.4 
RUN pip install --no-cache-dir filelock==3.12.3 
RUN pip install --no-cache-dir frozenlist==1.4.0 
RUN pip install --no-cache-dir fsspec==2023.9.0 
RUN pip install --no-cache-dir gitdb==4.0.10 
RUN pip install --no-cache-dir gitpython==3.1.32 
RUN pip install --no-cache-dir greenlet==2.0.2 
RUN pip install --no-cache-dir huggingface-hub==0.16.4 
RUN pip install --no-cache-dir idna==3.4 
RUN pip install --no-cache-dir importlib-metadata==6.8.0 
RUN pip install --no-cache-dir jinja2==3.1.2 
RUN pip install --no-cache-dir jsonschema-specifications==2023.7.1 
RUN pip install --no-cache-dir jsonschema==4.18.4 
RUN pip install --no-cache-dir langchainplus-sdk==0.0.20 
RUN pip install --no-cache-dir markdown-it-py==3.0.0 
RUN pip install --no-cache-dir markupsafe==2.1.3 
RUN pip install --no-cache-dir marshmallow-enum==1.5.1 
RUN pip install --no-cache-dir marshmallow==3.20.1 
RUN pip install --no-cache-dir mdurl==0.1.2 
RUN pip install --no-cache-dir multidict==6.0.4 
RUN pip install --no-cache-dir mypy-extensions==1.0.0 
RUN pip install --no-cache-dir numexpr==2.8.4 
RUN pip install --no-cache-dir numpy==1.25.1 
RUN pip install --no-cache-dir openapi-schema-pydantic==1.2.4 
RUN pip install --no-cache-dir packaging==23.1 
RUN pip install --no-cache-dir pandas==2.0.3 
RUN pip install --no-cache-dir pillow==9.5.0 
RUN pip install --no-cache-dir protobuf==4.23.4 
RUN pip install --no-cache-dir pyarrow==12.0.1 
RUN pip install --no-cache-dir pycryptodome==3.18.0 
RUN pip install --no-cache-dir pydantic==1.10.11 
RUN pip install --no-cache-dir pydeck==0.8.0 
RUN pip install --no-cache-dir pygments==2.15.1 
RUN pip install --no-cache-dir pympler==1.0.1 
RUN pip install --no-cache-dir pymupdf==1.22.5 
RUN pip install --no-cache-dir python-dateutil==2.8.2
RUN pip install --no-cache-dir pytz-deprecation-shim==0.1.0.post0 
RUN pip install --no-cache-dir pytz==2023.3 
RUN pip install --no-cache-dir pyyaml==6.0.1 
RUN pip install --no-cache-dir referencing==0.30.0 
RUN pip install --no-cache-dir regex==2023.6.3 
RUN pip install --no-cache-dir requests==2.31.0 
RUN pip install --no-cache-dir rich==13.4.2 
RUN pip install --no-cache-dir rpds-py==0.9.2 
RUN pip install --no-cache-dir safetensors==0.3.3 
RUN pip install --no-cache-dir six==1.16.0 
RUN pip install --no-cache-dir smmap==5.0.0 
RUN pip install --no-cache-dir sqlalchemy==2.0.19 
RUN pip install --no-cache-dir tenacity==8.2.2 
RUN pip install --no-cache-dir tiktoken==0.4.0 
RUN pip install --no-cache-dir tokenizers==0.13.3
RUN pip install --no-cache-dir toml==0.10.2 
RUN pip install --no-cache-dir toolz==0.12.0 
RUN pip install --no-cache-dir tornado==6.3.2 
RUN pip install --no-cache-dir tqdm==4.65.0 
RUN pip install --no-cache-dir transformers==4.33.1 
RUN pip install --no-cache-dir typing-extensions==4.7.1 
RUN pip install --no-cache-dir typing-inspect==0.9.0 
RUN pip install --no-cache-dir tzdata==2023.3 
RUN pip install --no-cache-dir tzlocal==4.3.1 
RUN pip install --no-cache-dir urllib3==1.26.16 
RUN pip install --no-cache-dir validators==0.20.0 
RUN pip install --no-cache-dir watchdog==3.0.0 
RUN pip install --no-cache-dir yarl==1.9.2 
RUN pip install --no-cache-dir zipp==3.16.2 

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