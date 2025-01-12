import asyncio
import websockets

# Función que envía y recibe mensajes desde el servidor WebSocket
async def communicate():
    uri = "ws://127.0.0.1:8765"
    async with websockets.connect(uri) as websocket:
        # Envía un mensaje al servidor
        message = "¡Hola desde el cliente!"
        print(f"Enviando: {message}")
        await websocket.send(message)

        # Recibe la respuesta del servidor
        response = await websocket.recv()
        print(f"Respuesta del servidor: {response}")

if __name__ == "__main__":
    asyncio.run(communicate())
