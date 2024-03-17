FROM python:3
WORKDIR /home/www

COPY main.py .

RUN chmod +x main.py && python3 main.py init && chmod +x ./*

EXPOSE 8080

CMD ["python3", "main.py"]

USER 10001
