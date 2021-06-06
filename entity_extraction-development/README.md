# Entity Extraction - Hindi

Hindi Entity Extraction for City and Towns names

Train and get the custom-named entity from the training data using spacy and python

Installation
pip3 install spacy

Steps for usage

- Initially, import the necessary packages required for the custom creation process
- Create custom entity data for the input text where the named entity is to be identified by the model during the testing period.
- Define the variables required for the training model to be processed
- Load a blank model for the process to carry out the NER action and set up the pipeline with only NER using create_pipe function.
- we want to train the recognizer by disabling the unnecessary pipeline except for NER. The nlp_update function can be used to train the recognizer.
- Test the trained model
- Finally, save the model to the path which stored in the output_dir variable.
- Once you saved the trained model you can load the model using the below and text again.


                        model = spacy.load('model_name')


Flask app for Hindi Entity Extraction for City and Towns

Steps are as follows

- To run this file download the Updated_Flask_app.py,hindi_model and templates folder as well which is having index_new.html file
- Place all three of them in one project folder.
- Run flask_app.py
- It will run and give you an IP to goto. This IP will be hosting the application.



