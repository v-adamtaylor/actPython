import logging
import azure.functions as func

otherFunction = func.Blueprint()

@otherFunction.route(route="http_trigger2")
def http_trigger2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger #2 function processed a request.')

    return func.HttpResponse(
            "HTTP Triggered Function #2 executed successfully.",
            status_code=200
    )
