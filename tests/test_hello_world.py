# pytest-tutorial-part1/tests/test_hello_world.py
def test_myfirst_test() -> None:
    message = 'Hello World'
    print('This is a test print')
    assert message.lower() == 'hello world', "The message should equal hello world"