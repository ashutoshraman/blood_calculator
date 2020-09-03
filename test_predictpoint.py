

def test_point_prediction():
    from predictpoint import point_prediction 
    answer= point_prediction((1, 2), (3, 4), 4)
    expected= 5
    assert answer== expected

