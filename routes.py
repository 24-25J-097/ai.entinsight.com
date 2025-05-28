from fastapi import APIRouter, File, UploadFile, HTTPException
import logging

from endpoints import process_xray_image, process_endoscopy_image, process_oral_image, run_inference, detect_objects

router = APIRouter()

# Test route to check server status
@router.get("/apiStatus")
async def test_api():
    """
    Test route to check if the API server is running.
    """
    return {"status": True, "message": "API Server is running and working fine!"}

# Define the API endpoint for predictions
@router.post("/sinusitis/analyze")
async def sinusitis_api(file: UploadFile = File(...)):
    """
    Endpoint to upload a file for sinusitis detection and severity classification.

    - **file**: The image file for sinusitis detection.
    """
    try:
        # Process the uploaded file and return prediction results
        result = await process_xray_image(file)
        return result
    except Exception as e:
        # Return error details in case of failure
        logging.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
     

# Define the API endpoint for cholesteatoma predictions
@router.post("/cholesteatoma/analyze")
async def cholesteatoma_api(file: UploadFile = File(...)):
    """
    Endpoint to upload a file for cholesteatoma detection and stage classification.

    - **file**: The image file for cholesteatoma detection.
    """
    try:
        # Process the uploaded file and return prediction results
        result = await process_endoscopy_image(file)
        return result
    except Exception as e:
        # Return error details in case of failure
        logging.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


# Define the API endpoint for pharyngitis predictions
@router.post("/pharyngitis/analyze")
async def pharyngitis_api(file: UploadFile = File(...)):
    """
    Endpoint to upload a file for pharyngitis detection and severity classification.

    - **file**: The image file for pharyngitis detection.
    """
    try:
        # Process the uploaded file and return prediction results
        result = await process_oral_image(file)
        return result
    except Exception as e:
        # Return error details in case of failure
        logging.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@router.post("/foreign/run-inference")
async def foreign_body_run_interface(file: UploadFile = File(...)):
   try:
      return await run_inference(file)
   except Exception as e:
        # Return error details in case of failure
        logging.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
     
@router.post("/foreign/detect")
async def foreign_body_detect(image: UploadFile = File(...)):
   try:
      return await detect_objects(image)
   except Exception as e:
        # Return error details in case of failure
        logging.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
     