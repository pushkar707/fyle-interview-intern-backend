FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN export FLASK_APP=core/server.py
RUN rm core/store.sqlite3
RUN flask db upgrade -d core/migrations/
EXPOSE 8000
CMD ["bash", "run.sh"]
