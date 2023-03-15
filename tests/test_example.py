import pytest
from mypackage import mymodule


@pytest.fixture
def doc_string() -> str:
    """Software test fixtures initialize test functions. They provide a fixed
    baseline so that tests execute reliably and produce consistent, repeatable,
    results. Initialization may setup services, state, or other operating
    environments. These are accessed by test functions through arguments;
    for each fixture used by a test function there is typically a parameter
    (named after the fixture) in the test function's definition."""
    doc_string = """Hello World!"""
    return doc_string


def test_from_string(doc_string):
    ex = mymodule.MyClass()
    assert ex.public_method(word=doc_string) is "Hello World!"


def test_sample_class():
    ex = mymodule.MyClass()
    assert ex.public_method() is "wuff"


# Run multiple test without even when the first tests fail.
# Specify test cases and use them in a single test funciton.
@pytest.mark.parametrize("test_input, expected", [
    ("Hi", "Hi"),
    ("HI", "HI"),
    ("", ""),
    ("Test case c", "Test case c"),
])
# Single test function using multiple test cases.
def test_multi_publics(test_input, expected):
    ex = mymodule.MyClass()
    assert ex.public_method(word=test_input) is expected


@pytest.mark.skip(reason="regexes not supported yet")
def test_regex_slaps():
    ex = mymodule.MyClass()
    assert ex.public_method(word='[ld]*ddl') is ""


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


#def test_invalid_slap():
#    with pytest.raises(ValueError):
#        ex = mymodule.MyClass()
#        ex.public_method() ...


@pytest.mark.xfail
def test_db_slap(db_conn):
    db_conn.read_slaps()
    assert ...


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
