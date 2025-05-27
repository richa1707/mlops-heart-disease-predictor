# Use an official Python image
FROM python:3.10

# Set work directory
WORKDIR /app

# Copy everything
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Flask app
CMD ["python", "src/api/app.py"]

