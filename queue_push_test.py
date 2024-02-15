import main

def test_queue():
    dmv = main.Queue()
    dmv.push(1)
    dmv.push(2)
    dmv.push(3)
    assert dmv.cards == [1,2,3]