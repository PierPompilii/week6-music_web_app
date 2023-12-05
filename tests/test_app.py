# Tests for your routes go here

# SCENARIO 1
# post/ albums 
#title: '10000 Wings'
#release_year: 2006
#artist_id: 1
#expected response (200 ok)

#(no contet)

#get/ albums
#expecte response (200 ok)

#Album (1, Lateralus, 2001, 1)
#Album (2, 1000 Wings, 2006, 2)

def test_get_albums(db_connection , web_client):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == '' \
        "Album(1, Lateralus, 2001, 1)"
    


def test_post_albums(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
    post_response = web_client.post('/albums', data={
        'title': '10000 Wings',
        'release_year': '2006',
        'artist_id': '1'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ''
    
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == '' \
        "Album(1, Lateralus, 2001, 1)\n"\
        "Album(2, 10000 Wings, 2006, 1)"


def test_post_albums_no_data(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
    post_response = web_client.post('/albums')
    assert post_response.status_code == 400
    assert post_response.data.decode("utf-8") == '' \
        'You need to submit a title, release_year and artist_id'

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode ('utf-8') == '' \
        'Album(1, Lateralus, 2001, 1)'
        
# SCENARIO 1
# post/ artist
#name: Tool'
#genre: 'Rock
#expected response (200 ok)

#(no contet)

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

def test_get_artist(db_connection , web_client):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == '' \
        "Artist(1, Tool, Rock)\n" \
        "Artist(2, Mastodon, Rock)"

def test_post_artist(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
    post_response = web_client.post('/artists', data={
        'name_artist': 'Gojira',
        'genre': 'Metal',
    })
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ''
    
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == '' \
        "Artist(1, Tool, Rock)\n" \
        "Artist(2, Mastodon, Rock)\n" \
        "Artist(3, Gojira, Metal)"
        
