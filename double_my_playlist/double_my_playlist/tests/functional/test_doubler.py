from double_my_playlist.tests import *

class TestDoublerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='doubler', action='index'))
        # Test response...
