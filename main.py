from TTS.api import TTS
import datetime
import subprocess
import pandas as pd
from contextlib import contextmanager
import sys, os


@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout


def get_clipboard_text():
    command = 'xclip -selection clipboard -o'.split()
    clipboard_text = subprocess.check_output(command).decode('utf-8').strip()
    return clipboard_text


def remove_dash(text):
    return text.replace("-", "")


def replace_acronyms(text):
    """Replace acronyms TPL with their hyphened version T-P-L."""
    # get all upper case words
    words = text.split()
    mapping_dict = dict()
    for i, word in enumerate(words):
        if len(word) > 2 and word.isupper():
            replacement_word = '-'.join(word.lower())
            mapping_dict[word] = replacement_word
    # replace all words in the mapping dict
    for key, value in mapping_dict.items():
        text = text.replace(key, value)
    return text


def replace_idioms(text):
    """Replace idioms such as "e.g." with "for example"."""
    df = pd.read_csv(
        "/home/kapil/PycharmProjects/coquiai-TTS/configuration/idiom.csv",
        header=0, delimiter=",")
    for i, row in df.iterrows():
        text = text.replace(str(row["idiom"]), str(row["replacement"]))
    return text

# text = "this is a fixed text for test purpose"
text = get_clipboard_text()


# print(text)
with suppress_stdout():
    text = remove_dash(text)
    text = replace_acronyms(text)
    # print(text)
    text = replace_idioms(text)
    # print(text)

    model_name = TTS.list_models()[0]
    tts = TTS(model_name)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output{timestamp}.wav"
    
    tts.tts_to_file(text=text, speaker=tts.speakers[0], language=tts.languages[0],
                file_path=f"/home/kapil/PycharmProjects/coquiai-TTS/{filename}")

path=f"/home/kapil/PycharmProjects/coquiai-TTS/{filename}"
#subprocess.run(["mpv --audio-display=yes", f"/home/kapil/PycharmProjects/coquiai-TTS/{filename}"])
print(path)