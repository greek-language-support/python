# Implementation of Greek Letters

# Copyright (C) 2025 Alexios Zavras
# SPDX-License-Identifier: LGPL-2.1-or-later


from .characters import GREEK_CHARACTERS, SPECIAL_GREEK_CHARACTERS

ALL_GREEK_CHARACTERS = {}

NAME_TO_CHAR = {n: uc for n, uc, _ in GREEK_CHARACTERS} | {n.lower(): lc for n, _, lc in GREEK_CHARACTERS}
CHAR_TO_NAME = {uc: n for n, uc, _ in GREEK_CHARACTERS} | {lc: n.lower() for n, _, lc in GREEK_CHARACTERS}
NAME_TO_CHAR |= {n: c for n, c in SPECIAL_GREEK_CHARACTERS}
CHAR_TO_NAME |= {c: n for n, c in SPECIAL_GREEK_CHARACTERS}

UPPER_TO_LOWER = {uc: lc for _, uc, lc in GREEK_CHARACTERS}
LOWER_TO_UPPER = {lc: uc for _, uc, lc in GREEK_CHARACTERS}
LOWER_TO_UPPER["ς"] = "Σ"


class InvalidGreekLetterOperationError(Exception):
    pass


def is_greek_char(c):
    return c in CHAR_TO_NAME


class GreekLetter:
    def __init__(self, c):
        self.char = c
        self.name = CHAR_TO_NAME.get(c, None)

    def upper(self):
        return LOWER_TO_UPPER.get(self.char, self.char)

    def lower(self):
        return UPPER_TO_LOWER.get(self.char, self.char)

    def is_lower(self):
        return self.char in UPPER_TO_LOWER.values()

    def is_upper(self):
        return self.char in LOWER_TO_UPPER.values()

    def has_diacritics(self):
        return "_" in self.name

    def has_accent(self):
        return "accent" in self.name

    def has_diaeresis(self):
        return "diaeresis" in self.name

    def add_accent(self):
        if self.has_accent():
            raise InvalidGreekLetterOperationError
        if self.has_diaeresis:
            n, d = self.name.split("_")
            n = n + "_accent_" + d
        else:
            n = self.name + "_accent"
        try:
            return NAME_TO_CHAR[n]
        except KeyError:
            raise InvalidGreekLetterOperationError from None

    def remove_accent(self):
        if not self.has_accent():
            raise InvalidGreekLetterOperationError
        try:
            n = self.name.replace("_accent", "")
            return NAME_TO_CHAR[n]
        except (AttributeError, KeyError):
            raise InvalidGreekLetterOperationError from None
