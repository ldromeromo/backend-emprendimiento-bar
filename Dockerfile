FROM python:3.9

# Instala las bibliotecas ODBC
RUN apt-get update && \
apt-get install -y --no-install-recommends \
unixodbc \
unixodbc-dev \
curl \
gnupg && \
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft-archive-keyring.gpg && \
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/ubuntu/20.04/prod focal main" > /etc/apt/sources.list.d/mssql-release.list && \
apt-get update && \
ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m venv venv

RUN sh venv/bin/activate

RUN ls -la

WORKDIR /backend-emprendimiento-bar

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]