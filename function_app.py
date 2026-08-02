# Import Azure Functions library for creating HTTP-triggered functions
import azure.functions as func

# Import JSON library for handling JSON data
import json

# Import logging library for logging information and errors
import logging

# Import the run_contract_risk_analysis function from the contract_risk_app module
from Src.contract_risk_app import run_contract_risk_analysis

# Create an instance of the Azure Functions app
app = func.FunctionApp()

# Define an HTTP-triggered function named ContractRiskAnalysis that handles POST requests
@app.route(
    # Define the route for the Azure Function that handles contract risk analysis requests
    route="ContractRiskAnalysis",
    # Anyone can access this function without authentication, as specified by the auth_level parameter
    auth_level=func.AuthLevel.ANONYMOUS
)
# Define the ContractRiskAnalysis function that processes incoming HTTP requests for contract risk analysis
# Req contains the HTTP request data, and -> func.HttpResponse indicates that the function will return an HTTP response
def ContractRiskAnalysis(req: func.HttpRequest) -> func.HttpResponse:

    # Log in Azure that a contract risk analysis request has been received
    logging.info("Contract Risk Analysis request received.")

    # Try to process the incoming request and handle any exceptions that may occur
    try:
        # Get the JSON data from the incoming HTTP request
        req_body = req.get_json()
        # Extract the "question" field from the JSON data, which contains the user's contract risk question
        question = req_body.get("question")

        # Check if the question is provided in the request body; if not, return an error response
        if not question:
            return func.HttpResponse(
                # Convert the error message to JSON format and set the response mimetype to application/json
                json.dumps({
                    "status": "error",
                    "message": "Question is required."
                }),
                #
                mimetype="application/json",
                status_code=400
            )
        # Call the run_contract_risk_analysis function to analyze the contract risk based on the provided question
        result = run_contract_risk_analysis(question)

        # Check if the analysis was successful; if so, return the answer and sources in the response
        return func.HttpResponse(
            json.dumps({
                "status": "success",
                "answer": result["answer"],
                "sources": result["sources"]
            }),
            mimetype="application/json",
            status_code=200
        )

    # Handle any exceptions that occur during processing and return an error response with the exception message
    except Exception as e:

        return func.HttpResponse(
            json.dumps({
                "status": "error",
                "message": str(e)
            }),
            # Set the response mimetype to application/json and return a 500 Internal Server Error status code
            mimetype="application/json",
            status_code=500
        )