subClaim = context.setVariable('subClaim', 'https://fhir.nhs.uk/Id/sds-role-profile-id|' + context.getVariable('request.header.nhsd-session-urid'))
requestingSystemClaim = context.setVariable('requestingSystemClaim', 'https://fhir.nhs.uk/Id/accredited-system|' + context.getVariable('verifyapikey.VerifyAPIKey.CustomAttributes.asid'))
requestingOrganisationClaim = context.setVariable('requestingOrganisationClaim', 'https://fhir.nhs.uk/Id/ods-organization-code|' + context.getVariable('verifyapikey.VerifyAPIKey.CustomAttributes.ods'))
requestingUserClaim = context.setVariable('requestingUserClaim', 'https://fhir.nhs.uk/Id/sds-role-profile-id|' + context.getVariable('request.header.nhsd-session-urid'))
scope = "scope here"

jwt = {
  reason_for_request: "directcare",
  scope: scope,
  requesting_organization: requestingOrganisationClaim,
  requesting_system: requestingSystemClaim,
  requesting_user: requestingUserClaim
}

jwt_b64 =btoa(JSON.stringify(jwt))

context.setVariable("spineJwt",jwt_b64)
