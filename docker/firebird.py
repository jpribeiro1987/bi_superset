from superset.db_engine_specs.base import BaseEngineSpec
from sqlalchemy.engine.reflection import Inspector

class FirebirdEngineSpec(BaseEngineSpec):
    engine = "firebird"
    engine_name = "Firebird"

    @classmethod
    def get_schema_names(cls, inspector: Inspector) -> set[str]:
        return {""}

