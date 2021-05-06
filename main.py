import eel
import vigenere

eel.init("web")


@eel.expose
def process_text(input_text, keywords, step_size=0, decrypt=False):
    """Call the Vigenere text processor"""
    return vigenere.process_text(input_text=input_text, keywords=keywords, step_size=int(step_size), decrypt=decrypt)


eel.start("index.html", size=(300, 300))

