# Version 2.3.0

- Manually updating enum handling for CategoriesEnum

# Version 2.2.9

- Add PARTIALLY_SYNCED to SyncStatusEnum

# Version 2.2.7

- Add field_mappings to all common models

# Version 2.2.6

## Date: 2023-03-28

- Fix deserialization bug where expanded lists where incorrectly returning only the first item

# Version 2.2.5

## Date: 2023-01-31

- Remove invalid `MergePythonSDK.shared.model.remote_user` import from `ats/api/users_api.py`

# Version 2.2.4

## Date: 2022-11-2

- `integration_params` and `linked_account_params` properties have long been a part of our POST endpoints but were missing from HRIS, Accounting and Ticketing model definitions. They are now usable.
- New query params for Ticketing category list tickets endpoint and list user endpoints. See docs.merge.dev for a full list.
- BETA - selective sync is Merge's upcoming feature to limit the amount of data ingested by dynamically setting query params or request properties to integrations to filter before it reaches Merge. This feature is under active development but the initial models are in this version. Subject to (likely minor) change. Feature limited by plan, consult your customer success contact before using.

# Version 2.2.3

## Date: 2022-10-20

- Remove erroneous shared.model.remote_user import

# Version 2.2.2

## Date: 2022-09-30

- Fix paths for shared passthrough models
- Do not attempt to serialize empty lists as null objects
- Fix datetime() default breaking sync status endpoints
- Improve expands model attribute handling
- Remove date and datetime from Any type

# Version 2.2.1

## Date: 2022-09-23

- Fix erroneous expands parameters for models without corresponding attribute

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
