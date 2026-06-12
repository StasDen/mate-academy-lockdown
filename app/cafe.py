# FIXME
# Please do not import multiple modules like this. To improve readability, use parentheses instead:
# from app.errors import (
#     NotVaccinatedError,
#     OutdatedVaccineError,
#     NotWearingMaskError
# )
from app.errors import NotVaccinatedError, \
                        OutdatedVaccineError, \
                        NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, vstr: dict) -> str:
        if "vaccine" not in vstr.keys() or vstr["vaccine"] == None:  # FIXME: 2nd statement could be more efficient: '... or not vstr["vaccine"]'
            raise NotVaccinatedError("not vaccinated")
        elif vstr["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("outdated")  # FIXME: error messages should be more descriptive (e.g., 'Client's vaccine is outdated')
        elif not vstr["wearing_a_mask"]:
            raise NotWearingMaskError("not wearing mask")
        else:
            return "Welcome to " + self.name  # FIXME: avoid using unnecessary 'else' statement
