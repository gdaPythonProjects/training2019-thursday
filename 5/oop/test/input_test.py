from unittest import TestCase

from managers.input import Input


class InputTest(TestCase):
    def test_constructor_none_a_b(self):
        x = Input()
        assert x.a is None and x.b is None, "A and B in class should be None after init"
