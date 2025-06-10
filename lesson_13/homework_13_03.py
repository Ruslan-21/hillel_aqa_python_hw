import xml.etree.ElementTree as ET
import logging
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


logger = logging.getLogger(__name__)


def find_timing_exbytes_incoming(xml_file, group_number):
    xml_path = Path(xml_file)
    if not xml_path.exists():
        logger.error(f"Файл не знайдено: {xml_path}")
        return

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()


        group = root.find(f"{group_number}")

        if group is not None:
            incoming = group.find(".//timingExbytes/incoming")
            if incoming is not None:
                logger.info(f"Для групи з номером {group_number},  {incoming.text}")
            else:
                logger.warning(f"Не знайдено елемента 'incoming' для групи з номером {group_number}.")
        else:
            logger.warning(f"Не знайдено групи з номером {group_number}.")

    except Exception as e:
        logger.error(f"Сталася помилка файлу: {e}")



xml_file_path = Path(__file__).parent /  "work_with_xml" / "groups.xml"
find_timing_exbytes_incoming(xml_file_path, '7')

