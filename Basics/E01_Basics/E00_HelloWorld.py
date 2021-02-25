#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#     E00_HelloWorld.py
#
#     Test handling of pages in a document.
#

from pagebot.contexts import getContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, mm
from pagebot.constants import CENTER, LEFT, EXPORT
from pagebot.toolbox.transformer import path2FileName
from pagebot.toolbox.loremipsum import  loremIpsum

# Template for the export path, allowing to include context name
W, H = pt(800), pt(600)
FILENAME = path2FileName(__file__)
FONTNAME = 'Arial'
SQ = 50

def draw(contextName):
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, doc.context.name)
    # Gets the first page from te document.
    page = doc[1]
    page.name = 'First page'
    page.padding = 20
    txt = 'Hello World'
    f = color(0.7)

    # TODO: test these:
    #xTextAlign=CENTER
    #yTextAlign=CENTER
    # showFlowConnections
    options = dict(
            showDimensions=True,
            showFrame=True,
            showOrigin=True,
            showElementInfo=True)

    textBox = newText('Hello World', parent=page, font=FONTNAME, fontSize=96,
            x=W/4, y=W/4, w=W/2, h=H/2, fill=f, **options)

    doc.export(exportPath)

for contextName in [
    # 'DrawBot', 
    'Flat'
]:
    draw(contextName)
