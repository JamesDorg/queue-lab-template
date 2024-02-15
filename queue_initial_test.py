import queued

def test_queue():
    dmv = queued.Queue()
    assert dmv.cards == []