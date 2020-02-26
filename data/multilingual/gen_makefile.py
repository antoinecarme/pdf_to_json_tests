import os, glob
def create_dir_if_needed(iDir):
    try:
        os.makedirs(iDir);
    except:
        pass

def create_script(lang , font):
    tgt = lang + "_" + font
    tgt = tgt.replace(" ", "_")
    fname = "data/multilingual/" + lang + "/" + font + "/pdf_to_json_test_" + tgt + ".py"
    pdf_files = sorted(glob.glob("data/multilingual/" + lang + "/" + font + "/*.pdf"))
    pdf_file = pdf_files[0]
    with open(fname, "w") as outfile:        
        outfile.write("import pdf_to_json as p2j\n\n")
        outfile.write("import json\n\n")
        outfile.write('url = "file:' + pdf_file + '"\n')
        outfile.write('lConverter = p2j.pdf_to_json.pdf_to_json_converter()\n')
        outfile.write('lConverter.mImageHashOnly = True\n')
        outfile.write('lDict = lConverter.convert(url)\n')
        outfile.write('print(json.dumps(lDict, indent=4, ensure_ascii=False, sort_keys=True))\n')

def process_language(lang):
    fonts = sorted(glob.glob("data/multilingual/" + lang + "/*_*"))
    K = len("data/multilingual/" + lang + "/")
    fonts = [x[K:] for x in fonts]
    print(lang, fonts)
    make_fname = "data/multilingual/" + lang + "/Makefile"
    tgts = []
    with open(make_fname, "w") as outfile:
        outfile.write("PYTHON=python3\n\n\n")
        for font in fonts:
            create_script(lang, font)
            tgt = lang + "_" + font
            tgt = tgt.replace(" ", "_")
            outfile.write(tgt + ":\n")
            script = "data/multilingual/" + lang + "/" + font + "/pdf_to_json_test_" + tgt + ".py"
            scriptlog = "data/multilingual/" + lang + "/" + font + "/pdf_to_json_test_" + tgt + ".json"
            # create_dir_if_needed("outputs/multilingual/" + lang + "/" + font)
            outfile.write("\t" + "-$(PYTHON) \"" + script + "\" > \"" + scriptlog + "\" 2>&1\n")
            tgts = tgts + [tgt]
        outfile.write("\n\n")
        outfile.write(lang + "_all : " + " ".join(tgts) + "\n")

languages = sorted(glob.glob("data/multilingual/????.???"))

global_make_fname = "data/multilingual/Makefile"
tgts2 = []
with open(global_make_fname, "w") as outfile2:
    for lang in languages:
        lang = lang[18:]
        print(lang)
        process_language(lang)
        outfile2.write("include data/multilingual/" + lang + "/Makefile\n")
        tgts2 = tgts2 + [lang + "_all"]
    outfile2.write("\n\n\nall : " + " ".join(tgts2) + "\n")
