import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import pymel.core as pm
import maya.cmds as mc
import maya.mel as mel

commandName = 'hello'
menuName = "TestMenu"

class MyCommandClass( OpenMayaMPx.MPxCommand ):
    
    def __init__(self):
        ''' Constructor. '''
        OpenMayaMPx.MPxCommand.__init__(self)
    
    def doIt(self, args):
        ''' Command execution. '''
        
        print 'hello world!'

class GUICommandClass( OpenMayaMPx.MPxCommand):

    def __init__(self):
        ''' Constructor. '''
        OpenMayaMPx.MPxCommand.__init__(self)
    def doIt(self, args):
        window = mc.window( title="Long Name", iconName='Short Name', widthHeight=(200, 55) )
        mc.columnLayout( adjustableColumn=True )
        mc.button( label='Say Hello', command=('import maya.cmds as mc; mc.hello()') )
        mc.showWindow( window )

        
def cmdCreator():
    ''' Create an instance of our command. '''
    return OpenMayaMPx.asMPxPtr( MyCommandClass() )

def guiCreator():
    return OpenMayaMPx.asMPxPtr( GUICommandClass() )

def initializePlugin( mobject ):
    ''' Initialize the plug-in when Maya loads it. '''
    mplugin = OpenMayaMPx.MFnPlugin( mobject )
    gMainWindow = mel.eval('$tmpVar=$gMainWindow')
    mc.setParent ( gMainWindow )
    if pm.menu(menuName, exists=True):
        print("Menu found")
    else:
        mc.menu( menuName, parent=gMainWindow, label=menuName)
        mc.menuItem( menuName+"Item1", label="Hello", command="import maya.cmds as mc; mc.hello()")
        mc.menuItem( menuName+"Item2", label="HelloGUI", command="import maya.cmds as mc; mc.hellogui()")
    try:
        mplugin.registerCommand( commandName, cmdCreator )
        mplugin.registerCommand( "hellogui", guiCreator)
    except:
        sys.stderr.write( 'Failed to register command: ' + commandName )

def uninitializePlugin( mobject ):
    ''' Uninitialize the plug-in when Maya un-loads it. '''
    pm.deleteUI(menuName)
    mplugin = OpenMayaMPx.MFnPlugin( mobject )
    try:
        mplugin.deregisterCommand( commandName )
        mplugin.deregisterCommand( 'hellogui' )
    except:
        sys.stderr.write( 'Failed to unregister command: ' + commandName )
