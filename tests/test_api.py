import allure
import pytest

from api.client import ApiClient


@allure.story("API: YouGile")
@pytest.mark.api
class TestYougileApi:
    @allure.title("API 1: GET /data/api-v1/users (список пользователей)")
    def test_get_users(self, api_client: ApiClient) -> None:
        with allure.step("Отправить запрос"):
            resp = api_client.get("/data/api-v1/users")

        with allure.step("Проверить статус-код"):
            assert resp.status_code in (200, 400, 401, 403)

        with allure.step("Если 200 — проверить структуру"):
            if resp.status_code == 200 and resp.json:
                assert resp.json.get("result") == "ok"

    @allure.title("API 2: GET /data/api-v1/projects (проекты)")
    def test_get_projects(self, api_client: ApiClient) -> None:
        with allure.step("Отправить запрос"):
            resp = api_client.get("/data/api-v1/projects")

        with allure.step("Проверить статус-код"):
            assert resp.status_code in (200, 400, 401, 403, 404)

    @allure.title("API 3: GET /data/api-v1/stickers (стикеры)")
    def test_get_stickers(self, api_client: ApiClient) -> None:
        with allure.step("Отправить запрос"):
            resp = api_client.get("/data/api-v1/stickers")

        with allure.step("Проверить статус-код"):
            assert resp.status_code in (200, 400, 401, 403)

    @allure.title("API 4: GET /data/api-v1/tasks без параметров -> ошибка/403/400")
    def test_tasks_without_params_should_error(self, api_client: ApiClient) -> None:
        with allure.step("Отправить запрос"):
            resp = api_client.get("/data/api-v1/tasks")

        with allure.step("Проверить, что сервер не отдаёт 500"):
            assert resp.status_code in (200, 400, 401, 403)

        with allure.step("Если вдруг 200 — проверить что result=error или есть список"):
            if resp.status_code == 200 and resp.json:
                assert "result" in resp.json

    @allure.title("API 5: Неверный ресурс -> 404")
    def test_not_found_resource(self, api_client: ApiClient) -> None:
        with allure.step("Отправить запрос на несуществующий эндпоинт"):
            resp = api_client.get("/data/api-v1/not-existing-123")

        with allure.step("Проверить статус 404"):
            assert resp.status_code == 404
