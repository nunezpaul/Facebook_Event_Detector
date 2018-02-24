# Facebook_Event_Detector

## Background and motivation
This is a simple natural language processing project in which the input will be some series of events that I mark that I'm going or interested in on Facebook. The model will process and determine if 1) a blackout Friday is happening and 2) if there already is a carpool event dedicated for it. The eventual use for this model is to have it running on a bot that checks whether or not to send out the reaction carpool event.

Blackout Friday(s) is an event in North Hollywood that is run on an infrequent bi-monthly basis. Since Caltech West Coast Swing regularly attends and hosts a carpool event, it would be nice to not have to do anything besides check that I'm going to the event and my server pops out the reaction event ( Caltech Carpool to Blackout Friday ).

The title for the event has small variantions to it (capitalizations, extra info, or a word play) such that simple string detection would not be as efficient. 


Using a bag of words model, a NN and the entirety of the constructed dictionary, I was able to achieve 99.1% accuracy. Not as perfect as I would like it to be but it's pretty close. 

## Future work
It would probably be best to eliminate words that appear not so frequently. This would help the NN focus more on what's important when classifying.

## Notes
Facebook no longer allows 64+ character long event titles. Previous limit was 84. Now it is 64. 
