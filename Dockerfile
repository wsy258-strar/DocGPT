# 基础镜像
FROM python:3.11-slim

# 设置工作目录为
WORKDIR /app

COPY . /app

ENV OPENAI_API_KEY = "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"

COPY . /DocGPT

# 安装requirments.txt中列举的包

# 向容器外暴露一个端口
EXPOSE 8501
# 在容器启动时运行main.py
CMD ["python", "-m", "streamlit", "run", "main.py", "--server.port=8501"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --verbose