import pdf_to_json as p2j

import json

url = "file:data/multilingual/Latn.KMB/Sans_12/udhr_Latn.KMB_Sans_12.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4))
