import asyncio
import websockets

# Función que maneja las conexiones de los clientes
async def echo(websocket, path):
    async for message in websocket:
        print(f"Mensaje recibido: {message}")
        response = f"Hola, recibí tu mensaje: {message}"
        await websocket.send(response)

# Configuración del servidor WebSocket
async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765):
        print("Servidor WebSocket iniciado en ws://0.0.0.0:8765")
        await asyncio.Future()  # Ejecuta el servidor indefinidamente

if __name__ == "__main__":
    asyncio.run(main())
