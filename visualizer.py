from enum import Enum, auto
from datetime import datetime, timedelta
import pandas as pd

from measure import Ex


class Unit(Enum):
    TONNAGE = auto()
    NB_REPS = auto()
    NB_SERIE = auto()
    KG_PAR_REPS = auto()
    TONNAGE_PAR_SERIE = auto()
    NB_REPS_PAR_SERIE = auto()
    REPOS = auto()
    TONNAGE_PAR_REPOS = auto()
    NB_REPS_PAR_REPOS = auto()


class Visualizer(pd.DataFrame) :


    
    def __init__(self, rhs):
        if isinstance(rhs, str):
            rhs = pd.read_csv(rhs, index_col="date", parse_dates=True)

        super().__init__(rhs)
    

    def print(self):
        print("\n", self, "\n")
    

    ########## DATE ##########


    def day_d(self, d : datetime):
        return Visualizer(self[self.index == d.date().__str__()])
    

    def today(self):
        return self.day_d(datetime.today())


    def dates_between(self, lhs : datetime, rhs : datetime):
        return Visualizer( self[ lhs.__str__() : rhs.__str__() ] )
    

    def dates_after(self, rhs : datetime):
        return Visualizer( self[ rhs.__str__() : datetime.today().__str__() ] )


    def n_days_ago(self, n : int):
        target_date = datetime.today() - timedelta(days = n)
        return self.dates_after(target_date.date())
    

    def this_week(self):
        today = datetime.today()
        last_monday = today - timedelta(days=today.isoweekday() - 1)
        return self.dates_after(last_monday.date())
    

    def this_month(self):
        today = datetime.today()
        first_day_of_the_month = today - timedelta(days=today.day - 1)
        return self.dates_after(first_day_of_the_month.date())
    

    ########## MEASURE ##########

        
    def filter_ex(self, rhs : Ex):
        return Visualizer(self[self["exercice"] == rhs.value])


    def filter_unit(self, u: Unit):
        match u:
            case Unit.TONNAGE:
                return Visualizer(self["tonnage"])
            case Unit.NB_REPS:
                return Visualizer(self["nb_reps"])
            case Unit.NB_SERIE:
                return Visualizer(self["nb_series"])
            case Unit.KG_PAR_REPS:
                return Visualizer(self["tonnage"] / self["nb_reps"])
            case Unit.TONNAGE_PAR_SERIE:
                return Visualizer(self["tonnage"] / self["nb_series"])
            case Unit.NB_REPS_PAR_SERIE:
                return Visualizer(self["nb_reps"] / self["nb_series"])
            case Unit.REPOS:
                return Visualizer(self["min_repos"])
            case Unit.TONNAGE_PAR_REPOS:
                return Visualizer(self["tonnage"] / self["min_repos"])
            case Unit.NB_REPS_PAR_REPOS:
                return Visualizer(self["nb_reps"] / self["min_repos"])

        

