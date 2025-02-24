# 1 
FROM python:3.7

# 2
RUN pip install --upgrade openai Flask gunicorn 

# 3
COPY . /app
WORKDIR /app

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app