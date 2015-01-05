#!/usr/bin/env python

class Element(object):
    """Create an html object."""
    opening_tag = "<>"
    closing_tag = "</>"
    tag = u"<html>"
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
    tag = u"<meta charset='UTF-8' />"+"<head>"

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
    tag = u"<hr />"

class br(SelfClosingTag):
    tag = u"<br />"

class A(Element):
    tag = u"<html>"
    def __init__(self, link, content):
        Element.__init__(self, link, content)

class Ul(Element):
    tag = u"<ul>"

class Li(Element):
    tag = u"<ul>"

class Header(OneLineTag):

    def __init__(self, integer, content):
        self.tag = u"<h"+string(integer)+">"
        Element.__init__(self, integer, content)

class Html(Element):

    def render(self, file_out, ind = ""):
        tag = "<!DOCTYPE html>"
        Element.render(self, file_out, ind)

class meta(SelfClosingTag):
    tag = "<meta charset='UTF-8' />"

