from fastapi import APIRouter, HTTPException
from app.adapters.xml_to_json_adapter import XMLToJsonAdapter

router = APIRouter()

@router.get("/convert")
def convert_xml_to_json():
    """
    Endpoint que obtiene XML desde una fuente externa y lo convierte a JSON
    """
    try:
        xml_data = """
        <response>
            <user>
                <id>123</id>
                <name>Nicolas Chaves</name>
                <email>nicolas.chaves93@hotmail.com</email>
            </user>
        </response>
        """
        
        json_data = XMLToJsonAdapter.convert(xml_data)
        return json_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
