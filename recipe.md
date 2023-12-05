
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

Your test should assert that the new album is present in the list of records returned by GET /albums.

# following the recipe as before i will create artist

POST/artist

name = artist_name
genre = artist_genre

expected response 200 ok 

Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing


1. Extract nouns from the user stories or specification
album             
title
release_year
artist
id  

artist
name
genre

2. Infer the Table Name and Columns

albums             id, title, release_year, artist_id     

artist             id, name, genre

3. Decide the column types

id:SERIAL
title: text,
release_yea: int,
artist_id: int

id:SERIAL
name: text
genre: text

4. Write the SQL
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

CREATE TABLE artist (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# EXAMPLE

# POST/artist
    name : string
    genre: string

# GET/ albums


2. Create Examples as Tests
```python
# SCENARIO 1
# post/ artist
#name: Tool'
#genre: 'Rock
#expected response (200 ok)

(no contet)

#get/ artist
#expecte response (200 ok)

#Artist ('Tool', 'Rock')
#Artist ('Mastodon', 'Rock')


#SCENARIO 2

#POST/artist
#expected response (400 bad request)

#you need submit name and genre

#get/artist
#expected response (200 ok)

#Artist ('Tool', 'Rock')
#Artist ('Mastodon', 'Rock')
 ```





"""
3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'