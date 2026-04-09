from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Verb
from app.utils.loader import load_verbs

router = APIRouter(prefix="/verbs", tags=["verbs"])

verbs_data = load_verbs()


@router.get("/", response_model=List[Verb])
def get_all_verbs():
    return verbs_data


@router.get("/{infinitive}", response_model=Verb)
def get_verb(infinitive: str):
    for verb in verbs_data:
        if verb["infinitif_en"].lower() == infinitive.lower():
            return verb
    raise HTTPException(status_code=404, detail="Verb not found")
