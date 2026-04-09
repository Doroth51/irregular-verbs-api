from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Verb
from app.utils.loader import load_verbs

router = APIRouter(prefix="/verbs", tags=["verbs"])

verbs_data = load_verbs()


@router.get("/list", response_model=List[Verb])
def get_all_verbs():
    return verbs_data


@router.get("/list/{ids}", response_model=List[Verb])
def get_list_verb_by_id(ids: str):
    ids_list = ids.split("-")
    verbs_list = []
    for verb in verbs_data:
        if verb["id"] in ids_list:
            verbs_list.append(verb)
    return verbs_list


@router.get("/id/{verb_id}")
def get_verb_by_id(verb_id: int):
    for verb in verbs_data:
        if int(verb["id"]) == verb_id:
            return verb
    raise HTTPException(status_code=404, detail="Verb not found")


@router.get("/infinitif/{infinitive}", response_model=Verb)
def get_verb(infinitive: str):
    for verb in verbs_data:
        if verb["infinitif_en"].lower() == infinitive.lower():
            return verb
    raise HTTPException(status_code=404, detail="Verb not found")
