global avgNum
import math
avgNum = 6.022140857*(math.pow(10,23))
def atomToMol(atom):
	#input number of atoms and get back moles
	global avgNum
	moles = atom/avgNum
	return moles
	
def molToAtom(mol):
	#input number of moles and get back atoms
	global avgNum
	atoms = (mol * avgNum)
	return atoms
	
def gToMol(grams, weight):
	moles = (grams/weight)
	return moles
  
def molToG(moles, weight):
	grams = (weight*moles)
	return grams

def atomToG(atom, weight):
    mol = atomToMol(atom)
    grams = molToG(mol,weight)
    return grams

def gToAtom(grams, weight):
    mol = gToMol(grams,weight)
    atom = molToAtom(mol)
    return atom

H = 1.008
He = 4.0026
Li = 6.941
Be = 9.0122
B = 10.81
C = 12.011
N = 14.007
O = 15.999
F = 18.998
Ne = 20.180
Na = 22.990
Mg = 24.305
Al = 26.98
Si = 28.085
P = 30.974
S = 32.06
Cl = 35.45
Ar = 39.948
K = 39.098
Ca = 40.078
Sc = 44.956
Ti = 47.867
V = 50.942
Cr = 51.996
Mn = 54.938
Fe = 55.845
Co = 58.933
Ni = 58.693
Cu = 63.55
Zn = 65.38
Ga = 69.723
Ge = 72.630
As = 74.922
Se = 78.971
Br = 79.904
Kr = 83.798
Rb = 85.468
Sr = 87.62
Y = 88.906
Zr = 91.224
Nb = 92.906
Mo = 95.95
Tc = 98
Ru = 101.07
Rh = 102.91
Pd = 106.42
Ag = 107.87
Cd = 112.41
In = 114.82
Sn = 118.71
Sb = 121.76
Te = 127.60
I = 126.90
Xe = 131.29
Cs = 132.91
Ba = 137.33
#Fill in 57-71
Hf = 178.49
Ta = 180.95
W = 183.84
Re = 186.21
Os = 190.23
Ir = 192.22
Pt = 195.08
Au = 196.97
Hg = 200.6
Tl = 204.38
Pb = 207.2
Bi = 208.98
Po = 209
At = 210
Rn = 222
Fr = 223
Ra = 226
#86-103
Rf = 267
Db = 268
Sg = 269
Bh = 270
Hs = 277
Mt = 278
Ds = 281
Rg = 282
Cn = 285
Nh = 286
Fl = 289
Mc = 290
Lv = 293
Ts = 294
Og = 294




