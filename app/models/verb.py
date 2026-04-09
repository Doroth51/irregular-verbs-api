from pydantic import BaseModel


class Verb(BaseModel):
    id: int
    infinitif_en: str
    preterit: str
    participe_passe: str
    francais: str
    allemand: str
    espagnol: str
    italien: str
    portugais: str
    arabe: str
    chinois: str
