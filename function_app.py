import logging
import azure.functions as func

from other_function import otherFunction
from import_function import importFunction

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger #1 function processed a request.')

    return func.HttpResponse(
            "HTTP Triggered Function #1 executed successfully.",
            status_code=200
    )

app.register_blueprint(otherFunction)
app.register_blueprint(importFunction)
