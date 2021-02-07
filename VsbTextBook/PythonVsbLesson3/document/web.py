class Document(object):
    no_of_documents = 0
    total_length = 0
    
    def __init__(self, content):
        self._content = content
        Document.no_of_documents += 1
        Document.total_length += len(self.content)

    def set_content(self, content):
        Document.total_length -= len(self._content)
        self._content = content
        Document.total_length += len(self._content)

    def get_content(self):
        return self._content

    def index(self, db):
        pass

    @staticmethod
    def get_average_length():
        return Document.total_length / Document.no_of_documents

    content = property(get_content, set_content)

d1 = Document("Text")
d2 = Document("Another text")
print(Document.get_average_length()) # 8
d2.content = "This is a bit longer text"
print(d2.content) # "This is a bit longer text"
print(Document.get_average_length()) # 14