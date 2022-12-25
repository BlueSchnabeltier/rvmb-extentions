from hashlib import md5
from random import choice
from utils import settings
from urllib.parse import urlencode
from urllib.request import urlretrieve

voices = ["Alan", "Allison", "Ashley", "Beth", "Brenda", "Bridget", "Catherine", "Daniel", "Dave", "Elizabeth", "Fiona", "Grace", "Hugh", "James", "Jill", "Julie", "Karen", "Kate", "Lakshmi", "Lee", "Matilda", "Moira", "Oliver", "Olivia", "Paul", "Prashant", "Samantha", "Sangeeta", "Serena", "Simon", "Steven", "Susan", "Tessa", "Tom", "Veena"]

class oddcast:
    def __init__(self):
        self.max_chars = 1000
        self.voices = voices

    def run(self, text, filepath, random_voice=False):
        if random_voice:
            voice = self.randomvoice()

        else:
            voice = settings.config["settings"]["tts"]["oddcast_voice"]

        if voice == "Alan":
            voice_id = 9
            engine_id = 2

        elif voice == "Allison":
            voice_id = 7
            engine_id = 2

        elif voice == "Ashley":
            voice_id = 6
            engine_id = 3

        elif voice == "Brenda":
            voice_id = 7
            engine_id = 7

        elif voice == "Bridget":
            voice_id = 4
            engine_id = 3

        elif voice == "Catherine":
            voice_id = 6
            engine_id = 2

        elif voice == "Daniel":
            voice_id = 5
            engine_id = 4

        elif voice == "Dave":
            voice_id = 2
            engine_id = 2

        elif voice == "Elizabeth":
            voice_id = 4
            engine_id = 2

        elif voice == "Fiona":
            voice_id = 12
            engine_id = 4

        elif voice == "Grace":
            voice_id = 10
            engine_id = 2

        elif voice == "Hugh":
            voice_id = 5
            engine_id = 3

        elif voice == "James":
            voice_id = 7
            engine_id = 3

        elif voice == "Jill":
            voice_id = 2
            engine_id = 4

        elif voice == "Julie":
            voice_id = 3
            engine_id = 3

        elif voice == "James":
            voice_id = 7
            engine_id = 3

        elif voice == "Karen":
            voice_id = 4
            engine_id = 4

        elif voice == "Kate":
            voice_id = 1
            engine_id = 3

        elif voice == "Lakshmi":
            voice_id = 5
            engine_id = 7

        elif voice == "Lee":
            voice_id = 10
            engine_id = 4

        elif voice == "Matilda":
            voice_id = 3
            engine_id = 7

        elif voice == "Moira":
            voice_id = 8
            engine_id = 4

        elif voice == "Oliver":
            voice_id = 2
            engine_id = 7

        elif voice == "Olivia":
            voice_id = 1
            engine_id = 7

        elif voice == "Paul":
            voice_id = 2
            engine_id = 3

        elif voice == "Prashant":
            voice_id = 6
            engine_id = 7

        elif voice == "Samantha":
            voice_id = 11
            engine_id = 4

        elif voice == "Sangeeta":
            voice_id = 9
            engine_id = 4

        elif voice == "Serena":
            voice_id = 7
            engine_id = 4

        elif voice == "Simon":
            voice_id = 5
            engine_id = 2

        elif voice == "Steven":
            voice_id = 8
            engine_id = 2

        elif voice == "Susan":
            voice_id = 1
            engine_id = 2

        elif voice == "Tessa":
            voice_id = 13
            engine_id = 4

        elif voice == "Tom":
            voice_id = 3
            engine_id = 4

        elif voice == "Veena":
            voice_id = 11
            engine_id = 2

        def build_hash():
            fragments = [f"<engineID>{engine_id}</engineID>", f"<voiceID>{voice_id}</voiceID>", "<langID>1</langID>", "<ext>mp3</ext>", text]

            return md5("".join(fragments).encode("utf-8")).hexdigest()

        def get_tts_url():
            hash = build_hash()
            params = [("engine", engine_id), ("language", 1), ("voice", voice_id), ("text", text), ("useUTF8", 1), ("fx_type", None), ("fx_level", None)]
            params = [(key, value) for (key, value) in params if (key and value)]

            return "http://cache-a.oddcast.com/c_fs/%s.mp3?%s" % (hash, urlencode(params))

        urlretrieve(get_tts_url(), filepath)

    def randomvoice(self):
        return choice(self.voices)