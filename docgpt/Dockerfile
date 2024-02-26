# 基础镜像
FROM python:3.11

# 设置工作目录为
WORKDIR /app

COPY . /app

# 安装requirments.txt中列举的包
RUN pip install -r requirements.txt
# 向容器外暴露一个端口
EXPOSE 8501
# 在容器启动时运行main.py
CMD ["python", "-m", "streamlit", "run", "main.py", "--server.port=8501"]
