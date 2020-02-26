import pdf_to_json as p2j

import json

url = "file:data/multilingual/Adlm.FUF/Noto Sans Adlam_12/udhr_Adlm.FUF_Noto Sans Adlam_12.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4))