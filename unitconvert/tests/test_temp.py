import pytest

from unitconvert.temperature import fahrenheit_to_celsius
from unitconvert.temperature import celsius_to_fahrenheit

def test_ftc():
    # some known results
    # 32 F is 0 C
    assert fahrenheit_to_celsius(32) == 0

    with pytest.raises(TypeError):
        fahrenheit_to_celsius(1, 2)

def test_ctf():
        # some known results
        # 32 F is 0 C
        assert celsius_to_fahrenheit(0) == 32

        with pytest.raises(TypeError):
            celsius_to_fahrenheit(1, 2)
