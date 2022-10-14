# import os, sys
# import time
# from pathlib import Path
# from transformers import logging
# from tools.recasepunc.recasepunc import CasePuncPredictor
# from tools.recasepunc.recasepunc import WordpieceTokenizer
# from tools.recasepunc.recasepunc import Config
# 
# 
# logging.set_verbosity_error()
# 
# curdir = Path(__file__).parent.resolve()
# models_path = os.path.join(curdir, 'recasepunc', 'checkpoint')
# 
# predictor = CasePuncPredictor(models_path, lang="ru")
# 
def punctuate(text):
#     tokens = list(enumerate(predictor.tokenize(text)))
#     results = ""
#     for token, case_label, punc_label in predictor.predict(tokens, lambda x: x[1]):
#         prediction = predictor.map_punc_label(predictor.map_case_label(token[1], case_label), punc_label)
#         if token[1][0] != '#':
#            results = results + ' ' + prediction
#         else:
#            results = results + prediction
#     print(result)    
#     return result.strip()
    return text
