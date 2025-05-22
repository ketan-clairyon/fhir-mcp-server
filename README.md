# FHIR MCP Server

This repository provides a Model Context Protocol (MCP) server implementation for interacting with FHIR Patient and Observation resources. Built using the FastMCP framework, it facilitates seamless integration with AI models like Claude via MCP.

## Features

* **FHIR Resource Management**: Retrieve, search, create, update, and delete FHIR Patient and Observation resources.
* **MCP Integration**: Exposes tools and prompts for AI models to interact with FHIR data.
* **FastMCP Framework**: Utilizes decorators for concise and readable code.
* **Transport Options**: Supports both STDIO and HTTP(S) transports for flexibility.

## Setup

### Clone the Repository

```bash
git clone git@github.com:ketan-clairyon/fhir-mcp-server.git
cd fhir-mcp-server
```

### Install Dependencies

Using the UV package manager:

```bash
uv add "mcp[cli]"
uv add requests
```

## Development

Run the server locally in development mode:

```bash
uv run mcp dev server.py
```

## Usage with Claude Desktop

To integrate this server with Claude Desktop:

```bash
uv run mcp install server.py
```

This command adds the MCP server to your Claude Desktop configuration for easy access.

## Server Details

The server exposes the following MCP tools:

* `get_patient(patient_id: str) -> str`: Retrieve a patient by ID.
* `search_patients(params: dict) -> str`: Search patients with query parameters.
* `create_patient(patient_data: dict) -> str`: Create a new patient record.
* `update_patient(patient_id: str, patient_data: dict) -> str`: Update an existing patient.
* `delete_patient(patient_id: str) -> str`: Delete a patient by ID.
* `get_observation(observation_id: str) -> str`: Retrieve an observation by ID.
* `search_observations(params: dict) -> str`: Search observations with query parameters.
* `create_observation(observation_data: dict) -> str`: Create a new observation record.
* `update_observation(observation_id: str, observation_data: dict) -> str`: Update an existing observation.
* `delete_observation(observation_id: str) -> str`: Delete an observation by ID.

## Requirements

* Python 3.8+
* `requests` library
* `mcp` package with CLI support

## Notes

* Ensure your virtual environment is activated when running commands.
* The server communicates via STDIO or HTTP(S) transport, as configured.
* For production deployments, consider securing the server with HTTPS and implementing authentication mechanisms.

