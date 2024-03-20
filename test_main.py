import json
from main import app


def test_new_quote_endpoint():
    client = app.test_client()

    # Make a request to the /new_quote endpoint
    response = client.get("/new_quote")

    # Check if the response has a 200 status code
    assert response.status_code == 200

    # Parse the JSON response
    data = json.loads(response.get_data(as_text=True))

    # Check if the expected keys are present in the JSON response
    assert "quote" in data
    assert "author" in data
