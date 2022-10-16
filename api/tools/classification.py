import torch
from transformers import pipeline
from abc import abstractmethod, ABC


class Detection(ABC):
    @abstractmethod
    def __call__(
        self,
        input: str
    ) -> object:
        raise NotImplementedError

class Classificate(Detection):
    '''Text classification'''
    def __init__(
        self,
    ):
        self.classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
        self.candidate_labels = [
            "преступление", "политика", "экономика", "спорт", 
            "игры", "кино", "авто", "здоровье"
        ]

    def __handler(self, text):
        output = self.classifier(text, self.candidate_labels, multi_label=False)
        max_value = output['scores'][0]
        max_type = output['labels'][0] 
        return {
            'crime': True if max_type == "преступление" else False,
            'max_value': max_value,
            'max_type': max_type
        }

    def __call__(self, text):
        return self.__handler(text)
     

classificate = Classificate()
