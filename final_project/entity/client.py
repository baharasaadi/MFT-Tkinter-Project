from final_project.tools.validators import *


class Client:
    def __init__(self, name, family, birth_date, gender, nationality, national_id, id, start_date, end_date):
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.gender = gender
        self.nationality = nationality
        self.national_id = national_id
        self.id = id
        self.start_date = start_date
        self.end_date = end_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name_validator(name):
            self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if family_validator(family):
            self._family = family

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        if date_validator(birth_date):
            self._birth_date = birth_date

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        if nationality_validator(nationality):
            self._nationality = nationality

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        if national_id_validator(national_id):
            self._national_id = national_id

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if date_validator(start_date):
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if date_validator(end_date):
            self._end_date = end_date
