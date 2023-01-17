from fastapi import FastAPI, Path

app = FastAPI()


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
