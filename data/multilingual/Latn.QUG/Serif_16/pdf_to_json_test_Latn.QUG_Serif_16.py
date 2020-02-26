import pdf_to_json as p2j

import json

url = "file:data/multilingual/Latn.QUG/Serif_16/udhr_Latn.QUG_Serif_16.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4))