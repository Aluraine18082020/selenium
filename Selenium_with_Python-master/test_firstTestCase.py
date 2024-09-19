from pytest import mark

def test_firstTest():
    assert True == False

@mark.regression
def test_secondTest():
    assert True == True

def test_thirdTest():
    assert "Hello !!!" == "Hello!!!"
