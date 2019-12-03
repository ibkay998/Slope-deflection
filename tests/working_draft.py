# from sloper_deflection import SlopeDeflectionMethod
import typing
import enum


class LoadType(enum.Enum):
    NONE = "none"
    POINT = "point"
    NOPOINT="nopoint"
    UDL = "udl"
    VDL = "vdl"
    MOMENT="moment"
    COMB= "comb"

class EndCondition(enum.Enum):
    FIXED = "fixed"
    ROLLER = "roller"

def determine_moment2(dataset: typing.List[typing.Any], decimal_places: int = None):
    result = get_user_input(dataset)
    a, c, b, d, x, y = result
    i1 = 1
    i2 = 1
    E = 1
    sinking1 = 0/x
    sinking2 = 0/y
    Fcb=d
    e =i1*y
    f=i2*x
    g=E*i2
    h=6*sinking2*(e+f)
    s = ((b) - (c))
    i=s*x*y
    oA = 0
    j=e*oA
    k=e*3*sinking1
    l=f*3*sinking2
    m=(0-((4*e)+(3*f)))
    oC=((((Fcb)*((e*y)+(f*y)))/g)-h-(i/(2*E))-(e*oA)+(e*3*sinking1)-(f*3*sinking2))/(m)
    oB=((0-Fcb)*y)/(2*g)+(3*sinking2) - (2*(oC))
    MAB = ((2 * E * i1) / x) * ((2 * oA) + oB - (3 * sinking1)) - a
    MBA = ((2 * E * i1) / x) * ((2 * oB) + oA - (3 * sinking1)) + b
    MBC = ((2 * E * i2) / y) * ((2 * oB) + oC - (3 * sinking2)) - c
    MCB = ((2 * E * i2) / y) * ((2 * oC) + oB - (3 * sinking2)) + d
    print(MAB)
    print(MBA)
    print(MBC)
    print(MCB)
    to_decimal_places = lambda x: float("%.{}f".format(decimal_places) % x)
    if decimal_places:
        return tuple([to_decimal_places(x) for x in [MAB, MBA, MBC, MCB]])
    return MAB, MBA, MBC, MCB

def determine_moment3(datasetA: typing.List[typing.Any],datasetB, decimal_places: int = None):
    result = get_user_input2(datasetA,datasetB)
    a, b, c, d, x, y = result
    i1 = 1
    i2 = 1
    e = i1 * x
    f = i2 * y
    oA = 0
    oC = 0
    deflection = 0
    s = 0 - ((b) - (c))
    E = 1
    oB = (
        (s * x * y) / (2 * E)
        - (e * oA)
        + (e * 3 * deflection)
        - (f * oC)
        - (f * 3 * deflection)
    ) / (2 * (e + f))
    MAB = ((2 * E * i1) / x) * ((2 * oA) + oB - 3 * deflection) - a
    MBA = ((2 * E * i1) / x) * ((2 * oB) + oA - 3 * deflection) + b
    MBC = ((2 * E * i2) / y) * ((2 * oB) + oC - 3 * deflection) - c
    MCB = ((2 * E * i2) / y) * ((2 * oC) + oB - 3 * deflection) + d
    print(MAB)
    print(MBA)
    print(MBC)
    print(MCB)
    to_decimal_places = lambda x: float("%.{}f".format(decimal_places) % x)
    if decimal_places:
        return tuple([to_decimal_places(x) for x in [MAB, MBA, MBC, MCB]])
    return MAB, MBA, MBC, MCB

def get_user_input(data_input: typing.List[typing.Any],decimal_places: int = None):
    result = [get_Complete(**x) for x in data_input]
    first_tuple_items = [x[0] for x in result]
    middle_tuple_items = [x[1] for x in result]
    last_tuple_items = [x[2] for x in result]
    to_decimal_places = lambda x: float("%.{}f".format(decimal_places) % x)
    if decimal_places:
        return tuple([to_decimal_places(x) for x in [*first_tuple_items,*middle_tuple_items,*last_tuple_items]])
    return [*first_tuple_items,*middle_tuple_items,*last_tuple_items]

def get_user_input2(data_input: typing.List[typing.Any],data_input2):
    result1 = [get_Complete(**x) for x in data_input]
    result2 = [get_Complete(**x) for x in data_input2]
    first=[]
    second=[]
    third=[]
    fourth=[]
    span1 = [i[2] for i in result1]
    span2 = [i[2] for i in result2]
    for i in result1:
        first.append(i[0])
        second.append(i[1])
    for j in result2:
        third.append(j[0])
        fourth.append(j[1])
   
    
    return [sum(first),sum(second),sum(third),sum(fourth),span1[0],span2[0]]


def get_Complete(load_type: LoadType = None, span=None, end_conditions: EndCondition = None, magnitude=None,distance=None,order=None):
    if end_conditions==EndCondition.FIXED: 
        if load_type == LoadType.POINT:
            FEM_point = (span * magnitude) / 8
            return FEM_point,FEM_point,span
        elif load_type == LoadType.UDL:
            FEM_pointu = (span * span * magnitude) / 12
            return FEM_pointu,FEM_pointu,span

        elif load_type == LoadType.MOMENT:
            a = distance
            b = span - distance
            FEM_pointm = (b * magnitude)*((2*a)-b) /(span * span)
            FEM_pointu = (a * magnitude)*((2*b)-a) /(span * span)
            return FEM_pointm,FEM_pointu,span

        elif load_type == LoadType.VDL:
            FEM_point1 = (span * span * magnitude)/30
            FEM_point2 = (span * span * magnitude)/20
            if order== 1:
                return FEM_point1,FEM_point2,span
            elif order ==2:
                return FEM_point2,FEM_point1,span
            else:
                return 0,0,span
        elif load_type == LoadType.NOPOINT:
            a = distance
            b = span - distance
            FEM_not_center_A = ((magnitude * a * b * b) / (span * span))
            FEM_not_center_B = ((magnitude * a * a * b) / (span * span))    
            return FEM_not_center_A,FEM_not_center_B,span
        else:
            pass

    elif end_conditions==EndCondition.ROLLER:
        if load_type == LoadType.POINT:
            FEM_point = (3*magnitude * span)/16
            return FEM_point,0,span

        elif load_type == LoadType.NOPOINT:
            a = distance
            b = span - distance
            FEM_not_center= ((magnitude  / (span * span)*((b*b*a) +((a*a*b)/2))))
            return FEM_not_center,0,span

        elif load_type == LoadType.MOMENT:
            a = distance
            b = span - distance
            FEM_pointm = (b * magnitude)*((2*a)-b) /(span * span)
            FEM_pointu = (a * magnitude)*((2*b)-a) /(span * span)
            return FEM_pointm,0,span

        elif load_type == LoadType.UDL:
            FEM_pointu = (span * span * magnitude) / 8
            return FEM_pointu,0,span
        
        elif load_type == LoadType.VDL:
            FEM_pointv = (span * span * magnitude) / 15
            return FEM_pointv,0,span
        
        else:
            pass
    else: 
        pass






    
