import ecg_plot

ecg = load_data("a01_3.csv") # load data should be implemented by yourself 
ecg_plot.plot(ecg, sample_rate = 500, title = 'ECG 12')
ecg_plot.show()
