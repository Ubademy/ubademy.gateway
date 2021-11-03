from app.service_caller import ServiceCaller


class Parser:
    @staticmethod
    def get_service_caller(url: str) -> ServiceCaller:
        return ServiceCaller(
            service_url=url,
        )
