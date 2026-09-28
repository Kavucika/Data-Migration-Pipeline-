from fastapi import APIRouter

from app.migration.pipeline import execute_migration


router = APIRouter()


@router.post("/migration")
async def migration(data: dict):

    try:

        migration_data = data["result"]

        if migration_data.get("source") != "oracle":
            return {
                "status": "error",
                "message": "Unsupported source. Only 'oracle' is supported."
            }

        if migration_data.get("target") != "postgresql":
            return {
                "status": "error",
                "message": "Unsupported target. Only 'postgresql' is supported."
            }

        if "data_extraction" not in migration_data:
            return {
                "status": "error",
                "message": "data_extraction is required."
            }

        if "data_management" not in migration_data:
            return {
                "status": "error",
                "message": "data_management is required."
            }

        execute_migration(
            migration_data["data_extraction"],
            migration_data["data_management"],
        )

        return {
            "status": "success",
            "message": "Migration completed successfully."
        }

    except Exception as error:

        return {
            "status": "error",
            "message": "Migration failed.",
            "details": str(error)
        }