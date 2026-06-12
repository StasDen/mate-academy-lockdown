from app.cafe import Cafe
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)

# FIXME: use annotations for function parameters (class 'Cafe' is already imported)
def go_to_cafe(friends, cafe) -> str:
    total = 0  # NOTE: the variable names should be aligned with implemented flow. I suggest renaming it to 'masks_to_buy'

    for i in range(len(friends)):
        try:
            cafe.visit_cafe(friends[i])
        except (NotVaccinatedError, OutdatedVaccineError):
            return 'All friends should be vaccinated'  # FIXME: use one style of quotes in your code (double quotes are preferable)
        except NotWearingMaskError:
            total += 1

    if total:
        return f'Friends should buy {total} masks'
    else:
        return f'Friends can go to {cafe.name}'  # FIXME: avoid using unnecessary 'else' statement
