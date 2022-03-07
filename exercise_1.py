
import requests

url = 'http://api.zippopotam.us/us/90210'

# Exercise 1.1: GET request to url, Check response status code equals 200
def test_get_req_200():
    response_1 = requests.get(url)
    assert response_1.status_code == 200

# Exercise 1.2: GET request to url
# Check that the value of the response header 'Content-Type' equals 'application/json'
def test_get_content_type():
    response_2 = requests.get(url)
    assert response_2.headers['Content-Type'] == 'application/json'

# Exercise 1.3: GET request to http://api.zippopotam.us/us/90210
# Check that the value of the response body encoding is not set (equal to None).
def test_get_resp_encode():
    response_3 = requests.get(url)
    assert response_3.encoding == 'utf-8'

# Exercise 1.4: GET request to http://api.zippopotam.us/us/90210
# Check that the value of the response body element 'country' has a value equal to 'United States'.
def test_get_json_body_element():
    response_4 = requests.get(url)
    response_body_1 = response_4.json()
    assert response_body_1['country'] == 'United States'

# Exercise 1.5: GET request to http://api.zippopotam.us/us/90210
# Check that the first 'place name' element in the list of places has a value equal to 'Beverly Hills'.
def test_get_first_elem():
    response_5 = requests.get(url)
    response_body_2 = response_5.json()
    assert response_body_2['places'][0]['place name'] == 'Beverly Hills'

# Exercise 1.6: GET request to http://api.zippopotam.us/us/90210
# check that the response of the body element 'places' has an array value with a length of 1.
def test_get_size_array():
    response_6 = requests.get(url)
    response_body_3 = response_6.json()
    assert len(response_body_3['places']) == 1
