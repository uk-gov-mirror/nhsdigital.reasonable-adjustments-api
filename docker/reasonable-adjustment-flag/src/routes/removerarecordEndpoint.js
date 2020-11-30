const removerarecordPost = {
    method: 'POST',
    path: '/$removerarecord',
    handler: (request, h) => {
        const path = 'removerarecordPOST.json'
        return h.file(path)
        .header('content-type', 'application/fhir+json')
        .header('Date', 'Tue, 24 Jul 2018 11:00:01 GMT');
    }
};

module.exports = [removerarecordPost]
