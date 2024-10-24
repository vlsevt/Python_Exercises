"""Music."""
from string import ascii_uppercase


class Note:
    """
    Note class.

    Every note has a name and a sharpness or alteration (supported values: "", "#", "b").
    """

    def __init__(self, note: str):
        """Initialize the class.

        To make the logic a bit easier it is recommended to normalize the notes, that is, choose a sharpness
        either '#' or 'b' and use it as the main, that means the notes will be either A, A#, B, B#, C etc or
        A Bb, B, Cb, C.
        Note is a single alphabetical letter which is always uppercase.
        NB! Ab == Z#
        """
        if len(note) > 1:
            self.note = note[0].upper() + note[1]
        else:
            self.note = note.upper()

    def __repr__(self) -> str:
        """
        Representation of the Note class.

        Return: <Note: [note]> where [note] is the note_name + sharpness if the sharpness is given, that is not "".
        Repr should display the original note and sharpness, before normalization.
        """
        return f"<Note: {self.note[0]}{self.note[1:]}>"

    def get_half(self):
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        letter_index = alphabet.index(self.note[0])
        if len(self.note) > 1:
            if self.note[1] == '#':
                letter_index += 0.5
            else:
                letter_index -= 0.5
        if letter_index == -0.5:
            letter_index = 25.5
        return letter_index

    def __eq__(self, other):
        """
        Compare two Notes.

        Return True if equal otherwise False. Used to check A# (1 + 0,5) == Bb (2 - 0,5) or Ab == Z#
        """
        if not isinstance(other, Note):
            return False
        return self.get_half() == other.get_half()


