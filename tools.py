import requests

FHIR_BASE_URL = "http://hapi.fhir.org/baseR4"

def register_tools(mcp):
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

    @mcp.tool()
    def get_observation(observation_id: str) -> str:
        """Retrieve FHIR Observation resource by ID"""
        url = f"{FHIR_BASE_URL}/Observation/{observation_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Unable to fetch observation with ID {observation_id}. Status code: {response.status_code}"

    @mcp.tool()
    def search_observations(params: dict) -> str:
        """Search for FHIR Observation resources based on query parameters"""
        url = f"{FHIR_BASE_URL}/Observation"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Search failed. Status code: {response.status_code}"

    @mcp.tool()
    def create_observation(observation_data: dict) -> str:
        """Create a new FHIR Observation resource"""
        url = f"{FHIR_BASE_URL}/Observation"
        headers = {'Content-Type': 'application/fhir+json'}
        response = requests.post(url, headers=headers, json=observation_data)
        if response.status_code in [200, 201]:
            return response.text
        else:
            return f"Error: Creation failed. Status code: {response.status_code}"

    @mcp.tool()
    def update_observation(observation_id: str, observation_data: dict) -> str:
        """Update an existing FHIR Observation resource by ID"""
        url = f"{FHIR_BASE_URL}/Observation/{observation_id}"
        headers = {'Content-Type': 'application/fhir+json'}
        response = requests.put(url, headers=headers, json=observation_data)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Update failed for ID {observation_id}. Status code: {response.status_code}"

    @mcp.tool()
    def delete_observation(observation_id: str) -> str:
        """Delete a FHIR Observation resource by ID"""
        url = f"{FHIR_BASE_URL}/Observation/{observation_id}"
        response = requests.delete(url)
        if response.status_code == 204:
            return f"Observation with ID {observation_id} successfully deleted."
        else:
            return f"Error: Deletion failed for ID {observation_id}. Status code: {response.status_code}"
