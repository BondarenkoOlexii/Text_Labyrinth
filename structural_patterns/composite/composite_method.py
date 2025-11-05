from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass


# Лист (файл)
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f"Файл: {self.name}")


# Композит (папка)
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show(self, indent=0):
        print(" " * indent + f"Папка: {self.name}")
        for child in self.children:
            child.show(indent + 2)



if __name__ == "__main__":
    root = Folder("Головна")
    folder_docs = Folder("Документи")
    folder_music = Folder("Музика")

    file1 = File("резюме.docx")
    file2 = File("звіт.pdf")
    file3 = File("пісня.mp3")

    folder_docs.add(file1)
    folder_docs.add(file2)
    folder_music.add(file3)

    root.add(folder_docs)
    root.add(folder_music)

    root.show()
