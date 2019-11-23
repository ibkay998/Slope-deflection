# from sloper_deflection import SlopeDeflectionMethod
import typing
from working_draft import determine_result, get_user_input


def test_moment():
    result = determine_result(
        [
            {"span": 6, "magnitude": 10},
            {"span": 6, "magnitude": 8},
        ]
    )
    assert result == (-7.875, 6.75, -6.75, 5.625)


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
    dataset = [
        {"span": 6, "magnitude": 10, "load_type": "point"},
        {"span": 6, "magnitude": 8, "load_type": "point"},
    ]
    result = get_user_input(dataset)
    assert result == [7.5, 6.0, 6, 6]

