import numpy as np
import scipy.stats as stats
import statistics as st

def getMeanInterval(data):
    mean_interval = stats.norm.interval(confidence=0.95, loc = np.mean(data), scale = stats.sem(data))
    return mean_interval

def getSquareDeviationInterval(data):
    df = len(data) - 1 
    confidence = 0.95  
    alpha = 1 - confidence

    chi2_lower = stats.chi2.ppf(alpha / 2, df)
    chi2_upper = stats.chi2.ppf(1 - alpha / 2, df)

    ci_lower = np.sqrt(df * st.stdev(data)**2 / chi2_upper)
    ci_upper = np.sqrt(df * st.stdev(data)**2 / chi2_lower)

    return f"({ci_lower}, {ci_upper})"