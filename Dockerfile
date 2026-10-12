FROM python:3.14.6-slim-bookworm
WORKDIR /docker

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY ./ ./

CMD ["python3", "-m", "flask", "--app", "loan", "run", "--host", "0.0.0.0"]