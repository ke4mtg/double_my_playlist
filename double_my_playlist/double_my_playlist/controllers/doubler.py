import json
import lastfm
import logging
import urllib

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from double_my_playlist.lib.base import BaseController, render

log = logging.getLogger(__name__)

LASTFM_API_PREFIX = 'http://ws.audioscrobbler.com/2.0/?'
LASTFM_API_KEY = '578ff28eb42a625b4beb7cd1ec8c1dae'

class Artist(object):
    def __init__(self, name):
        self.name = name


class Track(object):
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

    
class DoublerController(BaseController):

    def index(self, artist='The Temper Trap', track='Fader'):
        def find_similar(artist, track):
            params = {'method': 'track.getSimilar',
                      'limit': 25,
                      'format': 'json',
                      'api_key': LASTFM_API_KEY,
                      'artist': artist,
                      'track': track}
            data = json.loads(urllib.urlopen(LASTFM_API_PREFIX + urllib.urlencode(params)).read())
    
            tracks = []
            for d in data['similartracks']['track']:
                artist = Artist(d['artist']['name'])
                track = Track(d['name'], artist)
                tracks.append(track)
            return tracks
        
        c.playlist = request.params.get('playlist', 'The Temper Trap - Fader\nPearl Jam - Once')

        known_tracks = [x.split(' - ') for x in c.playlist.split('\n')]
        c.tracks = []
        for artist, track in known_tracks:
            for similar_track in find_similar(artist, track):
                c.tracks.append(similar_track)
            
        return render('doubler/index.html')
