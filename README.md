# Facebook_Event_Detector

## Background and motivation
This is a simple natural language processing project in which the input will be some series of events that I mark that I'm going or interested in on Facebook. The model will process and determine if 1) a blackout Friday is happening and 2) if there already is a carpool event dedicated for it.

Blackout Friday(s) is an event in North Hollywood that is run on an infrequent bi-monthly basis. Since Caltech West Coast Swing regularly attends and hosts a carpool event, it would be nice to not have to do anything besides check that I'm going to the event and my server pops out the reaction event ( Caltech Carpool to Blackout Friday ).

The title for the event has small variantions to it (capitalizations, extra info, or a word play) such that simple string detection would not be as efficient. 


## Notes
Facebook no longer allows 64+ character long event titles. Previous limit was 84. Now it is 64. Thus for the machine learning portion of this project, we will only take the first 64 characters.

First iteration of NLP model will incorporate uppercase characters.
Second iteration of NLP model will only incorporate lowercase characters.

Uppercase and lowercase letters have a different mapping and can potentially confuse the model. 
Ex:   A -> 97
      a -> 65
