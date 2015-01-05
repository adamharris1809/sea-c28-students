#!/usr/bin/env python

class Element(object):
    """Create an html object."""
    opening_tag = "<>"
    closing_tag = "</>"
    tag = u"html"
    indent = "    "

    def __init__(self, content = "", **kwargs):
        if kwargs:
            self.attribute = kwargs

    def append(self, add_content):
        content.append(add_content)

    def render(self, file_out, ind = ""):
        all_out = [self.opening_tag] + self + append.content + self.kwargs + [self.closing_tag]
        print "\n".join(all_out)
        file_out.write(all_out)

class body(Element):
    tag = "<body>"

class p(Element):
    tag = u'<p>'

class head(Element):
    tag = u'<head>'

class OneLineTag(Element):
    """Override the render method to render everything on one line."""

    def render(self,file_out, ind = ""):
        all_out = [self.opening_tag] + self + append.content + self.closing_tag
        print "\n".join(all_out)
        file_out.write(all_out)

class Title(OneLineTag):
    tag = u"<title>"

class SelfClosingTag(Element):
    def render(self, file_out, ind = ""):
        all_out = self.tag

class hr(SelfClosingTag):
    tag = "<hr />"

class br(SelfClosingTag):
    tag = "<br />"

