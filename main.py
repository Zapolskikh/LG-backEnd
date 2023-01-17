from fastapi import FastAPI, Path
from words_game import get_word
app = FastAPI()

data = []

word_obj = {
    1: {
        "language": "English",
        "value": "Apple",
        "difficult": "Easy"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path()):
    return word_obj[item_id]


@app.get("/get-by-value")
def get_item(value: str):
    for item_id in word_obj:
        if word_obj[item_id]["value"] == value:
            return word_obj[item_id]
    return {"Word": "Not found"}


@app.post("/create_item")
def create_item(language: str, value: str, difficult: str):
    data.append({
        "language": language,
        "value": value,
        "difficult": difficult
    })
 
    return {
        "language": language,
        "value": value,
        "difficult": difficult
    }

@app.get("/data")
def get_data():
    return data

@app.get("/get-word")
def get_word_from_db(word,source_language,dest_language):
    return get_word(word,source_language,dest_language)
