from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from docx import Document
from summa.summarizer import summarize
from summarizer import Summarizer

import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Load pre-trained Sentence BERT model
model = SentenceTransformer('bert-base-nli-mean-tokens')

# Function to calculate cosine similarity
def calculate_cosine_similarity(embedding1, embedding2):
    similarity = cosine_similarity(embedding1, embedding2)
    return similarity[0][0]


def extract_text_from_docx(docx_file):
    text = []
    document = Document(docx_file)
    for paragraph in document.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)



docx_text = extract_text_from_docx('Evidence1.docx')

action_item = "Ensure that all customer transactions exceeding $10,000 are accompanied by proper documentation and flagged for review, as per anti-money laundering regulations. Review current procedures and implement necessary controls to mitigate the risk of non-compliance and financial penalties."

rationale = "Implemented enhanced monitoring systems to automatically flag and review transactions exceeding $10,000, ensuring compliance with anti-money laundering regulations. All necessary documentation and controls are now in place to mitigate potential risks."

#rationale =  "Despite concerted efforts, the action item pertaining to the enhancement of monitoring systems for transactions exceeding $10,000 has not been fully completed. While progress has been made in reviewing procedures and exploring technological solutions, challenges remain in the implementation phase. Further coordination and resource allocation are necessary to ensure the effective deployment of enhanced monitoring capabilities and the establishment of robust controls. The issue will continue to be actively monitored and addressed until full compliance is achieved."

evidence = rationale + docx_text

# Set the parameters for summarization
summary_ratio = 0.2  # Summarize the document to 20% of its original length
split_text = True  # Split the text into sentences
return_scores = False  # Do not return sentence scores
language = "english"  # Set the language to English

summary = summarize(evidence, ratio=summary_ratio, split=split_text, scores=return_scores, language=language)


summarised_evidence = " ".join(summary)


# Encode action item and closure statement
action_item_embedding = model.encode([action_item])
closure_embedding = model.encode([summarised_evidence])

# Calculate cosine similarity
similarity_score = calculate_cosine_similarity(action_item_embedding, closure_embedding)
print("Action:", action_item)
print("\n")
print("Evidence:", summarised_evidence)
print("\n")
print("Similarity Score:", similarity_score)

genai.configure(api_key="AIzaSyC2DRYHQGqwXVB6I1BUYtCnNkW5ADQgD8s")

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(
    "; Action:" + action_item + 
    "; Evidence: "+ summarised_evidence + 
    "; Similarity Score: "+ str(similarity_score) + 
    "; Based on the action and summarised evidence statements along with cosine score, can you provide rationale on whether the action is closed or failed?​"
    )

for chunk in response:
  print(chunk.text)
  print("_"*80)
