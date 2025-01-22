from hexlet_pytest.example import reverse

def test_reverse():
    assert reverse('Hello') == 'olleH'


def test_reverse_with_empty_string():
    assert reverse('') == ''