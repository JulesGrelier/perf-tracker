from visualizer import Visualizer, datetime, Unit
from measure import Ex, measure_to_str, freeze_measure
import matplotlib.pyplot as plt

path = "./data.csv"
today = datetime.today()

df = Visualizer(path).filter_ex(Ex.TRACTION_SUPINATION).filter_unit(Unit.NB_REPS_PAR_SERIE)
