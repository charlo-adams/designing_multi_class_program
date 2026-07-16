class Diary:

    def __init__(self):
        self.diary = []
        self.todo_list = []
        self.contact_list = []

    def add_to_diary(self, entry):
        self.diary.append(entry)

    def read_diary(self, title):
        for entry in self.diary:
            if entry.title == title:
                return entry.contents
        return None
        
    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_can_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for entry in self.diary:
            if entry.count_words() <= words_can_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable

    def add_to_todo_list(self, todo):
        self.todo_list.append(todo)

    def add_to_contacts(self, number):
        self.contact_list.append(number)