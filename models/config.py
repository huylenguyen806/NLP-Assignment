from __future__ import absolute_import

pos_tags = {
    "A": "adjective",
    "C": "coordinating_conjunction",
    "E": "preposition",
    "I": "interjection",
    "L": "determiner",
    "M": "numeral",
    "N": "common_noun",
    "Nc": "noun_classifier",
    "Ny": "noun_abbreviation",
    "Np": "proper_noun",
    "Nu": "unit_noun",
    "P": "pronoun",
    "R": "adverb",
    "S": "subordinating conjunction",
    "T": "auxiliary",
    "V": "verb",
    "X": "unknown",
    "F": "punctuation",
    "ROOT": "ROOT"
}

name_to_pos = {v: k for k, v in pos_tags.items()}

dep_relations = {
    "common_noun+adjective": "amod",
    "common_noun+verb": "nsubj",
    "verb+common_noun": "dobj",
    "common_noun+proper_noun": "nmod",
    "preposition+common_noun": "pobj",
    "common_noun+numeral": "nummod",
    "common_noun+noun_abbreviation": "nmod",
    "common_noun+pronoun": "nmod"
}
