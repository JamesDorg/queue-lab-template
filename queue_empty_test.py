import main

def test_queue():
    dmv = main.Queue()
    dmv.push(1)
    dmv.pop()
    assert dmv.cards == []