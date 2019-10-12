from google.cloud import language_v1
from google.cloud.language_v1 import enums
import string
import nltk
nltk.download('punkt')

def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entities(document, encoding_type=encoding_type)
    
    KeyWords = []
    # Loop through entitites returned from the API
    for entity in response.entities:
        if enums.Entity.Type(entity.type).name == "OTHER":
            # Only add into our list if entity is not too low
            if entity.salience > 0.05:
                KeyWords.append(entity.name)
        else:
            KeyWords.append(entity.name)
    return KeyWords

def getKeyWords():
    text = input()
    return sample_analyze_entities(text)


if __name__ == '__main__':
    print(getKeyWords())
