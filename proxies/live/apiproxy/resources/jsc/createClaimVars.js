subClaim = context.setVariable('subClaim', 'https://fhir.nhs.uk/Id/sds-role-profile-id|' + context.getVariable('request.header.nhsd-session-urid'))
requestingSystemClaim = context.setVariable('requestingSystemClaim', 'https://fhir.nhs.uk/Id/accredited-system|' + context.getVariable('verifyapikey.VerifyAPIKey.CustomAttributes.asid'))
requestingOrganisationClaim = context.setVariable('requestingOrganisationClaim', 'https://fhir.nhs.uk/Id/ods-organization-code|' + context.getVariable('verifyapikey.VerifyAPIKey.CustomAttributes.ods'))
requestingUserClaim = context.setVariable('requestingUserClaim', 'https://fhir.nhs.uk/Id/sds-role-profile-id|' + context.getVariable('request.header.nhsd-session-urid'))
scope = "scope here"

header = {
  "alg": "none",
  "typ": "JWT"
}

content = {
  reason_for_request: "directcare",
  scope: scope,
  requesting_organization: requestingOrganisationClaim,
  requesting_system: requestingSystemClaim,
  requesting_user: requestingUserClaim
}

headerB64 =Base64.encode(JSON.stringify(header))
contentB64 =Base64.encode(JSON.stringify(content))

context.setVariable("spineJwt", header + "." + content)
