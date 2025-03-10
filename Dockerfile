FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

COPY . .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]