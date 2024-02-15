import queued

def test_queue():
    dmv = queued.Queue()
    dmv.push(1)
    dmv.pop()
    assert dmv.cards == []