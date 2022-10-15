import torch
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
    print('>class:', scores)
    max_value = max(scores)
    max_type = labels[scores.index(max_value)]
    return {
        'crime': True if max_type == candidate_labels[0] else False,
        'max_value': max_value,
        'max_type': max_type
    }
