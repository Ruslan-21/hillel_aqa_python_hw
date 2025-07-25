import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler("test_search.log", mode='w', encoding='utf-8')
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200
    token = response.json().get("access_token")
    assert token is not None

    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by,limit", [
        ("price", 3),
        ("year", 5),
        ("engine_volume", 4),
        ("brand", 2),
        ("", 6),
        ("year", 0),
        ("price", 100)
    ])
    def test_car_search(self, auth_session, sort_by, limit):
        url = f"{BASE_URL}/cars"
        params = {
            "sort_by": sort_by,
            "limit": limit
        }
        response = auth_session.get(url=url, params=params)
        logger.info(f"GET /cars | sort_by={sort_by} | limit={limit} | status={response.status_code}")
        assert response.status_code == 200

        data = response.json()

        if limit > 0:
            assert len(data) <= limit

        if sort_by:
            values = [item[sort_by] for item in data]
            assert values == sorted(values), f"{sort_by}"

        logger.info(f"Тест виконано: sort_by={sort_by}, limit={limit}")