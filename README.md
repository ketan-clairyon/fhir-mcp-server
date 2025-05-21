# FHIR MCP Server

This repository contains a Model Context Protocol (MCP) server implementation for interacting with FHIR Patient resources using the FastMCP framework.

## Features

- Retrieve, search, create, update, and delete FHIR Patient resources via the public FHIR API.
- Integrated MCP tools for streamlined interactions.
- Prompt functions for patient inquiries, code reviews, and debugging assistance.
- Uses the `requests` library for HTTP requests.
- Designed to work with Claude Desktop via MCP.

## Setup

### Clone the repository

```bash
git clone git@github.com:ketan-clairyon/fhir-mcp-server.git
cd fhir-mcp-server
````

### Install dependencies

Using UV package manager:

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

This will add the MCP server to your Claude Desktop configuration for easy access.

## Server Details

The server exposes the following MCP tools:

* `get_patient(patient_id: str) -> str`: Retrieve a patient by ID.
* `search_patients(params: dict) -> str`: Search patients with query parameters.
* `create_patient(patient_data: dict) -> str`: Create a new patient record.
* `update_patient(patient_id: str, patient_data: dict) -> str`: Update an existing patient.
* `delete_patient(patient_id: str) -> str`: Delete a patient by ID.

It also defines prompts for:

* Patient information requests.
* Code review.
* Debugging assistance.

## Requirements

* Python 3.8+
* `requests` library
* `mcp` package with CLI support

## Notes

* Ensure your virtual environment is activated when running commands.
* The server communicates via stdio transport.