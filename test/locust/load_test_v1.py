from locust import HttpUser, task, between


class MemberRetrieveUser(HttpUser):
    """
    /member API 성능 테스트용 Locust 스크립트
    """

    # 유저별 요청 간 대기 시간
    wait_time = between(0.5, 2)

    def on_start(self):
        """
        초기화 핸들러 (필요 시 헤더 설정 가능)
        """
        self.headers = {
            "Content-Type": "application/json"
        }

    @task
    def get_member(self):
        """
        GET /member API 호출
        """
        with self.client.get(
            "/member",
            headers=self.headers,
            name="GET /member",
            catch_response=True
        ) as response:

            # 응답 검증
            if response.status_code != 200:
                response.failure(f"Status Error: {response.status_code}")
                return

            # JSON 구조 검증
            try:
                data = response.json()
            except Exception as e:
                response.failure(f"JSON Parse Error: {e}")
                return

            # 응답 포맷 검증 (ResponseBaseModel 가정)
            if "data" not in data:
                response.failure("Invalid Response Format: 'data' missing")
                return

            response.success()
