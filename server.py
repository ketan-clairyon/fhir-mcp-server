from mcp.server.fastmcp import FastMCP
import requests
from mcp.server.fastmcp.prompts import base

# Initialize FastMCP server
mcp = FastMCP("fhir")

FHIR_BASE_URL = "http://hapi.fhir.org/baseR4"

@mcp.tool()
def get_patient(patient_id: str) -> str:
    """Retrieve FHIR Patient resource by ID"""
    url = f"{FHIR_BASE_URL}/Patient/{patient_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Unable to fetch patient with ID {patient_id}. Status code: {response.status_code}"

@mcp.tool()
def search_patients(params: dict) -> str:
    """Search for FHIR Patient resources based on query parameters"""
    url = f"{FHIR_BASE_URL}/Patient"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Search failed. Status code: {response.status_code}"

@mcp.tool()
def create_patient(patient_data: dict) -> str:
    """Create a new FHIR Patient resource"""
    url = f"{FHIR_BASE_URL}/Patient"
    headers = {'Content-Type': 'application/fhir+json'}
    response = requests.post(url, headers=headers, json=patient_data)
    if response.status_code in [200, 201]:
        return response.text
    else:
        return f"Error: Creation failed. Status code: {response.status_code}"

@mcp.tool()
def update_patient(patient_id: str, patient_data: dict) -> str:
    """Update an existing FHIR Patient resource by ID"""
    url = f"{FHIR_BASE_URL}/Patient/{patient_id}"
    headers = {'Content-Type': 'application/fhir+json'}
    response = requests.put(url, headers=headers, json=patient_data)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Update failed for ID {patient_id}. Status code: {response.status_code}"

@mcp.tool()
def delete_patient(patient_id: str) -> str:
    """Delete a FHIR Patient resource by ID"""
    url = f"{FHIR_BASE_URL}/Patient/{patient_id}"
    response = requests.delete(url)
    if response.status_code == 204:
        return f"Patient with ID {patient_id} successfully deleted."
    else:
        return f"Error: Deletion failed for ID {patient_id}. Status code: {response.status_code}"


@mcp.prompt()
def get_patient(patient_id: str) -> str:
    """Prompt to inquire about a patient's details."""
    return f"Please provide information about the patient with ID {patient_id}. Make sure to not reveal the name, but all other details."

@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"

@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    mcp.run(transport='stdio')
