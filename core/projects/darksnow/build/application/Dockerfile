FROM python:3.7

COPY ./app /app/app

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY prestart.sh /app

RUN chmod +x /app/prestart.sh

EXPOSE 3000

ENTRYPOINT ["/app/prestart.sh"]

#CMD ["uvicorn", "app.app.main:app" , "--host", "0.0.0.0", "--port", "3000"]


