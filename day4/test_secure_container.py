from secure_container import check_adjacent_chars

def test_answer():
    assert check_adjacent_chars('111111') == True
    assert check_adjacent_chars('223450') == True
    assert check_adjacent_chars('123789') == False