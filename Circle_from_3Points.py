# Enter coordinates for three points

X1 = 3
Y1 = 13
X2 = 15
Y2 = 5
X3 = 20
Y3 = 30

# Test for collinearity
M21 = (Y2 - Y1)/(X2 - X1)
M32 = (Y3 - Y2)/(X3 - X2)
if (M21 == M32):
    print("Those three points are collinear")
else:
    MPX21 = (X2 + X1)/2
    MPY21 = (Y2 + Y1)/2
    MPB21 = -(1/M21)
    print("MidPoint of AB: (" + str(MPX21) + "," + str(MPY21) + ")" )
    print("Slope of AB PerpBis: " + str(MPB21))
    MPX32 = (X3 + X2)/2
    MPY32 = (Y3 + Y2)/2
    MPB32 = (-(1/M32))
    print("MidPoint of BC: (" + str(MPX32) + "," + str(MPY32) + ")" )
    print("Slope of BC PerpBis: " + str(MPB32))
