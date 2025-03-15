#!/usr/bin/env python
# -*- coding: utf-8 -*-


from modules.utils import encode_to_morse


def test_encode_to_morse():
    assert encode_to_morse("Hello World!") == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--"
