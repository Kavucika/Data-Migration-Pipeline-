from fastapi import APIRouter

from app.transformation.pipeline import execute_table_management


router = APIRouter()


@router.post("/transformation")
async def transformation(data: dict):

    try:

        table_management_data = data["result"]["table_management"]

        if table_management_data.get("source") != "oracle":
            return {
                "status": "error",
                "message": "Unsupported source. Only 'oracle' is supported."
            }

        if table_management_data.get("target") != "postgresql":
            return {
                "status": "error",
                "message": "Unsupported target. Only 'postgresql' is supported."
            }

        table_management = table_management_data["table_management"]

        execute_table_management(
            table_management
        )

        return {
            "status": "success",
            "message": "Transformation completed successfully."
        }

    except Exception as error:

        return {
            "status": "error",
            "message": "Transformation failed.",
            "details": str(error)
        }