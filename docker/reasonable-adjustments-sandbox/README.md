# Stub API Server

Stub API Server built using [hapi](https://github.com/hapijs/hapi) deployable as a [Apigee Hosted Target](https://docs.apigee.com/api-platform/hosted-targets/hosted-targets-overview).

Intended for "sandbox" functionality, and is the target endpoint for the hosted docs' *Try it now* functionality.

## Developing

```
make build
make run
```

 * Use the examples from the OAS (`components/examples/`) sym-linking them into the app.

## Deployment

Redeploy the API Proxy. See the main [README.md](../README.md).

## Endpoints

Endpoints are found in /routes

