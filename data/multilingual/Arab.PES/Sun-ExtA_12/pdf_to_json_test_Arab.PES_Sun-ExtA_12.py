import pdf_to_json as p2j

import json

url = "file:data/multilingual/Arab.PES/Sun-ExtA_12/udhr_Arab.PES_Sun-ExtA_12.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4))
