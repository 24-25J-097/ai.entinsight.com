from .cholesteatoma import process_endoscopy_image
from .foreign_body import detect_objects, run_inference
from .pharyngitis import process_oral_image
from .sinusitis import process_xray_image

__all__ = [
    "process_oral_image",
    "process_xray_image",
    "detect_objects",
    "run_inference",
    "process_endoscopy_image"
]



