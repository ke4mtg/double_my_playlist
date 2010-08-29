import lastfm
import logging
import urllib

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from double_my_playlist.lib.base import BaseController, render

log = logging.getLogger(__name__)

LASTFM_API_PREFIX = 'http://ws.audioscrobbler.com/2.0/?'
LASTFM_API_KEY = '578ff28eb42a625b4beb7cd1ec8c1dae'

class DoublerController(BaseController):

    def index(self, artist='The Temper Trap', track='Fader'):
        params = {'method': 'track.getSimilar',
                  'limit': 10,
                  'api_key': LASTFM_API_KEY,
                  'artist': artist,
                  'track': track}
        c.data = urllib.urlopen(LASTFM_API_PREFIX + urllib.urlencode(params)).read()
        c.tracks = []
        return render('doubler/index.html')
