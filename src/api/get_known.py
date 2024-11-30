from fastapi import APIRouter
from helpers.cves_helper import retrieve_cves

MAX_CVES_COUNT = 10
KNOWN_RANSOMWARE_CAMPAIGN_USE = 'Known'

router = APIRouter(tags=['Known CVEs'])

@router.get('/get/known')
def get_known():
    cves  = [
        cve for cve in retrieve_cves()
            if cve['knownRansomwareCampaignUse'] == KNOWN_RANSOMWARE_CAMPAIGN_USE
    ]

    return cves[:MAX_CVES_COUNT]
