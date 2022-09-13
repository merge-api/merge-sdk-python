# Version 2.2.0

## Date: 2022-09-12

- Fix Enum serialization
- Fix bug in pypi setup causing installer to not find model files

# Version 2.1.0

## Date: 2022-08-29

- Add type hints 
  - Mypy type hints for model attributes
- Expands
  - APIs now support `expand` request query parameter
  - Expanded models are type checked and cast, attributes can be 
    accessed as a normal model

```python
from MergePythonSDK.shared import Configuration, ApiClient
from MergePythonSDK.hris.api.employees_api import EmployeesApi

configuration = Configuration()
configuration.access_token = "YOUR_API_KEY_HERE"
configuration.api_key_prefix['tokenAuth'] = 'Bearer'
configuration.api_key['accountTokenAuth'] = 'YOUR_X_ACCOUNT_TOKEN_HERE'
with ApiClient(configuration) as api_client:
    hris_employees_api_instance = EmployeesApi(api_client)
    try:
        # Test expands
        _id = "YOUR_EMPLOYEE_ID_HERE"
        employee_expands = hris_employees_api_instance.employees_retrieve(
          _id, expand="employments"
        )
        assert employee_expands.employments.employee == employee_expands.id
```
  
# Version 2.0.0

## Date: 2022-08-23

- Initial commit of the Merge Python SDK 
  - /merge-api/merge-sdk-python in github
  - MergePythonSDK in package naming
- Includes all Merge categories in one package
  - Accounting
  - ATS (applicant Tracking Systems)
  - CRM (Customer Relationship Management)
  - HRIS (Human Resource Information Systems)
  - Ticketing 
