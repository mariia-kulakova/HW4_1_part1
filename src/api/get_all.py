from fastapi import APIRouter
from helpers.date_time_helper import days_ago
from helpers.cves_helper import retrieve_cves

DATE_FORMAT = '%Y-%m-%d'
MAX_CVES_COUNT = 40

# 4 days ago + today = last 5 days
DAYS_AGO = 4

router = APIRouter(tags=['All CVEs'])

def is_recent(date_added_string):
    return date_added_string > str(days_ago(DAYS_AGO))

@router.get('/get/all')
def get_all():
    cves  = [
        cve for cve in retrieve_cves() if is_recent(cve['dateAdded'])
    ]

    return cves[:MAX_CVES_COUNT]