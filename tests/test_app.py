# from sloper_deflection import SlopeDeflectionMethod
import typing
<<<<<<< HEAD
from working_draft import LoadType, get_user_input,determine_moment2,EndCondition,get_user_input2,determine_moment3


def test_moment_endCondition():
    def assert_determine_moment2(dataset,_result, decimal_place=None):
        result = determine_moment2(dataset,decimal_places=decimal_place)
=======
from working_draft import (
    determine_moment,
    get_user_input1,
    LoadType,
    get_user_input,
    determine_moment1,
    determine_moment2,
)


# def test_moment():
#     # point scenario
#     def assert_determine_moment(dataset, _result, decimal_place=None):
#         result = determine_moment(dataset, decimal_places=decimal_place)
#         assert result == _result

#     assert_determine_moment(
#         [
#             {"span": 6, "magnitude": 10, "load_type": LoadType.POINT},
#             {"span": 6, "magnitude": 8, "load_type": LoadType.POINT},
#         ],
#         (-7.875, 6.75, -6.75, 5.625),
#     )
#     # udl scenario
#     assert_determine_moment(
#         [
#             {"span": 3, "magnitude": 10, "load_type": LoadType.UDL,},
#             {"span": 4, "magnitude": 10, "load_type": LoadType.UDL,},
#         ],
#         (-1.69643, 2.23214, -2.23214, 2.63393,),
#         decimal_place=5,
#     )
#     # vdl scenario
#     assert_determine_moment(
#         [
#             {"span": 9, "magnitude": 30, "load_type": LoadType.VDL,},
#             {"span": 4, "magnitude": 10, "load_type": LoadType.POINT,},
#         ],
#         (-1.69643, 2.23214, -2.23214, 2.63393,),
#         decimal_place=5,
#     )
def test_moment2():
    def assert_determine_moment2(dataset, _result, decimal_place=None):
        result = determine_moment2(dataset, decimal_places=decimal_place)
>>>>>>> 686e0f6fbb65200a465318d4f7093170dbc2467e
        assert result == _result

    assert_determine_moment2(
        [
<<<<<<< HEAD
            {"span": 4, "magnitude": 10, "load_type": LoadType.POINT,"end_conditions":EndCondition.FIXED, "distance":0,"order":0},
            {"span": 6, "magnitude": 20, "load_type": LoadType.VDL,"end_conditions":EndCondition.ROLLER,"distance":0,"order":1},
=======
            {
                "span": 4,
                "magnitude": 10,
                "load_type": LoadType.POINT,
                "distance": 0,
                "order": 0,
            },
            {
                "span": 6,
                "magnitude": 20,
                "load_type": LoadType.VDL,
                "distance": 0,
                "order": 1,
            },
>>>>>>> 686e0f6fbb65200a465318d4f7093170dbc2467e
        ],
        (7.33, 29.67, -29.67, 0),
        decimal_place=2,
    )

<<<<<<< HEAD
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
=======

def test_moment1():
    def assert_determine_moment1(dataset, _result, decimal_place=None):
        result = determine_moment1(dataset, decimal_places=decimal_place)
        assert result == _result

    assert_determine_moment1(
        [
            {
                "span": 6,
                "magnitude": 20,
                "load_type": LoadType.UDL,
                "distance": 0,
                "order": 0,
            },
            {
                "span": 8,
                "magnitude": 20,
                "load_type": LoadType.POINT,
                "distance": 0,
                "order": 0,
            },
        ],
        (-71.43, 37.14, -37.14, 11.43,),
        decimal_place=2,
    )

    assert_determine_moment1(
        [
            {
                "span": 6,
                "magnitude": 5,
                "load_type": LoadType.NOPOINT,
                "distance": 2,
                "order": 0,
            },
            {
                "span": 6,
                "magnitude": 20,
                "load_type": LoadType.VDL,
                "distance": 0,
                "order": 2,
            },
        ],
        (4.00, 19.11, -19.11, 32.44,),
>>>>>>> 686e0f6fbb65200a465318d4f7093170dbc2467e
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
<<<<<<< HEAD
            {"span": 4, "magnitude": 20, "load_type": LoadType.POINT,"end_conditions":EndCondition.FIXED, "distance":2,"order":0},
        ]
    ]

