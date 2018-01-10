import pickle
if __name__ == '__main__':
    fileName = 'labeledData/cleanedEvents.p'
    events = pickle.load(open(fileName, 'rb'))
    encodedEvents = [map(ord, event) for event in events]
    for i in range(len(encodedEvents)):
        if len(encodedEvents[i]) > 64:
            encodedEvents[i] = encodedEvents[i][:64]
        else:
            hold = [0]*64
            hold[:len(encodedEvents[i])] = encodedEvents[i]
            encodedEvents[i] = hold

    pickle.dump( encodedEvents, open('labeledData/encodedEvents.p', "wb" ) )

