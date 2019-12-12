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
#     TextBoxes.py
#
#     Tests pagebot text boxes.

from pagebot import getContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.fonttoolbox.objects.font import findFont, Font
from pagebot.toolbox.units import pt, upt
from pagebot.toolbox.color import noColor, color
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.constants import *
from pagebot.style import getRootStyle
from pagebot.contexts.base.babelstring import getFontPath

# TODO: move to basics when finished.

H, W = A3
W = pt(W)
H = pt(H)
M = 50 

roboto = findFont('Roboto-Regular')
pageBotBold = findFont('PageBot-Bold')
pageBotRegular = findFont('PageBot-Regular')
robotoBold = findFont('Roboto-Bold')
bungee = findFont('Bungee-Regular')
bungeeHairline = findFont('Bungee-HairlineRegular')
bungeeOutline = findFont('Bungee-OutlineRegular')

def getString(page):
    # Create a new BabelString with the DrawBot FormattedString inside.
    style=dict(font=bungee, fontSize=36, textFill=(1, 0, 0))
    s = page.newString('This is a string', style=style)

    # Adding or appending strings are added to the internal formatted string.
    # Adding plain strings should inherit the existing style.
    s += ' and more, more, more, more, more, more, more, more, more, more, more, more, more, more, more, more, more, more, more, more,'

    # Reusing the same style with different text fill color.
    style['textFill'] = 0.1, 0.5, 0.9
    style['font'] = bungeeHairline
    s += page.newString(' more and', style=style)

    # Different color and weight.
    style['textFill'] = 0.5, 0, 1
    style['font'] = bungeeOutline
    s += page.newString(' even more!', style=style)
    return s

def drawBaselines(x0, y0, w, baselines, lineHeight, descender, page):
    baseH0 = 0

    for i, baseline in enumerate(baselines):
        y = y0 - baseline
        baseH = baseline - baseH0
        baseH0 = baseline
        newLine(x=x0, y=y, w=w, h=0, stroke=color(0.5), strokeWidth=0.5,
                parent=page)

        if i == 0:
            newRect(x=x0, y=y, w=20, h=lineHeight, fill=color(1, 0, 0, 0.5),
                    parent=page)
            newRect(x=x0, y=y, w=20, h=descender, fill=color(0, 1, 0, 0.5),
                    parent=page)

def test(context):
    print("creating doc")
    doc = Document(w=W, h=H, context=context)
    doc.name = 'TextBoxes-%s' % doc.context.name
    print('# Testing text boxes in %s' % doc)

    page = doc[1]
    #s = getString(page)
    blurb = Blurb()
    txt = blurb.getBlurb('stylewars_bluray')

    i = len(txt.split('. ')[0]) + 1

    style1 = {'font': pageBotBold, 'fontSize': 24, 'lineHeight': 24}
    s = page.newString(txt[0:i], style=style1)

    #style = {'font': pageBotRegular, 'fontSize': 24, 'lineHeight': 24}
    style = {'font': pageBotRegular, 'fontSize': 24, 'lineHeight': 24}
    print(' 2 - %s' % style)
    s += page.newString(txt[i:], style=style)

    fontPath = getFontPath(style1)
    font = Font(fontPath)
    upem = font.getUpem()
    fontSize = style1.get('fontSize')
    ascender = font.getAscender()
    descender = font.getDescender()
    descender = ((fontSize / float(upem)) * descender)
    #leading = upt(style1.get('leading'), base=fontSize)
    lineHeight = style1.get('lineHeight')

    w = W/2 - 2*M
    h = 200 #H - 2*M
    x = M
    y = H - M - h

    sc = color(0.3, 0.2, 0.1, 0.5)
    tb = newTextBox(s, x=x, y=y, w=w, h=h, parent=page, stroke=sc)
    y0 = H - M
    drawBaselines(x, y0, w, tb.baselines, lineHeight, descender, page)

    txt = tb.getOverflow()

    style2 = {'font': bungeeHairline, 'fontSize': 24, 'lineHeight': 24}
    #print(' 3 - %s' % style2)
    print(style2['font'].path)
    s = page.newString(txt, style=style2)
    print(s.style['font'])

    fontPath = getFontPath(style2)
    font = Font(fontPath)
    upem = font.getUpem()
    fontSize = style2.get('fontSize')
    ascender = font.getAscender()
    descender = font.getDescender()
    descender = ((fontSize / float(upem)) * descender)
    #leading = upt(style2.get('leading'), base=fontSize)
    lineHeight = style2.get('lineHeight')

    h = 300 #H - 2*M
    x = W / 2
    y = H / 2 - M - h
    w = W/2 - 2*M
    sc = color(0.3, 0.2, 0.1, 0.5)
    tb = newTextBox(s, x=x, y=y, w=w, h=h, parent=page, stroke=sc)
    y0 =  H / 2 - M 
    drawBaselines(x, y0, w, tb.baselines, lineHeight, descender, page)

    '''
    style = dict(font=bungee, fontSize=pt(48), stroke=color(1, 0, 0))
    s = page.newString(txt, style=style)
    h1 = 300
    y = H - 3*M - h1

    tb = newTextBox(s, x=M, y=y, w=W/2, h=h1, parent=page,
            style=dict(hyphenation=True, language='en', leading=200))

    w, h = tb.getTextSize()
    rect = newRect(x=x, y=y, w=w, h=h, parent=page, stroke=color(1, 0, 0),
            strokeWidth=1)

    for baseline in tb.baselines:
        y = H - 3*M - baseline
        newLine(x=x, y=y, w=W/2, h=0, stroke=color(0.5), strokeWidth=0.5,
                parent=page)
    '''

    #doc.view.drawBaselines()
    print('Starting doc build')
    doc.build()

for contextName in ('DrawBot', 'Flat'):
#for contextName in ('DrawBot',):
#for contextName in ('Flat',):
    context = getContext(contextName)
    test(context)
