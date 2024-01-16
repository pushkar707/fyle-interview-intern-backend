FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install virtualenv
RUN virtualenv myenv
RUN /bin/bash -c "source myenv/bin/activate && pip install -r requirements.txt"
ENV FLASK_APP=core/server.py
RUN rm core/store.sqlite3
RUN flask db upgrade -d core/migrations/
EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn_config.py", "core.server:app"]