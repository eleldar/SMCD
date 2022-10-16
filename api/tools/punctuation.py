from sbert_punc_case_ru import SbertPuncCase
from abc import abstractmethod, ABC


class Detection(ABC):
    @abstractmethod
    def __call__(
        self,
        input: str
    ) -> object:
        raise NotImplementedError

class Punctuate(Detection):
    '''Text punctuation'''
    def __init__(
        self,
    ):
        self.model = SbertPuncCase()

    def __handler(self, text):
        return self.model.punctuate(text)

    def __call__(self, text):
        return self.__handler(text)
     

punctuate = Punctuate()


### https://huggingface.co/kontur-ai/sbert_punc_case_ru
