import nltk

class Analyzer():
    """Implements sentiment analysis."""
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # TODO
        self.tokenizer = nltk.tokenize.casual.TweetTokenizer()
        self.positives = set()
        self.negatives = set()
        file = open(positives, "r")
        for line in file:
            if line.startswith(";") or line.startswith('\n'):
                pass
            else:
                self.positives.add(line.rstrip('\n'))
        file.close()
        
        file = open(negatives, "r")
        for line in file:
            if line.startswith(";") or line.startswith('\n'):
                pass
            else:
                self.negatives.add(line.rstrip('\n'))
        file.close()
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
    
        # TODO
        positive = 0
        negative = 0
        neutral = 0
        score = 0
        text = str(text)
        text = text.lower()
        tokens = self.tokenizer.tokenize(text)
        for i in range(len(tokens)):    
            if tokens[i] in self.positives:
                score += 1
                positive += 1
            elif tokens[i] in self.negatives:
                score -= 1
                negative += 1
            else:
                neutral += 1
        return score, positive, negative, neutral
