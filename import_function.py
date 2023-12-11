import logging

logging.info('Starting Standard library imports.')
# Standard library imports
import os
import json
import sys

import azure.functions as func

# logging.info('Completed Standard library imports. Starting Third-party imports.')
# # Third-party imports

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

# from google.analytics import data_v1alpha
# from google.analytics.data_v1beta import BetaAnalyticsDataClient
# from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

# logging.info('Completed Third-party imports. Starting Local application imports.')
# # Local application imports
# from other_function import otherFunction

# logging.info('Completed Local application imports. Loading Imports Complete.')

# **NOTE**: The following import statements are not used in this example
# from models.api.request_parser import RequestParser
# from utils.google.ga_extract_data import GAExtractData
# from utils.google.google_auth import GoogleAuth
# from models.api.file_create import create_csv_ga4, get_blob_service_client, get_container_client, upload_blob
# from models.api.string_to_list_parser import string_to_list

importFunction = func.Blueprint()

@importFunction.route(route="import_function")
def import_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python Import Function processed a request.')

    logging.info('Appending Path')
    # Append the path to the packages folder
    sys.path.append(".python_packages\\lib\\site-packages")
    logging.info('Appended Path')

    type = req.params.get('type')
    if not type:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            type = req_body.get('type')

    if type:
        return func.HttpResponse(f"Hello, {type}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
                "This Import Function executed successfully.",
                status_code=200
        )
    