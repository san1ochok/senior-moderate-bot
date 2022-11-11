from pymongo import MongoClient
from datetime import datetime

from config.config import (
    MONGO_URI,
    DATABASE
)


cluster = MongoClient(MONGO_URI)
db = cluster[f"{DATABASE}"]


def CreateDB(group_id):
    collection = db[f"{group_id}"]


# DEFAULT FUNCTIONS FOR INDIVIDUAL GROUPS 

async def add_user(full_name, user_id, group_id):
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    db[f"{group_id}"].insert_one({
        "_id": user_id,
        "UID": f"{group_id}",
        "group_id": group_id,
        "full_name": full_name,
        "joining_date": str(date),
        "popularity": 0,
        "motto": "null",
        "count_messages": 0,
        "count_limitations": 0,
        "count_reports": 0
    })


async def update_popularity(full_name, user_id, group_id, index):
    db[f"{group_id}"].update_one({
        "_id": user_id,
        "full_name": full_name,
        "group_id": group_id
    },
        {
            "$inc": {
                "popularity": index
            }
        })


async def update_motto(full_name, user_id, group_id, index):
    db[f"{group_id}"].update_one({
        "_id": user_id,
        "full_name": full_name,
        "group_id": group_id
    },
        {
            "$set": {
                "motto": f"{index}"
            }
        }, upsert=False)


async def update_messages(full_name, user_id, group_id, index):
    db[f"{group_id}"].update_one({
        "_id": user_id,
        "full_name": full_name,
        "group_id": group_id
    },
        {
            "$inc": {
                "count_messages": index
            }
        }, upsert=False)


async def update_limitations(full_name, user_id, group_id, index):
    db[f"{group_id}"].update_one({
        "_id": user_id,
        "full_name": full_name,
        "group_id": group_id
    },
        {
            "$inc": {
                "count_limitations": index
            }
        }, upsert=False)


async def update_localization(group_id, index):
    db["localization"].update_one({
        "group_id": group_id
    },
        {
            "$set": {
                "localization": f"{index}"
            }
        }, upsert=False)


async def update_reports(full_name, user_id, group_id, index):
    db[f"{group_id}"].update_one({
        "_id": user_id,
        "full_name": full_name,
        "group_id": group_id
    },
        {
            "$inc": {
                "count_reports": index
            }
        }, upsert=False)


# GLOBAL FUNCTIONS FOR ALL GROUPS

async def add_localization(group_id):
    db["localization"].insert_one({
        "group_id": group_id,
        "localization": "ru"
    })


async def add_userGlobal(full_name, user_id):
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    db["global"].insert_one({
        "_id": user_id,
        "UID": "global",
        "full_name": full_name,
        "joining_date": str(date),
        "popularity": 0,
        "count_messages": 0,
        "count_limitations": 0,
        "count_reports": 0
    })


async def update_popularityGlobal(full_name, user_id, index):
    db[f"global"].update_one({
        "_id": user_id,
        "full_name": full_name
    },
        {
            "$inc": {
                "popularity": index
            }
        })


async def update_messagesGlobal(full_name, user_id, index):
    db[f"global"].update_one({
        "_id": user_id,
        "full_name": full_name
    },
        {
            "$inc": {
                "count_messages": index
            }
        }, upsert=False)


async def update_limitationsGlobal(full_name, user_id, index):
    db[f"global"].update_one({
        "_id": user_id,
        "full_name": full_name
    },
        {
            "$inc": {
                "count_limitations": index
            }
        }, upsert=False)


async def update_reportsGlobal(full_name, user_id, index):
    db[f"global"].update_one({
        "_id": user_id,
        "full_name": full_name
    },
        {
            "$inc": {
                "count_reports": index
            }
        }, upsert=False)


# GET ANY INFO FROM INDIVIDUAL GROUPS

async def get_joiningDate(user_id, group_id):
    index = db[f"{group_id}"].find_one({
        "_id": user_id,
        "group_id": group_id
    })["joining_date"]
    return index


async def get_popularity(user_id, group_id):
    index = db[f"{group_id}"].find_one({
        "_id": user_id,
        "group_id": group_id
    })["popularity"]
    return index


async def get_motto(user_id, group_id):
    index = db[f"{group_id}"].find_one({
        "_id": user_id,
        "group_id": group_id
    })["motto"]
    return index


async def get_localization(group_id):
    index = db["localization"].find_one({
        "group_id": group_id
    })["localization"]
    return index


async def get_messages(user_id, group_id):
    index = db[f"{group_id}"].find_one({
        "_id": user_id,
        "group_id": group_id
    })["count_messages"]
    return index


async def get_limitations(user_id, group_id):
    index = db[f"{group_id}"].find_one({
        "_id": user_id,
        "group_id": group_id
    })["count_limitations"]
    return index


async def get_reports(user_id, group_id):
    index = db[f"{group_id}"].find_one({
        "_id": user_id,
        "group_id": group_id
    })["count_reports"]
    return index


# GET ANY INFO FROM ALL GROUPS

async def get_joiningDateGlobal(user_id):
    index = db[f"global"].find_one({
        "_id": user_id
    })["joining_date"]
    return index


async def get_popularityGlobal(user_id):
    index = db[f"global"].find_one({
        "_id": user_id
    })["popularity"]
    return index


async def get_messagesGlobal(user_id):
    index = db[f"global"].find_one({
        "_id": user_id
    })["count_messages"]
    return index


async def get_limitationsGlobal(user_id):
    index = db[f"global"].find_one({
        "_id": user_id
    })["count_limitations"]
    return index


async def get_reportsGlobal(user_id):
    index = db[f"global"].find_one({
        "_id": user_id
    })["count_reports"]
    return index
