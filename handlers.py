import ipaddress

import requests


def validate_ip(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def get_info_by_ip(ip_address):
    if not validate_ip(ip_address):
        return {"error": {"title": "Invalid IP", "message": "Please provide a valid IP address"}, "status": 400}

    address = ip_address.strip()
    url = f"https://ipinfo.io/{address}/json"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Your User-Agent Here"  # Replace with appropriate user-agent
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": {"title": "Service Error", "message": "Unable to fetch IP information. Please try again later."},
            "status": response.status_code}
