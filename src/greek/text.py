# Implementation of Greek Texts

# Copyright (C) 2025 Alexios Zavras
# SPDX-License-Identifier: LGPL-2.1-or-later

from .letter import is_greek_char
from .word import GreekWord


class GreekText:
    def __init__(self, text):
        self.elements = self.tokenize(text)


    def __str__(self):
        return "".join(str(e) for e in self.elements)
# return "".join(str(element) if isinstance(element, GreekWord) else element for element in self.elements)


    def upper(self):
        return "".join(e.upper() for e in self.elements)


    def lower(self):
        return "".join(e.lower() for e in self.elements)

    @staticmethod
    def tokenize(text):
        if not text:
            return []

        elements = []
        word = ""
        current_state = None
        for c in text:
            char_state = is_greek_char(c)
            if current_state is None:
                word += c
                current_state = char_state
            elif char_state == current_state:
                word += c
            else:
                if char_state:
                    elements.append(GreekWord(word))
                else:
                    elements.append(word)
                word = c
                current_state = char_state
        if char_state:
            elements.append(GreekWord(word))
        else:
            elements.append(word)
        return elements
