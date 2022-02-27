from hello import hello

def test_hello():
    want = "Hello World"
    got = hello()

    assert want == got

