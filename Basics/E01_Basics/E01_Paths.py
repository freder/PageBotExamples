#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     01_FilePaths.py
#
#     Shows how get pagebot file paths.
#     Not to be confused with BezierPaths and PageBotPath,
#     which are a different things: paths of polyons to draw.
#

# Import all top-level values, such as the getContext() function.
from pagebot import *
from pagebot.filepaths import getResourcesPath
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.units import pt
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.document import Document
from pagebot.toolbox.units import pt

# Import a standard page size tuple with format (w, h) and unpack it.
from pagebot.constants import A3
H, W = A3
GUTTER = pt(12)

def showFilePaths(context):
    # Get the context that this script runs in, e.g. DrawBotApp.
    print('Context:', context)

    # Make a Document instance for this size and context, intializing one page.
    doc = Document(w=W, h=H, context=context)

    # Get the page.
    page = doc[1]

    # Make a set of conditions for the element positions of this page.
    c = (Left2Left(), Fit2Right(), Float2Top())

    # Find the demo font, as supplied with the PageBot library installation.
    # This is a subset of TYPETR Upgrade Regular.
    f = findFont('PageBot-Regular')

    rootPath = getRootPath() # Location of this PageBot library
    style = dict(fontSize=14, font=f)
    msg = 'Root path is %s' % rootPath
    bs = context.newString(msg, style)
    makeText(bs, page, f, c)

    resourcesPath = getResourcesPath()
    msg = 'Resources path is %s' % resourcesPath
    bs = context.newString(msg, style)
    makeText(bs, page, f, c)
    #print(glob.glob('%s/*' % resourcesPath))

    font = findFont('PageBot-Regular')
    msg = 'Default font path is %s' % font.path
    msg = '\n\t'.join(msg.split('/'))
    bs = context.newString(msg, style)
    c = (Right2Right(), Float2Top())
    e = makeText(bs, page, f, c)
    e.w = page.pw/2 - 2*GUTTER
    e.mr = 0

    msg = 'PageBot font path is %s' % f.path
    msg = '\n\t'.join(msg.split('/'))
    bs = context.newString(msg, style)
    c = (Left2Left(), Float2Top())
    e = makeText(bs, page, f, c)
    e.w = page.pw/2 - 2*GUTTER

    # Let the page solve all of its child element layout conditions.
    page.solve()
    doc.export('_export/01_Paths-%s.pdf' % context.name)

def makeText(t, page, f, c):
    """Create a new text box with e give layout conditions
    and with page as parent."""
    return newText(t, font=f, parent=page, conditions=c, fill=0.9,
        margin=GUTTER)


for contextName in ('DrawBot',): #, 'Flat'):
    context = getContext(contextName)
    showFilePaths(context)