from datetime import datetime, timedelta
import pandas as pd

from parser import Ex


class Visualizer(pd.DataFrame) :

    @staticmethod
    def new(path : str):
        df = Visualizer(pd.read_csv(path, index_col="date", parse_dates=True))

        #Création nouvelles mesures

        return df
    
    def view(self):
        print("\n", self, "\n")


    def select_exercice(self, rhs : Ex):
        return Visualizer(self[self["exercice"] == rhs.value])
    

    def mesure(self, rhs : str):
        return Visualizer(self[rhs])
    

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
