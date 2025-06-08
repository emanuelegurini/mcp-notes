"""
Configuration management for the MCP Server.
Handles environment variables and configuration settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

NWS_API_BASE = os.getenv("NWS_API_BASE")
USER_AGENT = os.getenv("USER_AGENT") 

# Server Configuration
SERVER_NAME = "weather-server"
SERVER_VERSION = "0.1.0"