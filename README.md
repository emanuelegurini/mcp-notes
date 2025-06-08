# MCP Weather Server

This is an MCP (Model Context Protocol) server. It provides weather information by connecting to the National Weather Service (NWS) API.

## Functionality

The server exposes tools that an MCP client can call:
-   `get_forecast`: Retrieves the weather forecast for a specified latitude and longitude.
-   `get_alerts`: Fetches active weather alerts for a specified US state.

## How it Works

The project is structured as follows:
-   **[`weather.py`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/weather.py)**: The main entry point. It initializes and starts the MCP server, and registers the available tools.
-   **[`mcp_server/tools.py`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/mcp_server/tools.py)**: Defines the `list_tools` function to announce available tools and the `call_tool` function to handle incoming tool execution requests. It maps tool names to their corresponding implementation in the integration layer.
-   **[`mcp_server/integrations/weather_integration.py`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/mcp_server/integrations/weather_integration.py)**: Contains the core logic for interacting with the NWS API. It includes functions to fetch weather forecasts and alerts, and helper functions for making HTTP requests and formatting API responses.
-   **[`mcp_server/config.py`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/mcp_server/config.py)**: Manages application configuration. It loads settings from environment variables, which are typically defined in a [`.env`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/.env) file.
-   **[`.env`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/.env)**: Stores environment-specific configuration values, such as API endpoints and user agents. This file is not committed to version control.

## Configuration

Server configuration is handled by [`mcp_server/config.py`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/mcp_server/config.py). It loads values from an [`.env`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/.env) file located in the project root.

Create an [`.env`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/.env) file with the following content:
```
NWS_API_BASE="https://api.weather.gov"
USER_AGENT="your-application-name/1.0"
```
-   `NWS_API_BASE`: The base URL for the National Weather Service API.
-   `USER_AGENT`: The user agent string to be used for making API requests.

## Running the Server

To start the MCP server, run the main script from the project root:
```bash
uv run weather.py
```
The server will then listen for MCP requests on stdio.

## TODO

-   Implement a structured logger for improved debugging and monitoring.
-   Develop and integrate prompts in [`mcp_server/prompts.py`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/mcp_server/prompts.py).
-   Define and implement resources in [`mcp_server/resources.py`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/mcp_server/resources.py).
-   Correct the tool invocation in [`mcp_server/tools.py`](/Users/emanuelegurini/Documents/1_Projects/dev/mcp-notes/mcp_server/tools.py): the condition `elif name == "get_margin_leverage":` should likely be `elif name == "get_alerts":` to correctly call `weather_integration.get_alerts`.