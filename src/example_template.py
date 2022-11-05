# -*- coding: utf-8 -*-
# @Time    : 04/11/2022 17:49
# @File    : example_template.py
from typing import Optional

from fastapi import FastAPI, Query, Path, HTTPException

app_template = FastAPI()


@app_template.get("/validate_query")
async def val_query(q: Optional[str] = Query(None, min_length=1,
                                             max_length=10)):
    result = {"value": "Hello!"}

    if q:
        result["value_updated"] = f"{result['value']} {q}"

    return q


@app_template.get("/retrieve_company/{company_id}")
async def ret_company(
        company_id: int = Path(...,
                               title="The id of the company to retrieve",
                               gt=0,
                               lt=10),
        company_name: str = None):
    return company_id, company_name


@app_template.get("/check_company_exists/{company_id}")
async def ret_company(company_id: int):
    if company_id not in list(range(100)):
        raise HTTPException(status_code=404, detail="Id do not exists")
    return company_id
