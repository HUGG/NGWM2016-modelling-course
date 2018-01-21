# Visit 2.10.0 log file
ScriptVersion = "2.10.0"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
ShowAllWindows()
