Lexor Language: HTML plain style writer
=======================================

The plain style writes the document as is. That is, the data in the
text node is printed without any processing.

Processing instruction gets written as

    <?target*

where `*` is a whitespace if the content has no newline. Otherwise
`*` is the newline character. Also, since the attributes do not
collect any of the spaces or newline characters, the plain style
cannot rewrite a file in the same way it was parsed. That is, if the
file was parsed from

    <parent att1="val1"
            att2="val2">
        <child></child>
    </parent>

then this style will print

    <parent att1="val1" att2="val2">
        <child></child>
    </parent>
