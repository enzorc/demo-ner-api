FROM python:3.9-slim

COPY . ./ner_api

WORKDIR ./ner_api

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["app:app_api", "--host", "0.0.0.0"]
