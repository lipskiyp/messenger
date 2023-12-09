FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8080

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /requirements.txt

COPY ./compose/entrypoint /entrypoint
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]