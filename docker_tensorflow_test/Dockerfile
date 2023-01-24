FROM tensorflow/tensorflow:2.5.0

WORKDIR /usr/src

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD ["model.py"]

ENTRYPOINT ["python3"]