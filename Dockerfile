FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]