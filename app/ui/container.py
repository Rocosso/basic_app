from dependency_injector import containers, providers
from app.services.aws_s3_service import AWSS3Service
from app.services.csv_service import CSVService
from app.core.config_loader import ConfigLoader
from app.core.use_cases import TankUseCase
from app.core.repository_interface import RepositoryInterface
from app.ui.controllers import TankController


class LocalRepository(RepositoryInterface):
    def __init__(self, csv_service: CSVService):
        self.csv_service = csv_service

    def get_tank_status(self):
        return self.csv_service.read_tank_status()

    def update_tank_status(self, tank_status):
        self.csv_service.write_tank_status(tank_status)


class CloudRepository(RepositoryInterface):
    def __init__(self, csv_service: CSVService, s3_service: AWSS3Service):
        self.csv_service = csv_service
        self.s3_service = s3_service

    def get_tank_status(self):
        return self.csv_service.read_tank_status()

    def update_tank_status(self, tank_status):
        self.csv_service.write_tank_status(tank_status)
        self.s3_service.upload_file(self.csv_service.file_path, "water_usage_data.csv")


class AppContainer(containers.DeclarativeContainer):
    # Carga la configuración desde config.json
    config = providers.Singleton(lambda: ConfigLoader(config_file="config.json"))

    # Servicios
    s3_service = providers.Singleton(
        AWSS3Service,
        access_key=config().get("aws_access_key", ""),
        secret_key=config().get("aws_secret_key", ""),
        bucket_name=config().get("aws_bucket_name", "")
    )
    csv_service = providers.Singleton(
        CSVService, file_path=config().get("csv_file_path", "water_usage_data.csv")
    )

    # Repositorio dinámico basado en sicall_cloud_active
    def repository_factory(config: ConfigLoader, csv_service: CSVService, s3_service: AWSS3Service):
        if config.get("sicall_cloud_active", False):
            return CloudRepository(csv_service=csv_service, s3_service=s3_service)
        return LocalRepository(csv_service=csv_service)

    repository = providers.Factory(
        repository_factory,
        config=config.provided,
        csv_service=csv_service.provided,
        s3_service=s3_service.provided
    )

    # Caso de uso y controlador
    use_case = providers.Factory(TankUseCase, repository=repository)
    controller = providers.Factory(TankController, tank_use_case=use_case)
