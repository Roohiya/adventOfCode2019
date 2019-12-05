from secure_container_2 import check_adjacent_chars

def test_answer():
    assert check_adjacent_chars('111111') == False
    assert check_adjacent_chars('111122') == True
    assert check_adjacent_chars('123444') == False
    assert check_adjacent_chars('344445') == False
    assert check_adjacent_chars('344444') == False
    assert check_adjacent_chars('112233') == True