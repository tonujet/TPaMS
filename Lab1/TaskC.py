import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import string


def pdf(k, arr):
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
      d = {'x': pdf_x, 'y': pdf_y}
      return d

def build_graphics(number_of_intervals, arr):
      coordinates = pdf(number_of_intervals, arr)
      coordinates["x"] = list(map(lambda el: round(el, 2), coordinates["x"]))
      #Діаграма розмаху
      plt.subplot(2, 2, 1)
      plt.title("Діаграма розмаху")
      plt.boxplot(arr)

      #Графік розподілу
      plt.subplot(2, 2, 2)
      plt.title("Графік розподілу")
      plt.plot(coordinates["x"], coordinates["y"])      

      #Діаграма Парето
      df = pd.DataFrame({'numbers': coordinates["y"]})
      df.index = coordinates["x"]
      df = df.sort_values(by='numbers', ascending=False)
      pareto_x = []
      for i in range(0, len(df.index.values)):
            x = string.ascii_uppercase[i] + f' {df.index.values[i]}'
            pareto_x.append(x)

      plt.subplot(2, 2, 3)
      plt.title("Діаграма Парето")
      plt.bar(pareto_x, df["numbers"].values)


      #Кругова діаграма розподілу
      explode = (0.4, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4, 0.4)
      plt.subplot(2, 2, 4)
      plt.title("Кругова діаграма розподілу")
      plt.pie(coordinates["y"], explode=explode, labels = coordinates["x"], autopct='%1.1f%%')

      plt.show()


