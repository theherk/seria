from seria.utils import str_to_num, set_defaults
import pytest


class TestSeriaUtils(object):
    # def test_set_default_add(self):
    # kwargs = {"arg1": True}
    #         defaults = {"arg2": True}
    #         combined = dict(kwargs.items() + defaults.items())
    #         set_defaults(kwargs, defaults)
    #         assert kwargs == combined
    #
    def test_set_default_dont_overide(self):
        kwargs = {"arg1": False}
        defaults = {"arg1": True}
        set_defaults(kwargs, defaults)
        assert kwargs == {"arg1": False}


class TestSeriaUtilsStrToNum(object):
    def test_00(self):
        """int input, exact_match=False
        """
        _in = 123
        _expected_out_type = int
        _exact_match = False
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == _in

    def test_01(self):
        """int input, exact_match=True
        """
        _in = 123
        _expected_out_type = int
        _exact_match = True
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == _in

    def test_02(self):
        """float input
        """
        _in = 123.124
        _expected_out_type = float
        _exact_match = False
        _out = str_to_num(_in, exact_match=_exact_match)

        assert isinstance(_out, _expected_out_type)
        assert _out == _in

    def test_04(self):
        """str input (all ints) with leading zero
        """
        _in = "0123"
        _exact_match = True
        _expected_out_type = str
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == "0123"

    def test_05(self):
        """str input (all ints) with leading zero, exact_match=False
        """
        _in = "0123"
        _exact_match = False
        _expected_out_type = int
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == 123

    def test_06(self):
        """str input (all ints) with leading zero, exact_match=True
        """
        _in = "0123"
        _exact_match = True
        _expected_out_type = str
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == "0123"

    def test_07(self):
        """str input (represents a float) with zero decimal, exact_match=False
        """
        _in = "1.0"
        _exact_match = False
        _expected_out_type = float
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == 1.0

    def test_08(self):
        """str input (represents a float) with non zero decimal, exact_match=False
        """
        _in = "1.1"
        _exact_match = False
        _expected_out_type = float
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == 1.1

    def test_09(self):
        """str input (represents a float) with non zero decimal, exact_match=True
        """
        _in = "1.1"
        _exact_match = True
        _expected_out_type = float
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == 1.1

    def test_10(self):
        """str input (represents a float) with non zero decimal and trailing zero, exact_match=False
        """
        _in = "1.10"
        _exact_match = False
        _expected_out_type = float
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == 1.1

    def test_11(self):
        """str input (represents a float) with non zero decimal and trailing zero, exact_match=True
        """
        _in = "1.10"
        _exact_match = True
        _expected_out_type = str
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == "1.10"


    def test_12(self):
        """str input (represents a float) with leading zero, with non zero decimal and trailing zero, exact_match=False
        """
        _in = "01.10"
        _exact_match = False
        _expected_out_type = float
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == 1.1

    def test_13(self):
        """str input (represents a float) with leading zero, with non zero decimal and trailing zero, exact_match=True
        """
        _in = "01.10"
        _exact_match = True
        _expected_out_type = str
        _out = str_to_num(_in, exact_match=_exact_match)
        assert isinstance(_out, _expected_out_type)
        assert _out == "01.10"


    def test_14(self):
        """list input, exact_match=True

        """
        _in = ['str_list_item', 123]
        _expected_out_type = list
        _out = str_to_num(_in)
        assert isinstance(_out, _expected_out_type)
        assert _out == _in


    def test_15(self):
        """list input, exact_match=True

        """
        _in = ['str_list_item', 123]
        _expected_out_type = list
        _out = str_to_num(_in)
        assert isinstance(_out, _expected_out_type)
        assert _out == _in