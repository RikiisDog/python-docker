from myproject.src.my_module import double_number


def test_double_number():
    """double_number関数をテストするための関数です"""
    assert double_number(2) == 4
    assert double_number(0) == 0
    assert double_number(-1) == -2
