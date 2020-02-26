import pdf_to_json as p2j

import json

url = "file:data/multilingual/Latn.AJG/Sans_12/udhr_Latn.AJG_Sans_12.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4))