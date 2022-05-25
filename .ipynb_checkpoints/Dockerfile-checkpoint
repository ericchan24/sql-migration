FROM python:3.9-slim
LABEL org.opencontainers.image.authors="eric.chan.24@gmail.com"
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN mkdir ~/.streamlit  
COPY .streamlit/config.toml ~/.streamlit/config.toml
RUN pip install -r requirements.txt
EXPOSE 80
COPY . /app     
ENTRYPOINT ["streamlit", "run"]
CMD ["a_app.py"]