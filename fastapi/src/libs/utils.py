def make_response(result: str) -> dict:
    return {
        "meta": {
            "code": 200,
            "message": "OK"
        },
        "data": str(result)
    }
