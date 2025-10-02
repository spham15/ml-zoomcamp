FROM agrigorev/model-2024-hairstyle:v3

RUN pip install keras-image-helper
RUN pip install --no-cache-dir \
  https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl \
  pillow==10.3.0 \
  requests==2.32.3 \
  "numpy<2"

COPY homework.py .
ENV MODEL_NAME=model_2024_hairstyle_v2.tflite

CMD [ "homework.lambda_handler" ]