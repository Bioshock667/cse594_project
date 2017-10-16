
#include <maya/MSimple.h>
#include <maya/MGlobal.h>
DeclareSimpleCommand(HelloWorld, "Autodesk", "2016");
MStatus HelloWorld::doIt(const MArgList&)
{
	MGlobal::displayInfo("Hello World!");
	return MS::kSuccess;
}