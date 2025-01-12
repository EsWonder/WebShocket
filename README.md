# WebSocket Client-Server Project

## Description  
This project showcases a simple WebSocket client-server interaction. The server listens for incoming connections, processes client messages, and responds in real-time. The application is Dockerized for easy deployment and testing.

## Requirements  
- **Python**: Version 3.10 or later  
- **Docker**: Version 20.10 or later  
- **Libraries**: `websockets` for handling WebSocket connections  

## Setup Instructions  

### Clone the Project  
Clone the repository and navigate to the directory:  
git clone <repository_url>  
cd <repository_directory>  

### Run Without Docker  
Install the required dependencies:  
pip install websockets  
Start the server:  
python server.py  
Run the client:  
python client.py  

### Docker Instructions  
Build the Docker image:  
docker build -t websocket-app .  
Run the Docker container:  
docker run --name websocket-app-container -p 8765:8765 websocket-app  

### Docker Hub  
Replace with your Docker Hub repository link when available.
