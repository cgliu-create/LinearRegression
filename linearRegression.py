import matplotlib.pyplot as plot


def makeScatterGraph(x_values=(), y_values=(), **kwargs):
    x_axis = kwargs.get('x_axis', 'x - axis')
    y_axis = kwargs.get('y_axis', 'y - axis')
    label = kwargs.get('label', 'stars')
    title = kwargs.get('title', 'My scatter plot!')
    plot.scatter(x_values, y_values, color="black", marker="*", label=label)
    calcLinearRegression(x_values, y_values)
    plot.xlabel(x_axis)
    plot.ylabel(y_axis)
    plot.title(title)
    plot.legend()
    plot.show()


def calcLinearRegression(x_values=(), y_values=()):
    multiply = lambda a, b: a * b
    n = len(x_values)
    x_sq_values = map(multiply, x_values, x_values)
    x_y_values = map(multiply, x_values, y_values)
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_x_sq = sum(x_sq_values)
    sum_x_y = sum(x_y_values)
    # equations
    a_value = (sum_y * sum_x_sq - sum_x * sum_x_y) / (n * sum_x_sq - sum_x * sum_x)
    b_value = (n * sum_x_y - sum_x * sum_y) / (n * sum_x_sq - sum_x * sum_x)
    Y = lambda a, b, X: a + b * X
    x_data = (min(x_values), max(x_values))
    a_data = [a_value for i in range(n)]
    b_data = [b_value for i in range(n)]
    y_data = list(map(Y, a_data, b_data, x_data))
    plot.plot(x_data, y_data, label="linear regression")


if __name__ == '__main__':
    xValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    yValues = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]
    makeScatterGraph(xValues, yValues)
