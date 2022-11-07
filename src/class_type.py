# -*- coding: utf-8 -*-
# @Time    : 04/11/2022 10:42
# @File    : class_type.py
from enum import Enum
from typing import List

from pydantic import BaseModel


class NerInput(BaseModel):
    text: str
    language: str


class NerEntity(BaseModel):
    label: str
    entity: str
    start: int
    end: int


class NerOutput(BaseModel):
    entities: List[NerEntity]
    anonymize_text: str


class NerModelLanguage(str, Enum):
    fr = "fr"
    en = "en"
