from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..controllers.count_words_controller import count_words_controller


router = APIRouter(prefix="/word", responses={404: {"description": "Not found"}})


class CountWord(BaseModel):
    text: str


@router.post("/")
async def count_word(data: CountWord):
    number_words = count_words_controller(full_text=data.text)
    if not isinstance(number_words, int) and "error" in number_words:
        raise HTTPException(status_code=400, detail={ "message": number_words["error"] })
    return {"text": data.text, "number": number_words}
