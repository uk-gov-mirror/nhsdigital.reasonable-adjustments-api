const consentGet =  {
    method: 'GET',       
    path: '/Consent',
    handler: (request, h) => { 
        if (request.query["patient"] != '9999999998') {
            const path = 'consentGETerror.json'
            return h.response(h.file(path)).code(404);
        }        
        const path = 'consentGET.json'
        return h.file(path)
        .header('content-type', 'application/fhir+json')
        .header('Date', 'Tue, 24 Jul 2018 11:00:01 GMT')
        .header('Access-Control-Allow-Origin', '*');
    }
  };

const consentPost = {
    method: 'POST',
    path: '/Consent',
    handler: (request, h) => {
        if (request.query["patient"] != '9999999998') {
            const path = 'consentPOSTerror.json'
            return h.response(h.file(path)).code(404);
        } 
        const path = 'consentPOST.json'
        return h.response(h.file(path)).code(201)
        .header('content-type', 'application/fhir+json')
        .header('Date', 'Tue, 24 Jul 2018 11:00:01 GMT')
        .header('Last-Modified', '2018-07-24T10:01:00+00:00')
        .header('Location', 'resourceURL')
        .header('Access-Control-Allow-Origin', '*')
        .header('Etag', 'W/"resourceVID”');
    }
};

const consentPut = {
    method: 'PUT',
    path: '/Consent/{consentID}',
    handler: (request, h) => {
        if (request.query["patient"] != '9999999998') {
            const path = 'consentPUTerror.json'
            return h.response(h.file(path)).code(404);
        } 
        const path = 'consentPUT.json'
        return h.file(path)
        .header('content-type', 'application/fhir+json')
        .header('Date', 'Tue, 24 Jul 2018 11:00:01 GMT')
        .header('Last-Modified', '2018-07-24T10:01:00+00:00')
        .header('Access-Control-Allow-Origin', '*')
        .header('Etag', 'W/"resourceVID”');
    }
};

module.exports = [consentGet, consentPost, consentPut]
