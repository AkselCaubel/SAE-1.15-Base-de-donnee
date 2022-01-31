import search_veloMag as vmag

y = (vmag.csv_file_reader_per_month_and_day_by_hour("stat_vmag.csv","01-21",["free_vmag_space","total_vmag_space"]))

print(y)