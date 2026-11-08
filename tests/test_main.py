from fastapi.testclient import TestClient

from src.main import app


def test_get_monologues():
    with TestClient(app) as client:
        response = client.get("/monologues")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "character": "Hamlet",
            "play": "Hamlet",
            "playwright": "William Shakespeare",
        }
    ]
    
def test_get_monologue_by_id():
    with TestClient(app) as client:
        response=client.get("/monologues/1")
    
    assert response.status_code==200
    assert response.json()["character"]=="Hamlet"

# with id that doesn't exist
def test_get_monologue_id_not_found():
    with TestClient(app) as client:
        response=client.get("/monologues/999")
    assert response.status_code==404

#invalid id, return 422 Unprocessable Content
#server understands but can't process due to invalid input
def test_get_monologue_invalid_id():
    with TestClient(app) as client:
        response = client.get("/monologues/abc")
    assert response.status_code==422