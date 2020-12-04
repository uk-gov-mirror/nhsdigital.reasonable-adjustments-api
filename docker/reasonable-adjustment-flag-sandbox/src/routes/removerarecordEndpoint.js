const removerarecordPost = {
    method: 'POST',
    path: '/$removerarecord',
    handler: (request, h) => {
        if (request.query["patient"] != '9999999998') {
            const path = 'removerarecordPOSTerror.json'
            return h.response(h.file(path)).code(404);
        } 
        const path = 'removerarecordPOST.json'
        return h.file(path)
        .header('content-type', 'application/fhir+json')
        .header('Access-Control-Allow-Origin', '*')
        .header('Date', 'Tue, 24 Jul 2018 11:00:01 GMT');
    }
};

module.exports = [removerarecordPost]
