from document.web import Document

class SearchEngine(object):
    
    def __init__(self):
        self.documents = []
    
    def add_document(self, document):
        self.documents.append(document)
    
    def get_documents(self):
        return self.documents
    
    def search(self, query):
        for doc in self.documents:
            if doc.content.find(query) >= 0:
                return doc

se = SearchEngine()
se.add_document(Document("Text"))
se.add_document(Document("Another text"))
for doc in se.get_documents():
    print (doc.get_content())
print(se.search("text").content)