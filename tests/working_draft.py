# from sloper_deflection import SlopeDeflectionMethod
import typing
import enum


class LoadType(enum.Enum):
    NONE = "none"
    POINT = "point"
    UDL = "udl"


def determine_result(dataset: typing.List[typing.Any], decimal_places: int = None):
    result = get_user_input(dataset)
    a, b, c, d = result
    i1 = 1
    i2 = 1
    e = i1 * d
    f = i2 * c
    oA = 0
    oC = 0
    deflection = 0
    s = 0 - ((a) - (b))
    E = 1
    oB = (
        (s * c * d) / (2 * E)
        - (e * oA)
        + (e * 3 * deflection)
        - (f * oC)
        - (f * 3 * deflection)
    ) / (2 * (e + f))
    MAB = ((2 * E * i1) / c) * ((2 * oA) + oB - 3 * deflection) - a
    MBA = ((2 * E * i1) / c) * ((2 * oB) + oA - 3 * deflection) + a
    MBC = ((2 * E * i2) / d) * ((2 * oB) + oC - 3 * deflection) - b
    MCB = ((2 * E * i2) / d) * ((2 * oC) + oB - 3 * deflection) + b
    print(MAB)
    print(MBA)
    print(MBC)
    print(MCB)
    to_decimal_places = lambda x: float("%.{}f".format(decimal_places) % x)
    if decimal_places:
        return tuple([to_decimal_places(x) for x in [MAB, MBA, MBC, MCB]])
    return MAB, MBA, MBC, MCB


def get_user_input(data_input: typing.List[typing.Any]):
    result = [get_FEM(**x) for x in data_input]
    first_tuple_items = [x[0] for x in result]
    last_tuple_items = [x[1] for x in result]
    return [*first_tuple_items, *last_tuple_items]


def get_FEM(load_type: LoadType = None, span=None, magnitude=None):
    if load_type == LoadType.POINT:
        FEM_point = (span * magnitude) / 8
    elif load_type == LoadType.UDL:
        FEM_point = (span * magnitude) / 16
    elif load_type == "vdl":
        FEM_point = (span * magnitude) / 16
    elif load_type == "combination":
        FEM_point == do_Combination()
    return FEM_point, span


def do_Combination(question=None, load_type=None, span=None, magnitude=None):
    question = input("How many loads on  span: ")
    for i in range(question):
        type_of_load = input("Enter the type of load")
