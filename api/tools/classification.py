from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")


def classificate(text):
    candidate_labels = [
        "преступление", "политика", "экономика", "спорт", "игры", "кино", "авто", "здоровье"
    ]
    output = classifier(text, candidate_labels, multi_label=False)
    sequence = output['sequence'] 
    labels   = output['labels'] 
    scores   = output['scores']
    return True if labels[scores.index(max(scores))] == candidate_labels[0] else False 

