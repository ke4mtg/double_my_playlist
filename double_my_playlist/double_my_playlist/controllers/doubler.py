import lastfm
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from double_my_playlist.lib.base import BaseController, render

log = logging.getLogger(__name__)

class DoublerController(BaseController):

    def index(self, artist='The Temper Trap', track='Fader'):
        api = lastfm.Api('578ff28eb42a625b4beb7cd1ec8c1dae')
        track = api.get_track(track, artist=artist)
        c.tracks = track.similar
        return render('doubler/index.html')
