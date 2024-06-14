import json

from abc import ABC, abstractmethod

import xml.etree.ElementTree as ET

from app.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book):
        pass


class JsonSerialize(Serialize):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XmlSerialize(Serialize):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def serialize(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")
