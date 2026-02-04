# from fastapi.testclient import TestClient
# from task.main import app
# import time

# client = TestClient(app)


# def test_ping():
#     for _ in range(5):
#         response = client.get("/ping")
#         assert response.status_code == 200

#     response = client.get("/ping")
#     assert response.status_code == 429


# def test_reset_window():
#     time.sleep(10)

#     response = client.get("/ping")
#     assert response.status_code == 200
