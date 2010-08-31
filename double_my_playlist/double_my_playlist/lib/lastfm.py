import json
import urllib

LASTFM_API_PREFIX = 'http://ws.audioscrobbler.com/2.0/?'
LASTFM_API_KEY = '578ff28eb42a625b4beb7cd1ec8c1dae'

class Artist(object):
    def __init__(self, name):
        self.name = name


class Track(object):
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
    
    def __str__(self):
        return self.artist.name + ' - ' + self.name

    def __repr__(self):
        return "Track('" + self.name + "', '" + self.artist.name + "')"


class TrackSearchResult(object):
    def __init__(self, track, score=100.0):
        self.track = track
        self.score = score
    
    def __repr__(self):
        return "TrackSearchResult('" + self.track.name + "', '" + str(self.score) + "')"


def find_similar(track):
    params = {'method': 'track.getSimilar',
              'limit': 25,
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
