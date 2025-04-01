# Stage 1 - Build
FROM python:3.11-slim as builder

WORKDIR /code

RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --user -r requirements.txt

COPY . .

# Stage 2 - Final runtime image
FROM python:3.11-slim

WORKDIR /code

RUN apt-get update && apt-get install -y libpq-dev

# Copy installed Python packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
