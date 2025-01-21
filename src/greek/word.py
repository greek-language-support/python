# Implementation of Greek Words

# Copyright (C) 2025 Alexios Zavras
# SPDX-License-Identifier: LGPL-2.1-or-later

from .letter import GreekLetter


class GreekWord:
    def __init__(self, word):
        self.letters = [GreekLetter(char) for char in word]

    def __str__(self):
        return "".join(letter.char for letter in self.letters)

    def upper(self):
        return "".join(letter.upper() for letter in self.letters)

    def lower(self):
        return "".join(letter.lower() for letter in self.letters)
