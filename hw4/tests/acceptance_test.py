import pytest
from server import app

@pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (5, -4, 1), (7, 8, 15)])
def test_sum_handler(a: int, b: int, expected: int) -> None:
    with app.test_client() as client:
        response = client.get(f'/sum?a={a}&b={b}')
        assert response.status_code == 200

        data = response.get_json()
        assert data["sum"] == expected
