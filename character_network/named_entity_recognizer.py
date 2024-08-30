import spacy
from nltk.tokenize import sent_tokenize
import pandas as pd
from ast import literal_eval
import os 
import sys
import pathlib
import re
folder_path = pathlib.Path().parent.resolve()
sys.path.append(os.path.join(folder_path, '../'))
from utils import load_subtitles_dataset

class NamedEntityRecognizer:
    def __init__(self):
        self.nlp_model = self.load_model()
        
        
    def load_model(self):
        nlp = spacy.load('en_core_web_trf')
        return nlp
    
    def get_ners_inference(self, script):
        script_sentences = sent_tokenize(script)
        
        ner_output = []
        
        for sentence in script_sentences:
            doc = self.nlp_model(sentence)
            ners = set()
            for entity in doc.ents:
                if entity.label_ == 'PERSON':
                    full_name = entity.text
                    first_name = full_name.split(' ')[0]
                    first_name = first_name.strip()
                    ners.add(first_name)
            ner_output.append(ners)
        
        return ner_output
    
    def parse_list_of_sets(self,val):
        if isinstance(val, str):
            try:
                # Replace set braces {} with set() to make them evaluable
                val = re.sub(r'\{([^{}]*)\}', r'set([\1])', val)
                # Evaluate the string to a list of sets
                return eval(val)
            except Exception as e:
                # Handle or log the error if needed
                return val  # or return None if you prefer
        return val
    
    def get_ners(self, dataset_path, save_path=None):
        if save_path is not None and os.path.exists(save_path):
            df = pd.read_csv(save_path)
            df['ners'] = df['ners'].apply(self.parse_list_of_sets)
            return df

        # load dataset 
        df = load_subtitles_dataset(dataset_path)

        # Run Inference
        df['ners'] = df['script'].apply(self.get_ners_inference)

        if save_path is not None:
            df.to_csv(save_path,index=False)
        
        return df
        