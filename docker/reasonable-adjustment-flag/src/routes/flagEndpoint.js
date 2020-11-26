const flagGet =  {
    method: 'GET',
    path: '/Flag',
    handler: (request, h) => {
        const path = 'flagGET.json'
        return h.file(path)
    }
  };

const flagPost = {
    method: 'POST',
    path: '/Flag',
    handler: (request, h) => {
        const path = 'flagPOST.json'
        return h.response(h.file(path)).code(201);
    }
};

const flagPut = {
    method: 'PUT',
    path: '/Flag/{flagID}',
    handler: (request, h) => {
        const path = 'flagPUT.json'
        return h.file(path)
    }
};

module.exports = [flagGet, flagPost, flagPut]