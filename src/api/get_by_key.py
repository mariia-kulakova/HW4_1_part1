from fastapi import APIRouter
from helpers.cves_helper import retrieve_cves

router = APIRouter(tags=['Known CVEs'])

@router.get('/get')
def get_by_key(query):
    return [
        cve for cve in retrieve_cves() if query.lower() in str(cve).lower()
    ]
