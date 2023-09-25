def test_passing():
    assert('home', 'work') == ('home', 'work')


def test_2_passing():
    assert not 'QA' == 'QC'


def test_3_passing():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
