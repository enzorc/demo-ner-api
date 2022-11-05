# -*- coding: utf-8 -*-
# @Time    : 04/11/2022 10:31
# @File    : app.py
from typing import Optional

from fastapi import FastAPI, Query, Path, HTTPException
from flair.data import Sentence

from src.class_type import NerInput, NerOutput
from src.model import load_models
from src.utils import parse_result_flair_ner, anonymize_text_flair_ner

app_api = FastAPI()
models = load_models()


@app_api.get("/")
async def root():
    return {"message": "Hello World"}


@app_api.post("/ner", response_model=NerOutput)
async def apply_ner(user_input: NerInput):
    text = user_input.text
    lang = user_input.language

    if lang in ["fr", "en"]:
        # make sentence
        sentence = Sentence(text)
        # predict NER tags
        models[lang].predict(sentence)

        # parse results
        results = parse_result_flair_ner(sentence)
        anonymize_text = anonymize_text_flair_ner(text, sentence)

        return {
            "entities": results,
            "anonymize_text": anonymize_text
        }

    else:
        raise HTTPException(status_code=404,
                            detail=f"Use lang 'en' or 'fr' not {lang}")
