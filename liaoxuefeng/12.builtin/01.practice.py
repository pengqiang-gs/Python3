# _*_ coding: utf-8 _*_

class SAXParseHandler(object):
    def start_element(self, name, attrs):
        print('sax start element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax end element: %s' % name)

    def char_data(self, text):
        print('sax data: %s' % text)

def parse_xml(xml):
    from xml.parsers.expat import ParserCreate

    handler = SAXParseHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)

if __name__ == '__main__':
    xml = """<?xml version="1.0" encoding="UTF-8"?>
        <section name="SearchInDialog">
		<item value="true" key="SearchInProjects"/>
		<item value="true" key="SearchInAppLibs"/>
		<item value="true" key="SearchInJRE"/>
		<item value="true" key="SearchInSources"/>
	</section>"""
    parse_xml(xml)
