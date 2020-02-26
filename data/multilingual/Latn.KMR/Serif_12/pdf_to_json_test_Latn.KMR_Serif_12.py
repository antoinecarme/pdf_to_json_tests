import pdf_to_json as p2j

import json

url = "file:data/multilingual/Latn.KMR/Serif_12/udhr_Latn.KMR_Serif_12.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4, ensure_ascii=False))
