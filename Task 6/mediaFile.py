class MediaFile:
    def play(self):
        pass


class MP3(MediaFile):
    def play(self):
        print("Playing MP3 file")


class MP4(MediaFile):
    def play(self):
        print("Playing MP4 file")


files = [MP3(), MP4()]

for f in files:
    f.play()
