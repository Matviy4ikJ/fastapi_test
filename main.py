from fastapi import FastAPI, Query, HTTPException
from typing import Union

app = FastAPI()

names_dict = {}
current_index = 0


@app.post("/add_name/")
def add_name(name: str):
    global current_index
    if name in names_dict.values():
        raise HTTPException(status_code=400, detail="Ім'я вже існує")
    names_dict[current_index] = name
    current_index += 1
    return {"message": f"Ім'я '{name}' додано"}


@app.get("/get_name/")
def get_names():
    return {"Всі ім'я": names_dict}


@app.delete("/delete_name/{index}")
def delete_name(index: int):
    if index not in names_dict:
        raise HTTPException(status_code=404, detail="таке ім'я не знайдено")
    del names_dict[index]
    return {"message": f"Ім'я з індексом '{index}' видалено"}


@app.get("/get_name_by_index/{index}")
def get_name_by_index(index: int):
    if index not in names_dict:
        raise HTTPException(status_code=404, detail="Index not found")
    return {"name": names_dict[index]}
