import re
from datetime import datetime, date


def name_validator(name):
    if type(name) == str and bool(re.match(r"^[\sa-zA-Z]{2,30}$", name)):
        return name
    else:
        # raise ValueError("Invalid Name !")
        name.set("Invalid Name!")


def family_validator(family):
    if type(family) == str and bool(re.match(r"^[\sa-zA-Z]{2,30}$", family)):
        return family
    else:
        raise ValueError("Invalid Family !")


def nationality_validator(nationality):
    if type(nationality) == str and bool(re.match(r"^[\sa-zA-Z]{2,30}$", nationality)):
        return nationality
    else:
        # raise ValueError("Invalid Name !")
        nationality.set("Invalid Name!")


def national_id_validator(national_id):
    if type(national_id) == str and bool(re.match(r"\d{3}-?\d{6}-?\d", national_id)):
        return national_id
    else:
        raise ValueError("Invalid National Id !")


def date_validator(_date):
    if type(_date) == date:
        return _date
    elif type(_date) == str:
        _date = _date.replace("/", "-").replace(".", "-").replace("_", "-")
        try:
            return datetime.strptime(_date, "%Y-%m-%d").date()
        except:
            raise ValueError("Invalid Date !")
    else:
        raise ValueError("Invalid Date !")
