def test_checkName():
    assert "varun" == "Varun"

def test_checkLastName():
    assert "Bajpai" == "Bajpai"

# Commands for running test
#   1. pytest -v { Verbose Mode } => It provides detailed results of each test case
#   2. pytest -m marker { Marker Mode } => To run specific test cases tagged under a marker
#   3. pytest -k "test_cases" => Run test cases having substring => "test_cases"
#   4. pytest -m regression -v
