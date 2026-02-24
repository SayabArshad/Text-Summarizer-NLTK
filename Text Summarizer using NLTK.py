#import libraries
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# example text to summarize
text = """Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. The ultimate objective of NLP is to enable computers to understand, interpret, and generate human language in a way that is valuable.
NLP encompasses a variety of tasks including text analysis, sentiment analysis, machine translation, and speech recognition. It combines computational linguistics with machine learning and deep learning techniques to process and analyze large amounts of natural language data.
Applications of NLP are widespread and include virtual assistants, chatbots, language translation services, and automated content generation. As technology advances, NLP continues to evolve, making it an exciting and dynamic field of study."""

# Function to summarize text
def summarize_text(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize the text into words and remove stopwords
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Calculate word frequency
    word_freq = {}
    for word in filtered_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Score sentences based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += word_freq[word]
                else:
                    sentence_scores[sentence] = word_freq[word]
    
    # Select the top N sentences for the summary
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    # Join the selected sentences to form the summary
    summary = ' '.join(summarized_sentences)
    return summary

# Generate and print the summary
summary = summarize_text(text)
print("Original Text:", text)
print("\n\n\nSummary:")
print(summary)
# Output:
# Summary:

