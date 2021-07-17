from main import client


def test_generate_winner():
    response = client.post("/api/v1/generate-winner/?activity_id=9")
    assert response.status_code == 200

