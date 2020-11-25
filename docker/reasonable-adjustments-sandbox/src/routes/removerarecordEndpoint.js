const removerarecordPost = {
    method: 'POST',
    path: '/$removerarecord',
    handler: (request, h) => {
        if (!request.headers["x-request-id"]) {
            const path = 'removerarecordPOSTerror.json'
            return h.response(h.file(path)).code(400);
        } 
        const path = 'removerarecordPOST.json'
        return h.file(path)
        .header('content-type', 'application/fhir+json')
        .header('Date', 'Tue, 24 Jul 2018 11:00:01 GMT');
    }
};

module.exports = [removerarecordPost]