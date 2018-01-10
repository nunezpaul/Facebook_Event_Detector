if __name__ == '__main__':
    fileName = 'labeledData/cleanedEvents.p'
    events = pickle.load(open(fileName, 'rb'))
    encodedEvents = [map(ord, event) for event in events]
    pickle.dump( events, open('labeledData/encodedEvents.p', "wb" ) )
