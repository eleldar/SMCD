from sbert_punc_case_ru import SbertPuncCase


def punctuate(text):
    model = SbertPuncCase()
    return model.punctuate(text)


### https://huggingface.co/kontur-ai/sbert_punc_case_ru
