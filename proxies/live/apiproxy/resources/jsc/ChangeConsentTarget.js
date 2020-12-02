if (context.flow === 'TARGET_REQ_FLOW') {
  url = context.getVariable('target.url')
  path = context.getVariable('proxy.pathsuffix')
  queryParams = context.getVariable('request.querystring')

  targetUri = url + path.replace('Consent', 'RAConsent') + '?' + queryParams

  context.setVariable('target.url', targetUri)
}
