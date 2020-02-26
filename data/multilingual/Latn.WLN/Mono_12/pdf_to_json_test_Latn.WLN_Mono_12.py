import pdf_to_json as p2j

import json

url = "file:data/multilingual/Latn.WLN/Mono_12/udhr_Latn.WLN_Mono_12.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4))
