# tests/test_users.py
import pytest
from utils.api_client import get, post
from jsonschema import validate, ValidationError
from schema.user_schema import user_schema
from utils.validator import validate_contract

def test_get_users_status(setup_teardown):
    response = get("/users")
    assert response.status_code == 200

def test_get_users_is_list(setup_teardown):
    response = get("/users")
    assert isinstance(response.json(), list)

def test_create_user_with_token(setup_teardown, auth_headers):
    payload = {"name": "Bharath", "job": "SDET"}
    response = post("/users", payload=payload, headers=auth_headers)
    assert response.status_code == 201

# def validate_user_contract(user, schema):
#     errors = []
#     try:
#         validate(instance=user, schema=schema)
#     except ValidationError as e:
#         errors.append(str(e.message))
#     return errors

def test_user_contract_validation(setup_teardown):
    response = get("/users")
    users = response.json()
    
    all_errors = []

    for user in users:
        errors = validate_contract(user, user_schema)
        all_errors.extend(errors)
    
    assert not all_errors, f"Schema errors found:\n{all_errors}"


@pytest.mark.parametrize("endpoint", [
    "/users",
    "/comments",
    "/posts"
])
def test_multiple_endpoint_status(setup_teardown, endpoint):
    response = get(endpoint)
    assert response.status_code == 200, f"{endpoint} endpoint failed with {response.status_code}"


@pytest.mark.parametrize(
    "name, job",
    [
        ("Bharath", "SDET"),
        ("Ravi", "QA"),
        ("Sneha", "Senior SDET")
    ]
)
def test_create_multiple_users_with_auth(auth_headers, name, job):
    payload = {
        "name": name,
        "job": job
    }
    response = post("/users", headers=auth_headers, payload=payload)
    assert response.status_code == 201, f"Users were not created"
    assert response.json().get("name") == name