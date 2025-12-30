from jsonschema import validate, ValidationError

def validate_contract(instance, schema):
    errors = []
    try:
        validate(instance=instance, schema=schema)
    except ValidationError as e:
        errors.append(e.message)
    return errors
