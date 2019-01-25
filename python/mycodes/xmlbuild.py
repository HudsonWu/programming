#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class XmlBase:
    '''xml文档的基本结构'''

    def __init__(self, name, level, *features):
        self._name = name
        self._indent = "    "
        self._level = level
        self._features = features

    def addContents(self, contents="\n"):
        self._contents = contents

    def getHead(self):
        self._head = self._indent * self._level + "<{}".format(self._name)
        if self._features:
            for feature in self._features:
                self._head += " {}='{}'".format(feature[0], feature[1])
        self._head += ">"
        return self._head

    def getContents(self):
        return self._contents

    def getEnd(self):
        if (self._contents == "\n"):
            self._end = self._indent * self._level + "</{}>\n".format(self._name)
        else:
            self._end = "</{}>\n".format(self._name)
        return self._end


class BookBuilder:
    '''book型xml构建'''

    def buildBookXml(self, *args, **kwargs):
        xmlTop = XmlBase("book", 0, *args)
        xmlTop.addContents()
        book_xml = xmlTop.getHead() + xmlTop.getContents()
        for key, value in kwargs.items():
            xmlCentre = XmlBase(key, 1)
            xmlCentre.addContents(value)
            book_xml += (xmlCentre.getHead() + xmlCentre.getContents() + \
                         xmlCentre.getEnd())
        book_xml += xmlTop.getEnd()
        return book_xml


class OutlineBuilder:
    '''outline型xml构建'''

    def buildKeywords(self, level, *args):
        '''keywords'''

        xmlTop = XmlBase("keywords", level)
        xmlTop.addContents()
        keywords_xml = xmlTop.getHead() + xmlTop.getContents()
        for keyword in args:
            xmlKeyword = XmlBase("keyword", level + 1)
            xmlKeyword.addContents(keyword)
            keywords_xml += (xmlKeyword.getHead() + xmlKeyword.getContents() + \
                             xmlKeyword.getEnd())
        keywords_xml += xmlTop.getEnd()
        return keywords_xml

    def buildLayer(self, level, name, title, layerxml):
        '''outline, chapter and section'''

        xmlTop = XmlBase(name, level)
        xmlTop.addContents()
        layer_xml = xmlTop.getHead() + xmlTop.getContents()
        if title:
            layerTitle = XmlBase("title", level + 1)
            layerTitle.addContents(title)
            layer_xml += (layerTitle.getHead() + layerTitle.getContents() + \
                      layerTitle.getEnd() + layerxml + xmlTop.getEnd())
        else:
            layer_xml += layerxml + xmlTop.getEnd()
        return layer_xml


def testBuilder():
    book1 = BookBuilder()
    book1Xml = book1.buildBookXml(("id", "book1"), title="Design Pattern", author="Tony", \
                                   description="How to comprehend Design Patterns from daily life.")
    print(book1Xml)

    outline1 = OutlineBuilder()
    keywords_1 = outline1.buildKeywords(3, "design pattern", "daily life")
    section_1 = outline1.buildLayer(2, "section", "section 1", keywords_1)
    chapter_1 = outline1.buildLayer(1, "chapter", "Chapter 1", section_1)
    outline_1 = outline1.buildLayer(0, "outline", None, chapter_1)
    print(outline_1)

if __name__ == "__main__":
    testBuilder()

