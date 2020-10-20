const { Module } = require("module");

const internalServerError = {
    method: 'GET',
    path: '/serverError',
    handler: (request, h) => {   
        const responseMessage = {
            error: 'Internal Server Error'
          } ;
          return h.response(responseMessage).code(500)
    }
};

module.exports = [internalServerError]