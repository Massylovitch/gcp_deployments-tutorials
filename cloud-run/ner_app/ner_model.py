import spacy

NLP = spacy.load("en_core_web_md")


def predict_entities(text):

    doc = NLP(text)

    entities = [
        {
            "text": entity.text,
            "label": entity.label_,
            "start_idx": entity.start_char,
            "end_idx": entity.end_char,
        }
        for entity in doc.ents
    ]

    return entities


if __name__ == "__main__":
    text = "Apple is looking at buying U.K. startup for $1 billion"

    entities = predict_entities(text)
    print(entities)