class NoteCollection:
    """NoteCollection class."""

    def __init__(self):
        """
        Initialize the NoteCollection class.

        You will likely need to add something here, maybe a dict or a list?
        """
        self.notes = []

    def add(self, note: Note) -> None:
        """
        Add note to the collection.

        Check that the note is an instance of Note, if it is not, raise the built-in TypeError exception.

        :param note: Input object to add to the collection
        """
        if not isinstance(note, Note):
            raise TypeError("Input must be an instance of the Note class")
        if note not in self.notes:
            self.notes.append(note)

    def pop(self, note: str) -> Note | None:
        """
        Remove and return previously added note from the collection by its name.

        If there are no elements with the given name, do not remove anything and return None.

        :param note: Note to remove
        :return: The removed Note object or None.
        """
        if len(note) > 1:
            note = note[0].upper() + note[1]
        else:
            note = note.upper()
        for n in self.notes[::-1]:
            if n.note == note:
                self.notes.remove(n)
                return n
        return None

    def extract(self) -> list[Note]:
        """
        Return a list of all the notes from the collection and empty the collection itself.

        Order of the list must be the same as the order in which the notes were added.

        Example:
          collection = NoteCollection()
          collection.add(Note('A'))
          collection.add(Note('C'))
          collection.extract() # -> [<Note: A>, <Note: C>]
          collection.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted everything.

        :return: A list of all the notes that were previously in the collection.
        """
        notes_copy = self.notes.copy()
        self.notes.clear()
        return notes_copy

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the collection.

        Example:
          collection = NoteCollection()
          collection.add(Note('C#'))
          collection.add(Note('Lb'))
          print(collection.get_content())

        Output in console:
           Notes:
            * C#
            * Lb

        The notes must be sorted alphabetically by name and then by sharpness, that is A, A#, B, Cb, C and so on.
        Recommendation: Use normalized note names, not just the __repr__()

        :return: Content as a string
        """
        sorted_notes = sorted(self.notes, key=lambda note: note.note)
        content = "Notes:\n"
        for note in sorted_notes:
            content += f" * {note.note}\n"
        return content.rstrip("\n")


class Chord:
    """Chord class."""

    def __init__(self, note_one: Note, note_two: Note, chord_name: str, note_three: Note = None):
        """
        Initialize chord class.

        A chord consists of 2-3 notes and their chord product (string).
        If any of the parameters are the same, raise the 'DuplicateNoteNamesException' exception.
        """
        if note_three:
            if note_one.note == note_two.note or note_one.note == note_three.note or note_two.note == note_three.note:
                raise DuplicateNoteNamesException("Chord notes must have distinct names.")
        else:
            if note_one.note == note_two.note:
                raise DuplicateNoteNamesException("Chord notes must have distinct names.")
        self.note_one = note_one
        self.note_two = note_two
        self.note_three = note_three
        self.chord_name = chord_name

    def __repr__(self) -> str:
        """
        Chord representation.

        Return as: <Chord: [chord_name]> where [chord_name] is the name of the chord.
        """
        return f"<Chord: {self.chord_name}>"


class Chords:
    """Chords class."""

    def __init__(self):
        """
        Initialize the Chords class.

        Add whatever you need to make this class function.
        """
        self.chords = []

    def add(self, chord: Chord) -> None:
        """
        Determine if chord is valid and then add it to chords.

        If there already exists a chord for the given pair of components, raise the 'ChordOverlapException' exception.

        :param chord: Chord to be added.
        """
        if any({str(chord.note_one), str(chord.note_two), str(chord.note_three)} == {str(c.note_one), str(c.note_two), str(c.note_three)} for c in self.chords):
            raise ChordOverlapException("Chord with these notes already exists.")
        self.chords.append(chord)

    def get(self, first_note: Note, second_note: Note, third_note: Note = None) -> Chord | None:
        """
        Return the chord for the 2-3 notes.

        The order of the first_note and second_note and third_note is interchangeable.

        If there are no combinations for the 2-3 notes, return None

        Example:
          chords = Chords()
          chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
          print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
          print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
          print(chords.get(Note('D'), Note('Z')))  # ->  None
          chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
          print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

        :param first_note: The first note of the chord.
        :param second_note: The second note of the chord.
        :param third_note: The third note of the chord.
        :return: Chord or None.
        """
        chord_notes = [first_note, second_note, third_note] if third_note else [first_note, second_note]
        for c in self.chords:
            if set(str(note) for note in chord_notes) == {str(c.note_one), str(c.note_two), str(c.note_three)}:
                return c
        return None


class DuplicateNoteNamesException(Exception):
    """Raised when attempting to add a chord that has same names for notes and product."""


class ChordOverlapException(Exception):
    """Raised when attempting to add a combination of notes that are already used for another existing chord."""


if __name__ == '__main__':
    note_one = Note('a')  # yes, lowercase
    note_two = Note('C')
    note_three = Note('Eb')
    collection = NoteCollection()

    print(note_one)  # <Note: A>
    print(note_three)  # <Note: Eb>

    print(note_one == note_three)

    collection.add(note_one)
    collection.add(note_two)

    print(collection.get_content())
    # Notes:
    #   * A
    #   * C

    print(collection.extract())  # [<Note: A>,<Note: C>]
    print(collection.get_content())
    # Notes:
    #  Empty

    collection.add(note_one)
    collection.add(note_two)
    collection.add(note_three)

    print(collection.pop('a') == note_one)  # True
    print(collection.pop('Eb') == note_three)  # True

    chords = Chords()
    chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
    print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
    print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
    print(chords.get(Note('D'), Note('Z')))  # ->  None
    chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
    print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

    chords = Chords()

    chord1 = Chord(Note('A'), Note('C#'), 'Amaj', Note('E'))
    chord2 = Chord(Note('E'), Note('G'), 'Emin', note_three=Note('B'))
    chord3 = Chord(Note('E'), Note('B'), 'E5')

    chords.add(chord1)
    chords.add(chord2)
    chords.add(chord3)

    print(chords.get(Note('e'), Note('b')))  # -> <Chord: E5>

    try:
        wrong_chord = Chord(Note('E'), Note('A'), 'E')
        print('Did not raise, not working as intended.')
    except DuplicateNoteNamesException:
        print('Raised DuplicateNoteNamesException, working as intended!')

    try:
        chords.add(Chord(Note('E'), Note('B'), 'Emaj7add9'))
        print('Did not raise, not working as intended.')
    except ChordOverlapException:
        print('Raised ChordOverlapException, working as intended!')
