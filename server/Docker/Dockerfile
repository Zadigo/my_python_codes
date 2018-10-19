FROM python:3
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
COPY ./gunicorn/entrypoint.sh /code/
# ENTRYPOINT [ "entrypoint.sh" ]
# CMD ["python3", "manage.py runserver 0.0.0.0:8000"]
# CMD ["gunicorn", "-c", "gunicorn.conf", "server:app"]