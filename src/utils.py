# -*- coding: utf-8 -*-
# @Time    : 04/11/2022 14:49
# @File    : utils.py

from copy import deepcopy


def anonymize_text_flair_ner(text, sentence):
    # anonymize_text:
    text_tmp = list(deepcopy(text))

    for ent in sentence.get_spans('ner'):
        start = ent.start_position
        end = ent.end_position
        text_tmp[start:end] = "X" * (end - start)

    return "".join(text_tmp)


def parse_result_flair_ner(sentence):
    # return results
    results = [
        {
            "label": ent.tag,
            "entity": ent.text,
            "start": ent.start_position,
            "end": ent.end_position,

        }
        for ent in sentence.get_spans('ner')
    ]
    print(results)
    return results
