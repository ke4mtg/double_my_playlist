import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from double_my_playlist.lib import lastfm, rules
from double_my_playlist.lib.base import BaseController, render
from double_my_playlist.lib.scorer import Scorer

log = logging.getLogger(__name__)

class DoublerController(BaseController):

    def index(self, artist='The Temper Trap', track='Fader'):
        c.dont_repeat_artists = request.params.get('dont-repeat-artists', False)
        c.playlist = request.params.get('playlist', 'The Temper Trap - Fader\nPearl Jam - Once')

        known_tracks = [x.split(' - ') for x in c.playlist.split('\n') if ' - ' in x]
        c.results = []
        originals = []
        fetched = []

        for artist, track in known_tracks:
            cur_track = lastfm.Track(track, lastfm.Artist(artist))
            originals.append(cur_track)
            for similar_track in lastfm.find_similar(cur_track):
                fetched.append(similar_track)
        
        scorer = Scorer(originals, fetched)       
        scorer.add_rule(rules.identity, 1)
        if c.dont_repeat_artists:
            scorer.add_rule(rules.remove_repeat_artists, 1)
        c.results = scorer.results(max_length=max(5, len(originals)))

        return render('doubler/index.html')
