import pdf_to_json as p2j

import json

url = "file:data/multilingual/Cans.IKE/Mono_16/udhr_Cans.IKE_Mono_16.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4, ensure_ascii=False, sort_keys=True))
