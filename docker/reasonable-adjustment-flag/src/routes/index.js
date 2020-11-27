const consentEndpoint = require('./consentEndpoint');
const flagEndpont = require('./flagEndpoint');
const listEndpoint = require('./listEndpoint');
const removerarecordEndpoint = require('./removerarecordEndpoint');
const statusEndpoint = require('./statusEndpoint');
const serverError = require('./serverError');


const routes = [].concat(consentEndpoint, flagEndpont, listEndpoint, removerarecordEndpoint, statusEndpoint, serverError)

module.exports = routes
