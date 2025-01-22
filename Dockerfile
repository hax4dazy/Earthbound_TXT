FROM python:3.10-alpine

WORKDIR /app
ADD * /app/
ADD src /app/src/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["python", "src/main.py"]