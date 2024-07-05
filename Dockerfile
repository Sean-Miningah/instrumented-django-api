FROM python:3.12-slim 

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip install poetry

# Set work directory
WORKDIR /code

# Copy only the necessary files to install dependencies
COPY pyproject.toml poetry.lock /code/

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy project
COPY . /code/

# Expose port 8000 for the app
EXPOSE 8000

# Command to run the Django server using Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
