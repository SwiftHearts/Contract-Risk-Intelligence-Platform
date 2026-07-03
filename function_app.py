import azure.functions as func
import json
import logging

from Src.contract_risk_app import run_contract_risk_analysis

app = func.FunctionApp()


@app.route(
    route="ContractRiskAnalysis",
    auth_level=func.AuthLevel.ANONYMOUS
)
def ContractRiskAnalysis(req: func.HttpRequest) -> func.HttpResponse:

    logging.info("Contract Risk Analysis request received.")

    try:
        req_body = req.get_json()
        question = req_body.get("question")

        if not question:
            return func.HttpResponse(
                json.dumps({
                    "status": "error",
                    "message": "Question is required."
                }),
                mimetype="application/json",
                status_code=400
            )

        result = run_contract_risk_analysis(question)

        return func.HttpResponse(
            json.dumps({
                "status": "success",
                "answer": result["answer"],
                "sources": result["sources"]
            }),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:

        return func.HttpResponse(
            json.dumps({
                "status": "error",
                "message": str(e)
            }),
            mimetype="application/json",
            status_code=500
        )