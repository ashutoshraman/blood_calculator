def point_prediction(tuple1, tuple2, xval):
    slope = (tuple2[1]-tuple1[1])/(tuple2[0]-tuple1[0])
    y_intercept = tuple1[1] - (slope * tuple1[0])
    yval = slope * xval + y_intercept
    return yval

if __name__ == "__main__":
    point_prediction((1, 2), (3, 4), 5)