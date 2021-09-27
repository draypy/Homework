# Task 4.8
#
# Implement a Pagination class helpful to arrange text on pages and list content on given page.
# The class should take in a text and a positive integer which indicate how many symbols
# will be allowed per each page (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that came out
# and method that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
# If you're familliar with using of Excpetions in Python display the error message in this way.
# Pages indexing starts with 0.

class Pagination:
    def __init__(self, text, number):
        self.text = text
        self.number = number
        self.text_on_page = ''
        self.book = self.create_book()

    def create_book(self):
        book = []
        for letter in self.text[:len(self.text) - (len(self.text) // self.number)]:
            self.text_on_page += letter
            if len(self.text_on_page) == self.number:
                book.append(self.text_on_page)
                self.text_on_page = ''
        book.append(self.text[len(self.text) - (len(self.text) // self.number) - 1:])
        return book

    def page_item_count(self):
        return len(self.text)

    def pages_count(self):
        return len(self.book)

    def count_items_on_page(self, number):
        try:
            return len(self.book[number])
        except IndexError:
            return f"Exception: Invalid index. Page is missing."

    def display_page(self, number):
        try:
            return self.book[number]
        except IndexError:
            return f"Exception: Invalid index. Page is missing."

    def find_page(self, string):
        if string in self.text:
            index_ = [i for i in range(len(self.text)) if self.text.startswith(string, i)]
            result = []
            for index in index_:
                if len(string) > self.number:
                    result.append(index // self.number)
                    result.append((index + len(string)) // self.number)
                    continue
                result.append(index // self.number)
            return result

        return f'Exception: "{string}" is missing on the pages'


if __name__ == '__main__':
    x = Pagination('Your beautiful text', 5)
    print(x.find_page('beautiful'))
    print(x.find_page('Your'))
    print(x.find_page('e'))
    print(x.find_page('u'))

    print(x.page_item_count())
    print(x.pages_count())
    print(x.count_items_on_page(0))
    print(x.count_items_on_page(3))
    print(x.count_items_on_page(4))
    print()
    print(x.display_page(0))
    print(x.display_page(3))
    print(x.display_page(5))
