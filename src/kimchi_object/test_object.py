from src.kimchi_object.string import String


def test_string_hash_key():
    hello1 = String("Hello World")
    hello2 = String("Hello World")
    diff1 = String("My name is kimchi")
    diff2 = String("My name is kimchi")
    assert hello1.hash_key() == hello2.hash_key()
    assert diff1.hash_key() == diff2.hash_key()
    assert hello1.hash_key() != diff1.hash_key()
