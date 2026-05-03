from enum import Enum

from datetime import datetime
import pandas as pd
from numpy import nan


class Ex(Enum):
    POMPE = "pompe"
    TRACTION_SUPINATION = "traction supination"
    TRACTION_PRONATION = "traction pronation"
    SQUAT = "squat"
    DIPS = "dips"




class Measure():


    @staticmethod
    def as_df(
            ex : Ex,
            kg : float | tuple[float],
            nb_reps : float | tuple[float],
            nb_series : int = nan,
            min_repos : float | tuple[float] = nan,
            date : datetime = datetime.today()
            ) -> pd.DataFrame:
            
            for i in [kg, nb_reps, min_repos] :
                 if type(i) == tuple :
                        nb_series = len(i)

            array = pd.DataFrame(index=range(nb_series), columns=range(3))

            array.iloc[:,0]=kg
            array.iloc[:,1]=nb_reps
            array.iloc[:,2]=min_repos

            return pd.DataFrame({
                "date" : [date.__str__()],
                "tonnage" : [(array.iloc[:,0] * array.iloc[:,1]).sum()],
                "nb_reps" : [array.iloc[:,1].sum()],
                "nb_series" : [nb_series],
                "exercice" : [ex.value],
                "min_repos" : [array.iloc[:,2].sum()]
            })





class Parser_CSV:
    def __init__(self, path):
        self.df_clone = pd.read_csv(path)
        self.path = path


    def add_measure(self, measure : pd.DataFrame):
        self.df_clone = pd.concat([self.df_clone, measure])
        return self


    def clean_measures_pending(self):
        self.df_clone = pd.read_csv(self.path)


    def print_df_clone(self):
        print(self.df_clone)


    def return_df_clone(self) -> pd.DataFrame :
        return self.df_clone


    def send(self):
        text = self.df_clone.to_csv(index=False)

        with open(self.path, "w") as f:
            f.write(text)