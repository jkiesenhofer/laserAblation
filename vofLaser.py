import matplotlib.pyplot as plt
import numpy as np
import numpy
import plotly.express as alpha
import plotly.figure_factory as ff
import plotly
import array as arr
# n-2 < 1 ? 1 : (((n+2) ** lambda(n-2)-3)**3)/264;
dict = {
0 : 265,
1 : 265,
2 : 265,
3 : 264.030303030303,
4 : 264.10227272727275,
5 : 263.97237488771356,
6 : 263.97924272590717,
7 : 263.96694040819915,
8 : 263.96752566320095,
9 : 263.9660990702714,
10 : 263.9660347160932,
11 : 263.96575165706764,
12 : 263.9656304120172,
13 : 263.96548988172816,
14 : 263.9653748517192,
15 : 263.96526278127294,
16 : 263.96515872657557,
17 : 263.9650593499736,
18 : 263.96496490092164,
19 : 263.96487458538815,
20 : 263.9647881315668,
21 : 263.9647051647878,
22 : 263.9646254143236,
23 : 263.96454862223527,
24 : 263.96447456828975,
25 : 263.96440305370066,
26 : 263.96433390197626,
27 : 263.9642669542837,
28 : 263.96420206768175,
29 : 263.96413911284236,
30 : 263.9640779724438,
31 : 263.96401853968615,
32 : 263.96396071707335,
33 : 263.96390441535044,
34 : 263.9638495525958,
35 : 263.9637960534323,
36 : 263.9637438483443,
37 : 263.9636928730802,
38 : 263.9636430681307,
39 : 263.9635943782696,
40 : 263.9635467521499,
41 : 263.96350014194564,
42 : 263.96345450303534,
43 : 263.96340979371945,
44 : 263.96336597496907,
45 : 263.96332301020095,
46 : 263.9632808650757,
47 : 263.9632395073169,
48 : 263.9631989065475,
49 : 263.96315903414285,
50 : 263.9631198630973,
51 : 263.9630813679034,
52 : 263.9630435244424,
53 : 263.9630063098846,
54 : 263.96296970259795,
55 : 263.96293368206557,
56 : 263.96289822880954,
57 : 263.96286332432146,
58 : 263.9628289509987,
59 : 263.9627950920857,
60 : 263.9627617316202,
61 : 263.96272885438344,
62 : 263.96269644585436,
63 : 263.9626644921673,
64 : 263.9626329800729,
65 : 263.96260189690156,
66 : 263.96257123053033,
67 : 263.96254096935104,
68 : 263.96251110224193,
69 : 263.96248161854027,
70 : 263.96245250801724,
71 : 263.9624237608548,
72 : 263.96239536762357,
73 : 263.9623673192625,
74 : 263.96233960705973,
75 : 263.96231222263486,
76 : 263.96228515792205,
77 : 263.96225840515456,
78 : 263.96223195684973,
79 : 263.9622058057955
}
transfertAvec = dict.items()
valeurs = list(transfertAvec)
numpyArray = np.array(valeurs)
convexite = numpyArray[:,1]-264;
vof=convexite;
for z in range(len(convexite)):
  vof[z]=abs(vof[z]-vof[z-1])
#plt.xlim(0,50)
#plt.ylim(0.0,2.5)
inclinaison = (vof[60]-vof[20])/40
plt.title("refractive index",inclinaison)
plt.plot(vof)
plt.grid()
plt.show()

c=24
a = 0.0*np.ones((c,c))
beam = np.ones((c,c))
a[0][0]=0.5
b = np.arange(c,0,-1)
i=0
j=0
for z in range(int(c/2),-int(c/2),-1):
  for y in range(-int(c/2),int(c/2),1):
    i=int(y)
    j=int(z)
    r=numpy.sqrt(i**2+j**2)
    beam[j][i]=numpy.exp(-r**2/c**2)
    beam[j][i]=beam[j][i]/beam.max()
    #beam[j][i]=1/r**2
rayf=a*beam;

# z0=1;
# z=0;
# W0=numpy.sqrt(wavelength*z0/numpy.pi);
# Wz=W0*numpy.sqrt(1+(z/z0)**2);
# I ~exp(2r^2/Wz^2)

#beam=100*beam;
# Solid steel (zeros) is surrounded by argon (float numbers) and molten 
# by a laser beam creating a potential flow (centric one number)
i=0
j=0
# iterating and printing each item
for z in range(int(c/2),int(c)-1,1):
  #for y in range(int(c)-7,int(c/2)-7,-1):
  for y in range(int(c/2)-1,0,-1):
    i=int(y)
    j=int(z)
    beam[j][i]=1
f=np.gradient(beam)

for z in range(int(c/2),-int(c/2),-1):
  for y in range(-int(c/2),int(c/2),1):
    i=int(y)
    j=int(z)
    beam[j][i]=abs(beam[j][i]-1)
for z in range(int(c/2),-int(c/2),-1):
  for y in range(-int(c/2),int(c/2),1):
    i=int(y)
    j=int(z)
    beam[j][i]=beam[j][i]/beam.max()

fig = alpha.imshow(beam,text_auto=True)
#fig.show()

#plotly.offline.plot(fig1, filename='alpha.html')

x,y = np.meshgrid(np.arange(0,int(c),1), np.arange(0,int(c),1))
# returns no list
u = np.cos(x)*y
v = np.sin(x)*y

fig = ff.create_quiver(x, y, u, v)
#fig.show()
