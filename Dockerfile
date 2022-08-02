# # Base on offical Python Slim image
FROM python:3.10-slim
# Set working directory
WORKDIR /calculator
# Copy all files
COPY . .
# Install dependencies
RUN pip install --upgrade pip && pip install --require-hashes -r /calculator/requirements/dev.txt
