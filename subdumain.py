import requests

target_input = "google.com"

with open ("subdomains.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "http://" + word + "." + target_input
        response = requests.get(url)