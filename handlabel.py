from curtsies import Input
import pickle

def handLabel(fileName, labelsName = None):
    print('\n\n\n\n\nloading name of events...')
    events = pickle.load(open(fileName, 'rb'))
    
    print('attempting to load old labels')
    if labelsName is None:
        labels = [False]*len(events)
        print('no old labels found, initializing new labels')
    else:
        try:
            print('Successfully loaded old labels')
            labels = pickle.load(open(labelsName, 'rb'))
        except:
            print('no old labels found, initializing new labels')
            labels = [False]*len(events)

    i = 0
    print('\n\n\n\n\n')
    print('Use left and right arrow keys to cycle through the events list')
    print('Use up and down arrow to mark events as True or False, respectively')
    print("Use 's' to save")
    print("Use 'n' to input the desired index. Hint: don't forget to hit enter")
    print("Use 'q' to quit hand labeling")
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if e == 'KEY_RIGHT':
                i+=1
                if i> len(events)-1:
                    i = len(events)-1
                print(i, events[i], labels[i])
            elif e == 'KEY_LEFT':
                i-=1
                if i < 0:
                    i = 0
                print(i, events[i], labels[i])
            elif e == 'KEY_UP':
                labels[i] = True
                print(i, events[i], labels[i])
            elif e == 'KEY_DOWN':
                labels[i] = False
                print(i, events[i], labels[i])
            elif e == 's':
                print('saved!')
                pickle.dump( labels, open( labelsName, "wb" ) )
            elif e == 'n':
                i = int(raw_input())
                if i < 0:
                    i = 0
                elif i > len(events)-1:
                    i = len(events)-1
                print(i, events[i], labels[i])
            elif e == 'q':
                return



if __name__ == '__main__':
    fileName = 'labeledData/cleanedEvents.p'
    labelsName1 = 'labeledData/labelsBOFCarpool.p'
    labelsName2 = 'labeledData/labelsBOF.p'
    handLabel(fileName = fileName, labelsName = labelsName1)
    handLabel(fileName = fileName, labelsName = labelsName2)

