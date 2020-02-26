import pdf_to_json as p2j

import json

url = "file:data/multilingual/Deva.MAG/Sun-ExtA_8/udhr_Deva.MAG_Sun-ExtA_8.pdf"
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lConverter.mImageHashOnly = True
lDict = lConverter.convert(url)
print(json.dumps(lDict, indent=4))
