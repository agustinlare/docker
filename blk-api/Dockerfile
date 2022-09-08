FROM arm32v7/python:3.7-buster

RUN mkdir /blk-api
ENV PORT=8080 \
    FLASK_APP="app.py" \
    FLASK_RUN_HOST="0.0.0.0" \
    FLASK_RUN_PORT=8881

COPY . /blk-api
WORKDIR /blk-api
RUN pip install -r requirements.txt

EXPOSE 8881:8881

CMD [ "app.py" ]
ENTRYPOINT [ "python3" ]
