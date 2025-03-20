import spacy
from flask import Flask, render_template, request
import pandas as pd
from spacy import displacy

# Load your trained NER model
nlp = spacy.load(r"C:\Users\suman\OneDrive\Desktop\my all projects\ML Project\NER MODEL")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    if request.method == 'POST':
        rawtext = request.form.get('rawtext')

        doc = nlp(rawtext)
        entities = [(ent.label_, ent.text) for ent in doc.ents]

        if not entities:
            return render_template("index.html", results=[], num_of_results=0, visual="")

        # Convert extracted entities into a DataFrame
        df = pd.DataFrame(entities, columns=['Entity Type', 'Entity'])
        
        # Generate HTML visualization using displacy
        html_visual = displacy.render(doc, style="ent", page=True)
        
        return render_template("index.html", tables=[df.to_html(classes='table table-striped', index=False)], visual=html_visual, num_of_results=len(entities))

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple("127.0.0.1", 5000, app, use_reloader=False)
    
