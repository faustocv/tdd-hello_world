from hello import hello

def test_hello_without_name():
    want = "Hello, World!"
    got = hello()

    assert want == got

def test_hello_with_name():
    want = "Hello, Douglas!"
    got = hello("Douglas")

    assert want == got
