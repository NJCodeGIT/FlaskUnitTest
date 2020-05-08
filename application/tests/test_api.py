
def test_index(client):
    result = client.get("/")
    assert result.status_code == 200


def test_failureCase(client):
    result = client.get("/failure")
    assert result.status_code == 200
