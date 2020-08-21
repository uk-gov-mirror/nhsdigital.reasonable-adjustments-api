doc = `
API Management Postman Test Runner

Usage:
  test-runner.js <service_name> <environment> [<base_path>]
  test-runner.js -h | --help

  -h --help  Show this text.
`

const docopt = require('docopt').docopt
const fs = require('fs')
const path = require('path')
const newman = require('newman')

function collectionRunner(serviceName, environmentName, basePath) {
  const collectionPath = path.resolve(`e2e/${serviceName}.collection.json`)
  const environmentPath = path.resolve(`e2e/environments/${environmentName}.postman.json`)

  const collection = JSON.parse(fs.readFileSync(collectionPath).toString())
  const environment = JSON.parse(fs.readFileSync(environmentPath).toString())

  const callback = err => {
    if (err) { throw err; }
    console.log('collection run complete!');
  }

  newman.run({
    collection,
    reporters: ['cli', 'junit'],
    reporter: {
      junit: {
        export: './test-report.xml'
      }
    },
    environment

  }, callback)
}

function main(args) {
  const serviceName = args['<service_name>']

  collectionRunner(serviceName, args['<environment>'], args['<base_path>'])
}

args = docopt(doc)
main(args)
