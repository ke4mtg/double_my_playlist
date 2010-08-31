import json
import urllib

LASTFM_API_PREFIX = 'http://ws.audioscrobbler.com/2.0/?'
LASTFM_API_KEY = '578ff28eb42a625b4beb7cd1ec8c1dae'

class Artist(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, artist):
        if type(self) != type(artist):
            return False
        return self.name == artist.name

    def __hash__(self):
        return hash(self.name)


class Track(object):
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
    
    def __str__(self):
        return self.artist.name + ' - ' + self.name

    def __repr__(self):
        return "Track('" + self.name + "', '" + self.artist.name + "')"

    def __eq__(self, track):
        if type(self) != type(track):
            return False
        return (self.artist == track.artist) and (self.name == track.name)

    def __hash__(self):
        return hash(self.name)


class TrackSearchResult(object):
    def __init__(self, track, score=100.0):
        self.track = track
        self.score = score
    
    def __repr__(self):
        return "TrackSearchResult('" + self.track.name + "', '" + str(self.score) + "')"


def find_similar(track, limit=25):
    params = {'method': 'track.getSimilar',
              'limit': limit,
              'format': 'json',
              'api_key': LASTFM_API_KEY,
              'artist': track.artist.name,
              'track': track.name}
    data = json.loads(urllib.urlopen(LASTFM_API_PREFIX + urllib.urlencode(params)).read())
    
    results = []
    for d in data['similartracks']['track']:
        artist = Artist(d['artist']['name'])
        track = Track(d['name'], artist)
        result = TrackSearchResult(track, float(d['match']) * 100.0)
        results.append(result)
    return results    
