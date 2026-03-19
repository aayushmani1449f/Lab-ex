class Song:
    def __init__(self, name):
        self.name = name
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, name):
        new_song = Song(name)
        if not self.head:
            self.head = new_song
            self.current = new_song
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_song

    def remove_song(self, name):
        temp = self.head
        prev = None

        if temp and temp.name == name:
            self.head = temp.next
            return

        while temp and temp.name != name:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.name, end=" -> ")
            temp = temp.next

    def play_next(self):
        if self.current:
            print("Playing:", self.current.name)
            self.current = self.current.next
        else:
            print("End of playlist")