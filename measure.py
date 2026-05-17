from pathlib import Path
from enum import Enum
from datetime import datetime

from numpy import nan
from pandas import DataFrame


class Ex(Enum):
    POMPE = "pompe"
    TRACTION_SUPINATION = "traction supination"
    TRACTION_PRONATION = "traction pronation"
    SQUAT = "squat"
    DIPS = "dips"



def measure_to_str(
        ex : Ex,
        kg : float | tuple[float],
        nb_reps : float | tuple[float],
        nb_series : int = 1,
        min_repos : float | tuple[float] = nan,
        date : datetime = datetime.today().date()
) -> str:
        
    for i in [kg, nb_reps, min_repos] :
            if type(i) == tuple :
                nb_series = len(i)

    array = DataFrame(index=range(nb_series), columns=range(3))

    array.iloc[:,0]=kg
    array.iloc[:,1]=nb_reps
    array.iloc[:,2]=min_repos

    return ",".join([
        date.__str__(),
        (array.iloc[:,0] * array.iloc[:,1]).sum(),
        array.iloc[:,1].sum(),
        nb_series,
        ex.value,
        array.iloc[:,2].sum(skipna=False)
    ])



def freeze_measure(textual_measure: str, path_file: Path | str) -> None:
    with open(path_file, mode="a") as f:
        f.write(f"\n{textual_measure}")
        print(f"Nouvelle mesure enregistrée en dur dans le fichier {path_file.__str__()}")