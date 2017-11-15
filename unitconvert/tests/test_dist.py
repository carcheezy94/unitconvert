import pytest

from unitconvert.distance import miles_to_kilometers
from unitconvert.distance import kilometers_to_miles

def test_mtk():
    # some known results
    # 0 km = 0 mi
    assert miles_to_kilometers(0) == 0

    with pytest.raises(TypeError):
        miles_to_kilometers(1,2)

def test_ktm():
    # some known results
    # 0 km = 0 mi
    assert kilometers_to_miles(0) == 0

    with pytest.raises(TypeError):
        kilometers_to_miles(1,2)
