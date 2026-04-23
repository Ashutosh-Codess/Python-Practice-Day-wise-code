class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist

        parts = duration.split(":")
        minutes = int(parts[0])
        seconds = int(parts[1])

        self.duration = minutes * 60 + seconds

    def show(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return self.title + " by " + self.artist + " [" + str(minutes) + ":" + str(seconds) + "]"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def total_duration(self):
        total = 0
        for t in self.tracks:
            total = total + t.duration

        minutes = total // 60
        seconds = total % 60
        return str(minutes) + ":" + str(seconds)

    def longest_track(self):
        longest = self.tracks[0]
        for t in self.tracks:
            if t.duration > longest.duration:
                longest = t
        return longest.show()

    def shortest_track(self):
        shortest = self.tracks[0]
        for t in self.tracks:
            if t.duration < shortest.duration:
                shortest = t
        return shortest.show()


# Main
t1 = Track("Song1", "Artist1", "3:20")
t2 = Track("Song2", "Artist2", "2:30")
t3 = Track("Song3", "Artist3", "4:10")

p = Playlist("My Playlist")

p.add(t1)
p.add(t2)
p.add(t3)

print("Total Duration:", p.total_duration())
print("Longest:", p.longest_track())
print("Shortest:", p.shortest_track())
