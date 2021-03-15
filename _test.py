import bigpy

if __name__ == "__main__":

    bigip = bigpy.Bigip(address="https://deadmgmt.dc2.fullproxylabs.com",
                        username="micheal",
                        password="hanbp2b@fullproxy",
                        verify=False,
                        token="4ZUOOTLYC3UX3AIAJDWEQDTYF5")

    response = bigip.ltm.virtual(selfLink="https://localhost/mgmt/tm/ltm/virtual/~Common~demo-app-2?ver=14.1.2.6")
    link = response.persist[0]["nameReference"]["link"]
    response = bigip.ltm.persistence.source_addr(selfLink=link)
    print(response)