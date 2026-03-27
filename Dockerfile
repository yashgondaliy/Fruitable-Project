#base image (OS)
FROM python:3.12-slim-bookworm

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

#copy file

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Copy project
COPY . .

# Run server
EXPOSE 8000

# Run server
CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
