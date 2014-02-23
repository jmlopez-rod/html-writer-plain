"""HTML: PLAIN writer NW test

Testing suite to write HTML in the PLAIN style.

"""

import lexor
from lexor.command.test import compare_with

DOCUMENT = """<!doctype html>
<html>
<body>
    <h1>
        First Heading
    </h1>
    <p>
        First paragraph.
        <?python
print 'This message was printed in python.'
?>
    </p>
</body>
</html>"""

EXPECTED = """<!DOCTYPE html>
<html>
<body>
    <h1>
        First Heading
    </h1>
    <p>
        First paragraph.
        <?python
print 'This message was printed in python.'
?>
    </p>
</body>
</html>"""

def test_plain():
    """html.writer.plain.nw """
    doc, _ = lexor.parse(DOCUMENT, 'html')
    doc.style = 'plain'
    compare_with(str(doc), EXPECTED)
