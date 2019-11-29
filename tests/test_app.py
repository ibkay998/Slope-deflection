# from sloper_deflection import SlopeDeflectionMethod
import typing
from working_draft import determine_moment, get_user_input1, LoadType, get_user_input, determine_moment1,determine_moment2


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
        result = determine_moment2(dataset,decimal_places=decimal_place)
        assert result == _result

    assert_determine_moment2(
        [
            {"span": 4, "magnitude": 10, "load_type": LoadType.POINT, "distance":0,"order":0},
            {"span": 6, "magnitude": 20, "load_type": LoadType.VDL,"distance":0,"order":1},
        ],
        (7.33,29.67,-29.67, 0),
        decimal_place=2,
    )


def test_moment1():
    def assert_determine_moment1(dataset, _result, decimal_place=None):
        result = determine_moment1(dataset,decimal_places=decimal_place)
        assert result == _result

    
    
    assert_determine_moment1(
        [
            {"span": 6, "magnitude": 20, "load_type": LoadType.UDL, "distance":0,"order":0},
            {"span": 8, "magnitude": 20, "load_type": LoadType.POINT,"distance":0,"order":0},
        ],
        (-71.43, 37.14, -37.14, 11.43,),
        decimal_place=2,
    )

    assert_determine_moment1(
        [
            {"span": 6, "magnitude": 5, "load_type": LoadType.NOPOINT, "distance":2,"order":0},
            {"span": 6, "magnitude": 20, "load_type": LoadType.VDL,"distance":0,"order":2},
        ],
        (4.00, 19.11, -19.11, 32.44,),
        decimal_place=2,
    )

    assert_determine_moment1(
        [
            {"span": 10, "magnitude": 30, "load_type": LoadType.UDL, "distance":0,"order":0},
            {"span": 10, "magnitude": 20, "load_type": LoadType.NOPOINT,"distance":4,"order":0},
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


def test_FEM_for_any_loadtype():
    def assert_determine_fem(dataset, _result, decimal_place=None):
        result = get_user_input(dataset,decimal_places=decimal_place)
        assert result == _result
    assert_determine_fem(
        [
            {"span": 6, "magnitude": 5, "load_type": LoadType.NOPOINT, "distance":2,"order":0},
            {"span": 6, "magnitude": 20, "load_type": LoadType.VDL,"distance":0,"order":2},
        ],
        (4.44,36,2.22,24, 6, 6),
        decimal_place=2,
    )
    assert_determine_fem(
        [
           {"span": 10, "magnitude": 30, "load_type": LoadType.UDL, "distance":0,"order":0},
           {"span": 10, "magnitude": 20, "load_type": LoadType.NOPOINT,"distance":4,"order":0},
        ],
        (250,28.8,250,19.2, 10, 10),
        decimal_place=2,
    )
    assert_determine_fem(
        [
           {"span": 4, "magnitude": 10, "load_type": LoadType.POINT, "distance":0,"order":0},
           {"span": 6, "magnitude": 20, "load_type": LoadType.VDL,"distance":0,"order":1},
        ],
        (5,24,5,36, 4,6),
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
