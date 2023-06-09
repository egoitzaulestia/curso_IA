import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

colors = ListedColormap(["#CF672D", "#13944B", "#2D62CF"])

def plot_fronteras_decision(model, X, ax):    
    # Muestra las fronteras de decisión de un modelo de clasificación:
    # * model: Modelo entrenado
    # * X: Array NumPy conteniendo las muestras sobre las que realizar la predicción
    # * ax: Conjunto de ejes de matplotlib en el que mostrar el resultado
    minX = min(X[:, 0]) #valor min de columna 0 de X
    maxX = max(X[:, 0])
    minY = min(X[:, 1])
    maxY = max(X[:, 1]) #valor max de columna 1 de X
    marginX = (maxX - minX) * 0.1
    marginY = (maxY - minY) * 0.1
    #linspace: genera un array NumPy formado por n números equiespaciados entre 2 dados
    #numpy.linspace(valor-inicial, valor-final, número de valores)
    xc = np.linspace(minX - marginX, maxX + marginX, 1000)
    yc = np.linspace(minY - marginY, maxY + marginY, 1000)
    Xc, Yc = np.meshgrid(xc, yc) # meshgrid devuelve matrices de coordenadas
    # ravel: para convertir un array multidimensional en un array de una sola dimensión
    Z = model.predict(np.c_[Xc.ravel(), Yc.ravel()]).reshape(Xc.shape)    
    ax.contourf(Xc, Yc, Z, levels = 2,
        colors = ["#e5c2b3", "#9ec3b6", "#69A3CF"],
        zorder = 0
    )

def mostrar_fronteras(model, X_train = None, X_test = None, 
                      y_train = None, y_test = None, labels = [], show = True):
    """
    Muestra las fronteras de decisión de un modelo de clasificación, y muestra sobre él las observaciones 
    de entrenamiento y de validación:
    * model: Modelo entrenado
    * X_train: Array NumPy con las características de entrenamiento
    * X_test: Array NumPy con las características de validación
    * y_train: Array NumPy con las etiquetas de entrenamiento
    * y_test: Array NumPy con las etiquetas de validación
    * Etiketas: Array NumPy con los identificadores de las etiquetas
    """
    fig, ax = plt.subplots(figsize = (7, 7))
    ax.set_aspect("equal")
    if model != None:
        plot_fronteras_decision(model, X_train, ax)
    # Train dataset
    scatter = plt.scatter(
        x = X_train[:, 0], y = X_train[:, 1], c = y_train,
        cmap = colors, zorder = 2, edgecolor = "#6c6960"
    )
    # Test dataset
    if not(X_test is None):
        scatter = plt.scatter(
            x = X_test[:, 0], y = X_test[:, 1], c = y_test,
            cmap = colors, zorder = 2, edgecolor = "#FFFFFF"
        )
    ax.legend(
        handles = scatter.legend_elements()[0],
        labels = list(labels)
    )

    ax.grid(color = "#f4f4f4", zorder = 1, alpha = 0.4)
    if show:
        plt.show()
    else:
        return fig, ax

