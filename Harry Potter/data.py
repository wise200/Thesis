import nltk
from matplotlib import pylab
from six import text_type

def _get_kwarg(kwargs, key, default):
    if key in kwargs:
        arg = kwargs[key]
        del kwargs[key]
    else:
        arg = default
    return arg

class Frequencies(nltk.FreqDist):
    def __init__(self, samples):
        self.jsize = len(samples)
        super().__init__(samples)
    
    def plotwith(self, other, *args, **kwargs):

        if len(args) == 0:
            args = [len(self)]
        samples = [item for item, _ in self.most_common(*args)]

        cumulative = _get_kwarg(kwargs, 'cumulative', False)
        if cumulative:
            freqs = list(self._cumulative_frequencies(samples))
            ylabel = "Cumulative Counts"
        else:
            my_freqs = [self[sample] for sample in samples]
            other_freqs = [other[sample] for sample in samples]
            ylabel = "Counts"
        my_percents = [f * 100 / self.jsize for f in my_freqs]
        other_percents = [f * 100 / other.jsize for f in other_freqs]

        pylab.grid(True, color="silver")
        if not "linewidth" in kwargs:
            kwargs["linewidth"] = 2
        if "title" in kwargs:
            pylab.title(kwargs["title"])
            del kwargs["title"]
        pylab.plot(my_percents,**kwargs)
        pylab.plot(other_percents,**kwargs)
        pylab.xticks(range(len(samples)), [text_type(s) for s in samples], rotation=90)
        pylab.xlabel("Samples")
        pylab.ylabel(ylabel)
        pylab.show()



hpwords = ""

for x in range(1,8):
    with open("HP" + str(x) + ".txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            hpwords += line + "\n"
        print("Completed HP " + str(x))

hpwords = nltk.word_tokenize(hpwords)
#punctuation = ".,?!();:-*\"\'&…0123456789\’\‘–—\”\“"
#words = [word for word in words if word not in punctuation]
hpwords = [word.lower() for word in hpwords]
hpwords = [word for word in hpwords if len(word) > 1 or word == 'a' or word == 'i']

HPdist = Frequencies(hpwords)

print("Potter finished")

gbwords = ""
titles = []
with open("Gutenberg/titles.txt", "r") as file:
    for title in file.readlines():
        titles.append(title)
        
for x in range(96):
    with open("Gutenberg/GB" + str(x) + ".txt", "r", encoding= "utf-8") as file:
        print("Beginning GB" + str(x) + ": " + titles[x], end="")
        for line in file.readlines():
            gbwords += line + "\n"
        print("Completed GB" + str(x) + ": " + titles[x], end="")

gbwords = nltk.word_tokenize(gbwords)
gbwords = [word.lower() for word in gbwords]
gbwords = [word for word in gbwords if len(word) > 1 or word == 'a' or word == 'i']

GBdist = Frequencies(gbwords)

HPdist.plotwith(GBdist, 50)