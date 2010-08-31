import logging

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

    def score(self):
        result = []
        for rule,weight in self.rules:
            rule_result = rule(self.originals, self.fetched) 
            for sr in rule_result:
                sr.score *= weight
            result.append(rule_result)
        
        return result


            
            
    
