import asyncio

from mcp.types import (
    TextContent,
    Tool
)

from .integrations import (
	weather_integration
)

async def get_list_tools(): 
	"""
	List all available tools for the MPC server
	"""
	return [
		Tool(
			name="get_forecast",
			description="Get weather forecast for a location",
			inputSchema={"type": "object", "properties": {}, "required": []}
		),
		Tool(
			name="get_alert",
			description="Get weather alerts for a US state",
			inputSchema={"type": "object", "properties": {}, "required": []}
		)
	]


async def get_call_tool(name: str, arguments: dict):
    """
    Handle tool calls based on the tool name.
    """
    try:
        if name == "get_forecast":
            # If the function is sync, use asyncio.to_thread
            if asyncio.iscoroutinefunction(weather_integration.get_forecast):
                result = await weather_integration.get_forecast()
            else:
                result = await asyncio.to_thread(weather_integration.get_forecast)
            return [TextContent(type="text", text=str(result))]

        elif name == "get_margin_leverage":
            if asyncio.iscoroutinefunction(weather_integration.get_alerts):
                result = await weather_integration.get_alerts()
            else:
                result = await asyncio.to_thread(weather_integration.get_alerts)
            return [TextContent(type="text", text=str(result))]

        else:
            raise ValueError(f"Unknown tool: {name}")
    except Exception as e:
        print(f"Error executing tool {name}: {str(e)}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]
