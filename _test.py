import bigpy

if __name__ == "__main__":

    test = bigpy.Bigip(address="https://deadmgmt.dc2.fullproxylabs.com/",
                       username="micheal",
                       password="hanbp2b@fullproxy",
                       key="OD5FURK6L2S5Q4OOPSHUEUFNW2")

    test_cursor = test.cm.SyncStatus(test)
    test_result = test_cursor()
    print(test_result)
