def userEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "fullName": item["fullName"],
        "email": item["email"],
        "mobileNumber": item["mobileNumber"],
        "dob": item["dob"]
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

