user_schema = {
    "type": "object",
    "required": ["id", "name", "email", "address", "company"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "address": {
            "type": "object",
            "required": ["city"],
            "properties": {
                "city": {"type": "string"}
            }
        },
        "company": {
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string"}
            }
        }
    }
}
