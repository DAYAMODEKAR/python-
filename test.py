# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:17:06 2020
PYTHON CASE STUDY
NAME:DAYA MODEKAR
EMP ID:142900
DATASET:AIRLINE DATA

@author: dayam1
"""

import flightcase as f

DATA = f.read_input_datafile()
print(DATA)
f.sort_by_attribute(DATA)
f.avg_taxout_value(DATA)
f.flight_with_mindist(DATA)
f.insert_avg_elapsed_time(DATA)
SRC = input("Enter the source(IND/IAD/JAX/JAN/ISP.....):")
DST = input("Enter the destination(PHX/BHM/BNA/BWI/MCO....):")
f.display_by_src_dest(DATA, SRC, DST)
f.plot_elapsedtime_avg(DATA)
TAXUPDATE = f.update_taxin_writeto_excel(DATA)
f.write_to_excel(TAXUPDATE)
