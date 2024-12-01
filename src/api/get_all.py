from fastapi import APIRouter
from helpers.date_time_helper import days_ago, datetime_by_format
from helpers.cves_helper import retrieve_cves

CVE_DATE_FORMAT = '%Y-%m-%d'
MAX_CVES_COUNT = 40

# 4 days ago + today = last 5 days
DAYS_AGO = 4

router = APIRouter(tags=['All CVEs'])

def is_recent(cve_date_added_str):
    cve_date_added = datetime_by_format(cve_date_added_str, CVE_DATE_FORMAT).date()

    return cve_date_added > days_ago(DAYS_AGO)

@router.get('/get/all')
def get_all():
    cves  = [
        cve for cve in retrieve_cves() if is_recent(cve['dateAdded'])
    ]

    return cves[:MAX_CVES_COUNT]