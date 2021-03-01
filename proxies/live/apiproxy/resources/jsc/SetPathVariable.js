var xSyncWrapped = context.getVariable('request.header.x-sync-wrapped') 
var path = "/STU3/RA"

if (!xSyncWrapped) {
    context.setVariable("Path", path);
} else {
    context.setVariable("Path", null);
}