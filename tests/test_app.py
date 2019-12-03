# from sloper_deflection import SlopeDeflectionMethod
import typing
from working_draft import LoadType, get_user_input,determine_moment2,EndCondition,get_user_input2,determine_moment3


def test_moment_endCondition():
    def assert_determine_moment2(dataset,_result, decimal_place=None):
        result = determine_moment2(dataset,decimal_places=decimal_place)
        assert result == _result

    assert_determine_moment2(
        [
            {"span": 4, "magnitude": 10, "load_type": LoadType.POINT,"end_conditions":EndCondition.FIXED, "distance":0,"order":0},
            {"span": 6, "magnitude": 20, "load_type": LoadType.VDL,"end_conditions":EndCondition.ROLLER,"distance":0,"order":1},
        ],
        (7.33,29.67,-29.67, 0),
        decimal_place=2,
    )

def test_moment():
    def assert_determine_moment2(datasetA, datasetB,_result, decimal_place=None):
        result = determine_moment3(datasetA,datasetB,decimal_places=decimal_place)
        assert result == _result

    assert_determine_moment2(
                [
                    {"span": 6, "magnitude": 10, "load_type": LoadType.POINT, "end_conditions":EndCondition.FIXED, "distance":2,"order":0},
                    {"span": 6, "magnitude": 8, "load_type": LoadType.UDL, "end_conditions":EndCondition.FIXED, "distance":2,"order":0,},
                ],
                [
                    {"span": 3, "magnitude": 20, "load_type": LoadType.POINT,"end_conditions":EndCondition.FIXED, "distance":2,"order":0},
                ],
        (7.33,29.67,-29.67, 0),
        decimal_place=2,
    )

def test_fem():
    dataset=[
                [
                    {"span": 3, "magnitude": 10, "load_type": LoadType.POINT, "end_conditions":EndCondition.FIXED, "distance":2,"order":0},
                    
                ],
            ]
    datasetB=[
        [
            {"span": 4, "magnitude": 20, "load_type": LoadType.POINT,"end_conditions":EndCondition.FIXED, "distance":2,"order":0},
        ]
    ]


    for i in dataset:
        for j in datasetB:
            assert get_user_input2(i,j) ==  [9.75, 7.5, 3, 4]

