# Use the official latest Python image from Docker Hub
FROM python:3.13.3

# Set the working directory in the container
WORKDIR /app

# (Optional) Copy your local files into the container
COPY . .

# (Optional) Install dependencies if you have a requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# (Optional) Set a default command, e.g., run a script
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# Expose the port the app runs on
EXPOSE 8000