# Dockerfile with VSCO Downloader GUI
# author: Micha Birklbauer
# version: 1.0.0

FROM python:3.12.0

LABEL maintainer="micha.birklbauer@gmail.com"

RUN mkdir app
RUN mkdir app/.streamlit
RUN mkdir app/.streamlit/ico
COPY requirements.txt app
COPY vsco_downloader.py app
COPY streamlit_app.py app
COPY .streamlit/config.toml app/.streamlit
COPY .streamlit/ico/download-icon.png app/.streamlit/ico
WORKDIR app
RUN pip install -r requirements.txt

CMD  ["streamlit", "run", "streamlit_app.py"]
