import heapq

class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        
    def latest(self):
        return self.scores[-1] #returns the latest score, that'd be the last one in the list
    
    def personal_best(self):
        return max(self.scores) #returns the max score
        
    def personal_top_three(self):
        return sorted(heapq.nlargest(3, self.scores), reverse=True) #returns the highest 3 scores from a list