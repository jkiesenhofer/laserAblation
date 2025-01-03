import matplotlib.pyplot as plt
import numpy as np
import numpy
import array as arr
dict = { 
0 : 265,
1 : 265,
2 : 265,
3 : 264.0151515151515,
4 : 264.03409090909093,
5 : 264.01470153650905,
6 : 264.01405887902126,
7 : 264.0146581739809,
8 : 264.0146571090187,
9 : 264.01461433569045,
10 : 264.01459471262206,
11 : 264.0145783073663,
12 : 264.01456239145693,
13 : 264.01454752960586,
14 : 264.01453367726754,
15 : 264.0145206847274,
16 : 264.0145084487321,
17 : 264.0144968878129,
18 : 264.0144859322255,
19 : 264.0144755222756,
20 : 264.0144656066925,
21 : 264.01445614109707,
22 : 264.0144470868102,
23 : 264.01443840991953,
24 : 264.0144300805285,
25 : 264.01442207214694,
26 : 264.0144143611937,
27 : 264.01440692658576,
28 : 264.01439974939836,
29 : 264.0143928125802,
30 : 264.0143861007147,
31 : 264.01437959981774,
32 : 264.01437329716555,
33 : 264.01436718114815,
34 : 264.0143612411433,
35 : 264.01435546740737,
36 : 264.01434985098155,
37 : 264.0143443836097,
38 : 264.0143390576668,
39 : 264.01433386609654,
40 : 264.01432880235603,
41 : 264.01432386036737,
42 : 264.01431903447457,
43 : 264.0143143194055,
44 : 264.0143097102381,
45 : 264.0143052023697,
46 : 264.01430079149065,
47 : 264.01429647355945,
48 : 264.01429224478125,
49 : 264.0142881015881,
50 : 264.01428404062136,
51 : 264.0142800587157,
52 : 264.01427615288435,
53 : 264.0142723203061,
54 : 264.01426855831323,
55 : 264.0142648643808,
56 : 264.01426123611634,
57 : 264.0142576712511,
58 : 264.0142541676312,
59 : 264.0142507232105,
60 : 264.01424733604347,
61 : 264.01424400427834,
62 : 264.01424072615157,
63 : 264.01423749998224,
64 : 264.0142343241669,
65 : 264.0142311971749,
66 : 264.0142281175442,
67 : 264.0142250838771,
68 : 264.0142220948367,
69 : 264.01421914914346,
70 : 264.0142162455718,
71 : 264.0142133829473,
72 : 264.0142105601436,
73 : 264.01420777608035,
74 : 264.01420502972013,
75 : 264.01420232006666,
76 : 264.01419964616247,
77 : 264.01419700708675,
78 : 264.014194401954,
79 : 264.0141918299117
}
transfertAvec = dict.items()
valeurs = list(transfertAvec)
numpyArray = np.array(valeurs)
convexite = numpyArray[:,1]-264;
vof=convexite;
for z in range(len(convexite)):
  vof[z]=abs(vof[z]-vof[z-1])/2
plt.plot(vof)
plt.grid()
plt.show()
