import xml.etree.ElementTree as ET

class XMLToJsonAdapter:
    """
    Clase Adaptadora que convierte XML a JSON
    """
    @staticmethod
    def convert(xml_data: str) -> dict:
        try:
            root = ET.fromstring(xml_data)
            return XMLToJsonAdapter._xml_to_dict(root)
        except ET.ParseError:
            raise ValueError("Error al analizar XML")

    @staticmethod
    def _xml_to_dict(element):
        children = list(element)
        
        # Si no tiene hijos, devuelve el texto directamente
        if not children:
            return element.text.strip() if element.text else ""

        # Si tiene hijos, crear un diccionario sin duplicar claves
        result = {}
        for child in children:
            result[child.tag] = XMLToJsonAdapter._xml_to_dict(child)
        
        return result