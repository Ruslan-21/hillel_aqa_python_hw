


def test_triagle():

    assert 2 == 2

    def test_reverse_string_positive():
        my_string = "Hello"
        result = reverse_string(my_string)
        assert "olleH"

    def test_reverse_string_negative():
        my_string = "Hello"
        result = reverse_string(my_string)
        assert "Hello"