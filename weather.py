import asyncio
from typing import Any
import httpx

from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server


from mcp_server.tools import get_call_tool, get_list_tools

# Create MCP server instance
server = Server("weather-mpc-server")

@server.list_tools()
async def list_tools():
    return await get_list_tools()

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    return await get_call_tool(name, arguments)

async def main():
    """
    Main entry point for the MCP Server.
    Validates configuration and starts the server with all tools registered.
    """
    try:
        print('start server')
        tools = await list_tools()
        print(f"Numero di tools: {len(tools)}")
        for tool in tools:
            print(f"Tool: {tool.name}")

        capabilities = server.get_capabilities(
            notification_options=NotificationOptions(), experimental_capabilities={}
        )

        # Initialize server options
        initialization_options = InitializationOptions(
            server_name="financial-mcp-server",
            server_version="1.0.0",
            capabilities=capabilities,
        )

        async with stdio_server() as (read_stream, write_stream):
            print("📡 Server listening on stdio...")
            await server.run(read_stream, write_stream, initialization_options)
        
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    asyncio.run(main())