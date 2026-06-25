import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dtw import *

# extract estimated data from results (the data obtained from the graph)
est_data = pd.read_excel("../results/FigureData1.xlsx", sheet_name="Y-values", header=0, na_values=["N/A", "NaN", "[z]"])
est_data = est_data.dropna()
est_data = est_data[est_data.columns[-1]].astype(float)
est_data = np.array(est_data)

# extract actual data from table - column "Count" on Table_1 from the excel file
actual_data = pd.read_excel("../data/virus-data-report.ods", sheet_name="Table_1", header=4, na_values=["N/A", "Nan", "[z]"])
actual_data = actual_data.dropna()
actual_data = actual_data["Count"].astype(float)
actual_data = np.array(actual_data)

print("\nestimated data: ")
print(est_data)

print("\nactual data: ")
print(actual_data)

# get the residual - vector of xi-hat - xi for the i-th week
residual = est_data - actual_data

print("\nresidual: ")
print(residual)
print("residual mean: ", np.mean(residual))

# modify the xs so they match the week labels
xs = np.arange(27, 27 + 52 - 4)
xs[xs > 52] -= 52


# plot the actual data and the estimated on one plot
plt.plot(range(len(xs)), actual_data, '-b')
plt.plot(range(len(xs)), est_data, '-r')
plt.title("Plot of actual data and estimated data")
plt.legend(["Actual", "Estimated"])
plt.xlabel("Week number")
plt.ylabel("Report count")
plt.xticks(range(0, len(xs), 4), xs[::4])
plt.show()


# plot for the residual
plt.subplot(1, 2, 1)
plt.title("Residual plot")
plt.xlabel("Week number")
plt.plot(range(len(xs)), residual, '-or')
plt.xticks(range(0, len(xs), 4), xs[::4])

# histogram for the residual
plt.subplot(1, 2, 2)
plt.title("Histogram of residual")
plt.hist(residual)
plt.show()

# dtw - estimated vs actual

# define the query and template
query = est_data
template = actual_data

# find the best match with the canonical recursion formula
alignment = dtw(query, template, keep_internals=True)

print(f"\ndistance: {alignment.distance:.2f}") # prints 105.40
print(f"normalized distance: {alignment.normalizedDistance}") # prints 1.10

# display the warping curve, i.e. the alignment curve
alignment.plot(type="threeway", xlab="Estimated data", ylab="Actual data")

# align and plot with the Rabiner-Juang type VI-c unsmoothed recursion
dtw(query, template, keep_internals=True, 
    step_pattern=rabinerJuangStepPattern(6, "c"))\
    .plot(type="twoway",offset=-2)


## see the recursion relation, as formula and diagram
# print(rabinerJuangStepPattern(6,"c"))
# rabinerJuangStepPattern(6,"c").plot()

plt.show()