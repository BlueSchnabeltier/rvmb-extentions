from hashlib import md5
from random import choice
from urllib.parse import urlencode
from urllib.request import urlretrieve

voices = ["Daniel"]

class Oddcast:
    def __init__(self):
        self.max_chars = 1000
        self.voices = voices

    def run(self, text, filepath, random_voice: bool = False):
        if random_voice:
            pass

        def build_hash(text, engine, voice, language, fx=None, fx_level=None):
            fragments = ["<engineID>%s</engineID>" % engine, "<voiceID>%s</voiceID>" % voice, "<langID>%s</langID>" % language, ("<FX>%s%s</FX>" % (fx, fx_level)) if fx else '', "<ext>mp3</ext>", text]

            return md5("".join(fragments).encode("utf-8")).hexdigest()

        def get_tts_url(text, engine=4, voice=5, language=1, fx=None, fx_level=None):
            hash = build_hash(text, engine=4, voice=5, language=1, fx=None, fx_level=None)
            params = [("engine", engine), ("language", language), ("voice", voice), ("text", text), ("useUTF8", 1), ("fx_type", fx), ("fx_level", fx_level)]
            params = [(key, value) for (key, value) in params if (key and value)]

            return "http://cache-a.oddcast.com/c_fs/%s.mp3?%s" % (hash, urlencode(params))

        urlretrieve(get_tts_url(text), filepath)

    def randomvoice(self):
        return choice(self.voices)