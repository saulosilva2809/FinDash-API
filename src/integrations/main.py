from excel.formater_json import pretty_json
from excel.repositories.kpis_repository import KpisRepository


pretty_json(KpisRepository().response())
