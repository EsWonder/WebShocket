# Dockerfile para el servidor y cliente WebSocket en un solo contenedor
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY server.py /app/server.py
COPY client.py /app/client.py
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto para WebSocket
EXPOSE 8765

# Comando para ejecutar el servidor y el cliente
CMD ["bash", "-c", "python server.py & python client.py"]
