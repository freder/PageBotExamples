#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     Documents.py
#
#     Pagebot documents tests. Should become unit tests when finished.

from pagebotcocoa.contexts.drawbot.context import DrawBotContext
from pagebot.contexts.flat.context import FlatContext
#from pagebot.contexts.indesigncontext import InDesignContext
#from pagebot.contexts.htmlcontext import HtmlContext
#from pagebot.contexts.svgcontext import SvgContext
#from pagebot.contexts.idmlcontext import IdmlContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.strings.babelstring import BabelString
from pagebotcocoa.contexts.drawbot.string import DrawBotString
from pagebot.contexts.flat.flatstring import FlatString
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import noColor, color
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.constants import *
from random import random

W, H = A5
H = pt(H)
W = pt(W)
M = 100
s = 36

roboto = findFont('Roboto-Regular')
robotoBold = findFont('Roboto-Bold')
bungee = findFont('BungeeHairline-Regular')

blurb = Blurb()
txt = blurb.getBlurb('news_headline', noTags=True)

testContexts = (
    (FlatContext(), '_export/testFlatString.pdf'),
    (DrawBotContext(), '_export/testDrawBotString.pdf'),
    #(InDesignContext(), '_export/testInDesignString.pdf'),
    #(HtmlContext(), '_export/testHtmlString.pdf'),
    #(InDesignContext(), '_export/testInDesignString.pdf'),
    #(IdmlContext(), '_export/testIdmlString.pdf')
)

def testDocument(context):
    doc = Document(w=W, h=H, context=context)
    print(' - Document in %s is %s' % (context, doc))
    return doc

def testPages(doc):
    page = doc[1]
    print(' - %s' % 'Current page: %s' % page)
    nextPage = page.next
    print(' - %s' % 'Next page: %s' % nextPage)
    print(' - %s' % type(page))
    print(' - %s' % doc.pages)

def testElements(page):
    """
    Functions to be tested:

    def newView(viewId, **kwargs):
    def newPage(**kwargs):
    def newTemplate(**kwargs):
    def newPlacer(**kwargs):
    def newColumn(**kwargs):
    def newTextBox(bs='', **kwargs):
    def newText(bs='', **kwargs):
    def newRect(**kwargs):
    def newQuire(**kwargs):
    def newArtboard(**kwargs):
    def newGroup(**kwargs):
    def newOval(**kwargs):
    def newCircle(**kwargs):
    def newLine(**kwargs):
    def newPolygon(points=None, **kwargs):
    def newRuler(**kwargs):
    def newPageBotPath(**kwargs):
    def newPaths(paths=None, **kwargs):
    def newImage(path=None, **kwargs):
    def newTable(cols=1, rows=1, **kwargs):
    def newGalley(**kwargs):
    """
    conditions = [Right2Right(), Float2Top(), Float2Left()]

    from pagebot.elements.views import viewClasses

    for viewID in viewClasses:
        view = newView(viewID)
        print(' - %s' % view)

    page = newPage()
    print(' - new page %s' % page)


    for n in range(10):
        newLine(x=100, y=n*100, parent=page, stroke=0)

    for n in range(10):
        newRect(w=40, h=42, mr=4, mt=4, parent=page,
                fill=color(random()*0.5 + 0.5, 0, 0.5),
                conditions=conditions)

    score = page.solve()
    print(' - %s' % score)

def build(doc):
    doc.build() # Export?

def export(context):
    context.saveDocument('_export/Test-Documents-%s.pdf' % context.name)

def test():
    objs = {}

    for context, path in testContexts:
        print('* %s' % context.name)
        objs[context.name] = {}
        print(' - Units: %s' % context.units)

        doc = testDocument(context)
        objs[context.name]['doc'] = doc

    for context, path in testContexts:
        print(context.name)
        doc = objs[context.name]['doc']
        testPages(doc)

    for context, path in testContexts:
        print(context.name)
        doc = objs[context.name]['doc']
        # TODO: maybe make this work?
        #page = doc.pages[-1]
        page = doc.pages[1][0]
        print(' - %s' % page)
        print(' - %s' % type(page))
        testElements(page)

    for context, path in testContexts:
        doc = objs[context.name]['doc']
        build(doc)
        export(context)

test()