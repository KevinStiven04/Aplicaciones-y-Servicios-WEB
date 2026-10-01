from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MedicionBase(BaseModel):
    estudiante_id: int
    variable: str
    valor: float
    unidad: str
    fecha_hora: datetime

class MedicionCreate(MedicionBase):
    pass

class MedicionUpdate(BaseModel):
    estudiante_id: int | None = None
    variable: str | None = None
    valor: float | None = None
    unidad: str | None = None
    fecha_hora: datetime | None = None

class MedicionResponse(MedicionBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
