import logging

from double_my_playlist.lib import lastfm

log = logging.getLogger(__name__)

""" The component for scoring lists of songs """
class Scorer(object):
    def __init__(self, originals, fetched):
       self.originals = originals 
       self.fetched = fetched
       self.rules = []
       log.debug('Making a Scorer')
    
    def add_rule(self, rule, weight):
       self.rules.append((rule,weight))

    def rule_scores(self):
        result = []
        for rule, weight in self.rules:
            rule_result = rule(self.originals, self.fetched) 
            for sr in rule_result:
                sr.score *= weight
            result.append(rule_result)
        
        return result

    def results(self, max_length=None):
        track_scores = {}
        scores = self.rule_scores()
        for rule_result in scores:
            for track_result in rule_result:
                if not track_scores.has_key(track_result.track): track_scores[track_result.track] = 100.0
                track_scores[track_result.track] *= track_result.score / 100.0

        results = []
        for track in track_scores:
            results.append(lastfm.TrackSearchResult(track, track_scores[track]))            
        results.sort(key=lambda x: -x.score)
        results = results[:max_length]
        return results
            
    
