from um import count

def test_count():
    assert count("yummy") == 0
    assert count("Hello, um, world") == 1
    assert count("Um, um, um, um") == 4
    assert count("UM um uM Um") == 4
