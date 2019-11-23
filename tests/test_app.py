# from sloper_deflection import SlopeDeflectionMethod
import typing
from working_draft import determine_result, get_user_input, LoadType


def test_moment():
    # point scenario
    def assert_determine_moment(dataset, _result, decimal_place=None):
        result = determine_result(dataset, decimal_places=decimal_place)
        assert result == _result

    assert_determine_moment(
        [
            {"span": 6, "magnitude": 10, "load_type": LoadType.POINT},
            {"span": 6, "magnitude": 8, "load_type": LoadType.POINT},
        ],
        (-7.875, 6.75, -6.75, 5.625),
    )
    # udl scenario
    assert_determine_moment(
        [
            {"span": 3, "magnitude": 10, "load_type": LoadType.UDL,},
            {"span": 4, "magnitude": 10, "load_type": LoadType.UDL,},
        ],
        (-1.69643, 2.23214, -2.23214, 2.63393,),
        decimal_place=5,
    )


def test_FEM_for_point():
    dataset = [
        [
            [
                {"span": 6, "magnitude": 10, "load_type": "udl"},
                {"span": 6, "magnitude": 8, "load_type": "point"},
            ],
            [7.5, 6.0, 6, 6],
        ],
    ]
    for i in dataset:
        print(i)
        assert get_user_input(i[0]) == i[1]


def test_single_use_case():
    # point test
    dataset = [
        {"span": 6, "magnitude": 10, "load_type": LoadType.POINT},
        {"span": 6, "magnitude": 8, "load_type": LoadType.POINT},
    ]
    result = get_user_input(dataset)
    assert result == [7.5, 6.0, 6, 6]
    # udl test
    dataset = [
        {"span": 3, "magnitude": 10, "load_type": LoadType.UDL,},
        {"span": 4, "magnitude": 10, "load_type": LoadType.UDL,},
    ]
    result = get_user_input(dataset)
    assert result == [1.875, 2.5, 3, 4]

