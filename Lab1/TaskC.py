import matplotlib.pyplot as plt
import pandas as pd
import string

# Helping functions
def ProbabilityDensityFunction(k, arr):
      pdf_x = [] 
      pdf_y = []  
      n = len(arr) 
      h = (max(arr) - min(arr)) / k 
      a = min(arr) 
      for i in range(0, k):  
            count = 0
            for j in arr:  
                  if (a + i * h) < j < (a + (i * h) + h):
                        count = count + 1
            pdf_x.append(a + i * h + h / 2)  
            pdf_y.append(count / (n * h)) 
      pdf_x = list(map(lambda el: round(el, 2),  pdf_x))
      d = {'x': pdf_x, 'y': pdf_y}
      return d

def sortValues(x, y):
      df = pd.DataFrame({'numbers': y})
      df.index = x
      df = df.sort_values(by='numbers', ascending=False)
      pareto_x = []
      for i in range(0, len(df.index.values)):
            x = string.ascii_uppercase[i] + f' {df.index.values[i]}'
            pareto_x.append(x)
      pareto = {'x': pareto_x, 'y': df["numbers"].values}
      return pareto


# Function to build graphics
def buildboxPlot(arr):
      plt.subplot(2, 2, 1)
      plt.title("Діаграма розмаху")
      plt.boxplot(arr)

def buildPDF(x, y):
      plt.subplot(2, 2, 2)
      plt.title("Графік розподілу")
      plt.plot(x, y) 

def buildPareto(x, y):
      pareto = sortValues(x, y)
      plt.subplot(2, 2, 3)
      plt.title("Діаграма Парето")
      plt.bar(pareto["x"], pareto["y"])

def buildPieDensity(x, y):
      explode = (0.4, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4, 0.4)
      plt.subplot(2, 2, 4)
      plt.title("Кругова діаграма розподілу")
      plt.pie(y, explode=explode, labels = x, autopct='%1.1f%%')

     

def build_graphics(number_of_intervals, arr):
      coordinates = ProbabilityDensityFunction(number_of_intervals, arr)

      buildboxPlot(arr)     
      buildPDF(coordinates["x"], coordinates["y"])
      buildPareto(coordinates["x"], coordinates["y"])
      buildPieDensity(coordinates["x"], coordinates["y"])

      plt.show()


