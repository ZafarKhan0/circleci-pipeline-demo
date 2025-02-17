def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5

if __name__ == "__main__":
    print("Running Tests...")
    test_add()
    print("All tests passed!")
