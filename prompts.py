def register_prompts(mcp):
    @mcp.prompt()
    def get_patient_prompt(patient_id: str) -> str:
        """Prompt to retrieve a FHIR Patient resource by ID"""
        return f"Retrieve the FHIR Patient resource with ID {patient_id}."

    @mcp.prompt()
    def search_patients_prompt(params: dict) -> str:
        """Prompt to search for FHIR Patient resources based on query parameters"""
        return f"Search for FHIR Patient resources with the following parameters: {params}."

    @mcp.prompt()
    def create_patient_prompt(patient_data: dict) -> str:
        """Prompt to create a new FHIR Patient resource"""
        return f"Create a new FHIR Patient resource with the following data: {patient_data}."

    @mcp.prompt()
    def update_patient_prompt(patient_id: str, patient_data: dict) -> str:
        """Prompt to update an existing FHIR Patient resource by ID"""
        return f"Update the FHIR Patient resource with ID {patient_id} using the following data: {patient_data}."

    @mcp.prompt()
    def delete_patient_prompt(patient_id: str) -> str:
        """Prompt to delete a FHIR Patient resource by ID"""
        return f"Delete the FHIR Patient resource with ID {patient_id}."

    @mcp.prompt()
    def get_observation_prompt(observation_id: str) -> str:
        """Prompt to retrieve a FHIR Observation resource by ID"""
        return f"Retrieve the FHIR Observation resource with ID {observation_id}."

    @mcp.prompt()
    def search_observations_prompt(params: dict) -> str:
        """Prompt to search for FHIR Observation resources based on query parameters"""
        return f"Search for FHIR Observation resources with the following parameters: {params}."

    @mcp.prompt()
    def create_observation_prompt(observation_data: dict) -> str:
        """Prompt to create a new FHIR Observation resource"""
        return f"Create a new FHIR Observation resource with the following data: {observation_data}."

    @mcp.prompt()
    def update_observation_prompt(observation_id: str, observation_data: dict) -> str:
        """Prompt to update an existing FHIR Observation resource by ID"""
        return f"Update the FHIR Observation resource with ID {observation_id} using the following data: {observation_data}."

    @mcp.prompt()
    def delete_observation_prompt(observation_id: str) -> str:
        """Prompt to delete a FHIR Observation resource by ID"""
        return f"Delete the FHIR Observation resource with ID {observation_id}."
