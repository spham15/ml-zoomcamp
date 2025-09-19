# docker build -t {name} .
# docker run -it --rm --entrypoint=bash {name} --- to test inside the container
# docker run -it --rm -p 9696:9696 {name}
    # - p 9696:9696 --- map port 9696 of the container to port 9696 on the host machine

FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

RUN rm -f /app/model2.bin /app/dv.bin

COPY ["flask_predict.py",  "dv.bin", "model1.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "flask_predict:app"]