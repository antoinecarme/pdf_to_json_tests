import pdf_to_json as p2j

import json

url = "file:data/multilingual/Cyrl.GLD/Sans_16/udhr_Cyrl.GLD_Sans_16.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4))
