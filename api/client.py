import requests


class ApiResponse:
    def __init__(self, response: requests.Response):
        self.status_code = response.status_code
        self.text = response.text
        try:
            self.json = response.json()
        except Exception:
            self.json = None


class ApiClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def get(self, path: str) -> ApiResponse:
        url = f"{self.base_url}{path}"
        r = requests.get(url, headers=self._headers(), timeout=20)
        return ApiResponse(r)
