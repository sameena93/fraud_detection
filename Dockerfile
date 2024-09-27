# Use an official Python runtime as a parent image
FROM python:3.10

# Create a non-root user
RUN useradd -m -u 1000 user
USER user

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY --chown=user . /app

# Expose the port that the application will run on
EXPOSE 7860

# Use Gunicorn to run the Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
