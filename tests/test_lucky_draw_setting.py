from main import client


def test_generate_lucky_draw_activity():
    response = client.post("/api/v1/generate-activity/")
    assert response.status_code == 200

