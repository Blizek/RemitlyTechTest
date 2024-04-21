from check_resource import check_policy_resource

# unit test that returns False because given file doesn't exist
def test_file_doesnt_exist():
    assert check_policy_resource("tests/data.json") == False, "Should be False"

# unit test that returns False because given data is not a JSON
def test_wrong_file_type():
    assert check_policy_resource("tests/policy.txt") == False, "Should be False"

# unit test that returns False because JSON data misses required filed/fields
def test_missing_field():
    assert check_policy_resource("tests/missing.json") == False, "Should be False"

# unit test that returns False because JSON Resource field contains single asterisk
def test_single_asterisk():
    assert check_policy_resource("tests/asterisk.json") == False, "Should be False"

# unit test that returns True because JSON Resource field doesn't contain single asterisk
def test_not_single_asterisk():
    assert check_policy_resource("tests/not_asterisk.json") == True, "Should be True"

# unit test that return True because JSON Resource field is a list and contains non-asterisk data inside
def test_resource_list():
    assert check_policy_resource("tests/list.json") == True, "Should be True"


if __name__ == "__main__":
    test_file_doesnt_exist()
    test_wrong_file_type()
    test_missing_field()
    test_single_asterisk()
    test_not_single_asterisk()
    test_resource_list()
    print("All tests passed!")