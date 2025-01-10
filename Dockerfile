# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    ENVIRONMENT=production

# Install system dependencies including Arabic language support
RUN apt-get update && apt-get install -y \
    locales \
    gcc \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && localedef -i ar_SA -c -f UTF-8 -A /usr/share/locale/locale.alias ar_SA.UTF-8

# Set locale for Arabic support
ENV LANG ar_SA.utf8

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${POETRY_HOME}/bin:$PATH"

# Copy only dependency files first to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install dependencies (without project)
RUN poetry install --no-root --no-dev

# Copy only the necessary project files
COPY qalamos/ qalamos/
COPY frontend/ frontend/

# Install the project
RUN poetry install --no-dev \
    && rm -rf /root/.cache/pypoetry

# Create a non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "gunicorn", \
     "qalamos.main:app", \
     "--workers", "4", \
     "--worker-class", "uvicorn.workers.UvicornWorker", \
     "--bind", "0.0.0.0:8000", \
     "--timeout", "120"]
