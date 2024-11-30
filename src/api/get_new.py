from fastapi import APIRouter
from helpers.cves_helper import retrieve_cves

MAX_CVES_COUNT = 10

router = APIRouter(tags=['New CVEs'])

def sort_by_date(cves):
    return sorted(cves, key = lambda cve: cve['dateAdded'], reverse=True)

@router.get('/get/new')
def get_new():
    cves = retrieve_cves()
    sorted_cves = sort_by_date(cves)

    return sorted_cves[:MAX_CVES_COUNT]
