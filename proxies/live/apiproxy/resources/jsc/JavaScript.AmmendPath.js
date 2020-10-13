var parameter = properties.path; // Returns "response.status.code"
var path = context.getVariable(parameter).substring(1); // Get the value of response.status.code
context.setVariable("trimmedPath", path);