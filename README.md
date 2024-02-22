<h1 align="center">
📖DocGPT
</h1>

<div id="top" align="center">

![Github](https://img.shields.io/github/license/wsy258-strar/DocGPT)
![GitHub Repo stars](https://img.shields.io/github/stars/wsy258-strar%2FDocGPT)
![GitHub forks](https://img.shields.io/github/forks/wsy258-strar/DocGPT)
[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/shunyi%20wang
)](https://twitter.com/wangshunyi_)

</div>

**Accurate answers and instant citations for your documents.**

This is a document knowledge Q&A system that integrates technology chains such as LangChain, OpenAI, FAISS, etc. You can upload your own documents and have conversations with LLM.

[Demo待部署....](待部署....)

## Installation

Follow the instructions below to run the Streamlit server locally.

### Pre-requisites

Make sure you have 3.12 > Python ≥3.10 installed.

### Steps

1. Clone the repository

```bash
git clone https://github.com/wsy258-strar/DocGPT

```

2. Install dependencies:

```bash
pip install -r requirements.txt

```

3. (Optional) Avoid adding the OpenAI API every time you run the server by adding it to environment variables.
   - Make a copy of `.env.example` named `.env`
   - Add your API key to the `.env` file

> **Note:** Make sure you have a paid OpenAI API key for faster completions and to avoid hitting rate limits.

4. Run the Streamlit server

```bash
streamlit run main.py
```


Open http://localhost:8501 in your browser to access the app.

## Customization

You can increase the max upload file size by changing `maxUploadSize` in `.streamlit/config.toml`.
Currently, the max upload size is 25MB for the hosted version.

## Tech Stack

- User Interface - [Streamlit](https://streamlit.io/)
- LLM Tooling - [Langchain](https://github.com/hwchase17/langchain)

## Roadmap

- Add support for more formats (e.g. webpages, PPTX, etc.)
- Highlight relevant phrases in citations
- Support scanned documents with OCR
- More customization options (e.g. chain type, chunk size, etc.)
- Visual PDF viewer
- Support for Local LLMs

## Contributing

Thank you for your interest in my application.At present, I haven't linked to the database for backend development. Interested developers can contribute together.All contributions are welcome!



## License

Distributed under the MIT License. See [LICENSE](https://github.com/wsy258-strar/DocGPT/blob/main/LICENSE) for more information.
