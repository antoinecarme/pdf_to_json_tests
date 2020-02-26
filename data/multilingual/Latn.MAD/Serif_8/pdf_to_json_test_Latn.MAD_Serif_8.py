import pdf_to_json as p2j

import json

url = "file:data/multilingual/Latn.MAD/Serif_8/udhr_Latn.MAD_Serif_8.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4, ensure_ascii=False))
