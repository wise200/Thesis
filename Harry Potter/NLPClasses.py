from matplotlib import pyplot as plt

class FreqTable:
    def __init__(self, name=""):
        self.vals = dict()
        self.size = 0
        self.name = name
    
    def add(self, item):
        self.size += 1
        if item in self.vals:
            self.vals[item] += 1
        else:
            self.vals[item] = 1
    
    def __len__(self):
        return len(self.vals)
    
    def __str__(self):
        return self.name + ": " + str(self.vals)
    
    def __getitem__(self, key):
        return self.vals[key] if key in self.vals.keys() else 0
    
    def relFreq(self, key):
        return 100 * self[key] / self.size
    
    def freq(self, key, relative):
        return self.relFreq(key) if relative else self[key]
    
    def printItems(self):
        print(self.name + ":")
        for key, value in self.vals:
            print(key + ":\t" + str(value) + ",\t" + str(value/self.size*100) + "%")
    
    def subplot(pos):
        plt.subplot(pos[0],pos[1],pos[2])
    
    def pieplot(self, show = True, pos=(1,1,1)):
        labels = list(self.vals.keys())
        sizes = list(self.vals.values())
        FreqTable.subplot(pos)
        plt.pie(sizes, labels=labels, autopct="%1.2f%%")
        if show:
            plt.show()
    
    def plotMultiple(list, *args):
        list[0].plotWith(list[1:], *args)
    
    def plotWith(self, others, show=True, pos=(1,1,1), title=None, legend=None, relative=False, size=0):
        FreqTable.subplot(pos)
        plt.grid(True, color="silver")
        if not title == None:
            plt.title(title)
        if size == 0:
            size = len(self)
        labels = [key for key in sorted(self.vals, reverse= True, key=self.vals.__getitem__)]
        labels = labels[:size]
        myFreqs = [self.freq(key, relative) for x in labels]
        otherFreqs = [[table.freq(key, relative) for x in labels] for table in others]
        plt.plot(myFreqs, linewidth=2)
        for table in otherFreqs:
            plt.plot(table, linewidth=2)
        plt.xticks(range(len(labels)), labels, rotation=90)
        if not legend == None:
            plt.legend(legend, loc="upper right")
        if show:
            plt.show()
            
    def plotDiffs(tables, key, show=True, pos=(1,1,1), title=None, relative=False):
        FreqTable.subplot(pos)
        plt.grid(True, color="silver")
        if not title == None:
            plt.title(title)
        vals = [table.freq(key, relative) for table in tables]
        names = [table.name for table in tables]
        plt.plot(vals, linewidth=2)
        plt.xticks(range(len(vals)), names, rotation=90)
        if show:
            plt.show()