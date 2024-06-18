#!/usr/bin/env python3
""" Python script that provides some stats
about Nginx logs stored in MongoDB """


from pymongo import MongoClient


def nginx_logs():
    """ Returns some stats about Nginx logs """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # print total number of documents in the collection nginx
    tot_docs = collection.count_documents({})
    print("{} logs".format(tot_docs))

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count_meth = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count_meth))

    status_check = collection.count_documents(
                                              {"method": "GET",
                                               "path": "/status"}
                                              )
    print("{} status check".format(status_check))


if __name__ == "__main__":
    nginx_logs()