=======
            {
                "span": 10,
                "magnitude": 30,
                "load_type": LoadType.UDL,
                "distance": 0,
                "order": 0,
            },
            {
                "span": 10,
                "magnitude": 20,
                "load_type": LoadType.NOPOINT,
                "distance": 4,
                "order": 0,
            },
        ],
        (-305.3, 139.4, -139.4, -36.1,),
        decimal_place=2,
    )


# def test_FEM_for_point():
#     dataset = [
#         [
#             [
#                 {"span": 6, "magnitude": 10, "load_type": LoadType.POINT},
#                 {"span": 6, "magnitude": 10, "load_type": LoadType.UDL},
#             ],
#             [30, 30, 6, 6],
#         ],

#     ]
#     released = dataset[0][0]
#     value = [x.get("load_type",None) for x in released]
#     for i in dataset:
#         for j in value:
#             assert get_user_input1(i[0],j) == i[1]
>>>>>>> 686e0f6fbb65200a465318d4f7093170dbc2467e

    for i in dataset:
        for j in datasetB:
            assert get_user_input2(i,j) ==  [9.75, 7.5, 3, 4]

<<<<<<< HEAD
=======
def test_FEM_for_any_loadtype():
    def assert_determine_fem(dataset, _result, decimal_place=None):
        result = get_user_input(dataset, decimal_places=decimal_place)
        assert result == _result

    assert_determine_fem(
        [
            {
                "span": 6,
                "magnitude": 5,
                "load_type": LoadType.NOPOINT,
                "distance": 2,
                "order": 0,
            },
            {
                "span": 6,
                "magnitude": 20,
                "load_type": LoadType.VDL,
                "distance": 0,
                "order": 2,
            },
        ],
        (4.44, 36, 2.22, 24, 6, 6),
        decimal_place=2,
    )
    assert_determine_fem(
        [
            {
                "span": 10,
                "magnitude": 30,
                "load_type": LoadType.UDL,
                "distance": 0,
                "order": 0,
            },
            {
                "span": 10,
                "magnitude": 20,
                "load_type": LoadType.NOPOINT,
                "distance": 4,
                "order": 0,
            },
        ],
        (250, 28.8, 250, 19.2, 10, 10),
        decimal_place=2,
    )
    assert_determine_fem(
        [
            {
                "span": 4,
                "magnitude": 10,
                "load_type": LoadType.POINT,
                "distance": 0,
                "order": 0,
            },
            {
                "span": 6,
                "magnitude": 20,
                "load_type": LoadType.VDL,
                "distance": 0,
                "order": 1,
            },
        ],
        (5, 24, 5, 36, 4, 6),
        decimal_place=2,
    )


# def test_other_types_of_load():
#     # point test
#     dataset = [
#         {"span": 6, "magnitude": 10, "load_type": LoadType.POINT},
#         {"span": 6, "magnitude": 8, "load_type": LoadType.POINT},
#     ]
#     result = get_user_input(dataset)
#     assert result == [7.5, 6.0, 6, 6]
#     # udl test
#     dataset = [
#         {"span": 3, "magnitude": 10, "load_type": LoadType.UDL,},
#         {"span": 4, "magnitude": 10, "load_type": LoadType.UDL,},
#     ]
#     result = get_user_input(dataset)
#     assert result == [1.875, 2.5, 3, 4]
#     # vdl test
#     dataset = [
#         {"span": 9, "magnitude": 30, "load_type": LoadType.VDL,},
#         {"span": 4, "magnitude": 10, "load_type": LoadType.UDL,},
#     ]
#     result = get_user_input(dataset)
#     assert result == [1.875, 2.5, 3, 4]


def custom_result(first, second):
    pass


def one_plus_one(first, second):
    result = custom_result(first, second)
    return result


def test_one_plus_one_equals_two(custom_mocker):
    result = one_plus_one(1, 1)
    assert result == 2
    custom_mocker.assert_called_once_with(1, 1)

>>>>>>> 686e0f6fbb65200a465318d4f7093170dbc2467e
