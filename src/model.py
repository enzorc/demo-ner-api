# -*- coding: utf-8 -*-
# @Time    : 04/11/2022 14:49
# @File    : model.py
from flair.models import SequenceTagger


def load_models():
    # load tagger
    tagger_multi = SequenceTagger.load("flair/ner-multi")
    # tagger_english = SequenceTagger.load("flair/ner-english-fast")
    # tagger_french = SequenceTagger.load("flair/ner-french")
    return {
        "en": tagger_multi,
        "fr": tagger_multi
    }

