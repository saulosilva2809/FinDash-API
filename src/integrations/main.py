from excel.formater_json import pretty_json
from excel.repositories.commercials_repository import CommercialsRepository


pretty_json(CommercialsRepository().response())
