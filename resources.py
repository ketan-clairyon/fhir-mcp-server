
def register_resources(mcp):
    @mcp.resource("docs://observation-guide")
    def observation_guide() -> str:
        """Provide a guide on how to use Observation tools"""
        return """
        Observation Tools Guide:
        - Use 'get_observation' to retrieve an observation by ID.
        - Use 'search_observations' with parameters like patient ID, code, or date.
        - Use 'create_observation' to add a new observation.
        - Use 'update_observation' to modify an existing observation.
        - Use 'delete_observation' to remove an observation by ID.
        """
    @mcp.resource("docs://patient-guide")
    def patient_guide() -> str:
        """Provide a guide on how to use Patient tools"""
        return """
        Patient Tools Guide:
        - Use 'get_patient' to retrieve a patient's details by ID.
        - Use 'search_patients' with parameters like name, gender, or birth date.
        - Use 'create_patient' to add a new patient record.
        - Use 'update_patient' to modify an existing patient's information.
        - Use 'delete_patient' to remove a patient record by ID.
        """
