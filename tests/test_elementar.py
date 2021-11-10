import requests

def soma():
    res =  requests.get("http://localhost:5004/api_gateway/soma?arg1=5&arg2=5")
    resultJson = res.json()
    return resultJson['result']

def test_function_soma():
    assert soma() == 10