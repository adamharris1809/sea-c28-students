#!/usr/bin/env python

class Element(object):
    """Create an html object."""
    opening_tag = "<>"
    closing_tag = "</>"
    indent = ""

class ind(Element):
    indent = "    "

    def __init__(self, content = ""):

        def append(add_content):
            content.append(add_content)

        def render(self, file_out, ind = ""):
            all_out = [self.opening_tag] + self + append + self.closing_tag
            print "\n".join(all_out)
            file_out.write(all_out)
