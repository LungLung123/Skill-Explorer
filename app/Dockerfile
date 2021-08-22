FROM python:3.9.1

WORKDIR /app

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY * /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python main.py