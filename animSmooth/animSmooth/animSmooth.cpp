
#include <maya/MSimple.h>
#include <maya/MGlobal.h>
#include <maya/MString.h>
#include <maya/MPxToolCommand.h>
#include <maya/MFnPlugin.h>

class animSmooth : public MPxCommand {
public:
	static void* creator()
	{
		return new animSmooth();
	}
	virtual ~animSmooth() {}
	animSmooth() {}
	virtual MStatus doIt(const MArgList& args);
private:
	void printHello(MString name);
};

MStatus animSmooth::doIt(const MArgList& args) {
	printHello(args.asString(0));
	return MS::kSuccess;
}

void animSmooth::printHello(MString name) {
	MString message = MString("Hello ");
	message += name;
	MGlobal::displayInfo(message);
}
MStatus initializePlugin(MObject obj) {
	MStatus status = MStatus::kSuccess;
	MFnPlugin plugin(obj, "AnimSmooth", "1.0", "Any");
	// Register Command
	MGlobal::executeCommand("global string $gMainWindow;\n setParent $gMainWindow;");
	MGlobal::executeCommand("menu -label \"AnimSmooth\" -parent MayaWindow -tearOff 1 TestMenu;");
	MGlobal::executeCommand(MString("menuItem -label \"Say Hello\" -echoCommand true -command \"python(\\\"execfile(\\\\\\\"" +
		plugin.loadPath() + "/menu.py" + "\\\\\\\")\\\")\" TestMenuItem1;"));
   status = plugin.registerCommand("helloWorld", animSmooth::creator);
   return status;

}

MStatus uninitializePlugin(MObject obj)
{
	MStatus   status = MStatus::kSuccess;
	MFnPlugin plugin(obj);

	MGlobal::executeCommand("deleteUI -m TestMenu");

	status = plugin.deregisterCommand("helloWorld");
	if (!status) {
		status.perror("deregisterCommand");
		return status;
	}

	return status;
}
