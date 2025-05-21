# fhir-mcp-server

# 🏥 FHIR MCP Server (Patient Tools)

This project exposes FHIR **Patient resource operations** (CRUD + search) using [FastMCP](https://github.com/microsoft/mcp), making it easy to plug into multi-agent systems.

---

## 🚀 Features

* ✅ Retrieve a Patient by ID
* 🔍 Search Patients by parameters (e.g., name, gender)
* ➕ Create a Patient resource
* ✏️ Update existing Patient data
* ❌ Delete a Patient by ID

All operations use the public [HAPI FHIR R4 server](http://hapi.fhir.org/baseR4).

---

## 🧱 Requirements

* Python 3.9+
* `mcp` and `requests` libraries

### 🔧 Install dependencies

```bash
pip install mcp requests
```

---

## 📦 Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fhir-mcp-server.git
cd fhir-mcp-server
```

### 2. Run the server

```bash
python server.py
```

This starts the MCP server and exposes tools over standard I/O (`stdio`).

---

## 🧠 Available Tools

Each tool is callable from an MCP agent environment.

---

### 🔹 `get_patient(patient_id: str)`

Retrieve a FHIR Patient by ID.

```python
get_patient("example-patient-id")
```

---

### 🔹 `search_patients(params: dict)`

Search for Patients using query parameters.

Example:

```python
search_patients({"name": "John", "gender": "male"})
```

---

### 🔹 `create_patient(patient_data: dict)`

Create a new Patient resource.

Example:

```python
create_patient({
  "resourceType": "Patient",
  "name": [{ "given": ["Alice"], "family": "Smith" }],
  "gender": "female",
  "birthDate": "1990-01-01"
})
```

---

### 🔹 `update_patient(patient_id: str, patient_data: dict)`

Update an existing Patient record.

```python
update_patient("patient-id", {
  "resourceType": "Patient",
  "id": "patient-id",
  "name": [{ "given": ["Alice"], "family": "Smith" }],
  "gender": "female",
  "birthDate": "1990-01-01"
})
```

---

### 🔹 `delete_patient(patient_id: str)`

Delete a patient by ID.

```python
delete_patient("example-id")
```

---

## 🧪 Testing the API (Optional)

You can manually test endpoints using curl or Postman against the [HAPI FHIR server](http://hapi.fhir.org/baseR4/Patient).

---

## 🛠 Dev Notes

* `mcp.run(transport='stdio')` is ideal for agent-based usage.
* This uses `application/fhir+json` headers for full FHIR compatibility.
* Responses are raw JSON strings from the server.

---

## 📄 License

MIT – feel free to use and adapt.

