# import numpy as np
# A = np.array([[5, 3], [1, 2]])
# B = np.array([40, 18])
# C = np.linalg.solve(A, B)


class SlopeDeflectionMethod(object):
    def __init__(self, span):
        self.span = span

    def get_value_span(self,):
        self.valueOfspan = int(input("Enter the length of the span: "))
        return self.valueOfspan

    def get_point_load(self,):
        self.point_load_magnitude = int(
            input("Enter the magnitude of the point load: "))
        return self.point_load_magnitude

    def get_point(self):
        self.point_distance = int(
            input("Enter the distance from the left end"))
        return self.point_distance

    def get_fixed_end_moment_point_not_center(self, magnitude, span):
        a = self.get_point()
        b = span - a
        self.FEM_not_center_A = 0 - ((magnitude * a * b * b) / span * span)
        self.FEM_not_center_B = ((magnitude * a * a * b) / span * span)
        return self.FEM_not_center_A, self.FEM_not_center_B

    # def get_fem_udl_notfullspan(self):
    #     return pass

    def get_type_of_support():
        SA=input("Enter the type of support 1 for fixed 2 for hinge 3e for rollers:")
        SB=input("Enter the type of support 1 for fixed 2 for hinge 3e for rollers:")
        SC=input("Enter the type of support 1 for fixed 2 for hinge 3e for rollers:")
        return SA,SB,SC

    # def get_type_dl():
    #     return

    # def get_all_the_combination():
    #     return

    def get_udl(self,):
        self.udl_magnitude = int(input("Enter the magnitude of the udl: "))
        return self.udl_magnitude

    def get_fixed_end_moment_point(self, get_point_load, get_value_span):
        self.FEM_point = (get_value_span * get_point_load) / 8
        return self.FEM_point

    def get_fem_udl(self, get_udl, get_value_span):
        self.Fem_udl = ((get_udl * get_value_span * get_value_span) / 12)
        return self.Fem_udl

    def get_FEM(self):
        counter=1
        lengthOfspan = self.get_value_span()
        typeOfLoad = int(input(
            "Enter the type of load for the span 0 for point load 1 for point load(not at center) 2 for udl 3 for vdl and 4 for combination: "))
        if typeOfLoad == 0:
            magnitude = self.get_point_load()
            FEM = self.get_fixed_end_moment_point(magnitude, lengthOfspan)
            counter+=1
            return FEM, lengthOfspan
        
        elif typeOfLoad == 1:
            magnitude = self.get_point_load()
            FEM1,FEM2=self.get_fixed_end_moment_point_not_center(magnitude,lengthOfspan)
            return FEM2, lengthOfspan

        elif typeOfLoad == 2:
            magnitude = self.get_udl()
            FEM = self.get_fem_udl(magnitude, lengthOfspan)
            return FEM, lengthOfspan
        else:
            return ("Your input has either not been taken care of yet or ypo have a wrong input")

    def call_no_of_FeM(self):
        
        span = int(input("Enter the  span  "))

        if span == 2:
            AB, lone = self.get_FEM()
            print("Values for the next span")
            BC, ltwo = self.get_FEM()
            return AB, BC, lone, ltwo

    def get_moment(self):
        a, b, c, d = self.call_no_of_FeM()
        i1 = 1
        i2 = 1
        e = i1 * d
        f = i2 * c
        oA = 0
        oC = 0
        deflection = 0
        s = 0 - ((a) - (b))
        E = 1

        oB = (((s * c * d) / (2 * E) - (e * oA) + (e * 3 * deflection) -
               (f * oC) - (f * 3 * deflection)) / (2 * (e + f)))
        MAB=((2*E*i1)/c)*((2*oA)+oB-3*deflection)-a
        MBA=((2*E*i1)/c)*((2*oB)+oA-3*deflection)+a
        MBC=((2*E*i2)/d)*((2*oB)+oC-3*deflection)-b
        MCB=((2*E*i2)/d)*((2*oC)+oB-3*deflection)+b
        

        return MAB,MBA,MBC,MCB


jeff = SlopeDeflectionMethod("Enter your Span")
print(jeff.get_moment())
# print(jeff.get_FEM())


# point load
# magnitude=[]
# totalDistance=[]
# Moment=[]
# noLoadings=int(input("how many loads are in the System: "))
# for x in range(noLoadings):
#     value=int(input("Enter the magnitude:"))
#     distance=int(input("Enter the distance from the right: "))
#     magnitude.append(value)
#     totalDistance.append(distance)

# for i,j in enumerate(magnitude):
#     answer = j * totalDistance[i]
#     Moment.append(answer)

# print(Moment)

# uniformly distributed
# values=int(input("Enter the magnitude of the udl: "))
# span=int(input("Enter the span: "))
# x=int(input("Enter the First cordinate from the right: "))
# y=int(input("Enter the second cordinate: "))
# udlMagnitude=values * (y-x)  *((y+x)/2)
# print(udlMagnitude)

# varying
# spans

# fixedEndAP=(magnitude[0] * span)/8
# def getFixedEndMoment(value,no,span,magnitude):
#     if value == "point" & no == 1:
#         FEM = (span * magnitude)/8
#         return FEM
#     else:
#         return "not acconted for"


# print("Enter the loads on span AB")
# print("Enter the loads on span BC")
