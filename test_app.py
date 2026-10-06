from appy_v2 import app, calls


def test_duplicate_call_does_not_create_second_record():
    calls.clear()

    client = app.test_client()

    data = {
        "call_id": "TEST123",
        "status": "answered",
        "duration_secs": 42
    }

    response1 = client.post("/call-ended", json=data)
    response2 = client.post("/call-ended", json=data)

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert len(calls) == 1