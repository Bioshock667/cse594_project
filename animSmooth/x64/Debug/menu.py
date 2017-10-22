import maya.cmds as mc

win = cmds.window( title="Test Menu", iconName='Short Name', widthHeight=(200, 55) )
mc.columnLayout( adjustableColumn=True )
mc.button( label='Print hello', command="hello()" )
mc.text(label="Name", align='left')
email = mc.textField()
mc.button( label='Close', command=('cmds.deleteUI(\"' + win + '\", window=True)') )
mc.setParent( '..' )
mc.showWindow( win )

def hello():
    name = mc.textField(email, q=True, text=True)
    mc.helloWorld(name)
