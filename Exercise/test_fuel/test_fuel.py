from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(25) == '25%'
    assert gauge(75) == '75%'

def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_convert_ValueError():
    for str in ['cat', '4/3', 'three/four', '1.5/3']:
        with pytest.raises(ValueError):
            convert(str)

def test_convert():
    assert convert('3/4') == 75
    assert convert('1/4') == 25