from textwrap import dedent

# AMBER General Force Field for organic molecules (Version 2.11, May 2016)
gaff_atom_types = dedent("""
c  12.01         0.616               Sp2 C carbonyl group
cs 12.01         0.616               Sp2 C in c=S
c1 12.01         0.360               Sp C
c2 12.01         0.360               Sp2 C
c3 12.01         0.878               Sp3 C
ca 12.01         0.360               Sp2 C in pure aromatic systems
cp 12.01         0.360               Head Sp2 C that connect two rings in biphenyl sys.
cq 12.01         0.360               Head Sp2 C that connect two rings in biphenyl sys. identical to cp
cc 12.01         0.360               Sp2 carbons in non-pure aromatic systems
cd 12.01         0.360               Sp2 carbons in non-pure aromatic systems, identical to cc
ce 12.01         0.360               Inner Sp2 carbons in conjugated systems
cf 12.01         0.360               Inner Sp2 carbons in conjugated systems, identical to ce
cg 12.01         0.360               Inner Sp carbons in conjugated systems
ch 12.01         0.360               Inner Sp carbons in conjugated systems, identical to cg
cx 12.01         0.360               Sp3 carbons in triangle systems
cy 12.01         0.360               Sp3 carbons in square systems
cu 12.01         0.360               Sp2 carbons in triangle systems
cv 12.01         0.360               Sp2 carbons in square systems
cz 12.01         0.360               Sp2 carbon in guanidine group
h1 1.008         0.135               H bonded to aliphatic carbon with 1 electrwd. group
h2 1.008         0.135               H bonded to aliphatic carbon with 2 electrwd. group
h3 1.008         0.135               H bonded to aliphatic carbon with 3 electrwd. group
h4 1.008         0.135               H bonded to non-sp3 carbon with 1 electrwd. group
h5 1.008         0.135               H bonded to non-sp3 carbon with 2 electrwd. group
ha 1.008         0.135               H bonded to aromatic carbon
hc 1.008         0.135               H bonded to aliphatic carbon without electrwd. group
hn 1.008         0.161               H bonded to nitrogen atoms
ho 1.008         0.135               Hydroxyl group
hp 1.008         0.135               H bonded to phosphate
hs 1.008         0.135               Hydrogen bonded to sulphur
hw 1.008         0.135               Hydrogen in water
hx 1.008         0.135               H bonded to C next to positively charged group
f  19.00         0.320               Fluorine
cl 35.45         1.910               Chlorine
br 79.90         2.880               Bromine
i  126.9         4.690               Iodine
n  14.01         0.530               Sp2 nitrogen in amide groups
n1 14.01         0.530               Sp N
n2 14.01         0.530               aliphatic Sp2 N with two connected atoms
n3 14.01         0.530               Sp3 N with three connected atoms
n4 14.01         0.530               Sp3 N with four connected atoms
na 14.01         0.530               Sp2 N with three connected atoms
nb 14.01         0.530               Sp2 N in pure aromatic systems
nc 14.01         0.530               Sp2 N in non-pure aromatic systems
nd 14.01         0.530               Sp2 N in non-pure aromatic systems, identical to nc
ne 14.01         0.530               Inner Sp2 N in conjugated systems
nf 14.01         0.530               Inner Sp2 N in conjugated systems, identical to ne
nh 14.01         0.530               Amine N connected one or more aromatic rings
no 14.01         0.530               Nitro N
ns 14.01         0.530               amind N, with 1 attached hydrogen atom
nt 14.01         0.530               amide N, with 2 attached hydrogen atoms
nx 14.01         0.530               like n4, but only has one hydrogen atom
ny 14.01         0.530               like n4, but only has two hydrogen atoms
nz 14.01         0.530               like n4, but only has three three hydrogen atoms
n+ 14.01         0.530               NH4+
nu 14.01         0.530               like nh, but only has one attached hydrogen atom
nv 14.01         0.530               like nh, but only has two attached hydrogen atoms
n7 14.01         0.530               like n3, but only has one attached hydrogen atom
n8 14.01         0.530               like n3, but only has two attached hydrogen atoms
n9 14.01         0.530               NH3
ni 14.01         0.530               like n in RG3
nj 14.01         0.530               like n in RG4
nk 14.01         0.530               like n4/nx/ny in RG3
nl 14.01         0.530               like n4/nx/ny in RG4
nm 14.01         0.530               like nh in RG3
nn 14.01         0.530               like nh in RG4
np 14.01         0.530               like n3 in RG3
nq 14.01         0.530               like n3 in RG4
n5 14.01         0.530               like n7 in RG3
n6 14.01         0.530               like n7 in RG4
o  16.00         0.434               Oxygen with one connected atom
oh 16.00         0.465               Oxygen in hydroxyl group
op 16.00         0.465
oq 16.00         0.465
os 16.00         0.465               Ether and ester oxygen
ow 16.00         0.465               Oxygen in water
p2 30.97         1.538               Phosphate with two connected atoms
p3 30.97         1.538               Phosphate with three connected atoms, such as PH3
p4 30.97         1.538               Phosphate with three connected atoms, such as O=P(CH3)2
p5 30.97         1.538               Phosphate with four connected atoms, such as O=P(OH)3
pb 30.97         1.538               Sp2 P in pure aromatic systems
pc 30.97         1.538               Sp2 P in non-pure aromatic systems
pd 30.97         1.538               Sp2 P in non-pure aromatic systems, identical to pc
pe 30.97         1.538               Inner Sp2 P in conjugated systems
pf 30.97         1.538               Inner Sp2 P in conjugated systems, identical to pe
px 30.97         1.538               Special p4 in conjugated systems
py 30.97         1.538               Special p5 in conjugated systems
s  32.06         2.900               S with one connected atom
s2 32.06         2.900               S with two connected atom, involved at least one double bond
s4 32.06         2.900               S with three connected atoms
s6 32.06         2.900               S with four connected atoms
sh 32.06         2.900               Sp3 S connected with hydrogen
sp 32.06         2.900
sq 32.06         2.900
ss 32.06         2.900               Sp3 S in thio-ester and thio-ether
sx 32.06         2.900               Special s4 in conjugated systems
sy 32.06         2.900               Special s6 in conjugated systems
""")

# hn  ho  hs  n   na  nc  nd  ne  nf  n2  n3  n4  o   oh  os  ow  sh  ss
gaff_bonds = dedent("""
ow-hw  553.0    0.9572          TIP3P_Water       1
hw-hw  553.0    1.5136          TIP3P_Water       1
br-br   81.0    2.5420              SOURCE1       4
br-c1  227.0    1.7870              SOURCE2       4	 0.0024
br-c2  168.9    1.8930      SOURCE1_SOURCE5      25	 0.0078
br-c   146.5    1.9460              SOURCE2       2	 0.0285
br-c3  134.7    1.9780      SOURCE1_SOURCE5     146	 0.0118
br-ca  162.2    1.9080      SOURCE1_SOURCE5     462	 0.0052
br-cc  172.5    1.8850      SOURCE4_SOURCE5     128	 0.0078
br-cx  150.0    1.9370               5/2017      11	 0.0019
br-n1  141.5    1.8600              SOUECE3       1
br-n2   88.5    2.0380              SOURCE3       5	 0.1082
br-n   136.5    1.8730              SOURCE3       4	 0.0046
br-n3  110.4    1.9520              SOURCE3       2
br-n4  118.3    1.9260              SOURCE3       3	 0.0013
br-na   97.0    2.0020              SOURCE3       7	 0.2156
br-nh  112.8    1.9440              SOURCE3       1
br-no   75.7    2.1010              SOURCE3       1
br-o   193.6    1.8000              SOUECE3       1
br-oh  160.9    1.8660              SOURCE3       1
br-os  151.9    1.8870              SOURCE3       2
br-p2  133.1    2.2100              SOURCE3       9	 0.0510
br-p3  126.8    2.2310              SOURCE3       3	 0.0101
br-p4  145.9    2.1710              SOUECE3       1
br-p5  137.5    2.1960              SOURCE3       3	 0.0099
br-s   169.2    2.2200              SOUECE3       1
br-s4  128.8    2.3410              SOURCE3       1
br-s6  171.6    2.2140              SOURCE3       3	 0.0443
br-sh  173.6    2.2090              SOURCE3       1
br-ss  176.0    2.2030              SOURCE3       3	 0.0035
c1-c1  837.3    1.1980      SOURCE1_SOURCE5     659	 0.0039
c1-c2  535.9    1.3070              SOURCE1      18
c1-c3  295.9    1.4670      SOURCE1_SOURCE5     795	 0.0034
c1-ca  325.6    1.4400              SOUECE3       1
c1-ce  518.7    1.3150              SOURCE4       6	 0.0086
c1-cg  776.8    1.2160      SOURCE3_SOURCE5     179	 0.0036
c1-ch  765.4    1.2190      SOURCE3_SOURCE5      13	 0.0016
c1-cl  261.5    1.6310              SOURCE2       6	 0.0050
c1-cx  319.9    1.4450               5/2017      24	 0.0043
c1-f   482.2    1.2700              SOURCE2       2	 0.0085
c1-ha  433.7    1.0670      SOURCE3_SOURCE5     343	 0.0013
c1-hc  448.2    1.0600              SOUECE3       1
c1-i   153.5    1.9890              SOURCE2       4	 0.0032
c1-n1  891.5    1.1530      SOURCE1_SOURCE5     481	 0.0035
c1-n2  736.8    1.1970      SOURCE3_SOURCE5      36	 0.0076
c1-n3  401.0    1.3470      SOURCE2_SOURCE5      10	 0.0093
c1-n4  309.6    1.4170              SOURCE3       3	 0.0032
c1-n   428.9    1.3300              SOUECE3       1
c1-na  379.5    1.3620              SOURCE3       8	 0.0034
c1-ne  720.5    1.2020      SOURCE4_SOURCE5      31	 0.0124
c1-nf  720.5    1.2020      SOURCE4_SOURCE5      21	 0.0141
c1-nh  409.0    1.3420      SOURCE4_SOURCE5      33	 0.0061
c1-no  323.5    1.4050              SOURCE3       3	 0.0005
c1-o   795.0    1.1720      SOURCE2_SOURCE5      31	 0.0068
c1-oh  422.2    1.3260              SOURCE3       1
c1-os  435.4    1.3180      SOURCE3_SOURCE5       8	 0.0079
c1-p2  216.0    1.7700              SOUECE3       1
c1-p3  203.9    1.7900              SOUECE3       1
c1-p4  203.9    1.7900              SOUECE3       1
c1-p5  227.0    1.7530              SOURCE3       2
c1-s2  380.5    1.5950              SOURCE3       1
c1-s   370.6    1.6030      SOURCE1_SOURCE5      37	 0.0043
c1-s4  239.0    1.7460              SOURCE3       2
c1-s6  256.6    1.7220              SOURCE3       2
c1-sh  291.4    1.6800              SOUECE3       1
c1-ss  282.8    1.6900      SOURCE1_SOURCE5      49	 0.0113
c2-c2  481.8    1.3340      SOURCE1_SOURCE5    3727	 0.0053
c2-c3  255.6    1.5100      SOURCE1_SOURCE5   10204	 0.0042
c2-ca  398.4    1.3850      SOUECE3_SOURCE5       9	 0.0149
c2-cc  438.0    1.3590      SOURCE1_SOURCE5     882	 0.0181
c2-cd  438.0    1.3590      SOURCE1_SOURCE5     882	 0.0181
c2-ce  460.5    1.3460      SOURCE3_SOURCE5    3239	 0.0058
c2-cf  460.5    1.3460      SOURCE3_SOURCE5    3177	 0.0057
c2-cl  192.7    1.7310      SOURCE1_SOURCE5     290	 0.0098
c2-cu  501.4    1.3240               5/2017      11	 0.0010
c2-cx  278.0    1.4850               5/2017      76	 0.0060
c2-cy  254.3    1.5110               5/2017      21	 0.0067
c2-f   368.1    1.3390      SOURCE1_SOURCE5      35	 0.0085
c2-h4  394.2    1.0870      SOURCE3_SOURCE5     517	 0.0028
c2-h5  386.1    1.0910      SOURCE4_SOURCE5     116	 0.0021
c2-ha  392.2    1.0880      SOURCE3_SOURCE5    5991	 0.0019
c2-hc  393.9    1.0870              SOURCE3     789	 0.0046
c2-hx  401.4    1.0830              SOURCE3       3	 0.0008
c2-i    98.1    2.1700      SOURCE3_SOURCE5       7	 0.0194
c2-n1  470.9    1.3060              SOURCE3       4	 0.0161
c2-n2  518.7    1.2820      SOURCE1_SOURCE5    1004	 0.0051
c2-n3  412.7    1.3400              SOUECE3       1
c2-n   330.2    1.3990      SOURCE3_SOURCE5     174	 0.0100
c2-n4  221.4    1.5120      SOURCE3_SOURCE5      21	 0.0133
c2-na  327.7    1.4010      SOURCE3_SOURCE5      65	 0.0179
c2-nc  458.2    1.3130              SOURCE1      99	 0.0095
c2-nd  458.2    1.3130              SOURCE1      99
c2-ne  498.8    1.2920      SOURCE3_SOURCE5     310	 0.0099
c2-nf  498.8    1.2920      SOURCE3_SOURCE5     273	 0.0098
c2-nh  345.4    1.3870      SOURCE3_SOURCE5    1559	 0.0120
c2-no  276.9    1.4480      SOURCE4_SOURCE5      27	 0.0139
c2-o   635.2    1.2250      SOURCE4_SOURCE5      35	 0.0033
c2-oh  402.3    1.3390      SOURCE1_SOURCE5      85	 0.0126
c2-os  371.3    1.3600      SOURCE1_SOURCE5     548	 0.0107
c2-p2  292.5    1.6690      SOURCE3_SOURCE5      87	 0.0126
c2-p3  179.9    1.8340              SOURCE3       5	 0.0042
c2-p4  186.1    1.8220              SOUECE3       1
c2-p5  166.2    1.8630      SOURCE4_SOURCE5      15	 0.0083
c2-pe  275.1    1.6890      SOURCE3_SOURCE5      60	 0.0472
c2-pf  275.1    1.6890      SOURCE3_SOURCE5       8	 0.0019
c2-s2  362.6    1.6100              SOURCE2       1
c2-s   247.7    1.7340              SOURCE3       4	 0.0034
c2-s4  229.4    1.7600              SOUECE3       1
c2-s6  229.4    1.7600              SOUECE3       1
c2-sh  215.2    1.7820      SOURCE4_SOURCE5      13	 0.0077
c2-ss  246.2    1.7360              SOURCE1     209	 0.0155
c3-c3  232.5    1.5380      SOURCE1_SOURCE5   88072	 0.0058
c3-ca  250.3    1.5160      SOURCE1_SOURCE5   10699	 0.0054
c3-cc  262.6    1.5020      SOURCE3_SOURCE5    3926	 0.0049
c3-cd  262.6    1.5020      SOURCE3_SOURCE5    3926	 0.0049
c3-ce  250.1    1.5160      SOURCE3_SOURCE5    1210	 0.0060
c3-cf  250.2    1.5160      SOURCE3_SOURCE5     345	 0.0071
c3-cl  155.5    1.8040      SOURCE1_SOURCE5    1173	 0.0119
c3-cu  278.9    1.4840               5/2017       2
c3-cv  263.1    1.5010               5/2017       1
c3-cx  244.9    1.5220               5/2017     849	 0.0062
c3-cy  235.3    1.5340               5/2017     522	 0.0055
c3-f   352.6    1.3500      SOURCE1_SOURCE5    2188	 0.0139
c3-h1  375.9    1.0970      SOURCE3_SOURCE5  112144	 0.0055
c3-h2  377.3    1.0960      SOURCE3_SOURCE5    2681	 0.0032
c3-h3  379.5    1.0950      SOURCE4_SOURCE5      64	 0.0028
c3-hc  375.9    1.0970      SOURCE3_SOURCE5  133628	 0.0015
c3-hx  386.5    1.0910      SOURCE3_SOURCE5    6495	 0.0022
c3-i    89.0    2.2120      SOURCE1_SOURCE5      35	 0.0128
c3-n1  292.3    1.4330      SOURCE3_SOURCE5       7	 0.0033
c3-n2  259.9    1.4660      SOURCE1_SOURCE5     816	 0.0087
c3-n   263.8    1.4620      SOURCE1_SOURCE5    4576	 0.0061
c3-n3  261.2    1.4650      SOURCE1_SOURCE5   15206	 0.0039
c3-n4  222.6    1.5110      SOURCE1_SOURCE5    2375	 0.0125
c3-na  262.9    1.4630      SOURCE3_SOURCE5    1732	 0.0077
c3-nc  269.3    1.4560              SOURCE3       9	 0.0109
c3-nd  269.3    1.4560              SOURCE3       9
c3-nh  261.8    1.4640      SOURCE3_SOURCE5    3492	 0.0064
c3-no  206.4    1.5330      SOURCE1_SOURCE5     150	 0.0187
c3-o   438.1    1.3170              SOURCE4       8	 0.0193
c3-oh  293.4    1.4230      SOURCE1_SOURCE5    8884	 0.0067
c3-os  284.8    1.4320      SOURCE1_SOURCE5   17971	 0.0103
c3-p2  169.7    1.8550              SOURCE3       9	 0.0125
c3-p3  168.2    1.8580      SOURCE3_SOURCE5     221	 0.0094
c3-p4  177.6    1.8390      SOURCE3_SOURCE5      45	 0.0106
c3-p5  177.2    1.8390      SOURCE1_SOURCE5     408	 0.0183
c3-px  182.7    1.8290      SOURCE3_SOURCE5      35	 0.0083
c3-py  177.1    1.8400      SOURCE3_SOURCE5      39	 0.0126
c3-s   180.0    1.8450              SOURCE3       4	 0.0185
c3-s4  187.5    1.8310      SOURCE1_SOURCE5     326	 0.0096
c3-s6  200.1    1.8080      SOURCE1_SOURCE5     644	 0.0143
c3-sh  180.8    1.8430      SOURCE3_SOURCE5     189	 0.0058
c3-ss  183.0    1.8390      SOURCE1_SOURCE5    2732	 0.0105
c3-sx  181.6    1.8420      SOURCE3_SOURCE5      99	 0.0121
c3-sy  199.4    1.8090      SOURCE3_SOURCE5     162	 0.0094
ca-ca  378.6    1.3980      SOURCE1_SOURCE5  121206	 0.0061
ca-cc  308.2    1.4560      SOURCE1_SOURCE5    2424	 0.0121
ca-cd  308.2    1.4560      SOURCE1_SOURCE5    2424	 0.0121
ca-ce  286.5    1.4760      SOURCE1_SOURCE5    1750	 0.0089
ca-cf  286.5    1.4760      SOURCE1_SOURCE5    1750	 0.0089
ca-cg  334.1    1.4330      SOURCE1_SOURCE5     318	 0.0029
ca-ch  334.1    1.4330      SOURCE1_SOURCE5     318	 0.0029
ca-cl  182.0    1.7500      SOURCE1_SOURCE5    2919	 0.0059
ca-cp  368.4    1.4060         CORR_SOURCE5    2042	 0.0049
ca-cq  368.4    1.4060         CORR_SOURCE5    2042	 0.0049
ca-cx  267.6    1.4960               5/2017      67	 0.0051
ca-cy  250.0    1.5160               5/2017      27	 0.0058
ca-f   353.6    1.3490      SOURCE1_SOURCE5    1239	 0.0057
ca-h4  390.1    1.0890      SOURCE3_SOURCE5    2643	 0.0010
ca-h5  392.4    1.0880      SOURCE3_SOURCE5     299	 0.0007
ca-ha  395.7    1.0860      SOURCE3_SOURCE5   65456	 0.0010
ca-i   108.3    2.1290      SOURCE1_SOURCE5      61	 0.0076
ca-n1  420.7    1.3350      SOURCE3_SOURCE5       6	 0.0078
ca-n2  476.5    1.3030              SOURCE4       7	 0.0058
ca-n   315.2    1.4120      SOURCE3_SOURCE5    1254	 0.0090
ca-n4  244.0    1.4840      SOURCE1_SOURCE5      28	 0.0065
ca-na  349.5    1.3840      SOURCE1_SOURCE5    2751	 0.0095
ca-nb  414.2    1.3390      SOURCE3_SOURCE5    6806	 0.0055
ca-nc  394.6    1.3520      SOURCE1_SOURCE5    2672	 0.0030
ca-nd  394.6    1.3520      SOURCE1_SOURCE5    2672	 0.0030
ca-ne  320.1    1.4080      SOURCE1_SOURCE5     276	 0.0093
ca-nf  320.1    1.4080      SOURCE1_SOURCE5     276	 0.0093
ca-nh  347.1    1.3860      SOURCE1_SOURCE5    2785	 0.0134
ca-no  257.4    1.4690      SOURCE1_SOURCE5     454	 0.0049
ca-o   606.5    1.2360      SOURCE4_SOURCE5      17	 0.0088
ca-oh  365.6    1.3640      SOURCE1_SOURCE5    3637	 0.0062
ca-os  357.5    1.3700      SOURCE1_SOURCE5    6900	 0.0064
ca-p2  176.9    1.8400              SOUECE3       1
ca-p3  184.2    1.8260      SOURCE1_SOURCE5     156	 0.0180
ca-p4  194.7    1.8060              SOUECE3       1
ca-p5  200.8    1.7950      SOURCE1_SOURCE5     577	 0.0028
ca-pe  182.5    1.8290              SOURCE3      10	 0.0042
ca-pf  182.5    1.8290              SOURCE3      10	 0.0042
ca-px  184.5    1.8250              SOURCE3       5	 0.0168
ca-py  189.2    1.8160      SOURCE4_SOURCE5      34	 0.0098
ca-s   244.0    1.7390              SOURCE3       2
ca-s4  211.5    1.7880              SOURCE1      51	 0.0048
ca-s6  224.8    1.7670      SOURCE1_SOURCE5     258	 0.0041
ca-sh  215.9    1.7810      SOURCE4_SOURCE5      40	 0.0053
ca-ss  216.1    1.7810      SOURCE1_SOURCE5    1016	 0.0068
ca-sx  190.3    1.8250      SOURCE4_SOURCE5      90	 0.0050
ca-sy  209.8    1.7910      SOURCE3_SOURCE5     703	 0.0076
c -c1  303.3    1.4600              SOUECE3       1
c -c2  368.2    1.4060              SOURCE3       2	 0.0370
c -c   224.4    1.5480      SOURCE1_SOURCE5     254	 0.0090
c -c3  243.2    1.5240      SOURCE1_SOURCE5   12697	 0.0077
c -ca  272.7    1.4910      SOURCE1_SOURCE5    4357	 0.0085
c -cc  295.4    1.4680      SOURCE3_SOURCE5    1864	 0.0130
cc-cc  340.2    1.4280      SOURCE1_SOURCE5    4559	 0.0096
cc-cd  416.1    1.3730      SOURCE3_SOURCE5    8451	 0.0091
cc-ce  309.8    1.4540         CORR_SOURCE5     396	 0.0089
cc-cf  427.7    1.3660         CORR_SOURCE5     156	 0.0107
cc-cg  342.8    1.4260      SOURCE1_SOURCE5     109	 0.0049
cc-ch  341.2    1.4270              SOURCE1     560
cc-cl  190.1    1.7350         CORR_SOURCE5     137	 0.0076
cc-cx  293.9    1.4690               5/2017      24	 0.0036
c -cd  295.4    1.4680      SOURCE3_SOURCE5    1864	 0.0130
c -ce  280.4    1.4820      SOURCE1_SOURCE5    3022	 0.0115
c -cf  280.4    1.4820      SOURCE1_SOURCE5    3022	 0.0115
cc-f   365.0    1.3410      SOURCE4_SOURCE5      70	 0.0039
c -cg  312.9    1.4510      SOURCE3_SOURCE5      11	 0.0089
c -ch  312.9    1.4510      SOURCE3_SOURCE5      11	 0.0089
cc-h4  403.9    1.0820      SOURCE3_SOURCE5    4457	 0.0016
cc-h5  403.5    1.0820      SOURCE3_SOURCE5     879	 0.0012
cc-ha  400.1    1.0840      SOURCE3_SOURCE5    4706	 0.0018
c -cl  156.2    1.8030      SOURCE3_SOURCE5      16	 0.0187
cc-n2  500.7    1.2900         CORR_SOURCE5     156	 0.0074
cc-n   353.8    1.3810      SOURCE3_SOURCE5    1142	 0.0085
cc-n4  236.7    1.4930              SOURCE4       7	 0.0148
cc-na  354.5    1.3800      SOURCE3_SOURCE5    6739	 0.0088
cc-nc  369.1    1.3690      SOURCE1_SOURCE5    2269	 0.0086
cc-nd  450.7    1.3170      SOURCE3_SOURCE5    4612	 0.0083
cc-ne  356.6    1.3790      SOURCE4_SOURCE5      82	 0.0119
cc-nf  485.1    1.2980         CORR_SOURCE5      41	 0.0113
cc-nh  363.5    1.3730      SOURCE3_SOURCE5     976	 0.0106
cc-no  296.6    1.4290      SOURCE4_SOURCE5     386	 0.0074
cc-oh  389.4    1.3470         CORR_SOURCE5     248	 0.0073
cc-os  367.9    1.3620      SOURCE3_SOURCE5    1859	 0.0083
cc-pd  240.8    1.7330              SOURCE3      84	 0.0161
cc-sh  223.3    1.7690      SOURCE4_SOURCE5      22	 0.0030
cc-ss  232.0    1.7560      SOURCE3_SOURCE5    2011	 0.0134
cc-sx  198.3    1.8110      SOURCE4_SOURCE5      44	 0.0033
cc-sy  214.1    1.7840         CORR_SOURCE5      73	 0.0082
c -cu  360.2    1.4120              SOURCE2       1
c -cx  261.3    1.5030               5/2017     246	 0.0109
c -cy  221.6    1.5520               5/2017     374	 0.0059
cd-cd  340.2    1.4280      SOURCE1_SOURCE5    4559	 0.0096
cd-ce  427.7    1.3660         CORR_SOURCE5     156	 0.0107
cd-cf  309.8    1.4540         CORR_SOURCE5     396	 0.0089
cd-cg  341.2    1.4270              SOURCE1     560
cd-ch  342.8    1.4260      SOURCE1_SOURCE5     109	 0.0049
cd-cl  190.1    1.7350         CORR_SOURCE5     137	 0.0076
cd-cx  282.9    1.4800               5/2017      13	 0.0034
cd-cy  259.5    1.5050               5/2017      11	 0.0006
cd-h4  403.9    1.0820      SOURCE3_SOURCE5    4457	 0.0016
cd-h5  403.7    1.0820      SOURCE3_SOURCE5     578	 0.0013
cd-ha  400.1    1.0840      SOURCE3_SOURCE5    4706	 0.0018
cd-n2  500.7    1.2900         CORR_SOURCE5     156	 0.0074
cd-n   353.8    1.3810      SOURCE3_SOURCE5    1142	 0.0085
cd-na  354.5    1.3800      SOURCE3_SOURCE5    6739	 0.0088
cd-nc  450.7    1.3170      SOURCE3_SOURCE5    4612	 0.0083
cd-nd  369.1    1.3690      SOURCE1_SOURCE5    2269	 0.0086
cd-ne  485.1    1.2980         CORR_SOURCE5      41	 0.0113
cd-nh  363.5    1.3730      SOURCE3_SOURCE5     976	 0.0106
cd-oh  389.4    1.3470         CORR_SOURCE5     248	 0.0073
cd-os  367.9    1.3620      SOURCE3_SOURCE5    1859	 0.0083
cd-pc  240.8    1.7330              SOURCE3      84
cd-ss  232.0    1.7560      SOURCE3_SOURCE5    2011	 0.0134
cd-sy  214.1    1.7840         CORR_SOURCE5      73	 0.0082
ce-ce  306.1    1.4570      SOURCE1_SOURCE5    1000	 0.0092
ce-cf  452.2    1.3510      SOURCE1_SOURCE5    1908	 0.0059
ce-cg  341.2    1.4270      SOURCE1_SOURCE5     238	 0.0053
ce-ch  336.3    1.4310              SOURCE1      22
ce-cl  174.7    1.7640      SOURCE4_SOURCE5      90	 0.0111
ce-cx  261.3    1.5030               5/2017      26	 0.0077
ce-cy  249.1    1.5170               5/2017      36	 0.0052
ce-h4  385.4    1.0920         CORR_SOURCE5     315	 0.0033
ce-ha  391.4    1.0880      SOURCE3_SOURCE5    2751	 0.0014
ce-n1  461.6    1.3110         CORR_SOURCE5      16	 0.0049
ce-n2  507.0    1.2870      SOURCE1_SOURCE5     896	 0.0038
ce-n   301.7    1.4240         CORR_SOURCE5     209	 0.0059
ce-na  305.3    1.4210      SOURCE4_SOURCE5      11	 0.0050
ce-ne  336.6    1.3940      SOURCE3_SOURCE5      69	 0.0151
ce-nf  489.1    1.2960         CORR_SOURCE5     101	 0.0097
ce-nh  341.7    1.3900         CORR_SOURCE5     300	 0.0133
ce-oh  384.7    1.3500         CORR_SOURCE5      58	 0.0102
ce-os  355.7    1.3710         CORR_SOURCE5      96	 0.0128
ce-p2  190.4    1.8140              SOUECE3       1
ce-pe  188.2    1.8180              SOURCE3       8	 0.0108
ce-px  186.6    1.8210              SOURCE3       6	 0.0046
ce-py  195.0    1.8060      SOURCE3_SOURCE5      22	 0.0142
ce-s   291.4    1.6800              SOUECE3       1
ce-ss  215.6    1.7810      SOURCE4_SOURCE5      56	 0.0098
ce-sx  193.9    1.8190      SOURCE3_SOURCE5      30	 0.0101
ce-sy  211.5    1.7880      SOURCE3_SOURCE5      41	 0.0169
c -f   387.8    1.3250              SOURCE2       6	 0.0147
cf-cf  306.1    1.4570      SOURCE1_SOURCE5    1000	 0.0092
cf-cg  336.3    1.4310              SOURCE1      22
cf-ch  341.2    1.4270      SOURCE1_SOURCE5     238	 0.0053
cf-h4  385.4    1.0920         CORR_SOURCE5     315	 0.0033
cf-ha  391.4    1.0880      SOURCE3_SOURCE5    2751	 0.0014
cf-n1  461.6    1.3110         CORR_SOURCE5      16	 0.0049
cf-n2  507.0    1.2870      SOURCE1_SOURCE5     896	 0.0038
cf-n   301.7    1.4240         CORR_SOURCE5     209	 0.0059
cf-ne  489.1    1.2960         CORR_SOURCE5     101	 0.0097
cf-nf  336.6    1.3940      SOURCE3_SOURCE5      62	 0.0156
cf-nh  341.7    1.3900         CORR_SOURCE5     300	 0.0133
cf-oh  384.7    1.3500         CORR_SOURCE5      58	 0.0102
cf-os  355.7    1.3710         CORR_SOURCE5      96	 0.0128
cf-p2  190.4    1.8140              SOUECE3       1
cf-pf  188.2    1.8180              SOURCE3       8
cf-px  186.6    1.8210              SOURCE3       6
cf-py  195.0    1.8060      SOURCE3_SOURCE5      17	 0.0171
cf-s   291.4    1.6800              SOUECE3       1
cf-sx  193.9    1.8190      SOURCE3_SOURCE5      25	 0.0105
cf-sy  211.5    1.7880      SOURCE3_SOURCE5      36	 0.0177
cg-cg  421.8    1.3690      SOURCE1_SOURCE5      62	 0.0025
cg-ch  811.5    1.2060      SOURCE1_SOURCE5     156	 0.0023
cg-n1  879.3    1.1570      SOURCE1_SOURCE5     879	 0.0015
cg-ne  435.4    1.3260      SOURCE4_SOURCE5      68	 0.0013
cg-pe  339.4    1.6210              SOURCE3      11	 0.2008
c -h4  350.2    1.1120      SOURCE4_SOURCE5     506	 0.0025
c -h5  361.8    1.1050      SOURCE4_SOURCE5     163	 0.0038
c -ha  368.8    1.1010              SOURCE3      53	 0.0102
ch-ch  421.8    1.3690      SOURCE1_SOURCE5      62	 0.0025
ch-n1  879.3    1.1570      SOURCE1_SOURCE5     879	 0.0015
ch-nf  435.4    1.3260      SOURCE4_SOURCE5      51	 0.0014
ch-pf  339.4    1.6210              SOURCE3      11
c -i    89.5    2.2090              SOURCE3       4	 0.0365
cl-cl   79.3    2.2670              SOURCE1       2	 0.0395
cl-cx  163.0    1.7880               5/2017      42	 0.0071
cl-cy  160.2    1.7940               5/2017      26	 0.0106
cl-n1  217.6    1.6300              SOUECE3       1
cl-n2  123.8    1.8190              SOURCE3       6	 0.1020
cl-n3  139.5    1.7770      SOURCE4_SOURCE5      16	 0.0044
cl-n   167.0    1.7160      SOURCE4_SOURCE5      17	 0.0049
cl-n4  149.7    1.7530              SOURCE3       4	 0.0098
cl-na  118.4    1.8350              SOURCE3       7	 0.2083
cl-nh  145.4    1.7630              SOURCE3       1
cl-no  116.7    1.8400              SOURCE2       1
cl-o   331.0    1.4830              SOURCE3       4
cl-oh  169.1    1.6900              SOURCE2       1
cl-os  149.9    1.7300              SOURCE3       4
cl-p2  143.5    2.0700              SOURCE3       6	 0.0108
cl-p3  167.8    2.0080              SOURCE1     111
cl-p4  167.8    2.0080              SOURCE1     111
cl-p5  167.8    2.0080              SOURCE1     111
cl-pb  172.6    1.9970              SOURCE1      46
cl-s   230.4    2.0720              SOURCE1       6
cl-s2  185.6    2.1610              SOURCE2       1
cl-s4  230.4    2.0720              SOURCE1       6
cl-s6  230.4    2.0720              SOURCE1       6
cl-sh  230.4    2.0720              SOURCE1       6
cl-ss  230.4    2.0720              SOURCE1       6
cl-sx  230.4    2.0720              SOURCE1       6
cl-sy  230.4    2.0720              SOURCE1       6
c -n2  306.3    1.4200              SOUECE3       1
c -n4  197.9    1.5460              SOURCE3       4	 0.0388
c -n   356.2    1.3790      SOURCE1_SOURCE5    9463	 0.0137
c -nc  346.0    1.3870         CORR_SOURCE5     179	 0.0121
c -nd  346.0    1.3870         CORR_SOURCE5     179	 0.0121
c -ne  340.7    1.3910         CORR_SOURCE5      87	 0.0140
c -nf  340.7    1.3910         CORR_SOURCE5      87	 0.0140
c -no  201.9    1.5400              SOUECE3       1
c -o   652.6    1.2180      SOURCE1_SOURCE5   27083	 0.0110
c -oh  383.1    1.3510      SOURCE1_SOURCE5    3610	 0.0055
c -os  372.9    1.3580      SOURCE1_SOURCE5    5555	 0.0163
c -p2  150.0    1.9000              SOUECE3       1
c -p3  157.1    1.8830              SOURCE3       6	 0.0129
c -p4  158.4    1.8800              SOUECE3       1
c -p5  157.6    1.8820      SOURCE4_SOURCE5      25	 0.0081
cp-cp  277.6    1.4850      SOURCE1_SOURCE5     728	 0.0059
cp-cq  309.6    1.4540      SOURCE4_SOURCE5      34	 0.0159
c -pe  145.7    1.9110              SOURCE3       3	 0.0025
c -pf  145.7    1.9110              SOURCE3       3
cp-na  349.5    1.3840              SOURCE4       7	 0.0181
cp-nb  414.7    1.3390      SOURCE4_SOURCE5     190	 0.0068
c -px  148.4    1.9040              SOURCE3       1
c -py  164.2    1.8670      SOURCE3_SOURCE5      17	 0.0103
cq-cq  277.6    1.4850      SOURCE1_SOURCE5     728	 0.0059
c -s   298.4    1.6720      SOURCE1_SOURCE5     875	 0.0114
c -s4  168.0    1.8700              SOUECE3       1
c -s6  168.0    1.8700              SOUECE3       1
c -sh  206.1    1.7970      SOURCE3_SOURCE5      39	 0.0097
c -ss  204.4    1.8000      SOURCE1_SOURCE5     249	 0.0157
c -sx  161.2    1.8850              SOURCE3       5	 0.0088
c -sy  170.3    1.8650              SOURCE3       5	 0.0085
cu-cu  550.8    1.3000               5/2017       2	 0.0001
cu-cx  292.9    1.4700               5/2017      31	 0.0066
cu-ha  409.1    1.0790               5/2017       1
cv-cv  469.6    1.3410               5/2017       3	 0.0026
cv-cy  245.8    1.5210               5/2017      19	 0.0057
cv-ha  392.0    1.0880               5/2017       3	 0.0001
cv-cx  259.5    1.5050               5/2017       2	 0.0002
cx-cx  256.9    1.5080               5/2017    1577	 0.0100
cx-cy  240.1    1.5280               5/2017       3	 0.0083
cx-f   337.9    1.3610               5/2017       7	 0.0043
cx-h1  390.2    1.0890               5/2017    1132	 0.0013
cx-h2  393.9    1.0870               5/2017       5	 0.0014
cx-hc  393.9    1.0870               5/2017    1658	 0.0009
cx-hx  397.6    1.0850               5/2017      14	 0.0002
cx-n2  273.1    1.4520               5/2017       3	 0.0065
cx-n3  282.0    1.4430               5/2017      23	 0.0030
cx-n   291.2    1.4340               5/2017      15	 0.0035
cx-na  264.6    1.4610               5/2017      38	 0.0029
cx-nh  291.2    1.4340               5/2017      16	 0.0017
cx-oh  322.9    1.3970               5/2017       3	 0.0035
cx-os  313.6    1.4050               5/2017      13	 0.0116
cx-p3  146.0    1.9100               5/2017       1
cx-s4  162.6    1.8820               5/2017       2	 0.0203
cx-s6  178.0    1.8490               5/2017       2	 0.0016
cx-ss  184.6    1.8360               5/2017       5	 0.0011
cy-cy  217.2    1.5580               5/2017     923	 0.0062
cy-f   343.0    1.3570               5/2017      28	 0.0109
cy-h1  379.3    1.0950               5/2017     460	 0.0018
cy-h2  382.9    1.0930               5/2017     130	 0.0016
cy-hc  379.3    1.0950               5/2017     777	 0.0011
cy-n   292.3    1.4330               5/2017     107	 0.0073
cy-n3  268.4    1.4570               5/2017      20	 0.0060
cy-oh  305.7    1.4120               5/2017      13	 0.0082
cy-os  294.8    1.4220               5/2017      28	 0.0080
cy-s6  177.1    1.8510               5/2017      30	 0.0135
cy-ss  177.6    1.8500               5/2017     100	 0.0087
cz-nh  414.2    1.3390      SOURCE4_SOURCE5      85	 0.0046
f -n1  167.3    1.4100              SOUECE3       1
f -n2  148.0    1.4440              SOURCE3       5	 0.0377
f -n3  169.8    1.4060              SOURCE1       9
f -n   175.5    1.3970              SOURCE3       3	 0.0112
f -n4  246.1    1.3080              SOURCE3       2
f -na  166.7    1.4110              SOURCE3       7	 0.0611
f -nh  157.9    1.4260              SOURCE3       3	 0.0085
f -no  136.5    1.4670              SOURCE2       1
f -o   198.1    1.3300              SOUECE3       1
f -oh  129.8    1.4440              SOURCE3       1
f -os  139.9    1.4230              SOURCE3       2
f -p2  522.3    1.5360              SOURCE3       7	 0.2054
f -p3  454.7    1.5780              SOURCE2       8	 0.0103
f -p4  437.3    1.5900              SOUECE3       1
f -p5  442.7    1.5860      SOURCE1_SOURCE5      18	 0.0161
f -s2  363.5    1.6430              SOURCE2       1
f -s   344.7    1.6600              SOUECE3       1
f -s4  428.8    1.5910              SOURCE2       4	 0.0065
f -s6  400.9    1.6120      SOURCE2_SOURCE5      15	 0.0133
f -sh  356.7    1.6490              SOURCE3       1
f -ss  373.9    1.6340              SOURCE3       3	 0.0156
hn-n1  605.5    0.9860              SOURCE2       1
hn-n2  501.1    1.0230      SOURCE3_SOURCE5     732	 0.0030
hn-n3  511.3    1.0190      SOURCE3_SOURCE5    5944	 0.0012
hn-n   527.3    1.0130      SOURCE3_SOURCE5    7593	 0.0034
hn-n4  482.9    1.0300      SOURCE3_SOURCE5     756	 0.0122
hn-na  535.1    1.0100      SOURCE3_SOURCE5    1755	 0.0019
hn-nh  529.5    1.0120      SOURCE3_SOURCE5    7230	 0.0022
hn-no  501.1    1.0230              SOURCE3       1
ho-o   540.3    0.9810              SOURCE3       1
ho-oh  563.5    0.9730      SOURCE3_SOURCE5   21237	 0.0034
hp-p2  266.5    1.3360              SOURCE3      87	 0.1706
hp-p3  200.6    1.4120      SOURCE3_SOURCE5     123	 0.0510
hp-p4  253.6    1.3490              SOURCE3      17	 0.1577
hp-p5  196.4    1.4180      SOURCE3_SOURCE5      31	 0.0077
hs-s   288.3    1.3530              SOURCE3       1
hs-s4  265.3    1.3750              SOURCE3       5	 0.0004
hs-s6  281.8    1.3590              SOURCE3       5	 0.0015
hs-sh  294.6    1.3470      SOURCE3_SOURCE5     477	 0.0118
i -i    50.3    2.9170              SOURCE1       1
i -n1  105.5    2.0600              SOUECE3       1
i -n2   59.4    2.3040              SOURCE3       6	 0.1186
i -n    96.0    2.0980              SOURCE3       5	 0.0156
i -n3   78.0    2.1850              SOURCE3       3	 0.0437
i -n4   83.7    2.1550              SOURCE3       3	 0.0168
i -na   89.1    2.1290              SOURCE3       8	 0.1276
i -nh   84.7    2.1500              SOURCE3       1
i -no   70.0    2.2310              SOURCE3       1
i -o   106.3    1.9800              SOUECE3       1
i -oh   78.4    2.1010              SOURCE3       2
i -os   73.2    2.1290              SOURCE3       3	 0.0146
i -p2   66.3    2.6430              SOURCE3       6	 0.0297
i -p3   77.2    2.5660              SOURCE3       3	 0.0016
i -p4  120.8    2.3520              SOURCE3       4	 0.2600
i -p5   72.7    2.5960              SOURCE3       3	 0.0143
i -s   115.8    2.4300              SOUECE3       1
i -s4   49.2    2.8700              SOUECE3       1
i -s6   49.2    2.8700              SOURCE3       1
i -sh   88.6    2.5600              SOUECE3       1
i -ss   86.6    2.5710              SOURCE3       3	 0.0065
n1-n1  751.0    1.1350      SOURCE1_SOURCE5      78	 0.0044
n1-n2  494.9    1.2300      SOURCE1_SOURCE5      36	 0.0029
n1-n3  307.2    1.3500              SOUECE3       1
n1-n4  295.8    1.3600              SOUECE3       1
n1-na  307.2    1.3500              SOUECE3       1
n1-nc  525.7    1.2160              SOURCE1      38
n1-nd  525.7    1.2160              SOURCE1      38
n1-ne  452.5    1.2520              SOURCE2       1
n1-nf  452.5    1.2520              SOURCE2       1
n1-nh  319.2    1.3400              SOUECE3       1
n1-no  254.8    1.4000              SOUECE3       1
n1-o   298.4    1.2770              SOURCE3       5	 0.0438
n1-oh  272.2    1.3000              SOUECE3       1
n1-os  261.7    1.3100              SOUECE3       1
n1-p2  268.9    1.6780              SOURCE3       2	 0.0282
n1-p3  284.3    1.6600              SOUECE3       1
n1-p4  267.3    1.6800              SOURCE3       0
n1-p5  377.4    1.5710              SOURCE1     132
n1-s2  681.1    1.4490              SOURCE2       2	 0.0010
n1-s   339.7    1.6590              SOURCE3       6	 0.0789
n1-s4  349.3    1.6500              SOUECE3       1
n1-s6  766.7    1.4160              SOURCE2       2
n1-sh  396.3    1.6100              SOUECE3       1
n1-ss  396.3    1.6100              SOUECE3       1
n2-n2  426.0    1.2670      SOURCE3_SOURCE5      40	 0.0268
n2-n3  333.0    1.3290              SOURCE2       1
n2-n4  100.1    1.6790              SOURCE3       7	 0.3138
n2-na  287.4    1.3680      SOURCE4_SOURCE5      49	 0.0087
n2-nc  447.0    1.2550              SOURCE1      13
n2-nd  447.0    1.2550              SOURCE1      13
n2-ne  418.1    1.2710      SOURCE3_SOURCE5      57	 0.0194
n2-nf  418.1    1.2710      SOURCE3_SOURCE5      27	 0.0074
n2-nh  304.4    1.3520      SOURCE3_SOURCE5     210	 0.0159
n2-no  224.8    1.4350      SOURCE3_SOURCE5      15	 0.0628
n2-o   381.8    1.2170      SOURCE3_SOURCE5     112	 0.0102
n2-oh  192.1    1.3910      SOURCE1_SOURCE5     149	 0.0171
n2-os  185.0    1.4010      SOURCE3_SOURCE5     108	 0.0101
n2-p2  338.0    1.6050              SOURCE3      35	 0.0737
n2-p3  208.0    1.7640              SOURCE3       7	 0.0374
n2-p4  234.1    1.7240              SOUECE3       1
n2-p5  344.6    1.5990              SOURCE1       7
n2-pe  418.1    1.5400              SOURCE3      20	 0.1392
n2-pf  418.1    1.5400              SOURCE3      20
n2-s2  491.3    1.5440      SOURCE2_SOURCE5      11	 0.0086
n2-s4  396.3    1.6100              SOUECE3       1
n2-s   496.4    1.5410              SOURCE1      37
n2-s6  475.7    1.5540      SOURCE4_SOURCE5      16	 0.0041
n2-sh  267.4    1.7380              SOURCE3       5	 0.0511
n2-ss  342.9    1.6560              SOURCE1      36
n3-n3  219.3    1.4420      SOURCE1_SOURCE5      48	 0.0063
n3-n4  228.5    1.4300      SOURCE1_SOURCE5       9	 0.0040
n3-na  236.9    1.4200              SOURCE1      68
n3-nh  240.7    1.4160      SOURCE1_SOURCE5      66	 0.0085
n3-no  256.9    1.3980      SOURCE3_SOURCE5      19	 0.0132
n3-o   269.0    1.3030              SOURCE3       4	 0.1217
n3-oh  176.2    1.4150      SOURCE1_SOURCE5      17	 0.0055
n3-os  160.6    1.4410      SOURCE1_SOURCE5      84	 0.0191
n3-p2  275.6    1.6700              SOUECE3       1
n3-p3  229.9    1.7300              SOURCE1      40
n3-p4  253.8    1.6970              SOURCE1      88
n3-p5  276.0    1.6700      SOURCE1_SOURCE5     680	 0.0109
n3-py  256.2    1.6940      SOURCE4_SOURCE5      16	 0.0080
n3-s   228.5    1.7920              SOURCE3       3	 0.0178
n3-s4  254.8    1.7540      SOURCE3_SOURCE5      15	 0.0416
n3-s6  326.0    1.6720      SOURCE1_SOURCE5     243	 0.0144
n3-sh  266.7    1.7390              SOURCE3       3	 0.0154
n3-ss  279.1    1.7240      SOURCE3_SOURCE5      25	 0.0197
n3-sy  303.1    1.6960      SOURCE4_SOURCE5     511	 0.0083
n4-n4  188.9    1.4840              SOURCE3       4	 0.0089
n4-na  224.4    1.4350              SOURCE3       9	 0.0390
n4-nh  201.1    1.4660              SOURCE3       5	 0.0108
n4-no  191.5    1.4800              SOUECE3       1
n4-o   215.1    1.3610              SOURCE3       3	 0.0041
n4-oh  186.0    1.4000              SOURCE3       3	 0.0115
n4-os  172.3    1.4210              SOURCE3       5	 0.0249
n4-p2  126.9    1.9420              SOURCE3      10	 0.0643
n4-p3  149.9    1.8800              SOURCE3       5	 0.0146
n4-p4  128.3    1.9380              SOURCE3       1
n4-p5  172.2    1.8300              SOURCE3       5	 0.0087
n4-py  141.2    1.9020              SOURCE3       4
n4-s   204.0    1.8320              SOURCE3       3	 0.0004
n4-s4  139.7    1.9720              SOURCE3       3	 0.0198
n4-s6  162.9    1.9140              SOURCE3       5	 0.0432
n4-sh  216.5    1.8110              SOURCE3       3	 0.0027
n4-ss  215.9    1.8120              SOURCE3       5	 0.0064
na-na  253.9    1.4010              SOURCE1      40
na-nb  310.5    1.3470      SOURCE4_SOURCE5      26	 0.0093
na-nc  300.5    1.3560      SOURCE3_SOURCE5     899	 0.0083
na-nd  302.4    1.3540      SOURCE3_SOURCE5     362	 0.0113
na-nh  254.8    1.4000      SOURCE1_SOURCE5      20	 0.0066
na-no  224.8    1.4350      SOURCE3_SOURCE5      16	 0.0192
na-o   347.9    1.2390      SOURCE1_SOURCE5      93	 0.0208
na-oh  191.2    1.3930      SOURCE3_SOURCE5      18	 0.0144
na-os  158.7    1.4440              SOURCE3      45	 0.0423
na-p2  217.3    1.7490              SOURCE3      11	 0.0192
na-p3  209.2    1.7620              SOURCE3       8	 0.0113
na-p4  386.1    1.5640              SOURCE3       5	 0.2161
na-p5  240.4    1.7150              SOURCE3      11	 0.0238
na-pc  228.5    1.7320              SOURCE3      81	 0.0207
na-pd  228.5    1.7320              SOURCE3      81
na-py  242.6    1.7120              SOURCE3       2
na-s   247.1    1.7650              SOURCE3       8	 0.0095
na-s4  227.9    1.7930              SOURCE3      10	 0.0421
na-s6  279.9    1.7230      SOURCE3_SOURCE5      15	 0.0153
na-sh  281.3    1.7210              SOURCE3       9	 0.0113
na-ss  271.9    1.7320      SOURCE3_SOURCE5      50	 0.0325
na-sy  276.3    1.7270              SOURCE3       1
nb-nb  327.2    1.3330      SOURCE1_SOURCE5      98	 0.0106
nb-pb  358.2    1.5870              SOURCE1     162	 0.0091
nc-nc  290.7    1.3650      SOURCE3_SOURCE5     271	 0.0065
nc-nd  374.7    1.2990      SOURCE3_SOURCE5     185	 0.0074
nc-os  185.1    1.4010      SOURCE1_SOURCE5     243	 0.0096
nc-ss  376.6    1.6260      SOURCE1_SOURCE5     114	 0.0148
nc-sy  473.8    1.5550              SOURCE3       2
nd-nd  290.7    1.3650      SOURCE3_SOURCE5     271	 0.0065
nd-os  185.1    1.4010      SOURCE1_SOURCE5     243	 0.0096
nd-ss  376.6    1.6260      SOURCE1_SOURCE5     114	 0.0148
nd-sy  473.8    1.5550              SOURCE3       2
ne-ne  235.0    1.4220      SOURCE3_SOURCE5      47	 0.0776
ne-nf  432.3    1.2630      SOURCE4_SOURCE5      78	 0.0037
ne-o   360.8    1.2310      SOURCE3_SOURCE5      55	 0.0223
ne-p2  387.4    1.5630              SOURCE3      14	 0.1325
ne-pe  242.6    1.7120              SOURCE3      28	 0.1076
ne-px  250.0    1.7020              SOURCE3      11	 0.0883
ne-py  338.1    1.6050      SOURCE4_SOURCE5      94	 0.0111
ne-s   503.0    1.5370              SOURCE3      22	 0.1708
ne-sx  200.6    1.8380              SOURCE3       7	 0.1060
ne-sy  326.0    1.6720      SOURCE3_SOURCE5      49	 0.0285
nf-nf  235.0    1.4220      SOURCE3_SOURCE5      28	 0.0146
nf-o   360.8    1.2310      SOURCE3_SOURCE5      15	 0.0138
nf-p2  387.4    1.5630              SOURCE3      14
nf-pf  242.6    1.7120              SOURCE3      28
nf-px  250.0    1.7020              SOURCE3      11
nf-py  338.1    1.6050      SOURCE4_SOURCE5      84	 0.0113
nf-s   503.0    1.5370              SOURCE3      22
nf-sx  200.6    1.8380              SOURCE3       7
nf-sy  326.0    1.6720      SOURCE3_SOURCE5      42	 0.0197
nh-nh  252.8    1.4020      SOURCE1_SOURCE5       8	 0.0109
nh-no  267.9    1.3860      SOURCE4_SOURCE5      22	 0.0046
nh-o   316.1    1.2630      SOURCE3_SOURCE5      18	 0.0143
nh-oh  175.3    1.4160      SOURCE4_SOURCE5      63	 0.0072
nh-os  175.9    1.4150      SOURCE4_SOURCE5      26	 0.0063
nh-p2  268.1    1.6790              SOURCE3      17	 0.0872
nh-p3  229.9    1.7300              SOURCE3       3	 0.0016
nh-p4  247.0    1.7060              SOURCE3       3	 0.0008
nh-p5  274.8    1.6710              SOURCE3       3	 0.0007
nh-s   233.8    1.7840              SOURCE3       3	 0.0076
nh-s4  258.9    1.7490              SOURCE3       3	 0.0203
nh-s6  301.9    1.6980      SOURCE4_SOURCE5      93	 0.0076
nh-sh  292.5    1.7080              SOURCE3       1
nh-ss  291.5    1.7090      SOURCE1_SOURCE5      58	 0.0020
nh-sy  287.2    1.7140      SOURCE4_SOURCE5     239	 0.0099
n -n1  319.2    1.3400              SOUECE3       1
n -n2  295.3    1.3600      SOURCE3_SOURCE5     272	 0.0114
n -n3  250.9    1.4040      SOURCE3_SOURCE5      87	 0.0076
n -n4  226.9    1.4320              SOURCE3       5	 0.0098
n -n   250.8    1.4040      SOURCE3_SOURCE5      47	 0.0125
n -na  248.3    1.4070      SOURCE3_SOURCE5      56	 0.0060
n -nc  295.9    1.3600         CORR_SOURCE5     121	 0.0130
n -nd  295.9    1.3600         CORR_SOURCE5     121	 0.0130
n -nh  253.3    1.4020      SOURCE4_SOURCE5      51	 0.0075
n -no  208.3    1.4560              SOURCE3       4	 0.0327
n -o   342.8    1.2430      SOURCE3_SOURCE5      16	 0.0255
n -oh  181.8    1.4060      SOURCE3_SOURCE5     119	 0.0062
no-no   65.4    1.8240              SOURCE3       1
no-o   367.9    1.2260      SOURCE1_SOURCE5    4403	 0.0099
no-oh  182.0    1.4060              SOURCE2       1
no-os  172.2    1.4210      SOURCE4_SOURCE5     138	 0.0070
no-p2  224.5    1.7380              SOURCE3      10	 0.2231
no-p3  165.6    1.8440              SOURCE3       3	 0.0005
no-p4  154.1    1.8700              SOURCE3       3	 0.0006
no-p5  170.3    1.8340              SOURCE3       4	 0.0020
no-s   264.3    1.7420              SOURCE3       2
n -os  180.0    1.4090      SOURCE4_SOURCE5      73	 0.0121
no-s4  131.3    1.9960              SOURCE3       3	 0.0313
no-s6  138.3    1.9760              SOURCE3       3	 0.0520
no-sh  220.8    1.8040              SOURCE3       1
no-ss  206.3    1.8280              SOURCE3       3	 0.0244
n -p2  227.9    1.7330              SOURCE3       8	 0.0217
n -p3  204.4    1.7700              SOURCE3       9	 0.0118
n -p4  227.2    1.7340              SOURCE3       1
n -p5  238.9    1.7170      SOURCE4_SOURCE5      25	 0.0133
n -pc  223.2    1.7400              SOURCE3       3	 0.0010
n -pd  223.2    1.7400              SOURCE3       3
n -s   245.6    1.7670              SOURCE3       3	 0.0011
n -s4  244.9    1.7680      SOURCE3_SOURCE5       9	 0.0163
n -s6  283.3    1.7190      SOURCE4_SOURCE5      45	 0.0154
n -sh  275.5    1.7280              SOURCE3       4	 0.0128
n -ss  277.2    1.7260      SOURCE3_SOURCE5      22	 0.0103
n -sy  285.3    1.7160      SOURCE4_SOURCE5     126	 0.0086
oh-oh  123.1    1.4690              SOURCE3       1
oh-os  129.1    1.4560      SOURCE4_SOURCE5      49	 0.0046
oh-p2  329.9    1.6300              SOURCE3       8	 0.0916
oh-p3  285.0    1.6770              SOURCE3       3	 0.0148
oh-p4  318.7    1.6410              SOURCE3       4	 0.0092
oh-p5  346.0    1.6150      SOURCE3_SOURCE5    1121	 0.0129
oh-py  344.6    1.6160      SOURCE3_SOURCE5     112	 0.0110
oh-s   219.8    1.8120              SOURCE3       2
oh-s4  309.0    1.6960      SOURCE4_SOURCE5      29	 0.0100
oh-s6  373.3    1.6350      SOURCE3_SOURCE5     193	 0.0162
oh-sh  312.6    1.6920              SOURCE3       2	 0.0003
oh-ss  316.4    1.6880      SOURCE3_SOURCE5      12	 0.0167
oh-sy  356.0    1.6500      SOURCE4_SOURCE5     123	 0.0037
o -o   141.4    1.4300              SOURCE3       2	 0.0500
o -oh  104.4    1.5170              SOURCE3       2
o -os  109.1    1.5040              SOURCE3       3	 0.0117
o -p2  492.0    1.5080              SOURCE3      17	 0.0306
o -p3  480.5    1.5150              SOURCE3      35	 0.0297
o -p4  499.0    1.5040      SOURCE3_SOURCE5      60	 0.0565
o -p5  529.5    1.4870      SOURCE1_SOURCE5    1318	 0.0133
o -pe  470.8    1.5210              SOURCE3      20	 0.0171
o -pf  470.8    1.5210              SOURCE3      20
o -px  499.7    1.5040      SOURCE3_SOURCE5      45	 0.0136
o -py  527.9    1.4880      SOURCE3_SOURCE5     119	 0.0072
o -s   226.1    1.8020              SOURCE3       2
o -s2  418.0    1.5990              SOURCE3       3	 0.0707
o -s4  572.3    1.5040      SOURCE1_SOURCE5     137	 0.0127
o -s6  683.0    1.4530      SOURCE1_SOURCE5    2456	 0.0105
o -sh  410.0    1.6050              SOURCE3       2
os-os  124.7    1.4650      SOURCE1_SOURCE5      69	 0.0090
os-p2  396.1    1.5730              SOURCE1      16
os-p3  287.3    1.6740      SOURCE3_SOURCE5      22	 0.0105
os-p4  323.7    1.6360              SOURCE3       4	 0.0057
os-p5  346.2    1.6150      SOURCE1_SOURCE5    1200	 0.0218
os-py  342.1    1.6190      SOURCE3_SOURCE5      68	 0.0106
os-s   227.4    1.8000              SOURCE3       3	 0.0052
o -ss  567.2    1.5070      SOURCE3_SOURCE5      22	 0.0235
os-s4  312.4    1.6920      SOURCE3_SOURCE5      25	 0.0189
os-s6  387.8    1.6230      SOURCE1_SOURCE5     242	 0.0147
os-sh  333.3    1.6710              SOURCE3       3	 0.0106
os-ss  301.4    1.7040              SOURCE3       9	 0.0277
os-sy  306.0    1.6990              SOURCE3       1
o -sx  555.5    1.5130      SOURCE3_SOURCE5     136	 0.0072
o -sy  653.2    1.4660      SOURCE3_SOURCE5    2007	 0.0061
p2-p2  307.6    1.7860              SOURCE3      25	 0.3488
p2-p3  118.0    2.1520              SOURCE3       9	 0.1777
p2-p4  110.7    2.1790              SOUECE3       1
p2-p5  110.4    2.1800              SOUECE3       1
p2-pe  244.9    1.8670              SOURCE3      16	 0.3571
p2-pf  244.9    1.8670              SOURCE3      16
p2-s   375.1    1.7720              SOURCE3      26	 0.3014
p2-s4  126.3    2.1900              SOUECE3       1
p2-s6  129.3    2.1800              SOUECE3       1
p2-sh  217.0    1.9710              SOURCE3      10	 0.2829
p2-ss  219.9    1.9660              SOURCE3      10	 0.2739
p3-p3  102.0    2.2140              SOURCE1      41
p3-p4  101.5    2.2160              SOURCE3       3	 0.0011
p3-p5  102.2    2.2130              SOURCE3       9	 0.0265
p3-s   168.7    2.0700              SOUECE3       1
p3-s4  161.8    2.0870              SOURCE3       8	 0.2235
p3-s6  165.8    2.0770              SOURCE3      11	 0.1420
p3-sh  144.9    2.1320              SOURCE3       3	 0.0078
p3-ss  148.9    2.1210              SOURCE3       3	 0.0059
p4-p4  157.7    2.0340              SOURCE1       1
p4-p5   96.7    2.2370              SOUECE3       1
p4-s   140.2    2.1460              SOURCE3       5	 0.0601
p4-s4  109.6    2.2510              SOUECE3       1
p4-s6  105.2    2.2690              SOUECE3       1
p4-sh  151.0    2.1150              SOURCE3       4	 0.0008
p4-ss  155.1    2.1040              SOURCE3       4	 0.0044
p5-p5  149.9    2.0540              SOURCE1       1
p5-s   239.2    1.9340      SOURCE1_SOURCE5     173	 0.0138
p5-s4  181.8    2.0400              SOUECE3       1
p5-s6  181.8    2.0400              SOUECE3       1
p5-sh  163.8    2.0820              SOURCE3       3	 0.0035
p5-ss  150.1    2.1180      SOURCE4_SOURCE5      70	 0.0117
pe-pe  136.5    2.0920              SOURCE3       7	 0.1369
pe-pf  149.6    2.0550              SOURCE3       1
pe-px  169.8    2.0050              SOURCE3      12	 0.2609
pe-py  161.3    2.0250              SOURCE3      12	 0.2617
pe-s   390.6    1.7580              SOURCE3      31	 0.3197
pe-sx  133.0    2.1680              SOURCE3       9	 0.1743
pe-sy  119.7    2.2130              SOURCE3       6	 0.0127
pf-pf  136.5    2.0920              SOURCE3       7
pf-px  169.8    2.0050              SOURCE3      12
pf-py  161.3    2.0250              SOURCE3      12
pf-s   390.6    1.7580              SOURCE3      31
pf-sx  133.0    2.1680              SOURCE3       9
pf-sy  119.7    2.2130              SOURCE3       6
px-py  105.6    2.1990              SOURCE3       5	 0.0238
px-sx  111.9    2.2420              SOURCE3       3	 0.0119
px-sy  110.1    2.2490              SOURCE3       3	 0.0272
py-py  108.9    2.1860              SOURCE3       8	 0.0132
py-sx  107.7    2.2590              SOURCE3       7	 0.0603
py-sy  128.7    2.1820              SOURCE3       5	 0.0047
s4-s4  243.6    2.0800              SOUECE3       1
s4-s6  243.6    2.0800              SOUECE3       1
s4-sh  196.9    2.1680              SOURCE3       3	 0.0227
s4-ss  197.8    2.1660              SOURCE3       5	 0.0247
s6-s6  243.6    2.0800              SOUECE3       1
s6-sh  227.4    2.1080              SOURCE3       3	 0.0144
s6-ss  222.0    2.1180              SOURCE3       5	 0.0209
sh-sh  257.3    2.0580              SOURCE2       1
sh-ss  251.6    2.0670              SOURCE3       3	 0.0029
s -s   276.1    2.0300              SOURCE3       1
s -s2  391.1    1.8970              SOURCE1       5
s -s4  246.1    2.0760              SOURCE3       4	 0.0345
s -s6  270.6    2.0380              SOURCE3       3	 0.0311
s -sh  226.3    2.1100              SOURCE3       2
s -ss  238.3    2.0890              SOURCE3       1
ss-ss  248.0    2.0730      SOURCE1_SOURCE5     457	 0.0074
sx-sx  119.0    2.3910              SOURCE3       3	 0.0185
sx-sy  160.8    2.2550              SOURCE3       5	 0.0737
sy-sy  162.7    2.2500              SOURCE3       3	 0.0289
br-cd  172.5    1.8850      SOURCE4_SOURCE5      89	 0.0082
c1-cf  518.7    1.3150              SOURCE4       6
cd-f   365.0    1.3410      SOURCE4_SOURCE5      46	 0.0041
cd-n4  236.7    1.4930              SOURCE4       7
cd-nf  356.6    1.3790      SOURCE4_SOURCE5      52	 0.0115
cd-no  296.6    1.4290      SOURCE4_SOURCE5     253	 0.0081
cd-sh  223.3    1.7690      SOURCE4_SOURCE5      14	 0.0031
cd-sx  198.3    1.8110      SOURCE4_SOURCE5      28	 0.0024
cc-cy  269.5    1.4940               5/2017       1
cf-cl  174.7    1.7640      SOURCE4_SOURCE5      66	 0.0129
cf-cx  264.0    1.5000               5/2017       2	 0.0008
cf-cy  250.1    1.5160      SOURCE4_SOURCE5      36	 0.0052
cf-na  305.3    1.4210      SOURCE4_SOURCE5       6	 0.0049
cf-ss  215.6    1.7810      SOURCE4_SOURCE5      46	 0.0106
cq-na  349.5    1.3840              SOURCE4       7
cq-nb  414.7    1.3390      SOURCE4_SOURCE5     120	 0.0071
cl-py  152.8    2.0450              SOURCE5      45	 0.0072
f -py  456.2    1.5770              SOURCE5      25	 0.0035
py-s   215.9    1.9730              SOURCE5      17	 0.0159
cy-nh  279.0    1.4460               5/2017       4	 0.0041
cy-hx  386.5    1.0910               5/2017      13	 0.0007
br-ce  163.4    1.9050              SOURCE5      12	 0.0099
cc-i   110.6    2.1200              SOURCE5      11	 0.0086
cy-n4  218.8    1.5160               5/2017       3	 0.0058
cy-p3  146.8    1.9080               5/2017      10	 0.0056
cy-na  279.0    1.4460               5/2017       8	 0.0049
cx-n4  227.2    1.5050               5/2017       1
ne-s4  338.6    1.6600              SOURCE5       6	 0.0027
cv-ss  255.1    1.7240               5/2017       1
cy-no  216.6    1.5190               5/2017       7	 0.0035
ce-cv  436.8    1.3600               5/2017       6	 0.0111
cd-i   112.0    2.1150              SOURCE5       7	 0.0138
cy-s4  149.5    1.9130               5/2017       5	 0.0068
n2-sy  491.4    1.5440              SOURCE5       7	 0.0042
cc-s6  196.4    1.8140              SOURCE5       6	 0.0108
i -s2   48.1    2.8830              SOURCE5       5	 0.0165
br-cy  144.6    1.9510               5/2017       5	 0.0056
br-cf  163.4    1.9050              SOURCE5      12	 0.0099
nf-s4  338.6    1.6600              SOURCE5       6	 0.0027
cf-cv  436.8    1.3600              SOURCE5       6	 0.0111
cd-s6  196.4    1.8140              SOURCE5       6	 0.0108
ss-sy  177.4    2.2120              SOURCE5       4	 0.0105
h5-ce  390.5    1.0890              SOURCE5       4	 0.0006
h5-cf  390.5    1.0890              SOURCE5       4	 0.0006
ce-s4  226.8    1.7640              SOURCE5       4	 0.0087
cf-s4  226.7    1.7640              SOURCE5       4	 0.0087
cy-py  135.9    1.9370               5/2017       4
cd-o   649.5    1.2190              SOURCE5       4	 0.0015
ne-s6  412.2    1.5980              SOURCE5       3	 0.0054
nf-s6  412.2    1.5980              SOURCE5       3	 0.0054
ce-no  262.7    1.4630              SOURCE5       3	 0.0129
cf-no  262.7    1.4630              SOURCE5       3	 0.0129
cx-op  279.3    1.4370               5/2017     666	 0.0065
c -nj  328.2    1.4010               5/2017     302	 0.0080
cy-nj  251.9    1.4750               5/2017     288	 0.0073
ce-nj  300.8    1.4250               5/2017     186	 0.0050
cx-np  256.4    1.4700               5/2017     185	 0.0035
cx-nm  270.3    1.4550               5/2017     111	 0.0081
c3-nj  273.1    1.4520               5/2017      67	 0.0054
np-p5  250.0    1.7020               5/2017      41	 0.0041
cy-nq  245.9    1.4820               5/2017      52	 0.0039
cy-oq  257.4    1.4600               5/2017      33	 0.0108
cc-nm  311.9    1.4150               5/2017      22	 0.0063
c3-np  263.7    1.4620               5/2017      27	 0.0036
c3-nq  270.3    1.4550               5/2017      15	 0.0039
ca-nm  352.1    1.3820               5/2017      19	 0.0036
cy-sq  178.0    1.8490               5/2017      19	 0.0085
c -oq  353.0    1.3730               5/2017      15	 0.0032
p5-sq  132.4    2.1700               5/2017      12	 0.0011
cf-nj  308.5    1.4180               5/2017       7	 0.0034
cy-nn  249.3    1.4780               5/2017      10	 0.0016
nj-s6  278.0    1.7250               5/2017      13	 0.0159
cd-nm  365.5    1.3720               5/2017       9	 0.0067
hn-np  506.2    1.0210               5/2017       9	 0.0009
hn-nq  513.9    1.0180               5/2017       9	 0.0008
cx-nk  234.3    1.4960               5/2017       9	 0.0009
c3-nk  226.4    1.5060               5/2017       6	 0.0073
cy-nl  213.0    1.5240               5/2017       7	 0.0075
ca-nn  361.4    1.3750               5/2017       7	 0.0030
cx-ni  241.7    1.4870               5/2017       8	 0.0076
cv-sq  228.8    1.7610               5/2017       8	 0.0086
np-py  251.5    1.7000               5/2017       5	 0.0044
cx-nj  277.0    1.4480               5/2017       6	 0.0040
nq-p5  227.2    1.7340               5/2017       4	 0.0747
hn-nj  527.1    1.0130               5/2017       5	 0.0006
c2-nm  325.9    1.4030               5/2017       4	 0.0014
ca-nj  322.3    1.4060               5/2017       2	 0.0004
c -ni  292.3    1.4330               5/2017       3	 0.0055
cy-n2  301.9    1.4240               5/2017       3	 0.0008
op-p5  342.6    1.6180               5/2017       3	 0.0012
cx-sp  190.9    1.8240               5/2017       3	 0.0172
hn-nl  442.6    1.0480               5/2017       3	 0.0410
nn-p5  279.9    1.6650               5/2017       2
nj-p5  208.6    1.7630               5/2017       2	 0.0519
cc-sq  218.4    1.7770               5/2017       3	 0.0006
c2-cv  484.2    1.3330               5/2017       2	 0.0002
c1-cy  299.1    1.4640               5/2017       3	 0.0061
cy-i    93.4    2.1910               5/2017       3	 0.0116
oq-p5  270.6    1.6940               5/2017       4	 0.0003
nj-os  187.4    1.3980               5/2017       2	 0.0028
op-op   80.1    1.5970               5/2017       2	 0.0081
cy-p5  153.7    1.8910               5/2017       2
cy-sx  171.8    1.8620               5/2017       1
cx-i    94.2    2.1870               5/2017       2	 0.0025
cx-no  231.9    1.4990               5/2017       1
ce-cu  535.9    1.3070               5/2017       2	 0.0055
np-sy  270.6    1.7340               5/2017       2	 0.0135
cl-nj  162.6    1.7250               5/2017       2
np-s6  226.6    1.7950               5/2017       2	 0.0042
np-op  139.3    1.4810               5/2017       2	 0.0016
cl-np  132.9    1.7940               5/2017       2	 0.0014
cx-p5  178.4    1.8370               5/2017       2	 0.0063
cl-cv  188.6    1.7380               5/2017       2	 0.0089
cv-nh  369.6    1.3690               5/2017       2	 0.0397
nq-s4  270.6    1.7340               5/2017       2
c3-nl  224.9    1.5080               5/2017       2	 0.0085
np-p3  212.3    1.7570               5/2017       1
cu-f   404.8    1.3140               5/2017       2
c -sq  190.4    1.8250               5/2017       1
cu-os  409.3    1.3340               5/2017       1
cy-sh  184.1    1.8370               5/2017       1
cv-oq  270.5    1.4460               5/2017       1
cu-cv  529.6    1.3100               5/2017       1
c1-nj  403.3    1.3460               5/2017       1
cu-ne  543.7    1.2700               5/2017       1
cu-op  430.5    1.3210               5/2017       1
s6-sp  244.8    2.0780               5/2017       1
sp-sp  218.8    2.1240               5/2017       1
cv-ne  577.9    1.2550               5/2017       1
op-s6  390.9    1.6200               5/2017       1
op-sp  191.1    1.8620               5/2017       1
c1-cv  538.0    1.3060               5/2017       1
n2-nj  275.4    1.3790               5/2017       1
nq-nq  182.5    1.4940               5/2017       1
cv-p3  193.6    1.8080               5/2017       1
cv-p5  281.6    1.6810               5/2017       1
np-os  163.8    1.4350               5/2017       1
nj-nq  206.1    1.4590               5/2017       1
no-nq  303.7    1.3530               5/2017       1
cy-sy  177.6    1.8500               5/2017       1
ce-nm  330.7    1.3990               5/2017       1
cv-os  359.7    1.3680               5/2017       1
cy-n1  298.6    1.4270               5/2017       1
c -op  423.8    1.3250               5/2017       1
cv-n2  539.3    1.2720               5/2017       1
cx-oq  280.3    1.4360               5/2017       1
cx-n1  339.3    1.3920               5/2017       1
""")

gaff_angles = dedent("""
hw-ow-hw   100.0      104.52                AMBER            1
hw-hw-ow     0.0      127.74                AMBER            1
br-c1-br    58.4      180.00                Guess            0
br-c1-c1    56.1      180.00              SOURCE3            1
c1-c1-c1    65.5      180.00              SOURCE3            1
c1-c1-c2    62.5      180.00              SOURCE3            2
c1-c1-c3    58.0      178.51      SOURCE4_SOURCE5          618    0.7369
c1-c1-ca    58.5      180.00              SOURCE3            1
c1-c1-cl    63.9      180.00              SOURCE3            1
c1-c1-f     80.7      180.00              SOURCE3            1
c1-c1-ha    44.8      179.11      SOURCE3_SOURCE5          219    0.5885
c1-c1-hc    44.8      180.00              SOURCE3            1
c1-c1-i     53.0      180.00              SOURCE3            1
c1-c1-n1    83.6      180.00              SOURCE3            1
c1-c1-n2    82.1      180.00              SOURCE3            1
c1-c1-n3    76.7      180.00              SOURCE3            1
c1-c1-n4    74.2      179.56              SOURCE3            3    0.3096
c1-c1-n     78.0      177.18              SOURCE3            1
c1-c1-na    76.9      176.75              SOURCE3            8    2.9328
c1-c1-nh    77.1      179.27              SOURCE3            3    0.2357
c1-c1-no    74.6      180.00              SOURCE3            3
c1-c1-o     82.9      180.00              SOURCE3            1
c1-c1-oh    78.2      176.65              SOURCE3            1
c1-c1-os    78.5      176.93      SOURCE3_SOURCE5            5    1.1927
c1-c1-p2    68.2      180.00              SOURCE3            1
c1-c1-p3    69.4      169.63              SOURCE3            2
c1-c1-p4    67.4      180.00              SOURCE3            1
c1-c1-p5    69.5      176.17              SOURCE3            2
c1-c1-s4    55.8      167.47              SOURCE3            2
c1-c1-s6    55.4      174.38              SOURCE3            2
c1-c1-s     58.1      179.97              SOURCE3            1
c1-c1-sh    55.8      180.00              SOURCE3            1
c1-c1-ss    56.2      175.60      SOURCE3_SOURCE5           19    1.3679
c2-c1-c2    60.2      179.37      SOURCE3_SOURCE5           14    0.3391
c2-c1-ce    60.0      179.05      SOURCE4_SOURCE5           15    0.4210
c2-c1-n1    79.3      180.00            HF/6-31G*            1
c2-c1-o     79.0      179.50              SOURCE2            1
c2-c1-s2    58.5      172.98              SOURCE3            1
c3-c1-c3    53.5      180.00                Guess            0
c3-c1-cg    57.8      178.43      SOURCE4_SOURCE5          134    0.5502
c3-c1-n1    73.2      178.58      SOURCE4_SOURCE5          245    0.5409
ca-c1-ca    54.5      180.00                Guess            0
c -c1-c1    57.9      180.00              SOURCE3            1
cg-c1-ha    44.4      178.83      SOURCE3_SOURCE5           60    1.1251
ch-c1-ha    44.3      178.83      SOURCE3_SOURCE5           38    0.3321
cl-c1-cl    70.2      180.00                Guess            0
f -c1-f     99.8      180.00                Guess            0
i -c1-i     58.4      180.00                Guess            0
n1-c1-n1   141.8      102.01              SOURCE3            1
n1-c1-n3    98.4      176.01      SOURCE2_SOURCE5            5    0.1498
n1-c1-nh    98.2      177.65      SOURCE4_SOURCE5           18    0.7845
n1-c1-os    99.2      178.59              SOURCE3            1
n1-c1-p3    86.6      171.20              SOURCE2            1
n1-c1-ss    70.1      177.47      SOURCE3_SOURCE5           15    0.7211
n2-c1-n2   102.9      180.00                Guess            0
n2-c1-o    106.1      172.73      SOURCE3_SOURCE5           10    0.3647
n2-c1-s     73.6      175.91      SOURCE4_SOURCE5           29    0.2046
n3-c1-n3    91.4      180.00                Guess            0
n4-c1-n4    86.9      180.00                Guess            0
na-c1-na    90.4      180.00                Guess            0
ne-c1-o    106.0      172.33              SOURCE3            1
ne-c1-s     73.6      175.82      SOURCE4_SOURCE5           23    0.2168
nf-c1-o    106.0      172.33              SOURCE3            1
nh-c1-nh    91.7      180.00                Guess            0
n -c1-n     92.6      180.00                Guess            0
no-c1-no    87.6      180.00                Guess            0
oh-c1-oh    92.9      180.00                Guess            0
o -c1-o    105.0      180.00                Guess            0
os-c1-os    93.4      180.00                Guess            0
p2-c1-p2    85.4      180.00                Guess            0
p3-c1-p3    84.4      180.00                Guess            0
p4-c1-p4    84.4      180.00                Guess            0
p5-c1-p5    86.2      180.00                Guess            0
s2-c1-s2    57.5      180.00                Guess            0
s4-c1-s4    52.6      180.00                Guess            0
s6-c1-s6    53.3      180.00                Guess            0
sh-c1-sh    54.6      180.00                Guess            0
s -c1-s     57.2      180.00                Guess            0
ss-c1-ss    54.3      180.00                Guess            0
br-c2-br    69.0      115.06              SOURCE3            1
br-c2-c2    64.5      121.03      SOURCE4_SOURCE5           18    0.8426
br-c2-c3    64.8      115.32      SOURCE4_SOURCE5           18    0.6855
br-c2-ce    64.3      121.53      SOURCE4_SOURCE5           18    0.7036
br-c2-h4    42.8      113.73      SOURCE4_SOURCE5           17    0.5888
br-c2-ha    42.9      113.28              SOURCE3            1
c1-c2-c1    74.6      116.77              SOURCE3            1
c1-c2-c2    72.3      121.62              SOURCE3            1
c1-c2-c3    66.2      124.90      SOURCE4_SOURCE5           44    0.7045
c1-c2-f     90.5      124.90              SOURCE2            1
c1-c2-ha    51.1      120.42      SOURCE3_SOURCE5           30    0.4602
c2-c2-c2    71.5      121.81              SOURCE3           10    0.3843
c2-c2-c3    66.1      123.63      SOURCE3_SOURCE5         4623    2.2803
c2-c2-ca    71.6      117.00              SOURCE3            1
c2-c2-cc    72.2      117.21              SOURCE3            2    0.3418
c2-c2-cd    72.2      117.21              SOURCE3            2
c2-c2-cl    72.3      123.11      SOURCE4_SOURCE5          103    1.0574
c2-c2-cx    66.5      124.81               5/2017           39    1.8529
c2-c2-cy    67.5      118.44               5/2017           11    1.7549
c2-c2-f     90.3      122.87      SOURCE4_SOURCE5           37    0.6494
c2-c2-h4    49.9      122.67      SOURCE4_SOURCE5          266    1.3387
c2-c2-ha    50.4      120.43      SOURCE3_SOURCE5         3764    1.3300
c2-c2-hc    50.5      119.70              SOURCE3            1
c2-c2-hx    49.2      126.45              SOURCE3            3    0.0219
c2-c2-i     59.3      121.03              SOURCE3            2
c2-c2-n1    90.1      122.98            HF/6-31G*            1
c2-c2-n2    89.8      126.01              SOURCE3            1
c2-c2-n3    88.4      124.55              SOURCE3            1
c2-c2-n4    83.4      121.52              SOURCE3            5    1.2656
c2-c2-n     86.7      123.67      SOURCE4_SOURCE5           48    1.8326
c2-c2-na    87.2      121.94      SOURCE3_SOURCE5           35    5.4059
c2-c2-nh    86.7      124.99              SOURCE3            7    0.9929
c2-c2-no    85.1      123.46      SOURCE4_SOURCE5           26    1.6311
c2-c2-o     89.8      130.89              SOURCE3            2    0.0201
c2-c2-oh    89.3      122.17      SOURCE4_SOURCE5           18    1.1206
c2-c2-os    88.7      121.87      SOURCE4_SOURCE5          114    1.6810
c2-c2-p2    88.5      115.10              SOURCE3            1
c2-c2-p3    78.6      124.83              SOURCE3            5    2.1222
c2-c2-p4    80.7      119.76              SOURCE3            1
c2-c2-p5    77.1      125.97              SOURCE3            1
c2-c2-s4    64.7      119.84              SOURCE3            1
c2-c2-s6    64.7      120.01              SOURCE3            1
c2-c2-s     63.1      129.37              SOURCE3            2
c2-c2-sh    62.6      125.70              SOURCE3            3    1.3390
c2-c2-ss    64.8      122.35      SOURCE4_SOURCE5           54    2.2017
c3-c2-c3    64.9      115.65      SOURCE3_SOURCE5         1743    1.5647
c3-c2-cc    65.3      125.19         CORR_SOURCE5           50    1.5929
c3-c2-cd    65.3      125.19         CORR_SOURCE5           50    1.5929
c3-c2-ce    66.1      123.15         CORR_SOURCE5         2644    2.0746
c3-c2-cf    66.1      123.15         CORR_SOURCE5         2644    2.0746
c3-c2-h4    45.8      119.02      SOURCE4_SOURCE5           63    1.6077
c3-c2-ha    46.4      115.68      SOURCE3_SOURCE5         3991    1.1961
c3-c2-hc    45.6      120.00              SOURCE3            1
c3-c2-n2    84.0      123.43      SOURCE4_SOURCE5          388    2.3609
c3-c2-n     84.4      114.80              SOURCE4           12    1.8112
c3-c2-na    83.5      117.20      SOURCE3_SOURCE5            5    0.8937
c3-c2-ne    84.7      120.71      SOURCE3_SOURCE5           11    0.9157
c3-c2-nf    84.7      120.71      SOURCE3_SOURCE5            7    1.3134
c3-c2-nh    84.2      116.21      SOURCE3_SOURCE5          339    2.4814
c3-c2-o     85.2      122.82      SOURCE4_SOURCE5           12    1.1220
c3-c2-oh    85.7      115.16      SOURCE4_SOURCE5           90    2.0675
c3-c2-os    86.1      112.80      SOURCE4_SOURCE5          148    2.4217
c3-c2-p2    82.6      122.74              SOURCE3            2
c3-c2-s     64.7      115.44              SOURCE3            2    0.0115
c3-c2-ss    63.5      119.66      SOURCE4_SOURCE5          137    2.1299
ca-c2-ca    70.1      117.88              SOURCE3            1
ca-c2-hc    48.4      123.30              SOURCE3            1
c -c2-c2    69.9      120.70              SOURCE3            1
c -c2-c3    65.9      119.70              SOURCE3            1
c -c2-c     68.7      118.88              SOURCE3            1
cc-c2-h4    49.8      119.85      SOURCE4_SOURCE5           23    0.5829
cc-c2-ha    50.0      118.75      SOURCE3_SOURCE5           72    1.1667
cc-c2-nh    86.6      123.12      SOURCE4_SOURCE5           27    1.0384
cc-c2-o     91.4      123.59      SOURCE4_SOURCE5           12    0.0560
cd-c2-ha    50.0      118.75      SOURCE3_SOURCE5           72    1.1667
ce-c2-cl    72.1      123.47      SOURCE4_SOURCE5           41    0.8440
ce-c2-h4    49.7      122.31      SOURCE4_SOURCE5          220    1.5462
ce-c2-ha    50.0      120.45      SOURCE3_SOURCE5         2139    1.1520
ce-c2-na    86.1      124.17      SOURCE4_SOURCE5           12    1.9766
ce-c2-nh    87.8      120.71      SOURCE4_SOURCE5          243    2.3407
ce-c2-no    86.1      119.65      SOURCE4_SOURCE5           10    0.9817
ce-c2-o     92.0      123.37      SOURCE4_SOURCE5           14    0.7592
ce-c2-oh    88.6      123.13      SOURCE4_SOURCE5          104    1.7734
ce-c2-os    88.0      122.80      SOURCE4_SOURCE5          149    2.3406
cf-c2-ha    50.0      120.45      SOURCE3_SOURCE5         2017    1.1895
c -c2-ha    48.2      121.33              SOURCE3            4    0.2462
c -c2-hc    48.5      119.70              SOURCE3            1
cl-c2-cl    83.0      114.34      SOURCE4_SOURCE5           29    0.6417
cl-c2-h4    49.5      113.54      SOURCE4_SOURCE5           33    0.7337
cl-c2-ha    49.6      113.20              SOURCE3            1
cx-c2-ha    47.0      116.23               5/2017           49    1.0274
f -c2-f    120.2      111.64      SOURCE2_SOURCE5           12    0.8567
f -c2-ha    66.8      110.00              SOURCE2            1
h4-c2-n2    64.8      120.99      SOURCE4_SOURCE5           77    1.9305
h4-c2-n     62.6      113.44      SOURCE4_SOURCE5           78    1.0580
h4-c2-na    62.7      112.97      SOURCE4_SOURCE5           27    0.6876
h4-c2-ne    64.9      119.51      SOURCE4_SOURCE5           52    1.6395
h4-c2-nh    62.6      115.08      SOURCE4_SOURCE5          109    1.1974
h4-c2-no    60.9      113.38      SOURCE4_SOURCE5           20    0.1373
h4-c2-os    64.0      113.73      SOURCE3_SOURCE5           89    1.3113
h4-c2-ss    43.6      116.67      SOURCE3_SOURCE5           49    1.4612
h5-c2-n2    64.5      121.70      SOURCE4_SOURCE5           71    2.1538
h5-c2-na    59.2      126.39              SOURCE3            4    0.3299
h5-c2-ne    64.7      119.85      SOURCE4_SOURCE5           44    1.3576
h5-c2-nh    62.9      113.91      SOURCE4_SOURCE5          119    0.8516
ha-c2-ha    37.7      116.90      SOURCE3_SOURCE5         1456    0.6313
ha-c2-n1    64.0      120.76              SOURCE3            8    0.6632
ha-c2-n2    64.9      120.54              SOURCE3           92    1.4571
ha-c2-n3    64.7      113.54              SOURCE3            1
ha-c2-n     62.6      113.40              SOURCE3            4    1.2182
ha-c2-na    62.8      112.42              SOURCE3            8    0.6507
ha-c2-ne    64.4      121.18              SOURCE3           68    0.6824
ha-c2-nf    64.4      121.18              SOURCE3           68
ha-c2-nh    62.2      116.68              SOURCE3           13    2.5734
ha-c2-no    61.2      112.14              SOURCE3            2    0.0264
ha-c2-o     67.9      117.23              SOURCE3            2    0.0201
ha-c2-oh    64.1      116.18              SOURCE3            2
ha-c2-os    64.3      112.69              SOURCE3           13    2.5851
ha-c2-p2    57.1      121.48              SOURCE3          122    0.4329
ha-c2-p3    53.3      114.31              SOURCE3            3
ha-c2-p4    52.8      117.86              SOURCE3            1
ha-c2-p5    52.0      116.00      SOURCE3_SOURCE5            6    0.1220
ha-c2-pe    56.4      121.40      SOURCE3_SOURCE5          119    0.8904
ha-c2-pf    56.4      121.40      SOURCE3_SOURCE5           15    1.6416
ha-c2-s2    46.6      118.74              SOURCE3            2
ha-c2-s4    43.2      115.30              SOURCE3            2
ha-c2-s     43.8      115.70              SOURCE3            2
ha-c2-s6    43.0      116.60              SOURCE3            2
ha-c2-sh    43.3      111.74              SOURCE3            1
ha-c2-ss    43.6      116.72              SOURCE3            7    2.7543
hc-c2-hc    37.4      118.92              SOURCE3            1
hc-c2-n2    65.0      120.40              SOURCE3            1
hc-c2-n     62.5      114.04              SOURCE3            1
hc-c2-na    61.0      119.10              SOURCE3            1
hc-c2-nh    63.1      113.36              SOURCE3            1
hc-c2-no    61.2      112.12              SOURCE3            1
hc-c2-oh    64.1      116.22              SOURCE3            1
hc-c2-os    63.3      116.11              SOURCE3            1
hc-c2-p3    52.6      117.19              SOURCE3            1
hc-c2-p5    51.2      119.58              SOURCE3            1
hc-c2-s4    43.1      116.12              SOURCE3            1
hc-c2-s6    43.2      115.45              SOURCE3            1
hc-c2-sh    42.6      115.63              SOURCE3            1
hc-c2-ss    43.8      115.62              SOURCE3            1
hx-c2-n4    58.7      113.03              SOURCE3            3    0.3873
i -c2-i     66.1      117.94              SOURCE3            1
n1-c2-n1   113.5      124.15            HF/6-31G*            1
n2-c2-n2   120.8      113.82              SOURCE3            1
n2-c2-n4   109.7      112.97      SOURCE4_SOURCE5           13    0.4034
n2-c2-na   110.3      123.62              SOURCE3            1
n2-c2-nh   110.7      124.27              SOURCE3           12    2.4114
n2-c2-oh   114.0      122.08              SOURCE3            1
n2-c2-os   114.1      119.78      SOURCE4_SOURCE5           55    1.3881
n2-c2-ss    79.3      129.77              SOURCE3            1
n3-c2-n3   113.3      118.47              SOURCE3            1
n4-c2-n4   102.3      113.93              SOURCE3            1
n4-c2-ss    80.7      116.27      SOURCE4_SOURCE5           14    2.4226
na-c2-na   112.7      109.33              SOURCE3            3    3.0187
ne-c2-nh   110.7      123.46         CORR_SOURCE5          241    2.3941
ne-c2-os   114.2      118.76              SOURCE4            5    0.3382
ne-c2-ss    82.2      120.51      SOURCE4_SOURCE5           32    2.1160
nf-c2-nh   110.7      123.46         CORR_SOURCE5          241    2.3941
nh-c2-nh   112.1      112.82      SOURCE4_SOURCE5          689    1.9577
nh-c2-oh   111.9      117.11      SOURCE4_SOURCE5           15    0.8639
nh-c2-os   112.5      114.30      SOURCE4_SOURCE5           50    1.3395
nh-c2-ss    84.3      111.55              SOURCE4           37    1.1778
n -c2-n2   110.8      122.82      SOURCE3_SOURCE5           46    2.2661
n -c2-n    110.9      113.23              SOURCE3            1
n -c2-na   114.9      105.42              SOURCE3            1
n -c2-ne   109.3      125.34      SOURCE4_SOURCE5           25    1.6082
n -c2-nh   113.4      109.35      SOURCE4_SOURCE5           61    1.6924
no-c2-no   106.9      113.90              SOURCE3            1
n -c2-ss    84.3      111.19      SOURCE4_SOURCE5           24    0.6195
oh-c2-oh   115.4      114.33              SOURCE3            1
o -c2-o    122.3      121.69              SOURCE3            1
o -c2-oh   116.6      121.23      SOURCE4_SOURCE5           12    0.0958
o -c2-s     80.4      127.68              SOURCE3            2    0.0547
os-c2-os   113.3      115.05      SOURCE3_SOURCE5            6    1.2203
p2-c2-p2   106.7      129.80              SOURCE3            1
p3-c2-p3   102.9      115.54              SOURCE3            1
p5-c2-p5    98.6      121.85              SOURCE3            1
s4-c2-s4    63.8      120.32              SOURCE3            1
s4-c2-s6    63.9      119.95              SOURCE3            1
s6-c2-s6    63.9      119.97              SOURCE3            1
sh-c2-sh    65.7      110.48              SOURCE3            1
sh-c2-ss    64.5      117.82              SOURCE3            1
s -c2-s     64.4      121.67              SOURCE3            1
ss-c2-ss    65.7      116.40      SOURCE3_SOURCE5           22    2.3993
br-c3-br    67.6      109.74      SOURCE4_SOURCE5           24    0.9971
br-c3-c1    63.8      111.80              SOURCE2            3    0.2160
br-c3-c3    63.9      110.01      SOURCE3_SOURCE5          216    1.1568
br-c3-c     64.3      108.92      SOURCE4_SOURCE5           35    2.3703
br-c3-h1    42.4      105.07      SOURCE3_SOURCE5          175    0.8275
br-c3-h2    42.1      106.80      SOURCE4_SOURCE5           25    0.8044
br-c3-hc    42.1      106.50              SOURCE3            1
c1-c3-c1    68.4      110.11      SOURCE2_SOURCE5           11    0.3454
c1-c3-c2    67.2      110.92      SOURCE4_SOURCE5           35    0.5903
c1-c3-c3    66.3      111.71      SOURCE4_SOURCE5          624    1.1320
c1-c3-ca    67.0      110.89      SOURCE4_SOURCE5           78    1.1306
c1-c3-cc    66.4      114.19         CORR_SOURCE5           15    0.1283
c1-c3-cd    66.4      114.19         CORR_SOURCE5           15    0.1283
c1-c3-cl    72.4      110.63              SOURCE2            3    1.2257
c1-c3-h1    48.9      109.24      SOURCE4_SOURCE5          436    0.5758
c1-c3-hc    48.9      109.41      SOURCE3_SOURCE5          495    0.5104
c1-c3-hx    48.3      112.04      SOURCE4_SOURCE5           52    0.3815
c1-c3-n3    84.8      112.73      SOURCE4_SOURCE5           99    0.7675
c1-c3-n4    83.7      112.06      SOURCE4_SOURCE5           25    0.5395
c1-c3-n     85.0      112.38      SOURCE4_SOURCE5           55    0.9540
c1-c3-nh    84.8      112.57      SOURCE4_SOURCE5           21    0.9525
c1-c3-oh    87.2      109.44      SOURCE4_SOURCE5          127    0.9878
c1-c3-os    87.2      109.00      SOURCE4_SOURCE5           87    0.9531
c2-c3-c2    65.9      112.00      SOURCE4_SOURCE5          453    0.8153
c2-c3-c3    65.5      111.56      SOURCE4_SOURCE5         9345    1.7373
c2-c3-ca    65.7      112.49      SOURCE4_SOURCE5          475    1.6791
c2-c3-cc    66.1      111.91         CORR_SOURCE5           65    1.7402
c2-c3-cd    66.1      111.91         CORR_SOURCE5           65    1.7402
c2-c3-ce    65.9      111.81         CORR_SOURCE5           85    1.8411
c2-c3-cf    65.9      111.81         CORR_SOURCE5           85    1.8411
c2-c3-cl    71.9      110.51      SOURCE4_SOURCE5           60    1.4762
c2-c3-cx    65.6      112.17               5/2017           59    1.2898
c2-c3-cy    68.6      101.79               5/2017          106    1.1242
c2-c3-f     88.4      110.76      SOURCE4_SOURCE5           69    0.5776
c2-c3-h1    47.6      109.96      SOURCE3_SOURCE5         2169    0.9645
c2-c3-h2    47.2      111.69      SOURCE4_SOURCE5           49    0.9061
c2-c3-hc    47.5      110.36      SOURCE3_SOURCE5        11033    0.8531
c2-c3-hx    47.3      111.34      SOURCE4_SOURCE5           56    0.8089
c2-c3-n2    85.0      108.72      SOURCE4_SOURCE5           36    1.3485
c2-c3-n3    84.0      111.42      SOURCE4_SOURCE5          447    1.5436
c2-c3-n     84.1      111.29      SOURCE4_SOURCE5          180    1.8899
c2-c3-na    83.4      113.27      SOURCE4_SOURCE5           78    1.2929
c2-c3-nh    84.4      110.41      SOURCE4_SOURCE5          134    1.7670
c2-c3-oh    85.5      110.35      SOURCE4_SOURCE5          793    1.4429
c2-c3-os    86.0      108.56      SOURCE4_SOURCE5          763    1.7474
c2-c3-s4    63.9      109.89      SOURCE4_SOURCE5           19    0.8365
c2-c3-ss    65.1      104.97              SOURCE3            2    2.2248
c3-c3-c3    64.9      111.51      SOURCE3_SOURCE5        61999    1.8007
c3-c3-ca    65.2      112.07      SOURCE4_SOURCE5        11982    1.5875
c3-c3-cc    65.5      111.93         CORR_SOURCE5         2280    1.5614
c3-c3-cd    65.5      111.93         CORR_SOURCE5         2280    1.5614
c3-c3-ce    65.5      110.92         CORR_SOURCE5         1159    1.8552
c3-c3-cf    65.5      110.92         CORR_SOURCE5         1159    1.8552
c3-c3-cl    71.5      110.41      SOURCE3_SOURCE5          824    0.9824
c3-c3-cx    65.2      111.36               5/2017          561    2.5219
c3-c3-cy    64.7      112.43               5/2017          317    1.3511
c3-c3-f     87.9      109.24      SOURCE3_SOURCE5          785    1.1106
c3-c3-h1    46.9      109.56      SOURCE3_SOURCE5        55294    0.8125
c3-c3-h2    46.7      110.22      SOURCE3_SOURCE5         1083    0.9457
c3-c3-hc    46.8      109.80      SOURCE3_SOURCE5       179054    0.7972
c3-c3-hx    46.7      110.56      SOURCE3_SOURCE5         1758    0.9658
c3-c3-i     60.8      111.15      SOURCE3_SOURCE5           48    1.3033
c3-c3-n1    84.9      108.98      SOURCE4_SOURCE5           20    0.8416
c3-c3-n2    84.1      108.80      SOURCE3_SOURCE5          665    2.1214
c3-c3-n3    83.3      111.04      SOURCE3_SOURCE5        12086    1.5519
c3-c3-n4    81.0      114.21      SOURCE4_SOURCE5         1537    2.4293
c3-c3-n     83.2      111.61      SOURCE3_SOURCE5         3543    1.6672
c3-c3-na    82.7      112.88      SOURCE4_SOURCE5         1677    1.4742
c3-c3-nh    83.5      110.46      SOURCE4_SOURCE5         3983    1.4189
c3-c3-no    82.1      109.41      SOURCE4_SOURCE5          111    1.3831
c3-c3-o     85.9      113.01      SOURCE4_SOURCE5           31    1.2728
c3-c3-oh    84.6      110.19      SOURCE3_SOURCE5        10188    1.4761
c3-c3-os    85.3      107.97      SOURCE3_SOURCE5        11384    1.3754
c3-c3-p3    79.4      113.36      SOURCE4_SOURCE5           47    0.9033
c3-c3-p5    80.5      112.02      SOURCE4_SOURCE5          346    1.5599
c3-c3-s4    63.5      110.12      SOURCE4_SOURCE5          117    0.9869
c3-c3-s6    64.0      110.22      SOURCE4_SOURCE5          420    1.6420
c3-c3-sh    62.3      113.13      SOURCE4_SOURCE5          226    1.3868
c3-c3-ss    63.2      110.27      SOURCE3_SOURCE5         1315    1.5441
c3-c3-sy    64.1      109.92      SOURCE4_SOURCE5           62    0.8825
ca-c3-ca    65.6      112.24      SOURCE4_SOURCE5         1062    1.7394
ca-c3-cc    65.7      112.88         CORR_SOURCE5          146    1.4369
ca-c3-cd    65.7      112.88         CORR_SOURCE5          146    1.4369
ca-c3-ce    65.6      112.21      SOURCE4_SOURCE5          144    1.2359
ca-c3-cl    71.6      110.98      SOURCE4_SOURCE5           62    0.7657
ca-c3-cx    65.4      112.62               5/2017           19    2.0061
ca-c3-f     87.8      111.77      SOURCE4_SOURCE5         1080    0.3344
ca-c3-h1    47.5      109.56      SOURCE3_SOURCE5         3349    0.8812
ca-c3-h2    47.5      109.70      SOURCE4_SOURCE5           86    1.1507
ca-c3-hc    47.3      110.47      SOURCE3_SOURCE5        13973    0.8325
ca-c3-hx    47.1      111.45      SOURCE4_SOURCE5          113    0.5046
ca-c3-n2    83.4      112.39      SOURCE4_SOURCE5           58    1.2061
ca-c3-n3    83.5      112.16      SOURCE4_SOURCE5         1125    1.2435
ca-c3-n4    81.7      113.80      SOURCE4_SOURCE5           79    2.4049
ca-c3-n     83.5      112.38      SOURCE4_SOURCE5          512    1.5411
ca-c3-na    83.3      112.87      SOURCE4_SOURCE5          240    1.5673
ca-c3-nc    86.0      106.51              SOURCE3            1
ca-c3-nd    86.0      106.51              SOURCE3            1
ca-c3-nh    83.9      111.39      SOURCE4_SOURCE5          349    0.9955
ca-c3-oh    85.2      110.62      SOURCE4_SOURCE5         1007    1.2078
ca-c3-os    85.6      108.95      SOURCE4_SOURCE5         1123    1.1238
ca-c3-p5    80.2      113.60      SOURCE4_SOURCE5           41    1.4171
ca-c3-s6    63.9      111.54      SOURCE4_SOURCE5           38    1.2112
ca-c3-ss    63.3      111.02      SOURCE4_SOURCE5          226    1.6105
ca-c3-sx    63.3      110.78      SOURCE4_SOURCE5           40    0.6145
c -c3-c1    66.4      112.38      SOURCE4_SOURCE5           32    1.1114
c -c3-c2    65.8      111.33      SOURCE4_SOURCE5          282    2.0882
c -c3-c3    65.3      111.04      SOURCE3_SOURCE5         8161    1.7693
c -c3-c     65.4      111.63      SOURCE4_SOURCE5          409    2.2030
c -c3-ca    65.8      111.01      SOURCE4_SOURCE5         1282    1.7239
c -c3-cc    65.5      113.17         CORR_SOURCE5          164    1.3730
cc-c3-cc    66.2      112.39         CORR_SOURCE5           14    0.8688
cc-c3-cd    66.0      112.89      SOURCE3_SOURCE5           10    1.0674
cc-c3-cx    65.9      111.78               5/2017            7    1.7201
c -c3-cd    65.5      113.17         CORR_SOURCE5          164    1.3730
c -c3-ce    65.5      111.89      SOURCE4_SOURCE5           75    1.6968
cc-c3-f     88.5      111.31         CORR_SOURCE5          105    0.4710
cc-c3-h1    47.9      109.64      SOURCE3_SOURCE5         1145    0.8896
cc-c3-hc    47.7      110.49      SOURCE3_SOURCE5         6781    0.7714
cc-c3-hx    47.6      111.01      SOURCE4_SOURCE5           19    0.7303
c -c3-cl    71.7      110.41      SOURCE4_SOURCE5          146    1.5057
cc-c3-n2    84.6      110.31      SOURCE4_SOURCE5           32    0.5465
cc-c3-n3    84.4      111.09         CORR_SOURCE5          192    1.4026
cc-c3-n4    81.5      115.58      SOURCE4_SOURCE5           12    1.1723
cc-c3-n     84.2      111.76         CORR_SOURCE5           51    1.5321
cc-c3-na    83.6      113.15      SOURCE4_SOURCE5           18    0.7152
cc-c3-nc    86.2      107.04              SOURCE3            2
cc-c3-nh    83.9      112.34         CORR_SOURCE5           25    1.8212
cc-c3-oh    85.4      111.16         CORR_SOURCE5          187    1.3741
cc-c3-os    86.1      108.90         CORR_SOURCE5          213    1.1488
cc-c3-p5    79.5      116.23      SOURCE4_SOURCE5           12    0.7766
cc-c3-sh    62.5      114.02              SOURCE3            1
cc-c3-ss    63.4      111.16         CORR_SOURCE5           65    0.8483
c -c3-cx    65.6      111.16               5/2017           39    1.9942
cd-c3-cd    66.2      112.39         CORR_SOURCE5           14    0.8688
cd-c3-f     88.5      111.31         CORR_SOURCE5          105    0.4710
cd-c3-h1    47.9      109.64      SOURCE3_SOURCE5         1145    0.8896
cd-c3-hc    47.7      110.49      SOURCE3_SOURCE5         6781    0.7714
cd-c3-n3    84.4      111.09         CORR_SOURCE5          192    1.4026
cd-c3-n     84.2      111.76         CORR_SOURCE5           51    1.5321
cd-c3-nd    86.2      107.04              SOURCE3            2
cd-c3-nh    83.9      112.34         CORR_SOURCE5           25    1.8212
cd-c3-oh    85.4      111.16         CORR_SOURCE5          187    1.3741
cd-c3-os    86.1      108.90         CORR_SOURCE5          213    1.1488
cd-c3-sh    62.5      114.02              SOURCE3            1
cd-c3-ss    63.4      111.16         CORR_SOURCE5           65    0.8483
ce-c3-ce    65.8      111.47      SOURCE4_SOURCE5           53    0.5207
ce-c3-cy    68.2      102.67               5/2017           14    0.3027
ce-c3-h1    47.5      109.54         CORR_SOURCE5          252    0.8257
ce-c3-hc    47.2      110.59      SOURCE3_SOURCE5         2438    0.7216
ce-c3-n3    83.7      111.76         CORR_SOURCE5           83    0.9878
ce-c3-n     84.3      110.22      SOURCE4_SOURCE5           16    1.1101
ce-c3-oh    85.0      111.19      SOURCE4_SOURCE5           74    1.5577
ce-c3-os    85.4      109.50      SOURCE4_SOURCE5           71    1.9041
ce-c3-ss    63.3      110.72      SOURCE4_SOURCE5           19    1.8179
c -c3-f     88.1      110.00      SOURCE4_SOURCE5          101    0.9951
cf-c3-cy    68.1      102.91               5/2017           58    0.2151
cf-c3-h1    47.5      109.54         CORR_SOURCE5          252    0.8257
cf-c3-hc    47.3      110.59      SOURCE3_SOURCE5         2411    0.7279
cf-c3-n3    83.7      111.76         CORR_SOURCE5           83    0.9878
c -c3-h1    47.5      108.22      SOURCE3_SOURCE5         3484    0.9857
c -c3-h2    47.2      109.69      SOURCE4_SOURCE5          100    1.0452
c -c3-hc    47.4      108.77      SOURCE3_SOURCE5        11750    0.9577
c -c3-hx    47.4      108.85      SOURCE4_SOURCE5          172    0.8753
cl-c3-cl    81.4      109.33      SOURCE2_SOURCE5          325    0.5772
cl-c3-f     94.1      109.11      SOURCE4_SOURCE5           57    0.3048
cl-c3-h1    48.9      106.78      SOURCE3_SOURCE5          860    0.4999
cl-c3-h2    48.8      106.99      SOURCE4_SOURCE5          147    0.6435
cl-c3-hc    48.7      107.65              SOURCE2            2    2.2500
cl-c3-os    91.0      110.86      SOURCE4_SOURCE5           26    1.1129
cl-c3-ss    71.1      112.53      SOURCE4_SOURCE5           39    1.6937
c -c3-n2    84.2      109.67      SOURCE4_SOURCE5          157    1.3668
c -c3-n3    83.7      111.14      SOURCE4_SOURCE5         1652    1.6694
c -c3-n4    82.6      110.73      SOURCE4_SOURCE5          103    1.8311
c -c3-n     84.5      109.06      SOURCE3_SOURCE5          905    1.7615
c -c3-na    83.6      111.50      SOURCE4_SOURCE5           87    1.4027
c -c3-nh    84.4      109.35      SOURCE4_SOURCE5          106    1.8043
c -c3-oh    85.6      108.79      SOURCE4_SOURCE5          824    1.3178
c -c3-os    85.3      109.21      SOURCE3_SOURCE5          429    1.7229
c -c3-p5    81.1      110.85      SOURCE4_SOURCE5           32    1.9944
c -c3-s6    64.1      110.67      SOURCE4_SOURCE5           14    2.0336
c -c3-sh    63.7      108.72      SOURCE4_SOURCE5           31    0.7714
c -c3-ss    63.8      108.84      SOURCE3_SOURCE5          149    1.5563
cx-c3-cx    64.8      113.94               5/2017           20    1.8637
cx-c3-h1    47.3      109.69               5/2017          436    0.9458
cx-c3-hc    47.2      110.17               5/2017         1010    0.9146
cx-c3-hx    46.7      112.70               5/2017           18    0.2742
cx-c3-n3    83.0      113.16               5/2017           64    1.4557
cx-c3-n4    86.4      101.42               5/2017           14    0.2262
cx-c3-n     83.3      112.36               5/2017           46    1.0272
cx-c3-oh    85.2      109.98               5/2017          120    1.6372
cx-c3-os    85.9      107.80               5/2017          100    1.5877
cy-c3-h1    47.2      108.54               5/2017          253    1.0959
cy-c3-hc    46.7      110.77               5/2017          523    0.9204
cy-c3-n3    82.3      113.90               5/2017           10    1.3405
cy-c3-oh    84.3      111.44               5/2017          209    0.6217
cy-c3-os    85.7      107.20               5/2017           11    1.1994
f -c3-f    121.6      107.36      SOURCE2_SOURCE5         1178    0.5429
f -c3-h1    66.9      107.90      SOURCE3_SOURCE5          181    0.5803
f -c3-h2    66.6      108.79      SOURCE3_SOURCE5           66    0.6474
f -c3-h3    66.2      110.08      SOURCE4_SOURCE5           45    0.6178
f -c3-hc    66.6      108.92              SOURCE2            5    3.0534
f -c3-n2   112.9      110.40              SOURCE2            3    2.6470
f -c3-os   114.4      110.58      SOURCE4_SOURCE5          114    1.2792
f -c3-p5   107.1      107.61      SOURCE4_SOURCE5           35    1.1282
f -c3-s6    83.9      109.68      SOURCE4_SOURCE5           57    0.4273
f -c3-ss    81.9      111.75      SOURCE4_SOURCE5           38    1.8571
h1-c3-h1    38.8      108.46      SOURCE3_SOURCE5        50971    0.8222
h1-c3-n1    62.8      107.99    HF/6-31G*_SOURCE5            7    0.3554
h1-c3-n2    61.1      109.81      SOURCE3_SOURCE5          957    1.0346
h1-c3-n3    61.2      109.88      SOURCE3_SOURCE5        20428    1.2681
h1-c3-n     61.5      108.88      SOURCE3_SOURCE5         6816    1.0842
h1-c3-na    61.5      108.78      SOURCE3_SOURCE5         2896    0.9339
h1-c3-nc    61.8      108.57              SOURCE3            6    0.0764
h1-c3-nd    61.8      108.57              SOURCE3            6
h1-c3-nh    61.2      109.79      SOURCE3_SOURCE5         6106    1.0471
h1-c3-no    60.0      105.47      SOURCE4_SOURCE5           73    0.6459
h1-c3-o     64.6      116.45      SOURCE3_SOURCE5           25    1.4798
h1-c3-oh    62.5      110.26      SOURCE3_SOURCE5         7971    1.1355
h1-c3-os    62.4      109.78      SOURCE3_SOURCE5        19982    1.1092
h1-c3-p5    54.6      108.27      SOURCE4_SOURCE5          222    1.1376
h1-c3-s4    42.9      107.92      SOURCE3_SOURCE5          496    0.6942
h1-c3-s     41.6      112.37      SOURCE3_SOURCE5           14    0.4580
h1-c3-s6    43.6      107.15      SOURCE3_SOURCE5         1022    0.8992
h1-c3-sh    42.4      108.42      SOURCE3_SOURCE5          259    1.4350
h1-c3-ss    42.5      108.76      SOURCE3_SOURCE5         3369    1.0506
h1-c3-sx    42.6      107.70      SOURCE3_SOURCE5          201    0.7977
h1-c3-sy    43.4      107.88      SOURCE3_SOURCE5          377    1.1089
h2-c3-h2    38.5      110.20      SOURCE3_SOURCE5          677    0.8586
h2-c3-i     39.1      104.99              SOURCE3            2
h2-c3-n2    61.0      110.20      SOURCE3_SOURCE5           69    0.8494
h2-c3-n3    61.3      109.35      SOURCE4_SOURCE5          660    0.9086
h2-c3-n     62.0      107.28      SOURCE4_SOURCE5          692    1.3634
h2-c3-na    62.0      107.31      SOURCE3_SOURCE5          428    0.9670
h2-c3-nc    61.6      109.47              SOURCE3           10    0.3133
h2-c3-nd    61.6      109.47              SOURCE3           10
h2-c3-nh    61.2      110.01      SOURCE4_SOURCE5          274    1.1061
h2-c3-no    59.2      108.27      SOURCE3_SOURCE5           13    0.4528
h2-c3-o     66.8      108.97              SOURCE3            4
h2-c3-oh    62.8      109.43      SOURCE3_SOURCE5          258    1.6998
h2-c3-os    62.4      109.58      SOURCE3_SOURCE5         2823    0.6377
h2-c3-s4    43.0      107.31      SOURCE3_SOURCE5           29    0.3344
h2-c3-s     42.7      106.75              SOURCE3            4
h2-c3-s6    43.7      106.51      SOURCE4_SOURCE5           67    1.0466
h2-c3-sh    42.5      107.87              SOURCE3            6    0.4376
h2-c3-ss    42.5      108.33      SOURCE3_SOURCE5          279    1.1804
h3-c3-n3    61.5      108.73      SOURCE4_SOURCE5           32    1.8953
h3-c3-nc    61.6      109.37              SOURCE3            1
h3-c3-nd    61.6      109.37              SOURCE3            1
h3-c3-nh    61.1      110.20      SOURCE4_SOURCE5           11    1.4222
h3-c3-os    61.9      111.51      SOURCE4_SOURCE5           44    1.4444
h3-c3-ss    42.4      109.09      SOURCE4_SOURCE5           19    0.8547
hc-c3-hc    39.0      107.58      SOURCE3_SOURCE5        92717    0.5328
hc-c3-i     39.1      104.99              SOURCE3            1
hc-c3-n2    61.2      109.50              SOURCE3            1
hc-c3-n3    61.2      109.80              SOURCE2            5    2.0070
hc-c3-n4    60.1      107.90              SOURCE3            1
hc-c3-n     61.4      109.50              SOURCE3            1
hc-c3-na    61.3      109.50              SOURCE3            1
hc-c3-nh    60.7      111.54              SOURCE3            1
hc-c3-no    59.5      107.20              SOURCE2            1
hc-c3-oh    62.8      109.50              SOURCE3            1
hc-c3-os    62.7      108.70              SOURCE2           13    2.3739
hc-c3-p2    53.6      110.18              SOURCE3           25    0.4057
hc-c3-p3    53.6      109.89      SOURCE3_SOURCE5          528    0.6740
hc-c3-p4    54.3      109.45      SOURCE3_SOURCE5          128    0.4042
hc-c3-p5    54.6      108.43      SOURCE3_SOURCE5          513    1.0539
hc-c3-px    54.6      109.70      SOURCE3_SOURCE5          103    0.3664
hc-c3-py    54.4      109.18      SOURCE3_SOURCE5           74    0.4506
hc-c3-s4    42.9      107.50              SOURCE2            1
hc-c3-s6    43.4      108.20              SOURCE3            1
hc-c3-sh    42.5      107.87              SOURCE2            3    2.0981
hc-c3-ss    42.5      108.76              SOURCE2            3    1.6891
hx-c3-hx    38.8      109.75      SOURCE3_SOURCE5         5075    0.8234
hx-c3-n4    60.1      108.01      SOURCE3_SOURCE5         6129    1.3658
i -c3-i     66.2      113.12              SOURCE3            1
n1-c3-n1   112.5      105.07            HF/6-31G*            1
n2-c3-n2   107.6      109.68      SOURCE3_SOURCE5            6    0.6095
n2-c3-nh   106.9      111.27      SOURCE4_SOURCE5           19    0.9194
n2-c3-oh   108.1      111.89      SOURCE4_SOURCE5           31    0.2948
n2-c3-os   108.2      111.04      SOURCE4_SOURCE5           16    1.7109
n3-c3-n3   106.9      111.23      SOURCE4_SOURCE5          123    1.3731
n3-c3-nc   106.3      113.29              SOURCE3            1
n3-c3-nd   106.3      113.29              SOURCE3            1
n3-c3-nh   107.3      110.61      SOURCE4_SOURCE5           58    1.2027
n3-c3-oh   108.7      110.70      SOURCE4_SOURCE5           52    0.9667
n3-c3-os   109.5      108.51      SOURCE4_SOURCE5           53    1.7879
n3-c3-p5   103.2      109.41      SOURCE4_SOURCE5           26    1.5078
n3-c3-ss    81.2      107.38      SOURCE4_SOURCE5           50    1.6843
n4-c3-n4   102.7      113.32              SOURCE3            1
na-c3-na   106.0      113.49              SOURCE3            1
na-c3-os   109.3      109.03      SOURCE4_SOURCE5          495    0.5894
nc-c3-nc   107.9      110.61              SOURCE3            1
nc-c3-nh   106.7      112.43              SOURCE3            1
nc-c3-os   106.5      115.41              SOURCE3            3    1.0288
nd-c3-nd   107.9      110.61              SOURCE3            1
nd-c3-nh   106.7      112.43              SOURCE3            1
nd-c3-os   106.5      115.41              SOURCE3            3
nh-c3-nh   109.7      105.87              SOURCE3            1
nh-c3-oh   108.0      112.27      SOURCE4_SOURCE5           43    0.9258
nh-c3-os   109.2      109.13      SOURCE4_SOURCE5           47    1.3529
nh-c3-p5   101.8      112.50              SOURCE4            5    1.7371
nh-c3-ss    80.6      109.01      SOURCE4_SOURCE5           19    2.2237
n -c3-n2   107.0      111.31      SOURCE4_SOURCE5           12    1.5991
n -c3-n3   107.1      111.11      SOURCE4_SOURCE5           37    1.6907
n -c3-n    106.5      112.65      SOURCE3_SOURCE5           30    2.1166
n -c3-nh   108.3      108.66      SOURCE4_SOURCE5           26    1.9779
n -c3-oh   107.9      112.56      SOURCE4_SOURCE5           75    1.1310
no-c3-no   105.1      105.18      SOURCE4_SOURCE5           23    1.9192
n -c3-os   109.3      109.13      SOURCE4_SOURCE5          432    0.8256
n -c3-p5   102.7      110.52      SOURCE4_SOURCE5           12    1.2739
oh-c3-oh   110.7      109.90      SOURCE4_SOURCE5           20    1.5118
oh-c3-os   110.7      109.38      SOURCE4_SOURCE5          280    1.2270
oh-c3-p5   104.2      108.68      SOURCE4_SOURCE5           77    1.3087
oh-c3-sh    78.6      115.46              SOURCE3            1
o -c3-o    113.5      122.30              SOURCE3            1
os-c3-os   110.9      108.29      SOURCE3_SOURCE5          723    1.0283
os-c3-p5   104.4      107.99      SOURCE4_SOURCE5           63    2.0205
os-c3-ss    81.1      108.59      SOURCE4_SOURCE5           54    1.6231
p2-c3-p2   104.0      110.48              SOURCE3            1
p3-c3-p3   104.0      110.16              SOURCE3            1
p5-c3-p5   105.0      110.13              SOURCE4           33    2.4116
p5-c3-ss    81.4      111.48      SOURCE4_SOURCE5           12    1.9291
s4-c3-s4    63.5      112.29              SOURCE3            2    1.2724
s4-c3-s6    63.5      113.52              SOURCE3            1
s6-c3-s6    64.6      111.22      SOURCE3_SOURCE5            6    1.7567
sh-c3-sh    61.9      116.26              SOURCE3            1
sh-c3-ss    63.5      110.73              SOURCE3            1
s -c3-s     60.1      123.35              SOURCE3            1
ss-c3-ss    63.4      111.44      SOURCE4_SOURCE5           66    1.6272
br-ca-br    67.7      117.60              SOURCE3            1
br-ca-ca    64.2      119.30      SOURCE3_SOURCE5          640    0.4898
c1-ca-c1    66.8      120.00              SOURCE3            1
c1-ca-ca    67.7      120.00              SOURCE3            1
c2-ca-c2    69.5      120.00              SOURCE3            1
c2-ca-ca    68.9      120.60              SOURCE3            1
c3-ca-c2    66.1      120.00              SOURCE3            1
c3-ca-c3    64.3      116.80              SOURCE3            1
c3-ca-ca    65.6      120.77      SOURCE3_SOURCE5        23865    1.2220
c3-ca-cp    65.5      120.63                 CORR          120
c3-ca-cq    65.5      120.63                 CORR          120
c3-ca-na    83.2      118.72      SOURCE4_SOURCE5          145    1.1124
c3-ca-nb    84.9      116.68      SOURCE4_SOURCE5         1062    0.9093
ca-ca-ca    68.8      120.02      SOURCE3_SOURCE5       108055    0.7701
ca-ca-cc    67.1      120.79      SOURCE3_SOURCE5         2048    2.0941
ca-ca-cd    67.1      120.79      SOURCE3_SOURCE5         2048    2.0941
ca-ca-ce    66.6      120.82      SOURCE3_SOURCE5         3962    1.5682
ca-ca-cf    66.6      120.82      SOURCE3_SOURCE5         3948    1.5732
ca-ca-cg    67.8      120.27      SOURCE3_SOURCE5          453    0.4194
ca-ca-ch    67.8      120.27      SOURCE3_SOURCE5          447    0.4218
ca-ca-cl    72.1      119.39      SOURCE4_SOURCE5         6669    0.5363
ca-ca-cp    68.4      120.69         CORR_SOURCE5         1915    0.8596
ca-ca-cq    68.4      120.69         CORR_SOURCE5         1915    0.8596
ca-ca-cx    66.0      120.95               5/2017          173    2.6958
ca-ca-cy    65.6      120.64               5/2017           46    3.4235
ca-ca-f     89.3      118.96      SOURCE4_SOURCE5         2636    0.3804
ca-ca-h4    48.6      120.34      SOURCE3_SOURCE5         2590    0.5568
ca-ca-ha    48.7      119.88      SOURCE3_SOURCE5       126779    0.4424
ca-ca-i     61.1      119.11      SOURCE3_SOURCE5          123    0.9416
ca-ca-n1    88.1      119.78    HF/6-31G*_SOURCE5           14    0.4655
ca-ca-n2    89.1      119.57              SOURCE3            1
ca-ca-n4    83.7      119.31      SOURCE3_SOURCE5           63    1.4960
ca-ca-n     85.6      120.19      SOURCE3_SOURCE5         3041    2.2480
ca-ca-na    87.2      118.34              SOURCE3           54    3.6168
ca-ca-nb    86.8      122.94      SOURCE3_SOURCE5         5507    1.1495
ca-ca-nc    87.6      119.72              SOURCE3           22    3.3994
ca-ca-nd    87.6      119.72              SOURCE3           22    3.3994
ca-ca-ne    85.6      120.61      SOURCE3_SOURCE5          349    2.0914
ca-ca-nf    85.6      120.61      SOURCE3_SOURCE5          349    2.0914
ca-ca-nh    86.2      120.95      SOURCE3_SOURCE5         4970    1.2168
ca-ca-no    84.2      119.01      SOURCE3_SOURCE5          854    0.7071
ca-ca-o     89.5      123.26      SOURCE4_SOURCE5           35    1.2620
ca-ca-oh    87.2      119.90      SOURCE3_SOURCE5         6384    1.7827
ca-ca-os    87.3      119.20              SOURCE3           52    0.5240
ca-ca-p2    81.3      114.36              SOURCE3            1
ca-ca-p3    79.9      120.01      SOURCE3_SOURCE5           24    1.1566
ca-ca-p4    80.5      120.30              SOURCE3            1
ca-ca-p5    80.9      120.24      SOURCE4_SOURCE5           15    0.0746
ca-ca-pe    79.6      120.45              SOURCE3           20    0.2719
ca-ca-pf    79.6      120.45              SOURCE3           20    0.2719
ca-ca-px    79.8      120.53              SOURCE3           10    0.4509
ca-ca-py    80.2      120.25      SOURCE3_SOURCE5           75    1.5353
ca-ca-s4    63.6      119.15              SOURCE3            1
ca-ca-s6    63.8      120.43      SOURCE4_SOURCE5           89    1.1843
ca-ca-s     64.1      122.55              SOURCE3            4
ca-ca-sh    63.1      121.78      SOURCE4_SOURCE5           54    1.3490
ca-ca-ss    63.5      120.06      SOURCE3_SOURCE5         1341    2.1632
ca-ca-sx    62.5      119.28      SOURCE3_SOURCE5          140    1.1919
ca-ca-sy    63.4      119.42      SOURCE3_SOURCE5         1489    0.7572
c -ca-c3    64.5      118.06              SOURCE3            1
c -ca-c     64.5      120.00              SOURCE3            1
c -ca-ca    66.4      120.33      SOURCE3_SOURCE5         8320    1.9221
cc-ca-cp    66.0      124.30      SOURCE4_SOURCE5           20    0.6423
cc-ca-nb    86.7      117.75         CORR_SOURCE5           42    1.7067
cd-ca-nb    86.7      117.75         CORR_SOURCE5           42    1.7067
ce-ca-na    84.1      119.92      SOURCE4_SOURCE5           38    0.5659
ce-ca-nb    86.0      117.56         CORR_SOURCE5           91    0.8492
cf-ca-nb    86.0      117.56         CORR_SOURCE5           91    0.8492
cg-ca-cp    67.3      121.53      SOURCE4_SOURCE5           24    0.1831
c -ca-ha    46.9      115.90              SOURCE3            1
cl-ca-cl    80.5      118.72              SOURCE3            1
cl-ca-cp    71.7      120.39      SOURCE4_SOURCE5           52    0.5449
cl-ca-nb    92.3      116.18      SOURCE4_SOURCE5          152    0.5909
c -ca-nb    85.4      117.78      SOURCE4_SOURCE5          262    1.1507
c -ca-nc    80.8      130.80              SOURCE3            1
c -ca-nd    80.8      130.80              SOURCE3            1
cp-ca-f     88.8      119.42      SOURCE4_SOURCE5           46    0.2425
cp-ca-h4    48.4      120.09      SOURCE4_SOURCE5           62    0.4243
cp-ca-ha    48.5      119.86         CORR_SOURCE5         1240    0.5472
cp-ca-na    90.7      108.79      SOURCE4_SOURCE5          514    0.5055
cp-ca-nb    86.4      123.58      SOURCE4_SOURCE5          129    0.8391
cp-ca-nh    85.7      121.56      SOURCE4_SOURCE5           30    0.5872
cp-ca-oh    86.6      120.85      SOURCE4_SOURCE5           41    1.3658
cp-ca-ss    66.0      111.17      SOURCE4_SOURCE5           24    1.8180
cp-ca-sy    65.6      111.18                 CORR            4
cq-ca-ha    48.5      119.86         CORR_SOURCE5         1240    0.5472
cq-ca-sy    65.6      111.18                 CORR            4
f -ca-f    116.3      117.50              SOURCE3            1
f -ca-nb   116.4      114.67      SOURCE4_SOURCE5           42    0.4295
h4-ca-n     61.4      116.02              SOURCE3            1
h4-ca-na    62.4      116.32      SOURCE3_SOURCE5          394    0.4031
h4-ca-nb    64.1      116.03      SOURCE3_SOURCE5         2217    0.2861
h4-ca-nc    63.0      118.36              SOURCE3            1
h4-ca-nd    63.0      118.36              SOURCE3            1
h4-ca-os    64.3      111.15              SOURCE3            1
h4-ca-ss    42.5      116.19              SOURCE3            1
h5-ca-nb    64.1      115.82      SOURCE3_SOURCE5          618    0.3893
h5-ca-nc    62.0      122.11              SOURCE3            1
h5-ca-nd    62.0      122.11              SOURCE3            1
ha-ca-n2    65.4      116.00              SOURCE2            1
ha-ca-p2    51.3      122.56              SOURCE3            1
i -ca-i     67.0      119.28              SOURCE3            1
n1-ca-n1   114.4      117.03            HF/6-31G*            1
n2-ca-n2   115.7      120.00              SOURCE3            1
n2-ca-na   112.2      119.60              SOURCE3            1
n4-ca-n4   103.0      116.82              SOURCE3            1
na-ca-na   115.1      107.62      SOURCE4_SOURCE5           11    0.8382
na-ca-nb   107.6      127.09      SOURCE4_SOURCE5          708    1.9791
na-ca-nh   109.5      118.66      SOURCE4_SOURCE5           73    0.9977
nb-ca-nb   109.4      127.26      SOURCE4_SOURCE5         1586    1.1854
nb-ca-nc   109.2      126.50         CORR_SOURCE5           33    1.0453
nb-ca-nd   109.2      126.50         CORR_SOURCE5           33    1.0453
nb-ca-nh   112.1      116.94      SOURCE4_SOURCE5         2042    0.7868
nb-ca-oh   112.7      117.68      SOURCE4_SOURCE5          182    0.7979
nb-ca-os   111.5      119.72      SOURCE4_SOURCE5          194    0.7211
nb-ca-sh    81.0      117.61      SOURCE4_SOURCE5           35    1.3741
nb-ca-ss    80.6      118.80      SOURCE4_SOURCE5          111    1.8247
nc-ca-nc   107.7      128.74              SOURCE3            1
nc-ca-nh   110.7      118.86              SOURCE3            1
nd-ca-nd   107.7      128.74              SOURCE3            1
nd-ca-nh   110.7      118.86              SOURCE3            1
nh-ca-nh   108.4      120.98              SOURCE3            1
n -ca-nc   107.3      123.86              SOURCE3            1
n -ca-nd   107.3      123.86              SOURCE3            1
n -ca-nh   109.5      116.16              SOURCE3            1
no-ca-no   103.9      117.14              SOURCE3            1
oh-ca-oh   110.6      120.00              SOURCE3            1
o -ca-o    118.7      126.82              SOURCE3            1
os-ca-os   113.1      113.73              SOURCE3            1
p2-ca-p2   100.1      121.20              SOURCE3            1
p3-ca-p3   100.8      121.46              SOURCE3            1
p5-ca-p5   103.1      120.00              SOURCE3            1
s4-ca-s4    66.9      105.81              SOURCE3            1
s6-ca-s6    67.7      105.81              SOURCE3            1
sh-ca-sh    63.1      120.24              SOURCE3            1
s -ca-s     63.3      125.14              SOURCE3            1
ss-ca-ss    64.4      115.15              SOURCE3            1
br-c -br    67.7      113.10              SOURCE3            1
br-c -c3    64.6      110.74              SOURCE3            1
br-c -o     78.5      121.46              SOURCE3            5    1.6264
c1-c -c1    67.2      115.32              SOURCE3            1
c1-c -o     87.6      122.34              SOURCE3            1
c2-c -c2    69.3      116.78              SOURCE3            1
c2-c -ha    49.2      115.95              SOURCE3            1
c2-c -o     91.2      119.12              SOURCE3            2
c2-c -s     66.8      119.16              SOURCE3            2
c3-c -c3    64.0      116.50      SOURCE3_SOURCE5          720    1.3034
c3-c -ca    64.2      118.40      SOURCE4_SOURCE5          749    1.4991
c3-c -cc    65.0      117.29         CORR_SOURCE5          118    1.7737
c3-c -cd    65.0      117.29         CORR_SOURCE5          118    1.7737
c3-c -ce    64.9      116.44         CORR_SOURCE5          543    1.3559
c3-c -cf    64.9      116.44         CORR_SOURCE5          543    1.3559
c3-c -cg    66.0      115.00              SOURCE2            1
c3-c -ch    66.0      115.00              SOURCE2            1
c3-c -cl    71.2      111.99              SOURCE3            2    0.0125
c3-c -f     88.4      110.70              SOURCE2            1
c3-c -h4    46.1      114.64      SOURCE4_SOURCE5          193    0.4989
c3-c -ha    46.0      115.22              SOURCE3           15    0.3181
c3-c -i     60.4      112.94              SOURCE3            1
c3-c -n2    83.5      114.53              SOURCE3            1
c3-c -n4    81.1      112.26              SOURCE3            2
c3-c -n     84.3      115.18      SOURCE3_SOURCE5         2997    1.3885
c3-c -ne    84.9      112.61         CORR_SOURCE5           19    2.4426
c3-c -nf    84.9      112.61         CORR_SOURCE5           19    2.4426
c3-c -o     84.6      123.20      SOURCE3_SOURCE5        10083    1.8011
c3-c -oh    85.8      112.73      SOURCE3_SOURCE5         1989    1.3796
c3-c -os    86.4      110.72      SOURCE3_SOURCE5         1786    0.9391
c3-c -p3    77.8      116.42              SOURCE3            3    0.1291
c3-c -p5    77.0      118.90              SOURCE3            1
c3-c -pe    77.4      114.85              SOURCE3            1
c3-c -pf    77.4      114.85              SOURCE3            1
c3-c -px    77.4      115.60              SOURCE3            1
c3-c -py    77.7      118.16              SOURCE3            3    1.0735
c3-c -s4    61.4      114.79              SOURCE3            1
c3-c -s6    61.4      114.72              SOURCE3            1
c3-c -s     63.9      123.15      SOURCE3_SOURCE5           66    1.3121
c3-c -sh    63.8      112.65      SOURCE3_SOURCE5            9    1.5127
c3-c -ss    63.4      113.51      SOURCE3_SOURCE5           65    0.9334
c3-c -sx    61.2      113.97              SOURCE3            3    0.0610
c3-c -sy    61.6      114.28              SOURCE3            3    0.7341
ca-c -ca    65.0      118.11      SOURCE4_SOURCE5          506    1.8633
ca-c -cc    66.1      116.00         CORR_SOURCE5          670    1.7109
ca-c -cd    66.1      116.00         CORR_SOURCE5          670    1.7109
ca-c -ce    65.0      119.02         CORR_SOURCE5           83    1.3943
ca-c -cf    65.0      119.02         CORR_SOURCE5           83    1.3943
ca-c -h4    46.9      115.14      SOURCE4_SOURCE5          122    0.7683
ca-c -ha    47.2      114.12              SOURCE3            1
ca-c -n     85.4      115.25      SOURCE4_SOURCE5         1494    1.4889
ca-c -ne    85.3      114.71      SOURCE4_SOURCE5           14    0.5855
ca-c -o     86.2      122.60      SOURCE3_SOURCE5         3960    1.5802
ca-c -oh    86.7      113.45      SOURCE4_SOURCE5          656    0.8414
ca-c -os    87.0      112.44      SOURCE3_SOURCE5          493    0.8365
ca-c -s     64.6      122.68      SOURCE4_SOURCE5           32    1.3788
ca-c -sh    62.5      118.63              SOURCE3            1
ca-c -ss    63.4      115.05      SOURCE4_SOURCE5           37    1.0695
br-cc-c     65.2      116.28      SOURCE4_SOURCE5           32    1.1116
br-cc-cc    63.4      124.05      SOURCE4_SOURCE5           31    1.9388
br-cc-cd    63.7      124.23      SOURCE4_SOURCE5          116    2.3356
br-cc-na    80.6      121.58      SOURCE4_SOURCE5           19    0.8500
c2-cc-c3    65.3      126.11              SOURCE3            2
c2-cc-ca    67.0      124.42         CORR_SOURCE5           25    1.8245
c2-cc-cc    68.3      122.19         CORR_SOURCE5           46    2.3853
c2-cc-cd    71.3      117.02              SOURCE3            2    0.0703
c2-cc-ha    49.2      122.72              SOURCE3            2    0.0092
c2-cc-n     86.2      124.91      SOURCE3_SOURCE5            5    1.6803
c2-cc-os    88.0      121.42         CORR_SOURCE5           24    0.9570
c -c -c3    63.6      116.17      SOURCE3_SOURCE5           58    1.1332
c3-cc-ca    63.3      126.52         CORR_SOURCE5          370    1.8946
c3-cc-cc    66.7      115.97              SOURCE3            4    3.0507
c3-cc-cd    66.8      119.45              SOURCE3           35    8.2040
c3-cc-cf    67.4      117.84                 CORR            2
c3-cc-ha    45.5      121.52              SOURCE3           32    3.2091
c3-cc-n2    83.3      125.69         CORR_SOURCE5           12    1.9935
c3-cc-n     83.6      119.19         CORR_SOURCE5          107    2.1078
c3-cc-na    82.4      122.73         CORR_SOURCE5          961    1.6482
c3-cc-nc    83.2      120.95         CORR_SOURCE5          456    0.8756
c3-cc-nd    83.9      122.41         CORR_SOURCE5          653    1.6992
c3-cc-os    84.9      116.80         CORR_SOURCE5          306    0.8990
c3-cc-ss    62.7      121.53         CORR_SOURCE5          270    1.0948
c -c -c     64.4      111.68              SOURCE3            2    6.1226
c -c -ca    63.6      118.60      SOURCE4_SOURCE5           90    1.0263
ca-cc-cc    69.3      111.04              SOURCE3            9    7.9455
ca-cc-cd    69.8      113.51              SOURCE3           26    7.4229
ca-cc-ce    64.3      127.01      SOURCE4_SOURCE5           38    1.6763
ca-cc-h4    45.4      129.25      SOURCE3_SOURCE5           54    1.5632
ca-cc-ha    46.3      124.04              SOURCE3           34    3.6691
ca-cc-n     85.6      117.67                 CORR           18
ca-cc-nc    84.9      120.59         CORR_SOURCE5          224    1.0853
ca-cc-nd    85.3      123.24         CORR_SOURCE5          246    2.3557
ca-cc-nh    84.3      122.13      SOURCE4_SOURCE5           20    1.7636
ca-cc-oh    86.6      117.55         CORR_SOURCE5           35    1.9318
ca-cc-os    87.2      114.75         CORR_SOURCE5          247    2.0579
ca-cc-ss    63.4      120.80         CORR_SOURCE5           80    2.1212
c -cc-c2    67.5      121.17         CORR_SOURCE5           28    1.6484
c -cc-c3    65.4      117.76         CORR_SOURCE5          566    1.9588
c -cc-c     65.2      121.07         CORR_SOURCE5          128    0.8902
c -c -cc    66.0      111.67              SOURCE3            4    5.5146
c -cc-ca    65.0      122.95              SOURCE3            1
c -cc-cc    65.7      122.69              SOURCE3            2
cc-c -cc    66.7      115.84         CORR_SOURCE5          115    1.4659
cc-cc-cc    70.1      110.70              SOURCE3           54    3.4091
cc-cc-cd    70.3      114.19              SOURCE3          517    6.5960
cc-cc-ce    64.9      127.06         CORR_SOURCE5           61    2.3233
cc-cc-cf    68.0      122.72         CORR_SOURCE5           66    1.9701
cc-cc-cg    65.8      125.91         CORR_SOURCE5           41    1.1646
c -cc-cd    67.2      121.35         CORR_SOURCE5         3554    2.2084
cc-c -cd    67.6      112.79              SOURCE3            1
c -cc-ce    65.4      121.57         CORR_SOURCE5           29    1.1305
cc-c -ce    66.4      115.57      SOURCE4_SOURCE5           14    1.2088
cc-cc-f     88.4      119.19      SOURCE4_SOURCE5           26    0.8983
c -cc-cg    67.0      117.88      SOURCE4_SOURCE5           26    0.6759
cc-cc-h4    46.3      127.96      SOURCE3_SOURCE5          391    2.1732
cc-cc-ha    47.6      121.07         CORR_SOURCE5         2414    2.2010
c -cc-cl    72.6      116.38         CORR_SOURCE5           50    1.2099
cc-cc-n2    87.4      122.21         CORR_SOURCE5           37    1.6493
cc-cc-n     85.8      119.89              SOURCE3           36    0.2095
cc-cc-na    86.5      117.77      SOURCE3_SOURCE5          865    1.5665
cc-cc-nc    85.3      121.98         CORR_SOURCE5          141    1.9633
cc-cc-nd    90.3      112.56              SOURCE3          141    4.2871
cc-cc-nh    86.0      119.72         CORR_SOURCE5          348    1.7785
cc-cc-oh    86.2      121.27         CORR_SOURCE5           11    2.2744
cc-cc-os    87.2      117.34         CORR_SOURCE5          217    1.9304
cc-cc-pd    84.5      115.36              SOURCE3           84
cc-cc-ss    63.9      120.21         CORR_SOURCE5           52    2.1160
cc-cc-sy    61.1      128.25      SOURCE4_SOURCE5           20    0.9014
c -c -cd    66.0      111.67              SOURCE3            4    5.5146
cd-cc-cd    70.0      120.08         CORR_SOURCE5          119    1.6139
cd-cc-ce    65.8      128.05         CORR_SOURCE5          350    2.4628
cd-cc-cl    71.7      123.41         CORR_SOURCE5          115    2.1217
cd-cc-f     89.6      121.19      SOURCE4_SOURCE5           82    0.7206
cd-cc-h4    47.8      128.48      SOURCE3_SOURCE5         3291    2.3189
cd-cc-ha    49.0      121.76      SOURCE3_SOURCE5         4433    1.8701
cd-cc-n     87.0      121.33      SOURCE3_SOURCE5          821    1.9126
cd-cc-na    92.7      106.99      SOURCE3_SOURCE5         3003    2.3845
cd-cc-nc    91.1      111.65         CORR_SOURCE5         1656    1.8430
cd-cc-nh    86.3      123.84         CORR_SOURCE5          152    2.2360
cd-cc-no    82.9      128.69      SOURCE4_SOURCE5          314    1.4409
cd-cc-oh    87.2      123.78         CORR_SOURCE5          251    1.1988
cd-cc-os    88.0      120.30              SOURCE3           64    5.4354
cd-cc-ss    66.9      111.55         CORR_SOURCE5         1048    1.8648
cd-cc-sy    62.5      124.55         CORR_SOURCE5           56    1.7107
ce-cc-na    83.4      124.35         CORR_SOURCE5           87    1.3591
ce-cc-nc    84.8      121.10         CORR_SOURCE5           43    1.2959
ce-cc-nd    85.9      121.70         CORR_SOURCE5           58    1.4179
ce-cc-os    85.8      118.76         CORR_SOURCE5           92    1.3159
ce-cc-ss    63.2      121.58         CORR_SOURCE5           54    1.3126
c -cc-f     87.8      116.98      SOURCE4_SOURCE5           49    0.4690
cg-cc-na    84.9      122.61      SOURCE4_SOURCE5           12    0.9695
cg-cc-ss    63.8      120.73      SOURCE4_SOURCE5           27    0.9221
cc-c -h4    47.6      114.83      SOURCE4_SOURCE5           25    0.5124
c -cc-ha    47.4      116.64      SOURCE3_SOURCE5          896    1.3075
cl-cc-na    90.5      121.12      SOURCE4_SOURCE5           37    0.7206
cl-cc-nd    91.0      122.07         CORR_SOURCE5           19    1.6973
cl-cc-ss    71.9      119.85      SOURCE4_SOURCE5           27    0.9529
c -cc-n2    85.2      123.93         CORR_SOURCE5            6    0.0993
c -cc-n     85.7      116.37         CORR_SOURCE5           41    2.4875
cc-c -n     87.1      112.70      SOURCE3_SOURCE5         1124    1.8431
c -cc-nc    83.5      123.32         CORR_SOURCE5           27    2.2025
cc-c -nd    85.6      116.24         CORR_SOURCE5           38    1.0053
c -cc-nd    85.3      121.88         CORR_SOURCE5           54    2.0672
c -cc-ne    84.5      119.88              SOURCE4            6    0.3139
cc-c -o     86.7      123.93      SOURCE3_SOURCE5         3463    2.3073
c -cc-oh    87.6      113.66         CORR_SOURCE5          190    1.6462
cc-c -oh    87.8      112.84         CORR_SOURCE5          184    0.7264
c -cc-os    85.1      119.26         CORR_SOURCE5          104    2.4145
cc-c -os    87.1      114.20      SOURCE3_SOURCE5          427    2.2749
cc-c -s     64.0      126.28      SOURCE4_SOURCE5           69    1.9867
cc-c -ss    64.4      112.40      SOURCE4_SOURCE5           42    0.9902
cx-cc-nd    83.2      127.88               5/2017           15    1.5594
cx-cc-os    85.5      118.06               5/2017           13    0.0898
cd-c -cd    66.7      115.84         CORR_SOURCE5          115    1.4659
cd-c -cx    65.4      117.42               5/2017           24    0.1441
cd-c -n     87.1      112.70      SOURCE3_SOURCE5         1124    1.8431
cd-c -nc    85.6      116.24         CORR_SOURCE5           38    1.0053
cd-c -nd    86.5      113.75      SOURCE4_SOURCE5           28    0.0860
cd-c -o     86.7      123.93      SOURCE3_SOURCE5         3463    2.3073
cd-c -oh    87.8      112.84         CORR_SOURCE5          184    0.7264
cd-c -os    87.1      114.20      SOURCE3_SOURCE5          427    2.2749
ce-c -ce    66.0      115.82         CORR_SOURCE5          103    0.7143
ce-c -cf    65.9      116.37      SOURCE4_SOURCE5           31    1.3157
ce-c -cx    65.8      114.98               5/2017           36    3.8282
ce-c -h4    47.2      114.89      SOURCE4_SOURCE5          113    0.4718
ce-c -ha    47.2      115.22              SOURCE3            7    2.4188
ce-c -n     85.7      115.22         CORR_SOURCE5           38    1.1173
ce-c -o     86.3      123.20      SOURCE3_SOURCE5         2306    2.0617
ce-c -oh    87.0      113.62         CORR_SOURCE5          273    1.4501
ce-c -os    87.8      110.93         CORR_SOURCE5          445    1.6899
ce-c -s     64.7      122.63      SOURCE3_SOURCE5           11    1.3034
ce-c -ss    64.8      110.49      SOURCE4_SOURCE5           13    0.5852
cf-c -cf    66.0      115.82         CORR_SOURCE5          103    0.7143
cf-c -ha    47.2      115.22              SOURCE3            7
cf-c -n     85.7      115.22         CORR_SOURCE5           38    1.1173
cf-c -o     86.3      123.20      SOURCE3_SOURCE5         2306    2.0617
cf-c -oh    87.0      113.62         CORR_SOURCE5          273    1.4501
cf-c -os    87.8      110.93         CORR_SOURCE5          445    1.6899
cf-c -s     64.7      122.63      SOURCE3_SOURCE5           11    1.3034
cg-c -cg    67.6      115.38              SOURCE3            1
cg-c -ha    48.3      113.90              SOURCE2            1
cg-c -o     88.2      121.78      SOURCE3_SOURCE5           13    0.8393
c -c -h4    45.2      115.80      SOURCE4_SOURCE5           17    0.7492
h4-cc-n     62.7      115.69      SOURCE3_SOURCE5          425    0.9142
h4-cc-na    61.5      120.53      SOURCE3_SOURCE5         1801    1.3882
h4-cc-nc    61.7      121.14      SOURCE3_SOURCE5          574    0.5658
h4-cc-nd    64.3      118.47      SOURCE3_SOURCE5          435    1.3360
h4-cc-os    63.6      114.90      SOURCE3_SOURCE5          456    0.8638
h4-cc-ss    42.5      119.97      SOURCE3_SOURCE5          496    0.7119
h5-cc-n     62.7      115.70         CORR_SOURCE5           41    0.7665
h5-cc-na    61.2      121.55      SOURCE3_SOURCE5         1138    0.7136
h5-cc-nc    61.3      122.92      SOURCE3_SOURCE5          136    0.3532
h5-cc-nd    62.5      125.52      SOURCE3_SOURCE5         1309    0.7276
h5-cc-os    63.1      116.83      SOURCE3_SOURCE5           42    1.3051
h5-cc-ss    42.3      121.02      SOURCE3_SOURCE5           46    0.6462
c -c -ha    45.4      115.43              SOURCE2            3    0.6549
ha-cc-na    61.2      121.50              SOURCE2            1
ha-cc-nc    62.9      116.54              SOURCE3            5    1.4482
ha-cc-nd    64.2      118.88              SOURCE3           20    2.8923
ha-cc-os    64.8      110.86              SOURCE3            7    1.3846
ha-cc-pd    54.9      121.76              SOURCE3           84
ha-cc-ss    42.2      121.64              SOURCE2            5    1.3276
ch-c -ch    67.6      115.38              SOURCE3            1
ch-c -ha    48.3      113.90              SOURCE2            1
ch-c -o     88.2      121.78      SOURCE3_SOURCE5           13    0.8393
cl-c -cl    80.7      111.30              SOURCE2            1
cl-c -f     93.2      112.00              SOURCE2            1
cl-c -ha    48.2      109.90              SOURCE2            1
cl-c -o     89.0      120.69      SOURCE3_SOURCE5           14    1.1076
cl-c -s     69.9      127.60              SOURCE2            1
c -c -n     84.3      112.74      SOURCE4_SOURCE5          157    2.1770
na-cc-nc   108.8      121.95         CORR_SOURCE5          321    1.6221
na-cc-nd   115.5      112.22      SOURCE3_SOURCE5         2726    1.5103
na-cc-no   105.3      124.59      SOURCE4_SOURCE5          162    0.8093
na-cc-oh   111.7      117.48      SOURCE4_SOURCE5           39    0.9806
na-cc-sx    79.7      117.02      SOURCE4_SOURCE5           32    0.3937
na-cc-sy    79.5      120.46      SOURCE4_SOURCE5           15    1.7292
nc-cc-nd   114.2      115.83         CORR_SOURCE5          309    1.2424
nc-cc-nh   111.3      117.23         CORR_SOURCE5           51    1.7463
nc-cc-no   106.9      121.73      SOURCE4_SOURCE5           17    0.8729
nc-cc-ss    79.9      122.64      SOURCE3_SOURCE5           10    1.3100
nd-cc-nd   110.8      128.07      SOURCE4_SOURCE5           17    0.2580
nd-cc-ne   107.8      129.01      SOURCE4_SOURCE5           20    1.2478
nd-cc-nh   111.7      120.65      SOURCE3_SOURCE5          554    1.6769
nd-cc-no   108.2      122.75      SOURCE4_SOURCE5           80    0.3006
nd-cc-oh   112.7      121.12         CORR_SOURCE5           31    1.3923
nd-cc-os   114.1      116.74         CORR_SOURCE5          156    2.0183
nd-cc-sh    79.2      124.97      SOURCE4_SOURCE5           18    0.8493
nd-cc-ss    83.3      114.51              SOURCE3            8    0.3449
nd-cc-sx    76.8      127.74      SOURCE4_SOURCE5           33    0.6804
nd-cc-sy    79.3      123.03      SOURCE4_SOURCE5           33    1.1587
ne-cc-ss    81.7      117.03      SOURCE4_SOURCE5           17    0.2106
nh-cc-nh   111.7      115.96              SOURCE3            1
nh-cc-os   111.8      116.68         CORR_SOURCE5           36    0.7439
nh-cc-ss    80.1      121.81         CORR_SOURCE5          128    1.0728
n -cc-n2   112.9      119.42      SOURCE4_SOURCE5           28    1.2985
n -cc-na   108.3      122.12         CORR_SOURCE5           15    1.1276
n -cc-nc   106.9      126.23         CORR_SOURCE5          118    0.4381
n -cc-nd   110.3      123.00         CORR_SOURCE5          354    1.4352
n -cc-nh   110.9      116.94         CORR_SOURCE5          126    0.5956
no-cc-os   109.1      117.55      SOURCE4_SOURCE5          144    0.2521
no-cc-ss    79.7      121.06      SOURCE4_SOURCE5           33    0.2051
n -cc-ss    79.7      122.88         CORR_SOURCE5           82    1.5666
c -c -o     84.3      120.85      SOURCE4_SOURCE5          712    2.3365
c -c -oh    85.2      112.07      SOURCE3_SOURCE5           45    0.4339
c -c -os    85.3      111.41      SOURCE4_SOURCE5           34    0.4577
os-cc-ss    81.1      119.28      SOURCE3_SOURCE5           10    1.6753
ss-cc-ss    63.6      121.37                 CORR           22
ss-cc-sy    63.0      121.70         CORR_SOURCE5           43    0.4842
cx-c -cx    65.7      113.92               5/2017            7    5.3745
cx-c -n     85.2      114.57               5/2017           35    1.0174
cx-c -o     85.6      122.72               5/2017          269    2.2381
cx-c -oh    86.6      112.58               5/2017           33    1.5746
cx-c -os    86.8      111.65               5/2017           39    1.4289
cy-c -cy    70.7       92.18               5/2017           10    0.6930
cy-c -n     83.4      114.77               5/2017            9    1.0901
cy-c -o     79.6      135.23               5/2017          412    1.4111
cy-c -oh    85.0      112.06               5/2017           12    0.6651
cy-c -os    85.2      111.21               5/2017            6    0.3594
c2-cd-c3    65.3      126.11              SOURCE3            2
c2-cd-ca    67.0      124.42         CORR_SOURCE5           25    1.8245
c2-cd-cc    71.3      117.02              SOURCE3            2
c2-cd-cd    68.3      122.19         CORR_SOURCE5           46    2.3853
c2-cd-ha    49.2      122.72              SOURCE3            2
c2-cd-n     86.2      124.91      SOURCE3_SOURCE5            5    1.6803
c2-cd-os    88.0      121.42         CORR_SOURCE5           24    0.9570
c3-cd-ca    63.3      126.52         CORR_SOURCE5          370    1.8946
c3-cd-cc    66.8      119.45              SOURCE3           35    8.2040
c3-cd-cd    66.7      115.97              SOURCE3            4    3.0507
c3-cd-ce    67.4      117.84                 CORR            2
c3-cd-ha    45.5      121.52              SOURCE3           32    3.2091
c3-cd-n2    83.3      125.69         CORR_SOURCE5           12    1.9935
c3-cd-n     83.6      119.19         CORR_SOURCE5          107    2.1078
c3-cd-na    82.4      122.73         CORR_SOURCE5          961    1.6482
c3-cd-nc    83.9      122.41         CORR_SOURCE5          653    1.6992
c3-cd-nd    83.2      120.95         CORR_SOURCE5          456    0.8756
c3-cd-os    84.9      116.80         CORR_SOURCE5          306    0.8990
c3-cd-ss    62.7      121.53         CORR_SOURCE5          270    1.0948
ca-cd-cc    69.8      113.51              SOURCE3           26    7.4229
ca-cd-cd    69.3      111.04              SOURCE3            9    7.9455
ca-cd-ce    66.7      124.90      SOURCE4_SOURCE5           41    1.7178
ca-cd-h4    45.4      129.25      SOURCE3_SOURCE5           54    1.5632
ca-cd-ha    46.3      124.04              SOURCE3           34    3.6691
ca-cd-n     85.6      117.67                 CORR           18
ca-cd-na    83.6      123.45              SOURCE4           39    1.9138
ca-cd-nc    85.3      123.24         CORR_SOURCE5          246    2.3557
ca-cd-nd    84.9      120.59         CORR_SOURCE5          224    1.0853
ca-cd-oh    86.6      117.55         CORR_SOURCE5           35    1.9318
ca-cd-os    87.2      114.75         CORR_SOURCE5          247    2.0579
ca-cd-ss    63.4      120.80         CORR_SOURCE5           80    2.1212
c -cd-c2    67.5      121.17         CORR_SOURCE5           28    1.6484
c -cd-c3    65.4      117.76         CORR_SOURCE5          566    1.9588
c -cd-c     65.2      121.07         CORR_SOURCE5          128    0.8902
c -cd-ca    65.0      122.95              SOURCE3            1
c -cd-cc    67.2      121.35         CORR_SOURCE5         3554    2.2084
cc-cd-cc    70.0      120.08         CORR_SOURCE5          119    1.6139
cc-cd-cd    70.3      114.19              SOURCE3          517    6.5960
cc-cd-cf    65.8      128.05         CORR_SOURCE5          350    2.4628
cc-cd-ch    67.1      125.79      SOURCE4_SOURCE5           84    1.6445
cc-cd-cl    71.7      123.41         CORR_SOURCE5          115    2.1217
cc-cd-cy    66.0      121.98               5/2017           12    0.8462
c -cd-cd    65.7      122.69              SOURCE3            2
c -cd-cf    65.4      121.57         CORR_SOURCE5           29    1.1305
cc-cd-h4    47.8      128.48      SOURCE3_SOURCE5         3291    2.3189
cc-cd-ha    49.0      121.76      SOURCE3_SOURCE5         4433    1.8701
c -cd-cl    72.6      116.38         CORR_SOURCE5           50    1.2099
cc-cd-n     87.0      121.33      SOURCE3_SOURCE5          821    1.9126
cc-cd-na    92.7      106.99      SOURCE3_SOURCE5         3003    2.3845
cc-cd-nc    88.1      123.82      SOURCE4_SOURCE5           28    0.3678
cc-cd-nd    91.1      111.65         CORR_SOURCE5         1656    1.8430
cc-cd-nh    86.3      123.84         CORR_SOURCE5          152    2.2360
cc-cd-oh    87.2      123.78         CORR_SOURCE5          251    1.1988
cc-cd-os    88.0      120.30              SOURCE3           64    5.4354
cc-cd-ss    66.9      111.55         CORR_SOURCE5         1048    1.8648
cc-cd-sy    62.5      124.55         CORR_SOURCE5           56    1.7107
cd-cd-cd    70.1      110.70              SOURCE3           54    3.4091
cd-cd-ce    68.0      122.72         CORR_SOURCE5           66    1.9701
cd-cd-cf    64.9      127.06         CORR_SOURCE5           61    2.3233
cd-cd-ch    65.8      125.91         CORR_SOURCE5           41    1.1646
cd-cd-cy    64.7      123.00               5/2017            7    0.2293
cd-cd-h4    46.3      127.96      SOURCE3_SOURCE5          391    2.1732
cd-cd-ha    47.6      121.07         CORR_SOURCE5         2414    2.2010
cd-cd-n2    87.4      122.21         CORR_SOURCE5           37    1.6493
cd-cd-n     85.8      119.89              SOURCE3           36    0.2095
cd-cd-na    86.5      117.77      SOURCE3_SOURCE5          832    1.6037
cd-cd-nc    90.3      112.56              SOURCE3          141    4.2871
cd-cd-nd    85.3      121.98         CORR_SOURCE5          141    1.9633
cd-cd-nh    86.0      119.72         CORR_SOURCE5          348    1.7785
cd-cd-oh    86.2      121.27         CORR_SOURCE5           11    2.2744
cd-cd-os    87.2      117.34         CORR_SOURCE5          217    1.9304
cd-cd-pc    84.5      115.36              SOURCE3           84    3.2889
cd-cd-ss    63.9      120.21         CORR_SOURCE5           52    2.1160
ce-cd-nd    86.6      123.98      SOURCE4_SOURCE5           10    2.4097
cf-cd-na    83.4      124.35         CORR_SOURCE5           87    1.3591
cf-cd-nc    85.9      121.70         CORR_SOURCE5           58    1.4179
cf-cd-nd    84.8      121.10         CORR_SOURCE5           43    1.2959
cf-cd-os    85.8      118.76         CORR_SOURCE5           92    1.3159
cf-cd-ss    63.2      121.58         CORR_SOURCE5           54    1.3126
c -cd-h4    47.1      118.19      SOURCE4_SOURCE5           16    0.2226
c -cd-ha    47.4      116.64      SOURCE3_SOURCE5          896    1.3075
cl-cd-nc    91.0      122.07         CORR_SOURCE5           19    1.6973
c -cd-n2    85.2      123.93         CORR_SOURCE5            6    0.0993
c -cd-n     85.7      116.37         CORR_SOURCE5           41    2.4875
c -cd-nc    85.3      121.88         CORR_SOURCE5           54    2.0672
c -cd-nd    83.5      123.32         CORR_SOURCE5           27    2.2025
c -cd-oh    87.6      113.66         CORR_SOURCE5          190    1.6462
c -cd-os    85.1      119.26         CORR_SOURCE5          104    2.4145
h4-cd-n     62.7      115.69      SOURCE3_SOURCE5          425    0.9142
h4-cd-na    61.5      120.53      SOURCE3_SOURCE5         1801    1.3882
h4-cd-nc    64.3      118.47      SOURCE3_SOURCE5          435    1.3360
h4-cd-nd    61.7      121.14      SOURCE3_SOURCE5          574    0.5658
h4-cd-os    63.6      114.90      SOURCE3_SOURCE5          456    0.8638
h4-cd-ss    42.5      119.97      SOURCE3_SOURCE5          496    0.7119
h5-cd-n     62.7      115.70         CORR_SOURCE5           41    0.7665
h5-cd-na    61.2      121.55      SOURCE3_SOURCE5         1138    0.7136
h5-cd-nc    62.5      125.52      SOURCE3_SOURCE5         1309    0.7276
h5-cd-nd    61.3      122.92      SOURCE3_SOURCE5          136    0.3532
h5-cd-os    63.1      116.83      SOURCE3_SOURCE5           42    1.3051
h5-cd-ss    42.3      121.02      SOURCE3_SOURCE5           46    0.6462
ha-cd-na    61.2      121.50              SOURCE2            1
ha-cd-nc    64.2      118.88              SOURCE3           20    2.8923
ha-cd-nd    62.9      116.54              SOURCE3            5    1.4482
ha-cd-os    64.8      110.86              SOURCE3            7    1.3846
ha-cd-pc    54.9      121.76              SOURCE3           84    2.2216
ha-cd-ss    42.2      121.64              SOURCE2            5
na-cd-nc   115.5      112.22      SOURCE3_SOURCE5         2726    1.5103
na-cd-nd   108.8      121.95         CORR_SOURCE5          321    1.6221
na-cd-nh   110.8      117.28      SOURCE4_SOURCE5          100    1.6359
na-cd-ss    83.7      111.46              SOURCE4           20    0.8600
nc-cd-nd   114.2      115.83         CORR_SOURCE5          309    1.2424
nc-cd-nh   111.7      120.65      SOURCE3_SOURCE5          554    1.6769
nc-cd-oh   112.7      121.12         CORR_SOURCE5           31    1.3923
nc-cd-os   114.1      116.74         CORR_SOURCE5          156    2.0183
nc-cd-ss    83.3      114.51              SOURCE3            8    0.3449
nd-cd-nd   107.6      125.70      SOURCE4_SOURCE5           31    0.5900
nd-cd-nh   111.3      117.23         CORR_SOURCE5           51    1.7463
nd-cd-ss    79.9      122.64      SOURCE3_SOURCE5           10    1.3100
nh-cd-nh   111.7      115.96              SOURCE3            1
nh-cd-os   111.8      116.68         CORR_SOURCE5           36    0.7439
nh-cd-ss    80.1      121.81         CORR_SOURCE5          128    1.0728
n -cd-na   108.3      122.12         CORR_SOURCE5           15    1.1276
n -cd-nc   110.3      123.00         CORR_SOURCE5          354    1.4352
n -cd-nd   106.9      126.23         CORR_SOURCE5          118    0.4381
n -cd-nh   110.9      116.94         CORR_SOURCE5          126    0.5956
n -cd-ss    79.7      122.88         CORR_SOURCE5           82    1.5666
oh-cd-os   115.4      111.61      SOURCE4_SOURCE5           12    1.1909
os-cd-ss    81.1      119.28      SOURCE3_SOURCE5           10    1.6753
ss-cd-ss    63.6      121.37                 CORR           22
ss-cd-sy    63.0      121.70         CORR_SOURCE5           43    0.4842
c2-ce-c3    66.0      122.53      SOURCE3_SOURCE5          882    1.9288
c2-ce-ca    67.4      121.78      SOURCE3_SOURCE5           11    1.7099
c2-ce-cc    67.6      123.32         CORR_SOURCE5          132    1.9068
c2-ce-ce    67.5      123.26      SOURCE3_SOURCE5          791    1.8772
c2-ce-cg    68.6      122.09         CORR_SOURCE5           54    1.3612
c2-ce-cl    72.1      119.76      SOURCE4_SOURCE5           62    1.3986
c2-ce-h4    49.2      124.55      SOURCE4_SOURCE5           43    1.6498
c2-ce-ha    50.1      119.94      SOURCE3_SOURCE5         1439    1.4338
c2-ce-n1    91.3      118.23      SOURCE4_SOURCE5           18    0.9047
c2-ce-n2    88.2      128.70              SOURCE3            1
c2-ce-na    87.2      119.19      SOURCE4_SOURCE5           10    0.8452
c2-ce-ne    88.5      118.32              SOURCE3            7    1.0468
c2-ce-oh    88.0      123.70      SOURCE4_SOURCE5           27    1.7525
c2-ce-p2    81.4      118.24              SOURCE3            1
c2-ce-pe    81.1      118.76              SOURCE3            8    2.3984
c2-ce-px    80.6      119.72              SOURCE3            6    0.5213
c2-ce-py    80.4      122.18      SOURCE3_SOURCE5           12    1.9482
c2-ce-sx    63.1      119.21      SOURCE3_SOURCE5           14    0.9863
c2-ce-sy    63.7      120.20      SOURCE3_SOURCE5           17    1.3599
c3-ce-ca    64.5      119.24         CORR_SOURCE5          312    1.7689
c3-ce-cc    65.2      118.03         CORR_SOURCE5           77    1.5840
c3-ce-ce    65.4      117.12         CORR_SOURCE5          524    1.4790
c3-ce-cf    66.0      122.38         CORR_SOURCE5          490    2.0752
c3-ce-cg    66.0      117.22      SOURCE4_SOURCE5           34    1.7153
c3-ce-n2    83.8      122.73         CORR_SOURCE5          149    1.8752
c3-ce-nf    84.4      120.68      SOURCE4_SOURCE5           13    2.1196
c3-ce-nh    82.7      119.56      SOURCE4_SOURCE5           10    1.0079
ca-ce-ca    65.7      117.83         CORR_SOURCE5          210    0.9675
ca-ce-cc    66.1      118.13         CORR_SOURCE5           30    0.7112
ca-ce-ce    65.7      119.54      SOURCE4_SOURCE5           32    1.9209
ca-ce-cf    65.7      127.52         CORR_SOURCE5          599    1.6916
ca-ce-cl    72.2      114.59      SOURCE4_SOURCE5           14    1.1195
ca-ce-h4    47.0      116.99      SOURCE4_SOURCE5          255    1.0051
ca-ce-ha    47.4      115.13         CORR_SOURCE5          720    0.9389
ca-ce-n2    86.1      120.72              SOURCE3            1
ca-ce-nf    85.5      121.71         CORR_SOURCE5           49    2.1313
ca-ce-nh    85.5      115.58      SOURCE4_SOURCE5          240    1.0372
ca-ce-oh    86.3      116.10         CORR_SOURCE5           15    0.6417
ca-ce-os    85.8      115.91      SOURCE4_SOURCE5           25    1.4247
ca-ce-ss    63.4      117.52      SOURCE4_SOURCE5           14    1.2435
c -ce-c2    67.6      120.42              SOURCE3           13    1.8877
c -ce-c3    64.9      117.22         CORR_SOURCE5          558    2.2754
c -ce-c     64.3      122.23         CORR_SOURCE5           52    2.1518
c -ce-ca    65.5      118.28      SOURCE4_SOURCE5           25    1.6999
cc-ce-cd    65.3      130.61      SOURCE4_SOURCE5           24    1.1422
cc-ce-cf    66.7      126.14         CORR_SOURCE5          122    1.8142
c -ce-cd    67.1      120.77         CORR_SOURCE5           15    1.8896
c -ce-ce    65.2      120.98      SOURCE4_SOURCE5           53    2.2319
c -ce-cf    65.9      126.41              SOURCE3            2    5.7847
c -ce-cg    66.5      118.42      SOURCE4_SOURCE5           49    1.0600
cc-ce-h4    47.9      115.68      SOURCE4_SOURCE5           77    0.8454
cc-ce-ha    48.0      115.44         CORR_SOURCE5          179    0.9381
c -ce-cl    71.8      115.47      SOURCE4_SOURCE5           25    1.2041
cc-ce-n2    86.9      120.96         CORR_SOURCE5          102    2.2421
cc-ce-nh    85.3      118.05      SOURCE4_SOURCE5           21    1.8052
c -ce-cy    74.6       88.56               5/2017           34    1.2419
cd-ce-ce    66.8      124.35         CORR_SOURCE5           18    1.4583
cd-ce-ha    50.6      114.95         CORR_SOURCE5           95    1.4175
ce-ce-ce    65.4      122.11      SOURCE3_SOURCE5            9    2.4680
ce-ce-cf    67.1      124.24         CORR_SOURCE5          866    1.6941
ce-ce-cl    71.6      117.22      SOURCE4_SOURCE5           35    0.8344
ce-ce-h4    47.3      118.13         CORR_SOURCE5           44    1.1161
ce-ce-ha    47.7      116.65      SOURCE3_SOURCE5         1159    0.9686
ce-ce-n1    84.0      127.15                 CORR            4
ce-ce-n2    87.5      118.93         CORR_SOURCE5           13    1.3210
ce-ce-oh    86.7      116.85      SOURCE4_SOURCE5           30    1.7182
cf-ce-cg    68.3      123.13         CORR_SOURCE5          115    2.1292
cf-ce-cy    62.2      137.46               5/2017           18    1.4229
cf-ce-h4    49.3      122.95      SOURCE4_SOURCE5           23    1.1580
cf-ce-ha    50.4      118.22         CORR_SOURCE5         1522    1.3445
cf-ce-n1    90.5      119.94      SOURCE4_SOURCE5           13    1.8896
cf-ce-n     91.2      108.39         CORR_SOURCE5           86    1.0066
cf-ce-nh    87.3      121.38      SOURCE4_SOURCE5           39    1.7667
cf-ce-oh    88.6      121.69         CORR_SOURCE5           37    1.2824
cg-ce-cg    68.4      116.52         CORR_SOURCE5           35    1.1031
cg-ce-ha    48.6      116.46         CORR_SOURCE5           58    0.6523
cg-ce-n1    87.8      119.50                 CORR            2
cg-ce-n2    87.9      121.14      SOURCE4_SOURCE5           14    0.8974
c -ce-ha    47.0      116.46      SOURCE3_SOURCE5         1028    1.3091
c -ce-n     83.3      118.45         CORR_SOURCE5          213    1.4857
c -ce-nh    85.3      115.36         CORR_SOURCE5           28    2.1980
c -ce-oh    86.2      115.76      SOURCE4_SOURCE5           20    2.0254
c -ce-os    86.1      114.67      SOURCE4_SOURCE5           47    2.1291
h4-ce-n1    64.9      116.64      SOURCE4_SOURCE5           19    0.4343
h4-ce-n2    64.4      121.48         CORR_SOURCE5          257    1.1842
h4-ce-ne    62.2      115.65      SOURCE4_SOURCE5           19    1.8165
ha-ce-n1    65.1      115.96                 CORR            4
ha-ce-n2    65.0      119.51              SOURCE3            2    0.4623
ha-ce-ne    61.4      118.59              SOURCE3            5    1.1113
ha-ce-nh    62.5      114.99                 CORR            2
ha-ce-p2    52.6      120.11              SOURCE3            1
ha-ce-pe    52.7      119.33              SOURCE3            6    0.8966
ha-ce-px    52.9      117.90              SOURCE3            6    0.1809
ha-ce-py    53.3      117.99      SOURCE3_SOURCE5           11    0.7169
ha-ce-sx    41.7      115.45              SOURCE3            3    0.6640
ha-ce-sy    42.6      114.86              SOURCE3            3    0.4717
n2-ce-nh   110.0      125.09         CORR_SOURCE5          163    1.6803
n2-ce-os   114.2      117.95      SOURCE4_SOURCE5           19    0.3524
n2-ce-ss    81.5      117.23              SOURCE4            6    2.0518
ne-ce-ne   106.5      123.87              SOURCE3            1
ne-ce-nh   111.3      113.64      SOURCE4_SOURCE5           41    1.4024
nf-ce-nh   112.3      119.27      SOURCE4_SOURCE5           23    1.5487
pe-ce-pe    97.9      129.79              SOURCE3            1
py-ce-py   108.0      108.06              SOURCE3            1
sx-ce-sx    61.7      120.32              SOURCE3            1
sy-ce-sy    62.9      119.97              SOURCE3            1
c2-cf-c3    66.0      122.53      SOURCE3_SOURCE5          875    1.9359
c2-cf-ca    67.4      121.78      SOURCE3_SOURCE5            5    1.1712
c2-cf-cd    67.6      123.32         CORR_SOURCE5          132    1.9068
c2-cf-cf    67.5      123.26      SOURCE3_SOURCE5          779    1.8961
c2-cf-ch    68.6      122.09         CORR_SOURCE5           54    1.3612
c2-cf-ha    50.1      119.94      SOURCE3_SOURCE5         1393    1.4017
c2-cf-n2    88.2      128.70              SOURCE3            1
c2-cf-nf    88.5      118.32              SOURCE3            7
c2-cf-p2    81.4      118.24              SOURCE3            1
c2-cf-pf    81.1      118.76              SOURCE3            8
c2-cf-px    80.6      119.72              SOURCE3            6
c2-cf-py    80.4      122.18      SOURCE3_SOURCE5            7    1.0992
c2-cf-sx    63.1      119.21      SOURCE3_SOURCE5            9    1.0588
c2-cf-sy    63.7      120.20      SOURCE3_SOURCE5           12    1.7015
c3-cf-ca    64.5      119.24         CORR_SOURCE5          312    1.7689
c3-cf-cd    65.3      118.03         CORR_SOURCE5           77    1.5840
c3-cf-ce    66.0      122.38         CORR_SOURCE5          490    2.0752
c3-cf-cf    65.4      117.12         CORR_SOURCE5          524    1.4790
c3-cf-n2    83.8      122.73         CORR_SOURCE5          149    1.8752
ca-cf-ca    65.7      117.83         CORR_SOURCE5          210    0.9675
ca-cf-cc    64.6      130.88      SOURCE4_SOURCE5           41    1.2386
ca-cf-cd    66.1      118.13         CORR_SOURCE5           30    0.7112
ca-cf-ce    65.7      127.52         CORR_SOURCE5          599    1.6916
ca-cf-ha    47.4      115.13         CORR_SOURCE5          720    0.9389
ca-cf-n2    86.1      120.72              SOURCE3            1
ca-cf-ne    85.5      121.71         CORR_SOURCE5           49    2.1313
ca-cf-oh    86.3      116.10         CORR_SOURCE5           15    0.6417
c -cf-c2    67.6      120.42              SOURCE3           13
c -cf-c3    64.9      117.22         CORR_SOURCE5          558    2.2754
c -cf-c     64.3      122.23         CORR_SOURCE5           52    2.1518
c -cf-cc    67.1      120.77         CORR_SOURCE5           15    1.8896
cc-cf-cf    66.8      124.35         CORR_SOURCE5           18    1.4583
c -cf-cd    66.1      117.82      SOURCE4_SOURCE5           29    1.0204
c -cf-ce    65.9      126.41              SOURCE3            2
cc-cf-ha    50.6      114.95         CORR_SOURCE5           95    1.4175
cd-cf-ce    66.7      126.14         CORR_SOURCE5          122    1.8142
cd-cf-ha    48.0      115.44         CORR_SOURCE5          179    0.9381
cd-cf-n2    86.9      120.96         CORR_SOURCE5          102    2.2421
ce-cf-cf    67.1      124.24         CORR_SOURCE5          866    1.6941
ce-cf-ch    68.3      123.13         CORR_SOURCE5          115    2.1292
ce-cf-ha    50.4      118.22         CORR_SOURCE5         1522    1.3445
ce-cf-n     91.2      108.39         CORR_SOURCE5           86    1.0066
ce-cf-oh    88.6      121.69         CORR_SOURCE5           37    1.2824
cf-cf-cf    65.4      122.11      SOURCE3_SOURCE5            9    2.4680
cf-cf-h4    47.3      118.13         CORR_SOURCE5           44    1.1161
cf-cf-ha    47.7      116.65      SOURCE3_SOURCE5         1159    0.9686
cf-cf-n1    84.0      127.15                 CORR            4
cf-cf-n2    87.5      118.93         CORR_SOURCE5           13    1.3210
c -cf-ha    47.0      116.46      SOURCE3_SOURCE5         1028    1.3091
ch-cf-ch    68.4      116.52         CORR_SOURCE5           35    1.1031
ch-cf-ha    48.6      116.46         CORR_SOURCE5           58    0.6523
ch-cf-n1    87.8      119.50                 CORR            2
c -cf-n2    88.2      114.41      SOURCE4_SOURCE5           13    1.4243
c -cf-n     83.3      118.45         CORR_SOURCE5          213    1.4857
c -cf-nh    85.3      115.36         CORR_SOURCE5           28    2.1980
f -c -f    123.8      107.35              SOURCE2            2    0.2500
h4-cf-n2    64.4      121.48         CORR_SOURCE5          257    1.1842
h4-cf-ne    64.3      120.56      SOURCE4_SOURCE5           39    0.8435
ha-cf-n1    65.1      115.96                 CORR            4
ha-cf-n2    65.0      119.51              SOURCE3            2
ha-cf-nf    61.4      118.59              SOURCE3            5
ha-cf-nh    62.5      114.99                 CORR            2
ha-cf-p2    52.6      120.11              SOURCE3            1
ha-cf-pf    52.7      119.33              SOURCE3            6
ha-cf-px    52.9      117.90              SOURCE3            6
ha-cf-py    53.3      117.99      SOURCE3_SOURCE5            8    0.8708
ha-cf-sx    41.7      115.45              SOURCE3            3
ha-cf-sy    42.6      114.86              SOURCE3            3
n2-cf-nh   110.0      125.09         CORR_SOURCE5          163    1.6803
nf-cf-nf   106.5      123.87              SOURCE3            1
f -c -o    118.2      123.44              SOURCE3            1
pf-cf-pf    97.9      129.79              SOURCE3            1
py-cf-py   108.0      108.06              SOURCE3            1
f -c -s     84.4      124.00              SOURCE2            1
sx-cf-sx    61.7      120.32              SOURCE3            1
sy-cf-sy    62.9      119.97              SOURCE3            1
c1-cg-ca    58.6      179.57         CORR_SOURCE5           38    0.4711
c1-cg-cc    58.9      178.61      SOURCE4_SOURCE5           13    0.3677
c1-cg-ce    59.0      178.05         CORR_SOURCE5           15    0.1905
c1-cg-cg    60.4      179.67         CORR_SOURCE5           90    0.1487
c1-cg-ne    79.3      170.02              SOURCE3            4    1.1724
c1-cg-pe    75.1      173.29              SOURCE3           11    4.9305
ca-cg-ch    58.7      179.43         CORR_SOURCE5           40    0.6103
ca-cg-n1    74.3      179.49         CORR_SOURCE5          186    0.6659
c -cg-c1    58.1      179.14              SOURCE3            2
cc-cg-n1    74.8      178.62         CORR_SOURCE5           43    0.6454
ce-cg-ch    59.2      177.94                 CORR           17
ce-cg-n1    74.9      177.97         CORR_SOURCE5          184    1.2220
n1-cg-ne    99.9      174.03         CORR_SOURCE5           30    0.6173
h4-c -o     66.6      120.70      SOURCE4_SOURCE5          491    0.4811
h5-c -n     63.5      112.16      SOURCE4_SOURCE5           98    0.3632
h5-c -o     65.9      123.65      SOURCE4_SOURCE5          150    0.7654
ha-c -ha    37.4      115.61              SOURCE3            4    0.0458
ha-c -i     38.2      110.58              SOURCE3            1
ha-c -n     63.5      112.37              SOURCE3            4    0.6424
ha-c -o     66.5      121.94              SOURCE3           51    2.3235
ha-c -oh    64.6      111.82              SOURCE3            4    1.9375
ha-c -os    64.8      110.34              SOURCE3            8    1.9344
ha-c -s     44.8      119.56              SOURCE3            3    0.7586
c1-ch-ca    58.5      179.57         CORR_SOURCE5           38    0.4711
c1-ch-cf    58.9      178.05         CORR_SOURCE5           15    0.1905
c1-ch-ch    60.3      179.67         CORR_SOURCE5           90    0.1487
c1-ch-nf    79.2      170.02              SOURCE3            4
c1-ch-pf    75.1      173.29              SOURCE3           11
ca-ch-cg    58.7      179.43         CORR_SOURCE5           40    0.6103
ca-ch-n1    74.3      179.49         CORR_SOURCE5          186    0.6659
c -ch-c1    58.1      179.14              SOURCE3            2
cd-ch-n1    74.8      178.63         CORR_SOURCE5           49    0.3708
cf-ch-cg    59.2      177.94                 CORR           17
cf-ch-n1    74.9      177.97         CORR_SOURCE5          184    1.2220
cg-ch-ch    60.6      179.58      SOURCE4_SOURCE5           55    0.2973
n1-ch-nf    99.9      174.03         CORR_SOURCE5           30    0.6173
i -c -i     65.4      116.45              SOURCE3            1
i -c -o     71.7      122.02              SOURCE3            4    1.2961
f -cl-f      0.0       87.50              SOURCE2            1
n2-c -n2   110.8      110.31              SOURCE3            1
n2-c -o    111.8      122.50              SOURCE3            1
n4-c -n4    99.8      114.64              SOURCE3            1
n4-c -o    106.6      118.83              SOURCE3            4    3.8516
nc-c -o    113.3      123.18         CORR_SOURCE5          172    1.0508
nd-c -o    113.3      123.18         CORR_SOURCE5          172    1.0508
ne-c -ne   113.1      110.31                 CORR            2
ne-c -o    111.9      125.81         CORR_SOURCE5           65    1.1135
nf-c -nf   113.1      110.31                 CORR            2
nf-c -o    111.9      125.81         CORR_SOURCE5           65    1.1135
n -c -n    112.4      113.56      SOURCE4_SOURCE5         1747    1.4619
n -c -nc   110.4      117.11         CORR_SOURCE5          131    0.7717
n -c -nd   110.4      117.11         CORR_SOURCE5          131    0.7717
n -c -ne   113.6      110.26      SOURCE4_SOURCE5           25    1.7043
n -c -o    113.8      123.05      SOURCE3_SOURCE5         8454    1.5552
n -c -oh   113.9      112.82      SOURCE4_SOURCE5           14    1.4518
no-c -no   102.6      109.28              SOURCE3            1
no-c -o    104.1      125.36              SOURCE3            1
n -c -os   115.5      109.22      SOURCE4_SOURCE5          821    0.9352
n -c -s     82.4      124.05      SOURCE3_SOURCE5          514    1.4099
n -c -sh    81.6      112.97      SOURCE4_SOURCE5           26    1.1725
n -c -ss    82.5      110.29      SOURCE4_SOURCE5          160    1.6051
oh-c -oh   116.3      110.56              SOURCE3            2    0.5498
oh-c -s     83.0      123.44              SOURCE3            1
o -c -o    118.8      130.25      SOURCE4_SOURCE5         1037    1.2396
o -c -oh   115.7      122.10      SOURCE3_SOURCE5         2859    0.8497
o -c -os   114.8      123.25      SOURCE4_SOURCE5         5492    1.1411
o -c -p2    96.2      123.10              SOURCE3            1
o -c -p3    98.0      120.79              SOURCE3            1
o -c -p5    97.9      121.17      SOURCE4_SOURCE5           18    1.1433
o -c -pe    95.6      123.02              SOURCE3            3    0.1404
o -c -pf    95.6      123.02              SOURCE3            3
o -c -px    97.6      119.10              SOURCE3            1
o -c -py    98.3      122.01      SOURCE4_SOURCE5           14    1.0132
o -c -s4    76.8      121.15              SOURCE3            1
o -c -s6    77.3      119.45              SOURCE3            1
o -c -s     85.6      120.44              SOURCE3            2
o -c -sh    79.5      122.05      SOURCE3_SOURCE5           10    1.1120
os-c -os   115.3      111.29      SOURCE4_SOURCE5           32    0.8183
o -c -ss    79.0      123.32      SOURCE3_SOURCE5          190    1.2053
os-c -s     82.4      125.01      SOURCE4_SOURCE5           62    1.0980
os-c -ss    82.3      111.40      SOURCE4_SOURCE5           23    1.7283
o -c -sx    76.1      121.15              SOURCE3            5    3.6452
o -c -sy    77.6      119.32              SOURCE3            5    2.4495
p2-c -p2   100.1      113.75              SOURCE3            1
p3-c -p3    99.1      118.04              SOURCE3            1
p3-c -py   113.9       90.08              SOURCE3            1
p5-c -p5    96.9      123.76              SOURCE3            1
ca-cp-ca    68.9      118.38         CORR_SOURCE5          959    0.6763
ca-cp-cp    66.1      121.11         CORR_SOURCE5         1631    1.6425
ca-cp-na    86.5      119.50      SOURCE4_SOURCE5           59    0.7877
ca-cp-nb    87.1      121.62      SOURCE4_SOURCE5          174    0.6998
cp-cp-cp    74.8       90.00              SOURCE3            4
cp-cp-cq    64.3      124.27         CORR_SOURCE5            8    2.0477
cp-cp-nb    86.1      116.61      SOURCE4_SOURCE5          235    1.1595
pe-c -pe    99.5      113.77              SOURCE3            1
pf-c -pf    99.5      113.77              SOURCE3            1
nb-cp-nb   110.0      125.79      SOURCE4_SOURCE5           11    0.6658
py-c -py    97.6      123.80              SOURCE3            1
ca-cq-ca    68.9      118.38         CORR_SOURCE5          959    0.6763
ca-cq-cq    66.1      121.11         CORR_SOURCE5         1631    1.6425
ca-cq-nb    87.1      121.62      SOURCE4_SOURCE5          111    0.7244
cp-cq-cq    64.3      124.29         CORR_SOURCE5            8    1.4947
cq-cq-cq    74.8       90.00              SOURCE3            4
cq-cq-nb    86.1      116.61      SOURCE4_SOURCE5          147    1.1420
s4-c -s4    63.1      108.81              SOURCE3            1
s6-c -s6    61.2      115.75              SOURCE3            1
sh-c -sh    63.8      115.33              SOURCE3            1
s -c -s     65.5      126.50      SOURCE3_SOURCE5           14    1.3489
s -c -sh    63.9      122.65      SOURCE4_SOURCE5           37    1.5614
s -c -ss    63.7      123.19      SOURCE3_SOURCE5           85    1.7112
ss-c -ss    64.5      112.42      SOURCE3_SOURCE5           17    0.4533
sx-c -sx    62.6      108.80              SOURCE3            1
sy-c -sy    61.4      115.78              SOURCE3            1
c2-cu-cx    61.5      148.60               5/2017           17    1.4719
c -cu-cu    98.0       62.60              SOURCE2            1
cu-cu-cx    94.0       64.55               5/2017            4    0.0062
cu-cu-ha    46.6      147.73              SOURCE2            3    2.0950
cv-cv-cy    75.1       94.49               5/2017            6    0.2122
cv-cv-ha    47.7      133.50               5/2017            3    0.0186
cx-cv-cx    73.4       90.85               5/2017            1
cy-cv-ha    43.1      132.01               5/2017            3    0.0362
c1-cx-cx    65.3      119.34               5/2017           42    1.0811
c2-cx-cx    64.2      120.22               5/2017          156    2.3854
c2-cx-h1    47.0      115.88               5/2017           26    0.7463
c2-cx-hc    47.2      115.17               5/2017           33    1.0389
c2-cx-os    87.0      109.89               5/2017            2    2.0524
c3-cx-c3    64.8      114.17               5/2017          161    2.2823
c3-cx-cx    63.4      120.11               5/2017         1291    2.3797
c3-cx-h1    46.1      115.28               5/2017          237    1.1012
c3-cx-hc    46.3      114.48               5/2017          206    1.5724
c3-cx-n3    84.0      111.78               5/2017            1
c3-cx-os    85.5      110.47               5/2017            5    1.4459
ca-cx-cx    63.5      121.84               5/2017          132    1.8829
ca-cx-h1    47.0      114.77               5/2017           12    0.6332
ca-cx-hc    47.2      113.72               5/2017           39    0.9866
ca-cx-oh    86.7      112.93              SOURCE3            1
ca-cx-os    82.8      118.31      SOURCE4_SOURCE5           18    0.7292
c -cx-c3    64.2      117.66               5/2017           53    1.9496
cc-cx-cx    64.8      119.04               5/2017           42    1.0449
cc-cx-hc    47.9      113.81               5/2017           20    0.6483
c -cx-cx    64.4      117.98               5/2017          407    2.1940
cd-cx-cx    64.2      120.77               5/2017           31    1.2872
c -cx-h1    46.5      116.28               5/2017           62    1.2929
c -cx-hc    46.4      116.67               5/2017           86    1.6963
cl-cx-cl    81.8      110.29               5/2017           14    0.4864
cl-cx-cx    69.5      119.79               5/2017           69    0.7321
cl-cx-h1    48.5      110.54               5/2017            2    0.1150
cl-cx-hc    47.9      115.80              SOURCE2            1
c -cx-os    86.9      108.60               5/2017            1
cu-cx-cu   100.4       50.91               5/2017            2    0.0020
cu-cx-cx    92.5       58.44               5/2017           28    0.4472
cu-cx-hc    46.9      118.69               5/2017           29    0.5914
cx-cx-cx    90.2       60.00               5/2017         1689    0.8111
cx-cx-cy    62.1      125.01               5/2017            7    2.6658
cx-cx-f     85.1      118.81               5/2017           17    1.2118
cx-cx-h1    45.9      118.69               5/2017         1339    1.3738
cx-cx-hc    46.1      117.69               5/2017         3482    0.9446
cx-cx-hx    45.7      119.61               5/2017           20    0.1625
cx-cx-n3    82.1      118.31               5/2017           44    1.4967
cx-cx-na    79.1      126.07               5/2017           53    1.5534
cx-cx-nh    82.3      118.36               5/2017           30    1.0567
cx-cx-os    83.5      117.05               5/2017           24    1.7797
cy-cx-hc    46.5      112.55               5/2017            1
f -cx-f    119.3      109.55               5/2017            2
f -cx-h1    65.5      111.68              SOURCE3            1
f -cx-hc    65.3      112.30              SOURCE2            1
h1-cx-h1    37.9      115.46               5/2017          355    0.3352
h1-cx-n3    61.0      113.39               5/2017           12    1.7033
h1-cx-n     61.1      114.26               5/2017            9    0.9343
h1-cx-na    61.8      108.27               5/2017           27    1.0053
h1-cx-nh    60.9      115.14               5/2017           13    0.0780
h1-cx-os    62.1      114.46               5/2017            3    0.8753
h2-cx-h2    37.9      115.54               5/2017            1
h2-cx-n2    58.7      117.18              SOURCE3            4
hc-cx-hc    38.1      114.43               5/2017          576    0.4881
hc-cx-os    61.1      114.10              SOURCE2            1
hx-cx-n4    59.7      110.22               5/2017            1
n2-cx-n2   162.4       49.07               5/2017            1
n -cx-oh   108.9      114.81               5/2017            1
n -cx-os   141.3       65.98              SOURCE3            1
oh-cx-oh   116.9      107.85              SOURCE3            1
oh-cx-os   108.5      118.12              SOURCE3            4    1.3581
os-cx-os   106.7      116.05      SOURCE4_SOURCE5           15    2.1532
c2-cy-cy    64.0      115.00               5/2017           33    3.1772
c3-cy-c3    65.1      111.38               5/2017           38    1.0405
c3-cy-cy    62.8      117.77               5/2017          593    2.7140
c3-cy-h1    46.5      111.78               5/2017          190    0.4589
c3-cy-hc    46.9      110.12               5/2017          286    0.5586
c3-cy-n3    83.9      110.25               5/2017            3    0.3967
c3-cy-n     84.2      111.04               5/2017            1
c3-cy-os    84.8      110.09               5/2017            2    0.2833
c -cy-c3    63.2      116.70               5/2017          203    0.5967
cc-cy-cy    62.5      121.63               5/2017            9    0.2884
c -cy-cy    73.4       85.16               5/2017          409    1.0345
cd-cy-cy    62.5      121.06               5/2017           18    0.5909
ce-cy-h2    45.8      117.52               5/2017           21    0.5798
ce-cy-n     94.2       87.94      SOURCE4_SOURCE5           38    0.1933
ce-cy-ss    60.4      120.60               5/2017           19    1.1851
c -cy-h1    45.8      112.97               5/2017           96    0.8493
c -cy-hc    46.1      111.24               5/2017          238    1.1926
cl-cy-cy    69.4      117.25               5/2017           41    1.1740
cl-cy-h1    49.1      107.03               5/2017            2    1.3003
cl-cy-hc    47.6      114.00              SOURCE2            1
c -cy-n     81.3      117.38               5/2017           90    1.1235
c -cy-os    82.4      115.16               5/2017            6    1.5549
cv-cy-cy    73.5       86.72               5/2017           24    1.1522
cv-cy-hc    46.3      114.40               5/2017           18    1.4851
cx-cy-cy    66.1      106.75               5/2017            3    4.9550
cx-cy-hc    45.7      118.30              SOURCE2            3    5.7799
cy-cy-cy    71.9       88.44               5/2017          714    1.4899
cy-cy-f     84.6      115.66               5/2017           27    3.1666
cy-cy-h1    45.6      113.17               5/2017          481    1.1549
cy-cy-h2    44.9      116.79               5/2017          123    0.8369
cy-cy-hc    45.2      114.76               5/2017         1518    2.4131
cy-cy-n3    80.9      116.60               5/2017           41    1.9946
cy-cy-n     80.3      119.87               5/2017          113    1.4402
cy-cy-na    80.1      119.48               5/2017           17    0.5542
cy-cy-oh    82.6      114.60               5/2017           24    2.6382
cy-cy-os    82.3      114.71               5/2017           39    2.3152
cy-cy-s6    60.8      117.08               5/2017           12    1.3239
cy-cy-ss    60.6      118.27               5/2017           90    1.2954
h1-cy-h1    38.7      109.44               5/2017           67    0.5923
h1-cy-n3    61.4      110.16               5/2017           15    1.4228
h1-cy-n     62.9      107.99               5/2017           80    0.6278
h1-cy-oh    63.3      109.11               5/2017            4    2.0154
h1-cy-os    62.9      109.23               5/2017           10    1.1356
h1-cy-s6    41.7      111.19               5/2017           11    1.1767
h2-cy-n     59.8      114.50      SOURCE4_SOURCE5          213    0.6904
h2-cy-os    63.0      108.84               5/2017           12    0.4716
h2-cy-s6    41.8      110.84               5/2017           23    1.9357
h2-cy-ss    42.0      109.66               5/2017           87    0.4949
hc-cy-hc    38.8      108.97               5/2017          285    0.5322
n -cy-os   109.9      110.91               5/2017            3    2.6953
n -cy-s6    82.4      103.18      SOURCE4_SOURCE5           18    0.8204
n -cy-ss    81.7      105.13      SOURCE4_SOURCE5          165    0.4214
nh-cz-nh   112.6      120.14      SOURCE4_SOURCE5           67    0.3910
br-n1-c1    52.1      180.00            HF/6-31G*            1
c1-n1-c1    65.9      179.92            HF/6-31G*            1
c1-n1-c2    61.7      177.73            HF/6-31G*            1
c1-n1-c3    57.8      177.72    HF/6-31G*_SOURCE5            6    0.4473
c1-n1-ca    60.5      179.99            HF/6-31G*            1
c1-n1-cl    62.2      179.95            HF/6-31G*            1
c1-n1-f     73.9      179.96            HF/6-31G*            1
c1-n1-hn    45.5      179.98            HF/6-31G*            1
c1-n1-i     49.1      179.95            HF/6-31G*            1
c1-n1-n1    83.2      180.00            HF/6-31G*            1
c1-n1-n2    81.6      171.56            HF/6-31G*            1
c1-n1-n3    76.1      175.59            HF/6-31G*            1
c1-n1-n4    74.8      179.69            HF/6-31G*            1
c1-n1-na    75.1      180.00            HF/6-31G*            1
c1-n1-nh    76.3      176.35            HF/6-31G*            1
c1-n1-o     77.9      179.95            HF/6-31G*            1
c1-n1-oh    78.3      174.31            HF/6-31G*            1
c1-n1-os    77.4      176.61            HF/6-31G*            1
c1-n1-p2    71.0      172.83            HF/6-31G*            1
c1-n1-p3    71.6      173.51            HF/6-31G*            1
c1-n1-p4    70.7      173.64            HF/6-31G*            1
c1-n1-p5    74.4      177.28            HF/6-31G*            1
c1-n1-s2    61.9      178.11            HF/6-31G*            1
c1-n1-s4    56.7      169.60            HF/6-31G*            1
c1-n1-s     54.8      179.99            HF/6-31G*            1
c1-n1-s6    63.4      175.92            HF/6-31G*            1
c1-n1-sh    57.2      174.25            HF/6-31G*            1
c1-n1-ss    56.9      176.06            HF/6-31G*            1
c2-n1-n1    77.2      180.00            HF/6-31G*            1
c2-n1-o     91.4      116.94              SOURCE3            2    0.0060
c2-n1-s     66.6      118.00              SOURCE3            2    0.0121
c3-n1-n1    72.2      180.00            HF/6-31G*            1
ca-n1-n1    76.1      180.00            HF/6-31G*            1
ce-n1-o     89.2      122.40                 CORR            2
ce-n1-s     66.7      117.34                 CORR            2
cf-n1-o     89.2      122.40                 CORR            2
cf-n1-s     66.7      117.34                 CORR            2
cl-n1-n1    78.0      179.94            HF/6-31G*            1
f -n1-n1    92.9      179.93            HF/6-31G*            1
hn-n1-n1    57.7      179.91            HF/6-31G*            1
i -n1-n1    61.3      179.94            HF/6-31G*            1
n1-n1-n1   105.1      179.97            HF/6-31G*            1
n1-n1-n2   102.5      172.85    HF/6-31G*_SOURCE5           38    0.7957
n1-n1-n3    95.8      175.09            HF/6-31G*            1
n1-n1-n4    94.1      179.91            HF/6-31G*            1
n1-n1-na    94.5      179.97            HF/6-31G*            1
n1-n1-nh    96.1      176.00            HF/6-31G*            1
n1-n1-o     98.2      179.94            HF/6-31G*            1
n1-n1-oh    98.8      173.77            HF/6-31G*            1
n1-n1-os    97.6      176.12            HF/6-31G*            1
n1-n1-p2    88.5      174.71            HF/6-31G*            1
n1-n1-p3    89.5      174.27            HF/6-31G*            1
n1-n1-s     68.7      180.00              SOURCE3            1
n1-n1-sh    71.6      175.07            HF/6-31G*            1
n1-n1-ss    71.5      175.61            HF/6-31G*            1
o -n1-p2   107.3      116.05              SOURCE3            1
p2-n1-s     83.7      119.93              SOURCE3            1
br-n2-br    64.5      106.60              SOURCE3            1
br-n2-c2    60.2      112.40              SOURCE3            1
br-n2-n2    76.1      110.42              SOURCE3            1
br-n2-o     74.5      114.47              SOURCE3            1
br-n2-p2    82.7      111.03              SOURCE3            1
br-n2-s     63.5      115.78              SOURCE3            1
c1-n2-c1    77.4      121.10              SOURCE3            1
c1-n2-c3    60.9      151.88              SOURCE3            4   15.8282
c1-n2-cl    68.8      118.80              SOURCE2            1
c1-n2-hn    52.3      126.50              SOURCE2            3    7.6267
c1-n2-n2    97.2      113.40              SOURCE3            1
c1-n2-o     99.3      113.59              SOURCE3            1
c1-n2-p2    88.5      119.57              SOURCE3            1
c1-n2-s     71.9      117.67              SOURCE3            1
c2-n2-c2    73.2      118.18              SOURCE3            1
c2-n2-c3    68.5      115.30              SOURCE3            8    4.2940
c2-n2-ca    72.1      119.94              SOURCE3            1
c2-n2-cl    70.5      112.64              SOURCE3            1
c2-n2-f     90.8      108.14              SOURCE3            1
c2-n2-hn    53.2      110.80      SOURCE3_SOURCE5          419    0.5563
c2-n2-i     54.9      114.74              SOURCE3            2    0.0139
c2-n2-n1    94.7      115.09            HF/6-31G*            1
c2-n2-n2    98.5      103.59              SOURCE3            2
c2-n2-n3    90.0      118.14              SOURCE3            1
c2-n2-n4    78.6      112.22              SOURCE3            3    0.0406
c2-n2-n     88.9      117.93      SOURCE4_SOURCE5           32    1.2067
c2-n2-na    88.7      117.58              SOURCE3            8    1.6671
c2-n2-nh    89.3      117.61              SOURCE3            6    3.2642
c2-n2-no    86.0      118.02      SOURCE3_SOURCE5            8    0.7772
c2-n2-o     94.4      116.94              SOURCE3            1
c2-n2-oh    90.4      111.12      SOURCE4_SOURCE5           59    1.2303
c2-n2-os    90.0      110.96      SOURCE4_SOURCE5           46    1.0478
c2-n2-p2    88.8      116.00              SOURCE3            1
c2-n2-p3    80.9      119.30              SOURCE3            3    2.8489
c2-n2-p4    82.7      118.77              SOURCE3            1
c2-n2-s4    70.1      112.29              SOURCE3            1
c2-n2-s6    70.8      116.24              SOURCE3            1
c2-n2-s     70.7      118.00              SOURCE3            1
c2-n2-sh    64.9      115.48              SOURCE3            1
c2-n2-ss    66.9      118.04              SOURCE3            4    2.2804
c3-n2-c3    66.1      110.70              SOURCE3            1
c3-n2-ca    68.2      115.05      SOURCE4_SOURCE5           12    1.0676
c3-n2-ce    67.4      118.67         CORR_SOURCE5          270    1.8559
c3-n2-cf    67.4      118.67         CORR_SOURCE5          270    1.8559
c3-n2-hn    45.9      118.40              SOURCE3            1
c3-n2-n1    86.6      116.10      SOURCE4_SOURCE5           33    0.4557
c3-n2-n2    87.8      110.84      SOURCE3_SOURCE5           20    1.2862
c3-n2-nh    86.1      109.99              SOURCE3            1
c3-n2-o     88.3      112.40              SOURCE2            1
c3-n2-p2    85.9      114.21              SOURCE3            2    2.2772
c3-n2-s6    68.3      113.84              SOURCE3            1
c3-n2-s     67.8      116.72              SOURCE3            1
ca-n2-ca    73.9      112.20              SOURCE3            1
ca-n2-hn    50.4      120.00              SOURCE3            1
ca-n2-n2    93.3      113.53              SOURCE3            1
ca-n2-o     93.9      116.00              SOURCE2            1
ca-n2-p2    87.6      118.11              SOURCE3            1
ca-n2-s     69.8      120.11              SOURCE3            1
c -n2-c2    68.3      120.97              SOURCE3            1
c -n2-c     64.6      123.80              SOURCE3            1
c -n2-ca    68.0      120.50              SOURCE3            1
cc-n2-cl    69.5      115.79                 CORR            2
cc-n2-hn    52.8      111.25         CORR_SOURCE5           44    0.9238
cc-n2-na    91.8      109.24      SOURCE4_SOURCE5           23    1.5921
cc-n2-nh    88.7      118.47      SOURCE4_SOURCE5           13    1.7276
cd-n2-cl    69.5      115.79                 CORR            2
cd-n2-hn    52.8      111.25         CORR_SOURCE5           44    0.9238
ce-n2-hn    53.0      111.00         CORR_SOURCE5          129    0.3980
ce-n2-n     88.7      117.98         CORR_SOURCE5          153    0.9604
ce-n2-nh    88.8      118.34         CORR_SOURCE5           99    1.0308
ce-n2-o     96.2      112.16              SOURCE3            1
ce-n2-oh    89.5      112.79         CORR_SOURCE5          124    1.4261
ce-n2-os    89.1      112.79         CORR_SOURCE5           58    1.1282
ce-n2-s     71.2      116.28              SOURCE3            1
cf-n2-hn    52.9      111.05         CORR_SOURCE5            5    0.7460
cf-n2-n     88.7      117.98         CORR_SOURCE5          153    0.9604
cf-n2-nh    88.8      118.34         CORR_SOURCE5           99    1.0308
cf-n2-o     96.2      112.16              SOURCE3            1
cf-n2-oh    89.5      112.79         CORR_SOURCE5          124    1.4261
cf-n2-os    89.1      112.79         CORR_SOURCE5           58    1.1282
cf-n2-s     71.2      116.28              SOURCE3            1
cl-n2-n1    90.0      108.70              SOURCE2            1
cl-n2-n2    89.2      110.47              SOURCE3            1
cl-n2-o     87.9      114.03              SOURCE3            1
cl-n2-p2    93.1      112.98              SOURCE3            1
cl-n2-s     72.6      115.77              SOURCE3            1
cx-n2-n2   115.2       65.27               5/2017            3    0.2783
f -n2-n2   110.9      114.60              SOURCE2            1
f -n2-o    114.5      110.10              SOURCE2            1
f -n2-p2   113.3      107.10              SOURCE3            1
f -n2-s     89.0      110.73              SOURCE3            1
hn-n2-hn    38.3      120.00              SOURCE3            1
hn-n2-n1    67.7      114.10              SOURCE2            1
hn-n2-n2    69.0      105.01              SOURCE3           19    1.5183
hn-n2-ne    67.7      108.56              SOURCE3           29    5.5708
hn-n2-nf    67.7      108.56              SOURCE3           29
hn-n2-o     70.3      107.37              SOURCE3            1
hn-n2-p2    59.8      112.09              SOURCE3           18    4.0663
hn-n2-p4    55.6      111.33              SOURCE3            1
hn-n2-p5    57.5      122.34              SOURCE3            1
hn-n2-pe    62.6      111.41              SOURCE3           20    4.9895
hn-n2-pf    62.6      111.41              SOURCE3           20
hn-n2-s2    47.7      115.80              SOURCE2            1
hn-n2-s4    46.6      111.21              SOURCE3            1
hn-n2-s     49.4      108.17              SOURCE3            1
hn-n2-s6    48.4      111.17      SOURCE3_SOURCE5            7    0.7012
i -n2-n2    69.5      111.79              SOURCE3            1
i -n2-o     67.5      116.82              SOURCE3            1
i -n2-p2    77.6      113.26              SOURCE3            1
i -n2-s     59.6      116.85              SOURCE3            1
n1-n2-n1   122.8      112.00            HF/6-31G*            1
n2-n2-n1    95.4      180.00       dac_for_azides            0
n2-n2-n2   120.7      109.49              SOURCE3            2
n2-n2-n3   118.0      108.88              SOURCE3            1
n2-n2-n4   101.2      106.45              SOURCE3            1
n2-n2-na   114.3      112.23              SOURCE3            1
n2-n2-nh   115.3      111.70              SOURCE3            5    0.3475
n2-n2-no   114.1      105.97              SOURCE3            1
n2-n2-o    122.4      110.43              SOURCE3            1
n2-n2-oh   113.5      111.51              SOURCE3            1
n2-n2-os   114.6      108.38              SOURCE3            1
n2-n2-p2   114.9      109.15              SOURCE3            1
n2-n2-p3   104.2      113.05              SOURCE3            1
n2-n2-p4   103.8      118.77              SOURCE3            1
n2-n2-p5   114.5      110.46              SOURCE3            1
n2-n2-s4    90.1      107.30              SOURCE3            1
n2-n2-s6    90.9      111.25              SOURCE3            1
n2-n2-s     89.6      115.91              SOURCE3            1
n2-n2-sh    83.0      111.10              SOURCE3            1
n2-n2-ss    86.1      112.14              SOURCE3            1
n3-n2-n3   112.2      115.07              SOURCE3            1
n3-n2-o    117.2      114.00              SOURCE2            1
n3-n2-p2   110.5      115.34              SOURCE3            1
n3-n2-s     87.9      117.13              SOURCE3            1
n4-n2-n4    92.2      106.70              SOURCE3            1
n4-n2-o     99.1      112.20              SOURCE3            1
n4-n2-p2   101.4      113.07              SOURCE3            1
n4-n2-s     78.5      118.50              SOURCE3            1
na-n2-na   113.1      107.00              SOURCE3            1
na-n2-o    115.6      113.09              SOURCE3            1
na-n2-p2   107.8      119.16              SOURCE3            1
na-n2-s     86.7      118.26              SOURCE3            1
ne-n2-nh   114.3      113.34         CORR_SOURCE5           18    1.2157
ne-n2-o    122.3      110.31              SOURCE3            1
ne-n2-s     89.4      116.22              SOURCE3            1
nf-n2-nh   114.3      113.34         CORR_SOURCE5           18    1.2157
nf-n2-o    122.3      110.31              SOURCE3            1
nf-n2-s     89.4      116.22              SOURCE3            1
nh-n2-nh   107.4      121.20              SOURCE3            1
nh-n2-o    116.0      113.85      SOURCE4_SOURCE5           33    1.0590
nh-n2-p2   108.3      118.83              SOURCE3            2    0.1024
nh-n2-s     87.5      116.90              SOURCE3            2    0.2276
n -n2-n2   116.8      108.16      SOURCE4_SOURCE5           18    0.3340
n -n2-o    115.0      115.11      SOURCE4_SOURCE5           85    0.2779
no-n2-no   109.5      103.70              SOURCE3            1
no-n2-o    118.6      100.76              SOURCE3            1
no-n2-p2   109.5      111.95              SOURCE3            1
n -n2-p2   108.9      117.30              SOURCE3            1
n -n2-s     87.8      115.74              SOURCE3            1
oh-n2-oh   114.0      101.70              SOURCE3            1
oh-n2-p2   109.1      115.11              SOURCE3            1
oh-n2-s     87.0      116.08              SOURCE3            1
o -n2-o    122.3      115.37              SOURCE3            1
o -n2-oh   114.8      112.15              SOURCE2            2    1.4500
o -n2-os   115.1      110.35              SOURCE3            2    0.0042
o -n2-p2   112.2      116.08              SOURCE3            1
o -n2-p3   104.4      113.43              SOURCE3            1
o -n2-p4   108.0      110.61              SOURCE3            1
o -n2-p5   116.1      109.11              SOURCE3            1
o -n2-pe   107.8      134.56              SOURCE3            1
o -n2-pf   107.8      134.56              SOURCE3            1
o -n2-s4    90.1      108.91              SOURCE3            1
o -n2-s6    91.7      111.34              SOURCE3            1
o -n2-s     90.0      117.18              SOURCE3            1
o -n2-sh    81.9      114.98              SOURCE3            1
os-n2-os   108.7      110.29              SOURCE3            1
os-n2-p2   111.3      110.20              SOURCE3            1
o -n2-ss    85.3      115.77      SOURCE3_SOURCE5            7    0.2342
os-n2-s     88.2      112.23              SOURCE3            1
p2-n2-p2   113.2      116.80              SOURCE3            1
p2-n2-p3   104.0      124.48              SOURCE3            1
p2-n2-p4   103.8      128.37              SOURCE3            1
p2-n2-p5   110.3      123.47              SOURCE3            1
p2-n2-s4    89.9      112.10              SOURCE3            1
p2-n2-s6    90.0      115.70              SOURCE3            1
p2-n2-s     89.5      117.84              SOURCE3            1
p2-n2-sh    83.8      118.45              SOURCE3            1
p2-n2-ss    85.5      120.43              SOURCE3            1
p3-n2-p3   101.4      120.40              SOURCE3            1
p3-n2-s     83.4      120.86              SOURCE3            1
p4-n2-s     81.1      131.84              SOURCE3            1
p5-n2-p5   111.8      120.60              SOURCE3            1
p5-n2-s     88.9      119.89              SOURCE3            1
pe-n2-s     92.3      115.73              SOURCE3            1
pf-n2-s     92.3      115.73              SOURCE3            1
s4-n2-s4    67.8      119.18              SOURCE3            1
s4-n2-s6    69.0      119.18              SOURCE3            1
s6-n2-s6    70.3      119.18              SOURCE3            1
sh-n2-sh    61.6      123.93              SOURCE3            1
sh-n2-ss    63.0      123.93              SOURCE3            1
s -n2-s     70.4      120.88              SOURCE3            1
s -n2-s4    71.1      113.00              SOURCE3            1
s -n2-s6    70.4      119.61              SOURCE3            1
s -n2-sh    65.3      122.05              SOURCE3            1
s -n2-ss    68.4      118.19              SOURCE3            1
ss-n2-ss    64.7      123.93              SOURCE3            1
br-n3-br    67.1      107.15              SOURCE3            1
br-n3-c3    63.9      106.93              SOURCE3            2
c1-n3-c1    68.2      123.34              SOURCE3            1
c1-n3-f     91.9      104.70              SOURCE2            1
c1-n3-hn    50.2      114.78      SOURCE3_SOURCE5            7    0.4776
c1-n3-o     89.2      116.63              SOURCE3            1
c2-n3-c2    68.2      124.68              SOURCE3            1
c2-n3-hn    49.5      119.38              SOURCE3            1
c3-n3-c3    65.7      112.35      SOURCE3_SOURCE5        10425    1.3688
c3-n3-cl    72.0      107.23              SOURCE3            3    0.3673
c3-n3-cx    65.7      114.10               5/2017           13    0.8187
c3-n3-cy    65.7      112.88               5/2017           15    1.5846
c3-n3-f     88.8      103.13              SOURCE3            2
c3-n3-hn    47.8      109.29      SOURCE3_SOURCE5         6742    0.6614
c3-n3-i     60.4      108.48              SOURCE3            2
c3-n3-n2    83.5      118.75              SOURCE2            2    2.6500
c3-n3-n3    83.5      110.80      SOURCE3_SOURCE5           91    1.4698
c3-n3-n4    84.2      109.65              SOURCE3            3    0.1146
c3-n3-n     84.2      111.71      SOURCE4_SOURCE5          108    1.7154
c3-n3-nh    83.8      111.77      SOURCE4_SOURCE5           54    1.2232
c3-n3-no    82.4      116.93      SOURCE3_SOURCE5           25    0.8475
c3-n3-o     86.1      113.31              SOURCE3            5    8.9081
c3-n3-oh    85.9      106.49      SOURCE4_SOURCE5           51    1.1723
c3-n3-os    85.5      105.80      SOURCE4_SOURCE5           28    1.5996
c3-n3-p3    79.9      119.67      SOURCE3_SOURCE5           17    1.9089
c3-n3-p5    81.8      119.86      SOURCE4_SOURCE5          188    2.0452
c3-n3-s4    63.0      114.49      SOURCE3_SOURCE5            8    1.8120
c3-n3-s6    64.5      116.55      SOURCE4_SOURCE5          179    1.8765
c3-n3-s     63.3      110.02              SOURCE3            1
c3-n3-sh    63.9      112.70              SOURCE3            1
c3-n3-ss    63.3      116.25      SOURCE3_SOURCE5           14    1.9512
c3-n3-sy    64.3      115.25      SOURCE4_SOURCE5          250    1.7586
cl-n3-cl    80.4      108.28              SOURCE3            1
cl-n3-hn    48.3      104.39              SOURCE3            2
cl-n3-n3    90.4      107.65              SOURCE3            1
cx-n3-cx    89.0       60.73      SOURCE4_SOURCE5          147    0.2518
cx-n3-hn    48.3      109.96               5/2017           39    0.5645
cx-n3-p5    81.8      119.41      SOURCE4_SOURCE5          173    1.2386
cx-n3-py    80.3      121.75      SOURCE4_SOURCE5           20    1.0295
cy-n3-cy    66.4      110.98               5/2017            1
cy-n3-hn    47.8      110.26               5/2017           37    0.6694
f -n3-f    115.8      102.22              SOURCE2            4    0.7562
f -n3-hn    65.9       99.80              SOURCE2            1
hn-n3-hn    40.8      106.40      SOURCE3_SOURCE5         2019    0.9777
hn-n3-i     36.7      109.98              SOURCE3            2
hn-n3-n1    64.1      110.17            HF/6-31G*            1
hn-n3-n2    63.3      115.94              SOURCE3            1
hn-n3-n3    61.2      107.68      SOURCE3_SOURCE5          107    1.7630
hn-n3-n4    61.9      106.91      SOURCE3_SOURCE5           18    0.7068
hn-n3-n     62.5      108.12      SOURCE3_SOURCE5           90    1.1435
hn-n3-na    62.0      107.89              SOURCE3            1
hn-n3-nh    62.0      108.31      SOURCE3_SOURCE5           85    1.2609
hn-n3-no    63.8      104.78              SOURCE3            3    1.1126
hn-n3-o     65.1      113.32              SOURCE3            3    4.3945
hn-n3-oh    63.8      102.30      SOURCE3_SOURCE5           14    0.6850
hn-n3-os    62.7      102.75      SOURCE3_SOURCE5           43    0.6086
hn-n3-p2    55.4      120.26              SOURCE3            1
hn-n3-p3    54.0      116.89              SOURCE3            9    3.8816
hn-n3-p4    56.1      113.05              SOURCE3            2
hn-n3-p5    56.8      114.32      SOURCE3_SOURCE5           63    1.6600
hn-n3-s4    42.9      109.14      SOURCE3_SOURCE5           13    1.2903
hn-n3-s     41.8      109.47              SOURCE3            1
hn-n3-s6    45.1      109.60      SOURCE4_SOURCE5          234    1.2605
hn-n3-sh    43.4      108.67              SOURCE3            3    2.5025
hn-n3-ss    43.4      110.83      SOURCE3_SOURCE5           14    1.1613
hn-n3-sy    44.5      109.50      SOURCE4_SOURCE5          617    0.8005
i -n3-i     65.5      111.27              SOURCE3            1
n1-n3-n1   111.3      113.21            HF/6-31G*            1
n2-n3-n2   110.4      118.73              SOURCE3            1
n2-n3-o    113.4      114.91              SOURCE3            1
n3-n3-n3   107.9      105.71              SOURCE3            3    0.3561
n4-n3-n4   105.0      113.48              SOURCE3            1
n4-n3-nh   108.6      107.14              SOURCE3            1
na-n3-na   106.4      112.00              SOURCE3            1
nh-n3-nh   109.2      107.15              SOURCE3            1
n -n3-n    108.3      110.55              SOURCE3            1
no-n3-no   106.6      115.26              SOURCE3            1
oh-n3-oh   109.2      107.18              SOURCE3            1
o -n3-o    109.3      126.14              SOURCE3            1
o -n3-p2   106.9      117.02              SOURCE3            1
o -n3-p4   105.7      116.65              SOURCE3            1
o -n3-s4    81.0      114.09              SOURCE3            1
o -n3-s6    84.4      113.80              SOURCE3            1
o -n3-s     77.5      119.81              SOURCE3            1
os-n3-os   107.6      106.52              SOURCE3            1
p2-n3-p2   103.1      130.13              SOURCE3            1
p3-n3-p3   104.1      118.74              SOURCE3            3    3.3755
p4-n3-p4   107.3      116.35              SOURCE3            1
p5-n3-p5   107.6      119.42              SOURCE3            1
s4-n3-s4    62.0      120.02              SOURCE3            1
s4-n3-s6    63.2      120.95              SOURCE3            1
s6-n3-s6    65.5      118.54      SOURCE3_SOURCE5           18    1.1456
sh-n3-sh    62.9      118.63              SOURCE3            1
sh-n3-ss    62.9      119.67              SOURCE3            1
s -n3-s     58.0      131.36              SOURCE3            1
ss-n3-ss    63.2      119.57              SOURCE3            1
br-n4-br    65.7      114.82              SOURCE3            1
br-n4-hn    41.3      108.44              SOURCE3            7    0.5630
c1-n4-c1    67.5      113.87              SOURCE3            1
c1-n4-hn    49.0      110.19              SOURCE3            7    1.0847
c2-n4-c2    63.6      112.58              SOURCE3            1
c2-n4-c3    64.0      110.96              SOURCE4           13    2.4632
c2-n4-hn    46.1      110.37      SOURCE3_SOURCE5           39    1.1227
c3-n4-c3    64.5      109.66      SOURCE3_SOURCE5         2931    1.1695
c3-n4-ca    64.8      110.53      SOURCE4_SOURCE5          127    1.4968
c3-n4-cc    64.4      111.04      SOURCE4_SOURCE5           18    1.4876
c3-n4-cl    71.8      108.04              SOURCE3            3
c3-n4-hn    46.2      110.11              SOURCE3          100    1.3136
c3-n4-n3    83.6      107.70      SOURCE3_SOURCE5           11    1.5498
c3-n4-n4    79.8      114.07              SOURCE3            4
c3-n4-n     82.7      109.74      SOURCE4_SOURCE5           17    2.0520
c3-n4-nh    81.1      111.73              SOURCE3            1
c3-n4-no    81.8      109.08              SOURCE3            1
c3-n4-o     84.1      110.52      SOURCE3_SOURCE5            7    0.8910
c3-n4-oh    82.0      113.73              SOURCE3            1
c3-n4-os    83.9      107.42              SOURCE3            3    3.5920
c3-n4-p2    74.9      112.52              SOURCE3            1
c3-n4-p3    77.5      110.73              SOURCE3            3    2.1084
c3-n4-p5    78.2      113.22              SOURCE3            3    0.4021
c3-n4-s4    58.8      108.23              SOURCE3            3    0.4195
c3-n4-s6    59.3      111.56              SOURCE3            3    1.8851
c3-n4-s     60.8      113.55              SOURCE3            1
c3-n4-sh    60.7      115.81              SOURCE3            1
c3-n4-ss    61.2      113.68              SOURCE3            3    1.1405
ca-n4-ca    64.2      114.48              SOURCE3            1
ca-n4-hn    46.9      110.50      SOURCE3_SOURCE5           23    1.4863
c -n4-c     63.3      108.61              SOURCE3            1
c -n4-hn    45.0      111.12      SOURCE3_SOURCE5           17    0.9627
cl-n4-cl    79.1      114.91              SOURCE3            1
cl-n4-hn    48.1      108.87              SOURCE3            7    0.7719
f -n4-f    120.5      109.05              SOURCE3            1
f -n4-hn    67.1      108.39              SOURCE3            4
hn-n4-hn    40.0      108.30      SOURCE3_SOURCE5          588    1.8224
hn-n4-i     37.8      108.72              SOURCE3            7    1.2717
hn-n4-n1    63.8      109.39            HF/6-31G*            1
hn-n4-n2    52.1      109.68              SOURCE3           19    0.6266
hn-n4-n3    60.8      110.40              SOURCE3           11    0.7307
hn-n4-n4    59.2      108.66              SOURCE3           18    1.2967
hn-n4-n     61.1      109.08              SOURCE3           13    1.6047
hn-n4-na    61.0      109.09      SOURCE3_SOURCE5           31    1.0459
hn-n4-nh    59.6      109.92              SOURCE3           12    0.7304
hn-n4-no    60.6      104.38              SOURCE3            2
hn-n4-o     63.2      111.35      SOURCE3_SOURCE5           11    1.4866
hn-n4-oh    62.6      108.09              SOURCE3            6    1.6728
hn-n4-os    61.4      109.39              SOURCE3           10    1.4403
hn-n4-p2    48.7      110.50              SOURCE3           25    1.0664
hn-n4-p3    50.7      109.89              SOURCE3           10    2.3870
hn-n4-p4    48.6      111.33              SOURCE3            3
hn-n4-p5    52.3      110.00              SOURCE3           10    1.0282
hn-n4-py    48.3      117.89              SOURCE3            8
hn-n4-s4    37.3      110.10              SOURCE3            6    0.8471
hn-n4-s     41.3      106.89              SOURCE3            6    1.0775
hn-n4-s6    38.9      108.94              SOURCE3           10    0.5715
hn-n4-sh    41.5      108.56              SOURCE3            6    0.8535
hn-n4-ss    41.4      109.17              SOURCE3           10    0.8455
i -n4-i     64.3      118.49              SOURCE3            1
n1-n4-n1   111.8      110.67            HF/6-31G*            1
n2-n4-n2    91.4      108.64              SOURCE3            1
n3-n4-n3   106.1      111.07              SOURCE3            1
n4-n4-n4   100.3      115.49              SOURCE3            1
na-n4-na   101.9      119.60              SOURCE3            1
nh-n4-nh   104.3      109.38              SOURCE3            1
n -n4-n    102.6      118.62              SOURCE3            1
oh-n4-oh   109.8      108.19              SOURCE3            1
o -n4-o    106.8      120.97              SOURCE3            1
os-n4-os   110.2      104.40              SOURCE3            1
p2-n4-p2    94.7      113.91              SOURCE3            2
p3-n4-p3    94.8      121.38              SOURCE3            1
p5-n4-p5   103.7      107.02              SOURCE3            1
py-n4-py   123.6       69.79              SOURCE3            2
s4-n4-s4    56.3      115.43              SOURCE3            1
s6-n4-s6    59.5      109.51              SOURCE3            1
sh-n4-sh    62.0      112.59              SOURCE3            1
s -n4-s     58.3      124.55              SOURCE3            1
ss-n4-ss    63.0      109.20              SOURCE3            1
br-na-br    61.1      123.00              SOURCE3            1
br-na-c2    64.8      100.48              SOURCE3            2    1.0536
br-na-ca    58.2      124.81              SOURCE3            1
br-na-cc    58.2      124.62              SOURCE3            3    0.5348
br-na-cd    58.2      124.62              SOURCE3            3
br-na-nc    74.5      119.42              SOURCE3            4    1.6703
br-na-nd    74.5      119.42              SOURCE3            4
br-na-os    79.2      104.99              SOURCE3            1
br-na-p2    78.4      121.01              SOURCE3            1
br-na-pc    78.9      120.26              SOURCE3            3    2.1456
br-na-pd    78.9      120.26              SOURCE3            3
br-na-ss    63.6      112.28              SOURCE3            1
c1-na-c1    69.2      117.20              SOURCE3            1
c1-na-c2    65.9      125.20              SOURCE3            1
c1-na-ca    67.6      120.57              SOURCE3            1
c1-na-cc    67.5      121.35              SOURCE3            6    0.6517
c1-na-cd    67.5      121.35              SOURCE3            6    0.6517
c1-na-nc    85.7      120.24              SOURCE3            4    1.6849
c1-na-nd    85.8      120.24              SOURCE3            4
c1-na-os    87.9      106.96              SOURCE3            2
c1-na-p2    79.8      122.25              SOURCE3            1
c1-na-pc    80.7      121.48              SOURCE3            3    2.1681
c1-na-pd    80.7      121.48              SOURCE3            3
c1-na-ss    63.7      118.30              SOURCE3            1
c2-na-c2    69.3      110.37              SOURCE3            6    0.5121
c2-na-c3    65.7      117.20              SOURCE3            2
c2-na-ca    65.5      124.97      SOURCE4_SOURCE5           19    0.9360
c2-na-cc    65.2      126.55      SOURCE3_SOURCE5           47    1.6996
c2-na-cd    65.2      126.55      SOURCE3_SOURCE5           47    1.6996
c2-na-cl    73.0      101.01              SOURCE3            2    1.5799
c2-na-f     90.7      103.11              SOURCE3            1
c2-na-hn    47.7      119.28              SOURCE3           14    6.6027
c2-na-i     62.5      106.74              SOURCE3            1
c2-na-n1    83.0      124.81            HF/6-31G*            1
c2-na-n2    82.5      125.00              SOURCE3            1
c2-na-n3    81.0      124.80              SOURCE3            1
c2-na-n4    81.7      121.32              SOURCE3            1
c2-na-n     81.4      124.70              SOURCE3            1
c2-na-na    81.7      124.60              SOURCE3            1
c2-na-nc    84.2      120.80         CORR_SOURCE5            5    1.0225
c2-na-nd    84.3      120.80         CORR_SOURCE5            5    1.0225
c2-na-nh    81.6      124.98              SOURCE3            1
c2-na-no    80.8      124.20              SOURCE3            1
c2-na-o     85.6      125.90              SOURCE3            1
c2-na-oh    82.1      123.90              SOURCE3            1
c2-na-os    85.4      110.33              SOURCE3            4    3.2172
c2-na-p2    79.3      122.14              SOURCE3            1
c2-na-p3    77.6      126.10              SOURCE3            1
c2-na-p4    84.8      125.00              SOURCE3            1
c2-na-p5    79.6      125.10              SOURCE3            1
c2-na-pc    80.1      121.56              SOURCE3            3    1.6252
c2-na-pd    80.1      121.56              SOURCE3            3
c2-na-s4    59.9      124.90              SOURCE3            1
c2-na-s6    62.0      124.40              SOURCE3            1
c2-na-s     60.5      125.80              SOURCE3            1
c2-na-sh    61.8      125.10              SOURCE3            1
c2-na-ss    64.0      115.53              SOURCE3            5    1.4036
c3-na-c3    62.2      125.59              SOURCE3            1
c3-na-ca    64.2      124.36              SOURCE3            5    4.2557
c3-na-cc    63.7      126.46      SOURCE3_SOURCE5         2025    1.8293
c3-na-cd    63.7      126.46      SOURCE3_SOURCE5         2025    1.8293
c3-na-cp    65.4      119.62      SOURCE4_SOURCE5           17    0.4924
c3-na-n2    82.5      119.24      SOURCE4_SOURCE5           15    0.8410
c3-na-n     83.7      112.88      SOURCE4_SOURCE5           34    0.6363
c3-na-nc    82.4      120.18      SOURCE3_SOURCE5          266    0.9487
c3-na-nd    82.5      120.18      SOURCE3_SOURCE5          266    0.9487
c3-na-os    86.0      104.39              SOURCE3            3    1.2017
c3-na-p2    78.2      123.12              SOURCE3            1
c3-na-pc    79.0      122.11              SOURCE3            3    2.8504
c3-na-pd    79.0      122.11              SOURCE3            3
c3-na-sh    65.1      110.28              SOURCE3            1
c3-na-ss    64.6      110.87              SOURCE3            3    0.8260
ca-na-ca    67.3      120.05      SOURCE4_SOURCE5          899    1.7177
ca-na-cc    69.4      113.15              SOURCE3           18    9.8644
ca-na-cd    69.4      113.15              SOURCE3           18    9.8644
ca-na-cl    65.8      124.79              SOURCE3            1
ca-na-cp    67.0      120.86      SOURCE4_SOURCE5           58    1.3836
ca-na-cx    64.1      124.74               5/2017           39    1.7411
ca-na-f     85.9      116.40              SOURCE3            1
ca-na-hn    47.0      125.54      SOURCE4_SOURCE5         1396    1.1217
ca-na-i     58.5      121.62              SOURCE3            1
ca-na-n2    85.1      119.07      SOURCE4_SOURCE5           19    2.0667
ca-na-n4    82.6      120.19              SOURCE3            1
ca-na-n     82.8      122.00              SOURCE3            1
ca-na-na    82.4      123.76              SOURCE3            1
ca-na-nb    84.4      122.64      SOURCE4_SOURCE5           30    1.1363
ca-na-nc    85.9      117.85              SOURCE3            6    3.6536
ca-na-nd    85.9      117.85              SOURCE3            6
ca-na-nh    82.3      124.41      SOURCE4_SOURCE5           15    1.3695
ca-na-o     88.3      120.17      SOURCE4_SOURCE5          161    1.3927
ca-na-oh    84.0      120.05      SOURCE3_SOURCE5            6    2.2969
ca-na-os    86.3      109.46              SOURCE3            1
ca-na-p2    78.4      125.85              SOURCE3            1
ca-na-p3    78.4      124.38              SOURCE3            1
ca-na-p4    85.2      124.97              SOURCE3            1
ca-na-p5    80.4      123.30              SOURCE3            1
ca-na-pc    80.2      122.13              SOURCE3            3    2.2393
ca-na-pd    80.2      122.13              SOURCE3            3
ca-na-py    75.3      140.88              SOURCE3            2
ca-na-s4    62.0      117.23              SOURCE3            1
ca-na-s6    63.1      120.69              SOURCE3            1
ca-na-s     60.7      125.64              SOURCE3            1
ca-na-sh    61.9      125.44              SOURCE3            1
ca-na-ss    60.5      129.92      SOURCE4_SOURCE5           17    0.1432
cc-na-cc    70.5      109.90              SOURCE3          109    1.5547
cc-na-cd    65.3      128.01              SOURCE3            1
cc-na-ce    64.7      126.61      SOURCE4_SOURCE5           16    0.5158
cc-na-cl    65.9      124.61              SOURCE3            3    0.5208
cc-na-f     85.4      118.03              SOURCE3            4    0.3081
cc-na-hn    47.1      125.50         CORR_SOURCE5         1758    1.2247
cc-na-i     57.6      125.70              SOURCE3            6    0.7821
cc-na-n2    84.5      121.09      SOURCE3_SOURCE5           21    1.2340
cc-na-n4    82.5      120.91      SOURCE3_SOURCE5           16    2.5151
cc-na-n     87.3      110.05      SOURCE3_SOURCE5           63    1.0193
cc-na-na    84.8      117.36      SOURCE3_SOURCE5           38    0.6452
cc-na-nc    88.1      112.36      SOURCE3_SOURCE5          209    2.0210
cc-na-nd    83.1      126.23         CORR_SOURCE5          157    1.3576
cc-na-nh    82.6      123.59      SOURCE3_SOURCE5           33    0.7437
cc-na-no    81.6      123.44      SOURCE3_SOURCE5           15    0.5273
cc-na-o     86.6      125.21              SOURCE3           10    0.0124
cc-na-oh    83.3      122.38              SOURCE3           10    0.1570
cc-na-os    83.6      116.86                 CORR           48
cc-na-p2    78.4      125.86              SOURCE3           14    2.2993
cc-na-p3    78.1      125.25              SOURCE3            8    0.1998
cc-na-p4    84.4      127.73              SOURCE3            7    3.6077
cc-na-p5    80.0      124.70              SOURCE3           13    1.4225
cc-na-s4    61.1      121.03              SOURCE3           10    0.5589
cc-na-s6    62.4      123.55      SOURCE3_SOURCE5           18    0.8360
cc-na-s     60.7      125.66              SOURCE3            8    0.1880
cc-na-sh    62.3      123.96              SOURCE3           10    0.3424
cc-na-ss    62.7      121.13         CORR_SOURCE5           13    0.6360
cd-na-cd    70.5      109.90              SOURCE3          109    1.5547
cd-na-cl    65.9      124.61              SOURCE3            3
cd-na-f     85.4      118.03              SOURCE3            4    0.3081
cd-na-hn    47.1      125.50         CORR_SOURCE5         1758    1.2247
cd-na-i     57.6      125.70              SOURCE3            6    0.7821
cd-na-n2    84.5      121.09      SOURCE3_SOURCE5           21    1.2340
cd-na-n4    82.5      120.91      SOURCE3_SOURCE5           16    2.5151
cd-na-n     87.3      110.05      SOURCE3_SOURCE5           63    1.0193
cd-na-na    84.8      117.36      SOURCE3_SOURCE5           38    0.6452
cd-na-nc    83.1      126.23         CORR_SOURCE5          157    1.3576
cd-na-nd    88.1      112.36      SOURCE3_SOURCE5          209    2.0210
cd-na-nh    82.6      123.64      SOURCE3_SOURCE5           34    0.8283
cd-na-no    81.6      123.44      SOURCE3_SOURCE5           15    0.5273
cd-na-o     86.6      125.21              SOURCE3           10    0.0124
cd-na-oh    83.3      122.38              SOURCE3           10    0.1570
cd-na-os    83.6      116.86                 CORR           48
cd-na-p2    78.4      125.86              SOURCE3           14    2.2993
cd-na-p3    78.1      125.25              SOURCE3            8    0.1998
cd-na-p4    84.4      127.73              SOURCE3            7
cd-na-p5    80.0      124.70              SOURCE3           13    1.4225
cd-na-s4    61.1      121.03              SOURCE3           10    0.5589
cd-na-s6    62.4      123.55      SOURCE3_SOURCE5           18    0.8360
cd-na-s     60.7      125.66              SOURCE3            8    0.1880
cd-na-sh    62.3      123.96              SOURCE3           10    0.3424
cd-na-ss    62.7      121.13         CORR_SOURCE5           13    0.6360
cl-na-cl    73.1      122.80              SOURCE3            1
cl-na-nc    84.6      119.36              SOURCE3            4    1.7128
cl-na-nd    84.6      119.36              SOURCE3            4
cl-na-os    88.5      106.58              SOURCE3            1
cl-na-p2    86.5      121.29              SOURCE3            1
cl-na-pc    87.1      120.51              SOURCE3            3    2.1985
cl-na-pd    87.1      120.51              SOURCE3            3
cl-na-ss    70.4      111.91              SOURCE3            1
f -na-f    106.4      120.20              SOURCE3            1
f -na-nc   107.9      118.05              SOURCE3            4    1.7931
f -na-nd   107.9      118.05              SOURCE3            4
f -na-os   111.5      103.86              SOURCE3            1
f -na-p2   101.5      119.95              SOURCE3            1
f -na-pc   102.6      119.10              SOURCE3            3    2.3967
f -na-pd   102.6      119.10              SOURCE3            3
f -na-ss    84.0      108.01              SOURCE3            1
hn-na-hn    39.3      116.80              SOURCE3            1
hn-na-n     61.5      111.44      SOURCE4_SOURCE5           14    1.2883
hn-na-nc    61.4      119.55      SOURCE3_SOURCE5          196    1.0024
hn-na-nd    61.4      119.55      SOURCE3_SOURCE5          196    1.0024
hn-na-os    62.8      102.12      SOURCE3_SOURCE5           20    2.5614
hn-na-p2    52.1      122.52              SOURCE3            1
hn-na-pc    52.9      121.48              SOURCE3            3    2.9355
hn-na-pd    52.9      121.48              SOURCE3            3
hn-na-ss    42.5      113.95              SOURCE3            1
i -na-i     63.6      124.20              SOURCE3            1
i -na-nc    73.7      120.03              SOURCE3            4    2.0032
i -na-nd    73.7      120.03              SOURCE3            4
i -na-os    77.1      109.91              SOURCE3            1
i -na-p2    78.7      122.28              SOURCE3            1
i -na-pc    79.2      121.40              SOURCE3            3    2.4763
i -na-pd    79.2      121.40              SOURCE3            3
i -na-ss    62.5      118.40              SOURCE3            1
n2-na-n2   108.3      116.71              SOURCE3            1
n2-na-nc   107.2      119.96              SOURCE3            4    4.5041
n2-na-nd   107.3      119.96              SOURCE3            4
n2-na-os   107.6      111.53              SOURCE3            1
n2-na-p2    98.8      124.88              SOURCE3            1
n2-na-pc   100.2      123.18              SOURCE3            3    4.7947
n2-na-pd   100.2      123.18              SOURCE3            3
n2-na-ss    77.6      124.64              SOURCE3            1
n3-na-n3   101.2      124.00              SOURCE3            1
n4-na-n4   105.5      111.70              SOURCE3            1
n4-na-nc   106.1      116.44              SOURCE3            4    3.6604
n4-na-nd   106.1      116.44              SOURCE3            4
n4-na-os   109.5      102.97              SOURCE3            1
n4-na-p2    98.2      123.56              SOURCE3            1
n4-na-pc    99.6      121.98              SOURCE3            3    4.4884
n4-na-pd    99.6      121.98              SOURCE3            3
na-na-na   102.7      123.60              SOURCE3            1
na-na-nc   106.0      119.64              SOURCE3            4    1.6920
na-na-nd   106.1      119.64              SOURCE3            4
na-na-os   107.4      109.47              SOURCE3            1
na-na-p2    99.5      121.72              SOURCE3            1
na-na-pc   100.6      120.91              SOURCE3            3    2.3033
na-na-pd   100.6      120.91              SOURCE3            3
na-na-ss    79.8      116.50              SOURCE3            1
nc-na-nc   109.4      116.30      SOURCE3_SOURCE5           57    1.3191
nc-na-nd   106.5      122.76      SOURCE4_SOURCE5           12    0.1496
nc-na-nh   105.7      120.55              SOURCE3            8    1.1436
nc-na-no   104.8      119.21      SOURCE3_SOURCE5            9    1.2751
nc-na-o    110.8      122.79              SOURCE3            6    1.3154
nc-na-oh   106.6      119.22              SOURCE3            4    1.7201
nc-na-os   104.2      119.65              SOURCE3            4    1.5019
nc-na-p2   100.9      119.99              SOURCE3            4    3.6009
nc-na-p3   100.3      120.07              SOURCE3            4    3.7188
nc-na-p4   109.8      119.77              SOURCE3            3    0.3747
nc-na-p5   103.0      118.95              SOURCE3            4    3.1194
nc-na-pc   102.3      118.66              SOURCE3           27    1.5082
nc-na-s4    77.3      119.20              SOURCE3            4    2.3841
nc-na-s6    79.8      119.24              SOURCE3            4    2.2262
nc-na-s     77.3      122.26              SOURCE3            4    0.9173
nc-na-sh    79.5      120.50              SOURCE3            4    1.5016
nc-na-ss    79.1      120.50              SOURCE3            4    1.5615
nd-na-nd   109.5      116.30      SOURCE3_SOURCE5           57    1.3191
nd-na-nh   105.7      120.55              SOURCE3            8
nd-na-no   104.9      119.21      SOURCE3_SOURCE5            5    1.0113
nd-na-o    110.9      122.79              SOURCE3            6
nd-na-oh   106.6      119.22              SOURCE3            4
nd-na-os   104.3      119.65              SOURCE3            4
nd-na-p2   100.9      119.99              SOURCE3            4
nd-na-p3   100.3      120.07              SOURCE3            4
nd-na-p4   109.8      119.77              SOURCE3            3
nd-na-p5   103.0      118.95              SOURCE3            4
nd-na-pd   102.3      118.66              SOURCE3           27
nd-na-s4    77.3      119.20              SOURCE3            4
nd-na-s6    79.9      119.24              SOURCE3            4
nd-na-s     77.3      122.26              SOURCE3            4
nd-na-sh    79.5      120.50              SOURCE3            4
nd-na-ss    79.1      120.50              SOURCE3            4
nh-na-nh   102.8      123.60              SOURCE3            1
nh-na-os   106.5      111.37              SOURCE3            1
nh-na-p2    99.9      120.86              SOURCE3            1
nh-na-pc   100.8      120.38              SOURCE3            6    1.3513
nh-na-pd   100.8      120.38              SOURCE3            6
nh-na-ss    81.3      112.35              SOURCE3            2    5.2951
n -na-n    102.2      123.80              SOURCE3            1
n -na-nc   105.7      119.85              SOURCE3            4    1.6156
n -na-nd   105.7      119.85              SOURCE3            4
no-na-no   100.6      122.80              SOURCE3            1
no-na-os   107.7      106.55              SOURCE3            1
no-na-pc   100.3      120.11              SOURCE3            3    2.0821
no-na-pd   100.3      120.11              SOURCE3            3
n -na-os   109.6      104.71              SOURCE3            1
no-na-ss    79.9      114.95              SOURCE3            1
n -na-p2    99.6      121.35              SOURCE3            1
n -na-pc   100.6      120.64              SOURCE3            3    2.0168
n -na-pd   100.6      120.64              SOURCE3            3
n -na-ss    79.9      116.10              SOURCE3            1
oh-na-oh   103.9      122.20              SOURCE3            1
oh-na-p2   100.0      120.76              SOURCE3            1
oh-na-pc   101.1      119.99              SOURCE3            3    2.1734
oh-na-pd   101.1      119.99              SOURCE3            3
oh-na-ss    81.2      113.04              SOURCE3            1
o -na-o    114.9      126.20              SOURCE3            1
o -na-os   108.1      118.78      SOURCE3_SOURCE5            6    0.4047
o -na-p2   101.0      122.80              SOURCE3            1
o -na-pc   102.1      122.34              SOURCE3            3    1.2908
o -na-pd   102.1      122.34              SOURCE3            3
os-na-os   108.4      104.45              SOURCE3            2    0.0983
os-na-p2   100.4      117.86              SOURCE3            1
os-na-p3   105.9      104.70              SOURCE3            1
os-na-p5   104.7      111.41              SOURCE3            1
os-na-pc   100.2      119.91              SOURCE3            3    1.9002
os-na-pd   100.2      119.91              SOURCE3            3
os-na-s4    81.0      105.88              SOURCE3            2
os-na-s6    81.1      112.00              SOURCE3            2
os-na-ss    81.7      109.64              SOURCE3            3    4.1395
p2-na-p2   102.1      120.91              SOURCE3            1
p2-na-p3   100.1      124.80              SOURCE3            1
p2-na-p5   101.8      123.99              SOURCE3            1
p2-na-pc   102.7      120.72              SOURCE3            3    0.2407
p2-na-pd   102.7      120.72              SOURCE3            3
p2-na-s4    78.0      122.47              SOURCE3            1
p2-na-s6    79.6      122.50              SOURCE3            1
p2-na-s     78.9      121.85              SOURCE3            1
p2-na-sh    79.9      121.75              SOURCE3            1
p2-na-ss    79.6      121.88              SOURCE3            1
p3-na-p3    99.0      126.60              SOURCE3            1
p3-na-pc   101.2      123.32              SOURCE3            3    4.1781
p3-na-pd   101.2      123.32              SOURCE3            3
p5-na-p5   102.6      124.60              SOURCE3            1
p5-na-pc   102.8      122.69              SOURCE3            3    3.6738
p5-na-pd   102.8      122.69              SOURCE3            3
p5-na-ss    81.5      118.52              SOURCE3            1
pc-na-pc   103.1      120.78              SOURCE3           27    1.6457
pc-na-s4    78.7      121.51              SOURCE3            3    2.7242
pc-na-s6    80.3      121.55              SOURCE3            3    2.7065
pc-na-s     79.4      121.47              SOURCE3            3    1.0668
pc-na-sh    80.5      121.08              SOURCE3            3    1.8942
pc-na-ss    80.2      121.20              SOURCE3            3    1.9295
pd-na-pd   103.1      120.78              SOURCE3           27
pd-na-s4    78.7      121.51              SOURCE3            3
pd-na-s6    80.3      121.55              SOURCE3            3
pd-na-s     79.4      121.47              SOURCE3            3
pd-na-sh    80.5      121.08              SOURCE3            3
pd-na-ss    80.2      121.20              SOURCE3            3
py-na-py   129.6       78.25              SOURCE3            1
s4-na-s4    59.7      124.20              SOURCE3            1
s4-na-s6    63.8      112.86              SOURCE3            1
s4-na-ss    63.9      111.92              SOURCE3            1
s6-na-s6    62.3      123.20              SOURCE3            1
s6-na-ss    63.2      119.10              SOURCE3            1
sh-na-sh    62.1      124.60              SOURCE3            1
sh-na-ss    63.3      118.79              SOURCE3            1
s -na-s     60.2      126.00              SOURCE3            1
s -na-ss    64.3      112.49              SOURCE3            1
ss-na-ss    64.7      113.24              SOURCE3            2    6.6084
sy-na-sy    62.2      123.20              SOURCE3            1
ca-nb-ca    70.4      117.22      SOURCE3_SOURCE5         3343    1.0306
ca-nb-cp    70.1      118.05      SOURCE4_SOURCE5          160    0.7542
ca-nb-cq    70.1      118.05      SOURCE4_SOURCE5          102    0.7384
ca-nb-nb    87.2      120.05      SOURCE3_SOURCE5          159    0.6095
cp-nb-nb    86.9      120.96      SOURCE4_SOURCE5           32    0.5601
nb-nb-nb   109.0      121.04              SOURCE3            1
br-n -br    67.2      116.20              SOURCE3            1
br-n -c     62.7      121.25      SOURCE3_SOURCE5           10    1.6266
br-n -ca    63.3      118.19              SOURCE3            1
br-n -cc    63.5      118.19              SOURCE3            1
br-n -cd    63.5      118.19              SOURCE3            1
c1-n -c1    75.7      102.69              SOURCE3            1
c1-n -ca    68.1      118.88              SOURCE3            1
c1-n -cc    69.0      118.88              SOURCE3            1
c1-n -cd    69.0      118.88              SOURCE3            1
c2-n -c2    67.5      116.75              SOURCE3            1
c2-n -c3    65.0      120.10      SOURCE4_SOURCE5           62    2.3796
c2-n -ca    67.2      116.54              SOURCE3            1
c2-n -cc    68.0      116.54              SOURCE3            1
c2-n -cd    68.0      116.54              SOURCE3            1
c2-n -hn    48.0      117.90      SOURCE4_SOURCE5          115    1.4688
c3-n -c3    64.9      115.64      SOURCE4_SOURCE5         1017    2.0256
c3-n -ca    64.8      119.83      SOURCE4_SOURCE5          448    1.9961
c3-n -cc    65.2      120.85         CORR_SOURCE5          523    1.4176
c3-n -cd    65.2      120.85         CORR_SOURCE5          523    1.4176
c3-n -cy    66.1      113.44               5/2017            9    3.2919
c3-n -hn    46.1      117.68      SOURCE3_SOURCE5         1934    1.5065
c3-n -n2    81.8      121.71      SOURCE4_SOURCE5          131    1.2251
c3-n -n     82.9      115.39      SOURCE4_SOURCE5           28    1.0963
c3-n -nc    84.1      115.28         CORR_SOURCE5           61    0.8561
c3-n -nd    84.1      115.28         CORR_SOURCE5           61    0.8561
c3-n -oh    83.7      112.97      SOURCE4_SOURCE5           82    0.8203
c3-n -os    83.8      112.54      SOURCE4_SOURCE5           42    1.7642
c3-n -sy    62.3      120.88      SOURCE4_SOURCE5           13    1.1569
ca-n -ca    66.7      117.37      SOURCE4_SOURCE5           99    1.5139
ca-n -cc    68.4      114.01         CORR_SOURCE5           53    1.0051
ca-n -cd    68.4      114.01         CORR_SOURCE5           53    1.0051
ca-n -cl    71.2      117.72              SOURCE3            1
ca-n -f     86.0      114.92              SOURCE3            1
ca-n -hn    48.0      116.00      SOURCE4_SOURCE5         1451    1.8612
ca-n -i     60.0      119.30              SOURCE3            1
ca-n -n2    83.4      122.02      SOURCE4_SOURCE5           12    0.9977
ca-n -n4    81.0      122.98              SOURCE3            1
ca-n -n     83.3      118.55      SOURCE4_SOURCE5           46    0.3283
ca-n -na    83.0      119.30      SOURCE4_SOURCE5           47    0.3131
ca-n -nc    85.3      116.50         CORR_SOURCE5           14    1.6910
ca-n -nd    85.3      116.50         CORR_SOURCE5           14    1.6910
ca-n -nh    84.1      116.45              SOURCE3            1
ca-n -p2    83.2      112.32              SOURCE3            1
ca-n -p3    77.5      125.11              SOURCE3            1
ca-n -s4    62.2      118.40              SOURCE3            1
ca-n -s6    63.8      117.32              SOURCE3            1
ca-n -ss    63.8      116.60              SOURCE3            1
c -n -c1    69.6      117.04              SOURCE3            1
c -n -c2    66.4      122.15              SOURCE3            9    5.1016
c -n -c3    65.3      120.69      SOURCE3_SOURCE5         4556    2.1510
c3-nc-cd    69.9      109.51              SOURCE3            9    5.4142
c -n -c     65.6      127.08      SOURCE4_SOURCE5         1415    2.1363
c -n -ca    65.7      123.71              SOURCE3           10    3.8159
ca-nc-ca    72.0      109.95              SOURCE3            1
ca-nc-cd    74.6      104.88         CORR_SOURCE5          766    1.8814
ca-nc-n     92.1      104.69                 CORR            2
ca-nc-na    93.1      102.76         CORR_SOURCE5           25    0.7558
ca-nc-os    90.7      104.48         CORR_SOURCE5           16    0.1832
ca-nc-ss    70.4      107.07      SOURCE3_SOURCE5           17    0.3771
c -n -cc    66.6      123.27      SOURCE3_SOURCE5          805    2.2636
c -nc-ca    67.8      120.66                 CORR            2
cc-n -cc    70.8      108.92              SOURCE3           11    0.3167
cc-nc-cc    73.1      103.76         CORR_SOURCE5            6    0.0439
cc-nc-cd    73.9      105.49         CORR_SOURCE5         1810    1.9032
c -nc-cd    68.6      120.49         CORR_SOURCE5          205    1.1318
cc-n -cl    71.6      117.72              SOURCE3            1
cc-nc-na    92.4      102.97              SOURCE3            1
cc-nc-nd    91.7      108.62      SOURCE3_SOURCE5           82    1.5614
c -n -cd    66.6      123.27      SOURCE3_SOURCE5          805    2.2636
cd-nc-cd    71.5      117.30         CORR_SOURCE5           18    0.3907
cd-nc-n     88.1      117.19                 CORR           64
cd-nc-na    93.8      103.82      SOURCE3_SOURCE5          919    1.7445
cd-nc-nc    91.7      107.82         CORR_SOURCE5          457    1.5268
cd-nc-os    91.7      104.67         CORR_SOURCE5          184    0.8204
cd-nc-ss    70.5      108.07         CORR_SOURCE5           95    1.3804
c -n -ce    63.5      131.38      SOURCE4_SOURCE5          371    1.5975
cc-n -f     87.0      114.92              SOURCE3            1
cc-n -hn    48.3      119.26         CORR_SOURCE5          459    1.7223
cc-n -i     60.0      119.30              SOURCE3            1
c -n -cl    72.0      116.35              SOURCE4           11    0.6829
cc-n -n2    88.5      110.87              SOURCE3            1
cc-n -n     83.2      121.37              SOURCE3            1
cc-n -na    84.5      117.57              SOURCE3            1
cc-n -nc    88.1      111.89         CORR_SOURCE5           20    0.7095
cc-n -nh    84.7      117.52              SOURCE3            1
cc-n -no    83.5      115.92              SOURCE3            1
cc-n -o     88.2      120.54              SOURCE3            1
cc-n -oh    83.9      119.30      SOURCE3_SOURCE5            7    0.3237
cc-n -os    85.2      115.56              SOURCE3            1
cc-n -p2    83.6      112.32              SOURCE3            1
cc-n -p3    77.9      125.11              SOURCE3            1
cc-n -p5    81.1      121.00              SOURCE3            1
cc-n -s4    62.4      118.40              SOURCE3            1
cc-n -s6    64.2      117.32              SOURCE3            1
cc-n -s     62.5      118.29              SOURCE3            1
cc-n -sh    63.4      119.13              SOURCE3            1
cc-n -ss    64.1      116.60              SOURCE3            2
c -n -cx    65.6      122.15               5/2017           13    1.4081
c -n -cy    65.7      121.71               5/2017          100    0.9993
cd-n -cd    70.8      108.92              SOURCE3           11
cd-n -cl    71.6      117.72              SOURCE3            1
cd-n -f     87.0      114.92              SOURCE3            1
cd-n -hn    48.3      119.26         CORR_SOURCE5          459    1.7223
cd-n -i     60.0      119.30              SOURCE3            1
cd-n -n2    88.5      110.87              SOURCE3            1
cd-n -n     83.2      121.37              SOURCE3            1
cd-n -na    84.5      117.57              SOURCE3            1
cd-n -nd    88.1      111.89         CORR_SOURCE5           20    0.7095
cd-n -nh    84.7      117.52              SOURCE3            1
cd-n -no    83.5      115.92              SOURCE3            1
cd-n -o     88.2      120.54              SOURCE3            1
cd-n -oh    83.9      119.30      SOURCE3_SOURCE5            7    0.3237
cd-n -os    85.2      115.56              SOURCE3            1
cd-n -p2    83.6      112.32              SOURCE3            1
cd-n -p3    77.9      125.11              SOURCE3            1
cd-n -p5    81.1      121.00              SOURCE3            1
cd-n -s4    62.4      118.40              SOURCE3            1
cd-n -s6    64.2      117.32              SOURCE3            1
cd-n -s     62.5      118.29              SOURCE3            1
cd-n -sh    63.4      119.13              SOURCE3            1
cd-n -ss    64.1      116.60              SOURCE3            2    1.8318
ce-n -cy    66.7      111.71         CORR_SOURCE5          226    2.0477
c -n -f     89.6      108.63              SOURCE3            3    4.6785
cf-n -cy    66.7      111.71         CORR_SOURCE5          226    2.0477
c -n -hn    48.7      117.55      SOURCE3_SOURCE5         5866    1.6058
c -n -i     59.7      120.38              SOURCE3            5    2.1600
cl-n -cl    82.0      111.69              SOURCE3            1
c -n -n2    85.2      119.91      SOURCE3_SOURCE5          237    1.7782
c -n -n3    83.7      120.10      SOURCE3_SOURCE5           90    1.4705
c -n -n4    85.7      112.32              SOURCE3            5    1.2622
c -n -n     84.3      118.42              SOURCE3           10    2.8922
c -n -na    86.8      111.50      SOURCE3_SOURCE5           60    1.0005
na-nc-nd   116.8      106.24      SOURCE3_SOURCE5          145    0.6824
c -n -nc    83.5      124.86         CORR_SOURCE5          117    2.2930
nc-nc-nd   113.6      111.46         CORR_SOURCE5           97    0.5962
c -n -nd    83.5      124.86         CORR_SOURCE5          117    2.2930
nd-nc-os   114.1      107.22              SOURCE3            3    0.4707
c -n -nh    84.3      118.71      SOURCE4_SOURCE5           52    1.7764
c -n -no    82.8      118.16              SOURCE3            4    5.4870
c -n -o     89.1      118.36      SOURCE3_SOURCE5           14    3.9188
c -n -oh    85.3      115.51      SOURCE3_SOURCE5          128    0.8808
c -n -os    86.1      113.14              SOURCE3            7    3.0839
c -n -p2    79.4      124.56              SOURCE3            8    3.6907
c -n -p3    78.7      122.54              SOURCE3            9    4.4802
c -n -p4    79.7      123.44              SOURCE3            1
c -n -p5    78.7      128.50              SOURCE4            6    0.5353
c -n -pc    79.9      122.23              SOURCE3            3    2.8787
c -n -pd    79.9      122.23              SOURCE3            3
c -n -s4    61.9      120.41              SOURCE3            4    3.1760
c -n -s6    62.2      124.76      SOURCE4_SOURCE5           44    1.7490
c -n -s     60.4      126.55              SOURCE3            3    4.3365
c -n -sh    63.3      119.54              SOURCE3            4    1.7681
c -n -ss    62.8      121.71      SOURCE3_SOURCE5           23    1.8428
c -n -sy    62.3      124.69      SOURCE4_SOURCE5          124    1.1647
cx-n -hn    46.8      118.44               5/2017            7    0.9581
cx-n -os    81.9      120.30               5/2017            1
cy-n -hn    46.8      118.85               5/2017           72    1.0030
c3-nd-cc    69.9      109.51              SOURCE3            9
ca-nd-ca    72.0      109.95              SOURCE3            1
ca-nd-cc    74.6      104.88         CORR_SOURCE5          766    1.8814
ca-nd-n     92.1      104.69                 CORR            2
ca-nd-na    93.1      102.76         CORR_SOURCE5           25    0.7558
ca-nd-nc    92.5      108.34      SOURCE4_SOURCE5           23    0.2293
ca-nd-os    90.7      104.48         CORR_SOURCE5           16    0.1832
ca-nd-ss    70.4      107.07      SOURCE3_SOURCE5           17    0.3771
c -nd-ca    67.8      120.66                 CORR            2
c -nd-cc    68.6      120.49         CORR_SOURCE5          205    1.1318
cc-nd-cc    71.5      117.30         CORR_SOURCE5           18    0.3907
cc-nd-cd    73.9      105.49         CORR_SOURCE5         1810    1.9032
cc-nd-n     88.1      117.19                 CORR           64
cc-nd-na    93.8      103.82      SOURCE3_SOURCE5          919    1.7445
cc-nd-nd    91.7      107.82         CORR_SOURCE5          457    1.5268
cc-nd-os    91.7      104.67         CORR_SOURCE5          184    0.8204
cc-nd-ss    70.5      108.07         CORR_SOURCE5           95    1.3804
cd-nd-cd    73.1      103.76         CORR_SOURCE5            6    0.0439
cd-nd-na    92.4      102.97              SOURCE3            1
cd-nd-nc    91.7      108.62      SOURCE3_SOURCE5           82    1.5614
na-nd-nc   116.9      106.24      SOURCE3_SOURCE5          145    0.6824
nc-nd-nd   113.6      111.46         CORR_SOURCE5           97    0.5962
nc-nd-os   114.1      107.22              SOURCE3            3
c1-ne-ca    62.6      151.95         CORR_SOURCE5           15    1.4352
c1-ne-cg    67.9      140.00              SOURCE2            1
c2-ne-ca    68.5      120.83         CORR_SOURCE5          103    1.9474
c2-ne-ce    70.3      116.01      SOURCE3_SOURCE5           34    2.0813
c2-ne-cg    70.2      123.23      SOURCE4_SOURCE5           39    1.0918
c2-ne-n2    93.6      113.31              SOURCE3            1
c2-ne-ne    89.0      110.86              SOURCE3            7    4.5874
c2-ne-p2    84.1      134.03              SOURCE3            1
c2-ne-pe    82.5      120.52              SOURCE3            8    8.1381
c2-ne-px    83.9      117.75              SOURCE3            5    0.8581
c2-ne-py    88.2      117.04              SOURCE3            3    1.4398
c2-ne-sx    62.7      111.98              SOURCE3            3    0.4090
c2-ne-sy    65.6      120.60         CORR_SOURCE5           19    1.1215
ca-ne-cf    68.1      121.71         CORR_SOURCE5           29    1.8572
ca-ne-n2    88.7      114.35         CORR_SOURCE5           15    1.3133
ca-ne-nf    88.6      115.17         CORR_SOURCE5           98    0.8636
ca-ne-o     89.2      115.69      SOURCE3_SOURCE5           18    1.7090
ca-ne-p2    87.2      118.09              SOURCE3            1
ca-ne-s     68.1      120.11              SOURCE3            1
c -ne-c2    69.7      118.53                 CORR            6
ce-ne-n2    90.5      111.19              SOURCE3            1
ce-ne-o     91.2      112.16              SOURCE3            1
ce-ne-p2    87.9      117.02              SOURCE3            1
ce-ne-s     69.4      116.28              SOURCE3            1
cg-ne-n1    90.2      120.20              SOURCE2            1
cg-ne-n2    92.3      113.39              SOURCE3            1
cg-ne-o     93.0      114.70              SOURCE2            1
cg-ne-p2    88.4      119.57              SOURCE3            1
cg-ne-s     70.2      117.70              SOURCE3            1
c -ne-sy    65.6      116.43      SOURCE4_SOURCE5           16    1.7300
n2-ne-n2   121.5      107.22              SOURCE3            1
n2-ne-ne   112.2      110.72              SOURCE3            9    6.1488
n2-ne-o    119.6      114.10              SOURCE3            1
n2-ne-p2   116.9      109.66              SOURCE3            1
n2-ne-pe   107.4      112.15              SOURCE3            7    6.5273
n2-ne-px   106.1      115.97              SOURCE3            3    1.9854
n2-ne-py   112.0      114.60              SOURCE3            3    2.9261
n2-ne-s     89.7      115.90              SOURCE3            1
n2-ne-sx    80.2      107.29              SOURCE3            1
n2-ne-sy    85.7      111.21              SOURCE3            1
ne-ne-o    113.5      110.45              SOURCE3           10    1.8535
ne-ne-p2   110.5      114.39              SOURCE3            6    4.0528
ne-ne-s     86.4      115.95              SOURCE3            6    3.4604
o -ne-o    116.7      124.09              SOURCE3            2    8.7534
o -ne-pe    99.2      132.32              SOURCE3           11   23.9559
o -ne-px   109.1      110.62              SOURCE3            1
o -ne-py   114.7      110.79              SOURCE3            4    1.6818
o -ne-s     89.9      117.19              SOURCE3            2    0.0225
o -ne-sx    79.7      108.92              SOURCE3            1
o -ne-sy    86.1      111.34              SOURCE3            1
p2-ne-pe   110.5      116.81              SOURCE3            1
p2-ne-px   105.8      128.35              SOURCE3            1
p2-ne-py   111.5      123.47              SOURCE3            1
p2-ne-sx    83.9      112.12              SOURCE3            1
p2-ne-sy    87.7      115.73              SOURCE3            1
pe-ne-s     87.0      115.73              SOURCE3            1
px-ne-s     81.8      131.84              SOURCE3            1
py-ne-s     90.3      116.18              SOURCE3            4    3.7135
s -ne-s     70.5      120.87              SOURCE3            1
s -ne-sx    65.4      112.96              SOURCE3            1
s -ne-sy    67.7      119.63              SOURCE3            1
c1-nf-ca    62.6      151.95         CORR_SOURCE5           15    1.4352
c1-nf-ch    67.9      140.00              SOURCE2            1
c2-nf-ca    68.5      120.83         CORR_SOURCE5          103    1.9474
c2-nf-cf    70.3      116.01      SOURCE3_SOURCE5           31    2.1630
c2-nf-n2    93.6      113.31              SOURCE3            1
c2-nf-nf    89.0      110.86              SOURCE3            7
c2-nf-p2    84.1      134.03              SOURCE3            1
c2-nf-pf    82.5      120.52              SOURCE3            8
c2-nf-px    83.9      117.75              SOURCE3            5
c2-nf-py    88.2      117.04              SOURCE3            3
c2-nf-sx    62.7      111.98              SOURCE3            3
c2-nf-sy    65.6      120.60         CORR_SOURCE5           19    1.1215
ca-nf-ce    68.1      121.71         CORR_SOURCE5           29    1.8572
ca-nf-n2    88.7      114.35         CORR_SOURCE5           15    1.3133
ca-nf-ne    88.6      115.17         CORR_SOURCE5           98    0.8636
ca-nf-o     89.2      115.69      SOURCE3_SOURCE5           15    1.8257
ca-nf-p2    87.2      118.09              SOURCE3            1
ca-nf-s     68.1      120.11              SOURCE3            1
c -nf-c2    69.7      118.53                 CORR            6
cf-nf-n2    90.5      111.19              SOURCE3            1
cf-nf-o     91.2      112.16              SOURCE3            1
cf-nf-p2    87.9      117.02              SOURCE3            1
cf-nf-s     69.4      116.28              SOURCE3            1
ch-nf-n1    90.2      120.20              SOURCE2            1
ch-nf-n2    92.3      113.39              SOURCE3            1
ch-nf-o     93.0      114.70              SOURCE2            1
ch-nf-p2    88.4      119.57              SOURCE3            1
ch-nf-s     70.2      117.70              SOURCE3            1
f -n -f    116.1      102.98              SOURCE3            1
n2-nf-n2   121.5      107.22              SOURCE3            1
n2-nf-nf   112.2      110.72              SOURCE3            9
n2-nf-o    119.6      114.10              SOURCE3            1
n2-nf-p2   116.9      109.66              SOURCE3            1
n2-nf-pf   107.4      112.15              SOURCE3            7
n2-nf-px   106.1      115.97              SOURCE3            3
n2-nf-py   112.0      114.60              SOURCE3            3
n2-nf-s     89.7      115.90              SOURCE3            1
n2-nf-sx    80.2      107.29              SOURCE3            1
n2-nf-sy    85.7      111.21              SOURCE3            1
nf-nf-o    113.5      110.45              SOURCE3           10
nf-nf-p2   110.5      114.39              SOURCE3            6
nf-nf-s     86.4      115.95              SOURCE3            6
o -nf-o    116.7      124.09              SOURCE3            2
o -nf-pf    99.2      132.32              SOURCE3           11
o -nf-px   109.1      110.62              SOURCE3            1
o -nf-py   114.7      110.79              SOURCE3            4
o -nf-s     89.9      117.19              SOURCE3            2
o -nf-sx    79.7      108.92              SOURCE3            1
o -nf-sy    86.1      111.34              SOURCE3            1
p2-nf-pf   110.5      116.81              SOURCE3            1
p2-nf-px   105.8      128.35              SOURCE3            1
p2-nf-py   111.5      123.47              SOURCE3            1
p2-nf-sx    83.9      112.12              SOURCE3            1
p2-nf-sy    87.7      115.73              SOURCE3            1
pf-nf-s     87.0      115.73              SOURCE3            1
px-nf-s     81.8      131.84              SOURCE3            1
py-nf-s     90.3      116.18              SOURCE3            4
s -nf-s     70.5      120.87              SOURCE3            1
s -nf-sx    65.4      112.96              SOURCE3            1
s -nf-sy    67.7      119.63              SOURCE3            1
br-nh-br    67.7      106.27              SOURCE3            1
br-nh-ca    63.1      111.88              SOURCE3            1
br-nh-hn    42.0      101.56              SOURCE3            1
c1-nh-c1    70.3      116.98              SOURCE3            1
c1-nh-c2    67.3      123.35      SOURCE4_SOURCE5           17    1.3108
c1-nh-ca    67.6      122.36              SOURCE3            3    1.2016
c1-nh-hn    49.9      117.40      SOURCE4_SOURCE5           22    0.6517
c2-nh-c2    65.8      124.73      SOURCE4_SOURCE5          107    1.4158
c2-nh-c3    64.2      123.71              SOURCE3            8    3.5348
c2-nh-ca    65.1      127.56      SOURCE4_SOURCE5          258    2.3985
c2-nh-cc    65.7      126.35         CORR_SOURCE5           14    0.8394
c2-nh-cd    65.7      126.35         CORR_SOURCE5           14    0.8394
c2-nh-cx    64.8      124.39               5/2017            3    1.3163
c2-nh-hn    49.0      115.09      SOURCE4_SOURCE5         2743    1.5424
c2-nh-n2    85.0      120.22      SOURCE4_SOURCE5          101    1.0922
c2-nh-n3    84.3      116.87      SOURCE4_SOURCE5           35    1.4173
c2-nh-no    82.2      125.62      SOURCE4_SOURCE5           19    0.8850
c2-nh-oh    86.0      112.18      SOURCE4_SOURCE5           38    1.3409
c2-nh-os    85.7      112.95      SOURCE4_SOURCE5           14    0.4455
c2-nh-sy    63.2      121.13      SOURCE4_SOURCE5           20    0.5133
c3-nh-c3    65.1      114.51      SOURCE4_SOURCE5         1386    2.1206
c3-nh-ca    65.2      119.98      SOURCE3_SOURCE5         1640    2.1716
c3-nh-cc    65.6      119.72         CORR_SOURCE5          638    2.4802
c3-nh-cd    65.6      119.72         CORR_SOURCE5          638    2.4802
c3-nh-cf    65.1      120.12      SOURCE4_SOURCE5           52    2.0459
c3-nh-cz    64.7      125.46      SOURCE4_SOURCE5           25    0.5651
c3-nh-hn    46.4      115.99      SOURCE3_SOURCE5         1206    1.7716
c3-nh-n2    85.3      112.35              SOURCE3            9    4.0058
c3-nh-n     84.4      111.27      SOURCE4_SOURCE5           20    2.2657
c3-nh-na    84.0      112.39      SOURCE4_SOURCE5           18    1.3421
c3-nh-p2    80.3      123.35              SOURCE3            1
c3-nh-sy    63.5      116.32      SOURCE4_SOURCE5           31    1.3018
ca-nh-ca    65.2      127.46              SOURCE3            2    0.0002
ca-nh-cc    64.9      129.80         CORR_SOURCE5           49    1.2126
ca-nh-cd    64.9      129.80         CORR_SOURCE5           49    1.2126
ca-nh-cl    71.4      113.15              SOURCE3            1
ca-nh-cx    64.9      124.23               5/2017           10    0.2451
ca-nh-f     89.4      106.09              SOURCE3            3    1.0660
ca-nh-hn    48.8      116.07      SOURCE4_SOURCE5         5026    1.3182
ca-nh-i     58.9      117.83              SOURCE3            1
ca-nh-n1    86.5      117.13            HF/6-31G*            1
ca-nh-n2    84.7      121.13      SOURCE4_SOURCE5           61    1.2262
ca-nh-n3    84.0      117.83      SOURCE3_SOURCE5           31    1.9504
ca-nh-n4    85.7      108.94              SOURCE3            5    0.6562
ca-nh-n     85.1      116.03      SOURCE4_SOURCE5           31    1.0216
ca-nh-na    85.1      115.96      SOURCE3_SOURCE5           14    0.6985
ca-nh-nh    85.5      114.84      SOURCE3_SOURCE5           14    1.2270
ca-nh-no    86.3      113.92              SOURCE3            4    2.9561
ca-nh-o     87.0      121.92              SOURCE3            2    3.9630
ca-nh-oh    85.8      112.97      SOURCE3_SOURCE5            7    0.3980
ca-nh-os    86.2      111.85      SOURCE3_SOURCE5            8    0.6032
ca-nh-p2    81.0      125.27              SOURCE3            8    5.1798
ca-nh-p3    79.1      125.70              SOURCE3            3    5.7796
ca-nh-p4    80.5      124.01              SOURCE3            3    2.5810
ca-nh-p5    80.4      128.17      SOURCE3_SOURCE5            9    0.9847
ca-nh-s4    63.7      115.62              SOURCE3            3    0.3434
ca-nh-s6    63.2      122.85      SOURCE4_SOURCE5           92    2.1278
ca-nh-s     60.9      122.54              SOURCE3            3    2.7001
ca-nh-sh    63.3      121.41              SOURCE3            1
ca-nh-ss    63.2      121.50              SOURCE3            3    2.6255
ca-nh-sy    62.2      125.23      SOURCE4_SOURCE5          116    1.6241
cc-nh-cx    64.3      127.53               5/2017            2    0.0096
cc-nh-hn    49.3      115.63      SOURCE3_SOURCE5         1084    1.8598
cc-nh-n2    85.5      120.09      SOURCE4_SOURCE5           21    1.0306
cc-nh-sy    63.0      122.52      SOURCE4_SOURCE5           60    1.2839
cd-nh-cx    64.7      123.70         CORR_SOURCE5           82    1.6057
cd-nh-hn    49.3      115.63      SOURCE3_SOURCE5         1084    1.8598
ce-nh-hn    48.7      115.68         CORR_SOURCE5          360    1.2286
ce-nh-o     84.2      129.43                 CORR            2
ce-nh-sy    65.3      113.39      SOURCE4_SOURCE5           15    1.0862
cf-nh-hn    48.7      115.68         CORR_SOURCE5          360    1.2286
cf-nh-o     84.2      129.43                 CORR            2
cl-nh-cl    81.7      106.60              SOURCE3            1
cl-nh-hn    48.7      104.14              SOURCE3            1
cx-nh-cx    89.0       62.01      SOURCE4_SOURCE5           98    0.5911
cx-nh-hn    46.7      118.88               5/2017           15    0.2217
cz-nh-hn    49.2      121.15      SOURCE4_SOURCE5          116    0.7805
f -nh-f    114.4      101.70              SOURCE3            1
f -nh-hn    64.7      101.23              SOURCE3            1
hn-nh-hn    39.5      115.12      SOURCE4_SOURCE5         3024    2.1393
hn-nh-i     37.9      107.57              SOURCE3            1
hn-nh-n1    64.4      110.57            HF/6-31G*            1
hn-nh-n2    61.9      118.14      SOURCE4_SOURCE5          220    2.1956
hn-nh-n3    60.5      113.97      SOURCE3_SOURCE5           53    1.8422
hn-nh-n4    61.2      104.40              SOURCE3            3    0.5056
hn-nh-n     62.7      108.17      SOURCE4_SOURCE5           39    1.1076
hn-nh-na    62.7      108.24      SOURCE3_SOURCE5           48    1.3913
hn-nh-nh    61.9      110.86      SOURCE4_SOURCE5           20    1.2814
hn-nh-no    62.8      109.94      SOURCE4_SOURCE5           17    0.1843
hn-nh-o     65.9      116.45              SOURCE3            2    0.6063
hn-nh-oh    62.6      106.49      SOURCE4_SOURCE5           45    1.2492
hn-nh-os    62.7      106.07      SOURCE3_SOURCE5           11    1.1257
hn-nh-p2    55.5      118.18              SOURCE3           21    3.6927
hn-nh-p3    54.2      116.19              SOURCE3            3    3.0539
hn-nh-p4    55.9      112.60              SOURCE3            3    0.8237
hn-nh-p5    56.5      115.09      SOURCE3_SOURCE5           12    1.4234
hn-nh-s4    43.3      107.48              SOURCE3            3    1.3960
hn-nh-s     41.1      114.37              SOURCE3            1
hn-nh-s6    44.3      109.92      SOURCE4_SOURCE5           70    0.7219
hn-nh-sh    43.5      112.25              SOURCE3            1
hn-nh-ss    43.2      114.10      SOURCE3_SOURCE5            9    0.8638
hn-nh-sy    43.6      110.91      SOURCE4_SOURCE5          174    1.2855
i -nh-i     65.2      115.82              SOURCE3            1
n1-nh-n1   115.5      106.71            HF/6-31G*            1
n2-nh-n2   109.1      117.50              SOURCE3            2    1.1907
n2-nh-n3   105.8      119.06      SOURCE3_SOURCE5            5    1.1057
n2-nh-o    108.7      126.06              SOURCE3            1
n3-nh-n3   107.3      110.98              SOURCE3            1
n4-nh-n4   104.8      108.36              SOURCE3            1
na-nh-na   107.9      112.01              SOURCE3            1
hn-n -hn    39.0      117.95      SOURCE3_SOURCE5          619    1.1004
nh-nh-nh   107.7      112.23              SOURCE3            1
hn-n -i     37.5      117.24              SOURCE3            2    0.4435
hn-n -n2    61.3      119.08      SOURCE3_SOURCE5          133    1.1985
hn-n -n3    60.1      117.24      SOURCE4_SOURCE5           85    1.3614
hn-n -n4    60.2      112.68              SOURCE3            3    1.9746
hn-n -n     61.1      113.20      SOURCE3_SOURCE5           44    1.5099
hn-n -na    60.7      114.35      SOURCE3_SOURCE5           14    1.6595
hn-n -nc    62.3      115.42      SOURCE4_SOURCE5           34    0.6814
hn-n -nh    61.2      113.21      SOURCE4_SOURCE5           34    1.4195
hn-n -no    60.0      110.11              SOURCE3            1
hn-n -o     66.7      116.32              SOURCE3            2    0.0175
n -nh-o    111.0      115.63              SOURCE3            1
hn-n -oh    61.7      110.74      SOURCE4_SOURCE5          106    1.1526
no-nh-no   110.7      108.55              SOURCE3            1
hn-n -os    61.8      110.01      SOURCE4_SOURCE5           28    0.8603
hn-n -p2    53.6      118.05              SOURCE3            7    3.0564
hn-n -p3    52.0      119.63              SOURCE3            2
hn-n -p4    54.1      115.71              SOURCE3            1
hn-n -p5    55.2      113.61      SOURCE4_SOURCE5           12    0.8598
hn-n -s4    41.9      112.46              SOURCE3            1
hn-n -s     41.4      114.92              SOURCE3            2    0.0260
hn-n -s6    43.2      112.56      SOURCE4_SOURCE5           18    0.6934
hn-n -sh    42.5      114.91              SOURCE3            1
hn-n -ss    42.4      115.60              SOURCE3            3    0.6414
hn-n -sy    43.3      112.33      SOURCE4_SOURCE5           87    0.6324
oh-nh-oh   109.6      106.27              SOURCE3            1
o -nh-o    111.9      128.06              SOURCE3            1
os-nh-os   110.1      105.27              SOURCE3            1
p2-nh-p2   103.6      127.33              SOURCE3            2    2.7857
p3-nh-p3   101.5      125.08              SOURCE3            1
p5-nh-p5   110.6      112.76              SOURCE3            1
s4-nh-s4    64.3      112.39              SOURCE3            1
s6-nh-s6    64.0      120.27              SOURCE3            1
sh-nh-sh    64.0      119.00              SOURCE3            1
s -nh-s     61.3      118.73              SOURCE3            1
ss-nh-ss    63.9      119.25              SOURCE3            1
i -n -i     66.1      118.20              SOURCE3            1
n2-n -n2   108.7      116.89              SOURCE3            1
n3-n -n3   104.9      117.94              SOURCE3            1
n4-n -n4   105.2      112.69              SOURCE3            1
na-n -na   104.9      117.38              SOURCE3            1
nc-n -nc   109.0      116.41                 CORR            2
nc-n -p2   102.8      117.21                 CORR            2
nc-n -pc   102.5      117.21                 CORR            2
nd-n -nd   109.0      116.41                 CORR            2
nd-n -p2   102.8      117.21                 CORR            2
nd-n -pd   102.5      117.21                 CORR            2
nh-n -nh   106.3      115.18              SOURCE3            1
n -n -n    106.4      114.62              SOURCE3            1
no-n -no   105.4      108.66              SOURCE3            1
br-no-o     72.5      113.19              SOURCE3            2
c1-no-o     89.1      116.63              SOURCE3            6
c2-no-o     86.9      117.67      SOURCE3_SOURCE5           49    0.7530
c3-no-o     83.5      116.93      SOURCE3_SOURCE5          182    0.7108
ca-no-o     85.9      117.76      SOURCE3_SOURCE5          886    0.2929
cc-no-o     87.7      117.49      SOURCE4_SOURCE5          624    0.5662
cl-no-o     86.5      115.08              SOURCE3            2
c -no-o     83.8      115.26              SOURCE3            1
hn-no-o     67.4      115.49              SOURCE3            2
oh-n -oh   109.8      107.26              SOURCE3            1
i -no-o     70.4      116.31              SOURCE3            2
n1-no-o    112.6      115.00            HF/6-31G*            1
n2-no-o    110.0      116.52      SOURCE2_SOURCE5           17    2.4833
n3-no-o    111.9      116.77      SOURCE3_SOURCE5           35    0.4158
n4-no-o    111.2      109.00              SOURCE3            2
na-no-o    110.5      115.57      SOURCE3_SOURCE5           29    0.5293
nh-no-o    112.8      116.08      SOURCE3_SOURCE5           32    0.8573
n -no-o    109.3      115.59      SOURCE3_SOURCE5           14    0.7108
no-no-o     91.6      112.38              SOURCE3            4
o -n -o    113.5      128.61              SOURCE3            3    1.0626
o -no-o    116.6      125.08      SOURCE4_SOURCE5         1464    0.8585
o -no-oh   112.4      114.70              SOURCE3            2
o -no-os   111.6      114.76      SOURCE3_SOURCE5          147    2.2227
o -no-p2   104.0      117.38              SOURCE3           20    0.8083
o -no-p3    98.5      116.78              SOURCE3            6    0.4929
o -no-p4    97.2      116.64              SOURCE3            6    0.0089
o -no-p5    99.1      116.69              SOURCE3            8    0.4507
o -no-s4    71.5      114.49              SOURCE3            6    0.5674
o -no-s6    72.3      114.39              SOURCE3            6    0.8311
o -no-s     80.0      119.81              SOURCE3            4    0.0042
o -no-sh    78.6      116.10              SOURCE3            2
o -no-ss    77.8      115.58              SOURCE3            6    0.5860
os-n -os   110.0      106.53              SOURCE3            1
p2-n -p2   103.6      119.62              SOURCE3            1
p3-n -p3   106.4      108.73              SOURCE3            3    0.2591
p4-n -p4   108.7      108.55              SOURCE3            1
p5-n -p5   114.3       99.99              SOURCE3            1
pc-n -pc   103.2      119.62              SOURCE3            1
pd-n -pd   103.2      119.62              SOURCE3            1
s4-n -s4    63.2      113.75              SOURCE3            1
s6-n -s6    63.4      119.68              SOURCE3            1
sh-n -sh    63.2      119.03              SOURCE3            1
s -n -s     60.1      126.00              SOURCE3            1
ss-n -ss    63.5      118.49              SOURCE3            1
br-oh-ho    43.2      101.60              SOURCE3            1
c1-oh-ho    52.0      108.76              SOURCE3            1
c2-oh-ho    51.8      107.63      SOURCE3_SOURCE5           86    1.5038
c3-oh-ho    49.0      107.26      SOURCE3_SOURCE5         7781    0.7665
ca-oh-ho    50.7      108.58      SOURCE3_SOURCE5         3580    0.7052
cc-oh-ho    51.6      107.12         CORR_SOURCE5          226    1.6427
cd-oh-ho    51.6      107.12         CORR_SOURCE5          226    1.6427
ce-oh-ho    51.6      106.83         CORR_SOURCE5           48    1.2629
cf-oh-ho    51.6      106.83         CORR_SOURCE5           48    1.2629
c -oh-ho    51.6      106.55      SOURCE3_SOURCE5         2765    1.0627
cl-oh-ho    50.6      102.40              SOURCE2            1
cx-oh-ho    50.0      106.76               5/2017            3    0.8687
cy-oh-ho    49.3      107.80               5/2017           16    0.6264
f -oh-ho    64.7       96.80              SOURCE2            1
ho-oh-ho    42.2      106.49      SOURCE2_SOURCE5           23    1.3050
ho-oh-i     38.0      107.98              SOURCE3            2
ho-oh-n1    66.5      107.81            HF/6-31G*            1
ho-oh-n2    64.0      103.09      SOURCE3_SOURCE5          185    1.2900
ho-oh-n3    63.2      102.26      SOURCE3_SOURCE5           28    0.5790
ho-oh-n4    62.5      106.63              SOURCE3            3    0.2770
ho-oh-n     63.9      101.29      SOURCE3_SOURCE5          114    1.0315
ho-oh-na    63.5      104.37      SOURCE3_SOURCE5           16    0.9188
ho-oh-nh    63.0      102.77      SOURCE4_SOURCE5           57    0.7554
ho-oh-no    63.6      102.17              SOURCE3            1
ho-oh-o     59.4      100.87              SOURCE3            1
ho-oh-oh    62.1       98.72              SOURCE3            2
ho-oh-os    62.3       99.68      SOURCE4_SOURCE5           45    0.3142
ho-oh-p2    58.6      109.45              SOURCE3            8    3.3491
ho-oh-p3    56.4      110.64              SOURCE3            3    0.5191
ho-oh-p4    57.9      110.19              SOURCE3            4    0.2372
ho-oh-p5    59.0      110.08      SOURCE3_SOURCE5         1074    1.1258
ho-oh-py    58.8      110.49      SOURCE3_SOURCE5          115    1.4927
ho-oh-s4    44.2      106.85      SOURCE4_SOURCE5           28    0.5669
ho-oh-s     42.2      100.15              SOURCE3            2
ho-oh-s6    46.0      107.26      SOURCE3_SOURCE5          180    0.7965
ho-oh-sh    44.4      106.24              SOURCE3            2    0.0661
ho-oh-ss    44.4      107.11      SOURCE3_SOURCE5           12    1.0472
ho-oh-sy    45.7      106.42      SOURCE4_SOURCE5          121    0.3216
br-os-br    67.4      110.63              SOURCE3            1
c1-os-c1    71.2      115.02              SOURCE3            1
c1-os-c3    68.5      113.39              SOURCE3            1
c2-os-c2    69.6      113.14              SOURCE3            6    2.1932
c2-os-c3    67.0      115.59      SOURCE3_SOURCE5          149    2.3501
c2-os-ca    67.8      118.20      SOURCE3_SOURCE5           13    0.6779
c2-os-n2    84.0      118.13              SOURCE3            1
c2-os-na    88.1      103.85              SOURCE3            4    0.6297
c2-os-os    87.8      102.77              SOURCE3            1
c2-os-p5    82.3      126.37              SOURCE4            7    1.7939
c2-os-ss    66.6      108.13              SOURCE3            1
c3-os-c3    66.3      112.48      SOURCE4_SOURCE5         4012    1.7399
c3-os-ca    66.1      117.96      SOURCE4_SOURCE5         7354    1.4497
c3-os-cc    66.4      117.37         CORR_SOURCE5          411    1.1548
c3-os-cd    66.4      117.37         CORR_SOURCE5          411    1.1548
c3-os-ce    66.6      116.09         CORR_SOURCE5           59    1.9942
c3-os-cf    66.6      116.09         CORR_SOURCE5           59    1.9942
c3-os-cl    71.8      110.50              SOURCE2            1
c3-os-cy    67.1      110.36               5/2017           14    0.9990
c3-os-i     59.7      113.70              SOURCE3            1
c3-os-n1    86.0      113.50            HF/6-31G*            1
c3-os-n2    85.1      109.23      SOURCE3_SOURCE5           93    0.8090
c3-os-n3    83.7      109.83      SOURCE4_SOURCE5           46    1.7350
c3-os-n4    84.1      110.50              SOURCE3            3    0.5426
c3-os-n     84.7      109.68      SOURCE4_SOURCE5           42    0.9897
c3-os-na    83.2      110.98      SOURCE3_SOURCE5           17    1.2781
c3-os-nc    83.8      112.73              SOURCE3            2    1.0358
c3-os-nd    83.8      112.73              SOURCE3            2
c3-os-nh    84.5      109.79      SOURCE4_SOURCE5           22    0.2157
c3-os-no    82.8      113.89      SOURCE4_SOURCE5          112    0.3140
c3-os-o     84.5      103.00              SOURCE3            1
c3-os-oh    84.0      108.11      SOURCE4_SOURCE5           34    0.5701
c3-os-os    84.0      107.37      SOURCE3_SOURCE5           55    0.9835
c3-os-p2    86.1      115.47              SOURCE3            8    2.6374
c3-os-p3    81.9      117.51      SOURCE3_SOURCE5           11    0.9552
c3-os-p4    83.3      117.48              SOURCE3            4    0.3850
c3-os-p5    83.3      119.54      SOURCE3_SOURCE5          665    1.1338
c3-os-py    83.1      119.57      SOURCE3_SOURCE5           59    1.1952
c3-os-s4    64.6      113.21      SOURCE3_SOURCE5           18    1.1865
c3-os-s6    65.7      115.87      SOURCE4_SOURCE5          144    1.2750
c3-os-s     62.7      109.55              SOURCE3            1
c3-os-sh    65.3      112.82              SOURCE3            1
c3-os-ss    64.0      114.01      SOURCE3_SOURCE5            8    0.2853
ca-os-ca    67.1      119.89      SOURCE4_SOURCE5          312    1.5712
ca-os-cc    69.3      113.08         CORR_SOURCE5          343    1.5098
ca-os-cd    69.3      113.08         CORR_SOURCE5          343    1.5098
ca-os-n3    84.6      112.19              SOURCE3            1
ca-os-na    86.0      108.24              SOURCE3            1
ca-os-nc    87.0      109.32      SOURCE3_SOURCE5            7    0.0434
ca-os-nd    87.0      109.32      SOURCE3_SOURCE5            7    0.0434
ca-os-p5    83.2      123.18      SOURCE4_SOURCE5          136    1.2191
ca-os-s6    66.2      117.18      SOURCE4_SOURCE5           46    1.0420
c -os-c2    68.1      118.22      SOURCE4_SOURCE5           22    0.6933
c -os-c3    66.9      115.98      SOURCE3_SOURCE5         2731    1.0103
c -os-c     67.5      120.64              SOURCE4            7    1.5114
c -os-ca    67.0      121.15      SOURCE4_SOURCE5          731    1.7389
c -os-cc    67.7      119.62              SOURCE3            5    6.0675
cc-os-cc    71.5      106.72         CORR_SOURCE5          406    0.7345
cc-os-cd    67.8      118.68      SOURCE4_SOURCE5           49    2.2289
c -os-cd    67.7      119.62              SOURCE3            5    6.0675
cc-os-na    84.9      111.66              SOURCE3           28    4.1343
cc-os-nc    87.6      108.37      SOURCE3_SOURCE5          148    0.8594
cc-os-os    85.4      108.47              SOURCE3            2
cc-os-ss    63.3      119.59              SOURCE3            1
c -os-cy    68.2      112.64               5/2017            3    1.5599
cd-os-cd    71.5      106.72         CORR_SOURCE5          406    0.7345
cd-os-na    84.9      111.66              SOURCE3           28    4.1343
cd-os-nd    87.6      108.37      SOURCE3_SOURCE5          148    0.8594
cd-os-os    85.4      108.47              SOURCE3            2
cd-os-ss    63.3      119.59              SOURCE3            1
cl-os-cl    80.6      110.76              SOURCE3            2
c -os-n2    86.2      112.12      SOURCE4_SOURCE5           16    0.1285
c -os-n     85.9      112.24      SOURCE4_SOURCE5           17    0.6206
c -os-oh    85.0      110.50              SOURCE3            1
c -os-os    84.8      110.20      SOURCE4_SOURCE5           22    1.3187
c -os-p5    83.7      122.13      SOURCE4_SOURCE5           11    0.5685
c -os-sy    65.2      113.49              SOURCE3            1
cx-os-cx    89.1       61.78      SOURCE4_SOURCE5          379    0.2104
cx-os-n    114.4       59.99              SOURCE3            1
cx-os-os    84.7      107.41               5/2017            2    0.8185
cy-os-cy    73.0       91.86      SOURCE2_SOURCE5           16    1.0042
f -os-f    112.3      103.30              SOURCE2            1
f -os-os   105.9      109.50              SOURCE2            1
i -os-i     65.0      115.67              SOURCE3            1
n1-os-n1   111.0      117.79            HF/6-31G*            1
n2-os-n2   109.0      106.83              SOURCE3            1
n2-os-s6    84.5      111.30      SOURCE4_SOURCE5           14    0.5651
n3-os-n3   107.0      104.88              SOURCE3            1
n4-os-n4   103.7      114.68              SOURCE3            1
na-os-na   104.4      109.59              SOURCE3            1
na-os-ss    83.6      104.34              SOURCE3            1
nc-os-nc   106.1      112.75      SOURCE2_SOURCE5           12    0.7540
nc-os-ss    81.7      110.97              SOURCE3            1
nd-os-nd   106.1      112.75      SOURCE2_SOURCE5           12    0.7540
nd-os-ss    81.7      110.97              SOURCE3            1
nh-os-nh   107.2      108.29              SOURCE3            1
n -os-n    107.6      108.31              SOURCE3            1
no-os-no   105.0      111.86              SOURCE3            1
n -os-s6    83.5      113.63      SOURCE4_SOURCE5           13    0.1799
o -os-o     98.0      114.68              SOURCE3            1
p2-os-p2   112.4      120.02              SOURCE3            1
p2-os-p5   117.0      107.86              SOURCE3            1
p3-os-p3   105.1      121.22              SOURCE3            1
p3-os-py   114.5      105.58              SOURCE3            1
p5-os-p5   106.8      126.25              SOURCE3            1
s4-os-s4    65.8      111.63              SOURCE3            1
s6-os-s6    66.4      119.07              SOURCE3            2    0.4318
sh-os-sh    64.5      118.95              SOURCE3            1
s -os-s     60.1      118.08              SOURCE3            1
ss-os-ss    64.2      115.64              SOURCE3            1
br-p2-br    50.4      108.60              SOURCE3            1
br-p2-c2    49.3      102.32              SOURCE3            2    0.0146
br-p2-n2    61.8      103.33              SOURCE3            1
br-p2-o     59.9      110.87              SOURCE3            1
br-p2-p2    63.6      115.46              SOURCE3            4    7.8622
br-p2-s     50.7      110.52              SOURCE3            1
c1-p2-c1    49.5       99.04              SOURCE3            1
c1-p2-c2    50.3      101.29              SOURCE3            1
c1-p2-n2    63.9      101.79              SOURCE3            1
c1-p2-o     63.4      107.62              SOURCE3            1
c1-p2-p2    68.2       99.54              SOURCE3            1
c1-p2-s     51.7      105.90              SOURCE3            1
c2-p2-c2    51.1      104.50              SOURCE3            1
c2-p2-c3    48.8      101.90              SOURCE3            4    0.1132
c2-p2-ca    49.0      101.95              SOURCE3            1
c2-p2-cl    54.3      102.72              SOURCE3            2
c2-p2-f     67.8      103.47              SOURCE3            2    0.0136
c2-p2-hp    37.3       97.19              SOURCE3            3    0.0216
c2-p2-i     44.0      101.94              SOURCE3            2    0.0368
c2-p2-n2    66.7       99.88              SOURCE3            1
c2-p2-n3    64.9      101.80              SOURCE3            1
c2-p2-n4    60.3       98.26              SOURCE3            6    0.1522
c2-p2-n     63.2      103.28              SOURCE3            4    3.3113
c2-p2-na    62.6      103.99              SOURCE3            8    1.6834
c2-p2-nh    63.6      105.17              SOURCE3            8    0.8263
c2-p2-no    64.7       97.97              SOURCE3            3    0.4175
c2-p2-o     63.8      115.16              SOURCE3            1
c2-p2-oh    65.3      102.89              SOURCE3            3    0.8191
c2-p2-os    66.6      102.12              SOURCE3            4    0.8783
c2-p2-p2    70.1       99.56              SOURCE3            1
c2-p2-p3    61.6       99.27              SOURCE3            4    1.1590
c2-p2-p4    61.7       96.94              SOURCE3            1
c2-p2-p5    61.5       97.61              SOURCE3            1
c2-p2-s4    48.3       95.15              SOURCE3            1
c2-p2-s6    48.4       95.51              SOURCE3            1
c2-p2-s     53.3      105.53              SOURCE3            1
c2-p2-sh    50.7      101.49              SOURCE3            3    0.0057
c2-p2-ss    50.7      101.81              SOURCE3            4    0.5883
c3-p2-c3    47.2       99.30              SOURCE3            1
c3-p2-n2    62.2      100.82              SOURCE3            1
c3-p2-o     61.6      106.72              SOURCE3            1
c3-p2-os    62.5      101.34              SOURCE3            1
c3-p2-p2    66.3      100.48              SOURCE3            1
c3-p2-s     50.5      105.68              SOURCE3            1
ca-p2-ca    47.5       99.70              SOURCE3            1
ca-p2-n2    62.6      100.82              SOURCE3            1
ca-p2-n     64.3       89.97              SOURCE3            1
ca-p2-na    64.4       89.21              SOURCE3            1
ca-p2-o     61.9      106.88              SOURCE3            1
ca-p2-s     50.2      107.93              SOURCE3            1
c -p2-c2    49.1       97.30              SOURCE3            1
c -p2-c     48.4       90.10              SOURCE3            1
ce-p2-o     62.4      107.44              SOURCE3            1
ce-p2-s     51.2      105.54              SOURCE3            1
cf-p2-o     62.4      107.44              SOURCE3            1
cf-p2-s     51.2      105.54              SOURCE3            1
cl-p2-cl    58.9      108.70              SOURCE3            1
cl-p2-n2    68.4      103.38              SOURCE3            1
cl-p2-o     66.7      110.57              SOURCE3            1
cl-p2-p2    73.8      103.11              SOURCE3            1
cl-p2-s     55.8      110.11              SOURCE3            1
f -p2-f     88.5      107.10              SOURCE3            1
f -p2-n2    86.7      103.57              SOURCE3            1
f -p2-o     86.7      110.61              SOURCE3            1
f -p2-p2    90.0      103.48              SOURCE3            1
f -p2-s     66.9      114.71              SOURCE3            2    5.2794
hp-p2-hp    27.6       98.76              SOURCE3            1
hp-p2-n1    47.0       95.18              SOURCE3            2    1.5708
hp-p2-n2    48.5       95.54              SOURCE3           19    4.7352
hp-p2-ne    48.3      100.10              SOURCE3           14    6.1290
hp-p2-nf    48.3      100.10              SOURCE3           14
hp-p2-o     48.1      105.58              SOURCE3            1
hp-p2-p2    47.8      101.88              SOURCE3           27   12.9535
hp-p2-p4    41.0       94.51              SOURCE3            1
hp-p2-p5    42.2       89.07              SOURCE3            1
hp-p2-pe    47.0       97.25              SOURCE3           16    8.8916
hp-p2-pf    47.0       97.25              SOURCE3           16
hp-p2-s4    32.5       89.99              SOURCE3            1
hp-p2-s     37.4      102.52              SOURCE3            1
hp-p2-s6    33.0       88.13              SOURCE3            1
i -p2-i     47.8      104.16              SOURCE3            1
i -p2-n2    55.0      101.77              SOURCE3            1
i -p2-o     52.7      109.51              SOURCE3            1
i -p2-p2    60.9      102.63              SOURCE3            1
i -p2-s     45.7      110.60              SOURCE3            1
n1-p2-n1    87.8       86.22            HF/6-31G*            1
n2-p2-n2    86.1       98.00              SOURCE3            1
n2-p2-n3    83.3      100.42              SOURCE3            1
n2-p2-n4    78.4       93.42              SOURCE3            1
n2-p2-na    80.5      102.03              SOURCE3            1
n2-p2-nh    82.5      101.87              SOURCE3            2    0.8491
n2-p2-no    82.4       98.12              SOURCE3            1
n2-p2-o     81.7      115.34              SOURCE3            1
n2-p2-oh    80.7      109.72              SOURCE3            1
n2-p2-os    85.1      102.29              SOURCE3            1
n2-p2-p3    77.5       99.51              SOURCE3            1
n2-p2-p4    75.8      101.73              SOURCE3            1
n2-p2-p5    79.0       93.68              SOURCE3            1
n2-p2-s4    60.0       97.83              SOURCE3            1
n2-p2-s6    60.1       98.14              SOURCE3            1
n2-p2-s     65.5      112.94              SOURCE3            1
n2-p2-sh    64.4      100.82              SOURCE3            1
n2-p2-ss    64.2      101.76              SOURCE3            1
n3-p2-n3    79.4      106.30              SOURCE3            1
n3-p2-o     82.9      106.83              SOURCE3            1
n3-p2-p2    87.3      100.58              SOURCE3            1
n3-p2-s     66.6      105.75              SOURCE3            1
n4-p2-n4    74.8       88.80              SOURCE3            1
n4-p2-o     76.3      101.36              SOURCE3            1
n4-p2-p2    82.5       96.53              SOURCE3            1
n4-p2-s     61.8      104.98              SOURCE3            1
na-p2-na    75.9      106.10              SOURCE3            1
na-p2-o     80.1      107.46              SOURCE3            1
na-p2-s     64.5      108.15              SOURCE3            1
ne-p2-o     85.8      107.71              SOURCE3            1
ne-p2-s     68.4      105.50              SOURCE3            1
nf-p2-o     85.8      107.71              SOURCE3            1
nf-p2-s     68.4      105.50              SOURCE3            1
nh-p2-nh    79.9      104.00              SOURCE3            1
nh-p2-o     82.1      108.11              SOURCE3            2    0.6773
nh-p2-p2    84.1      107.73              SOURCE3            3    3.1678
nh-p2-s     65.3      109.62              SOURCE3            2    1.7725
n -p2-n2    82.2       98.85              SOURCE3            1
n -p2-o     81.6      105.08              SOURCE3            1
no-p2-no    79.4       98.20              SOURCE3            1
no-p2-o     81.5      104.87              SOURCE3            1
no-p2-p2    82.5      108.57              SOURCE3            3    8.2121
no-p2-s     64.4      109.06              SOURCE3            2    5.4074
n -p2-p2    85.2      102.12              SOURCE3            1
n -p2-s     63.6      112.34              SOURCE3            1
oh-p2-oh    83.9      100.10              SOURCE3            1
oh-p2-p2    85.1      107.82              SOURCE3            2    2.6708
oh-p2-s     66.0      109.75              SOURCE3            1
o -p2-o     82.8      119.96              SOURCE3            1
o -p2-oh    82.7      110.46              SOURCE3            1
o -p2-os    85.1      108.81              SOURCE3            1
o -p2-p2    84.9      114.23              SOURCE3            1
o -p2-p3    75.4      106.69              SOURCE3            1
o -p2-p4    75.3      104.37              SOURCE3            1
o -p2-p5    75.2      104.49              SOURCE3            1
o -p2-pe    72.7      145.96              SOURCE3            1
o -p2-pf    72.7      145.96              SOURCE3            1
o -p2-s4    57.8      106.59              SOURCE3            1
o -p2-s6    58.5      105.04              SOURCE3            1
o -p2-s     65.6      117.42              SOURCE3            1
o -p2-sh    62.6      109.60              SOURCE3            1
os-p2-os    87.7       98.30              SOURCE3            1
os-p2-p2    88.9      101.46              SOURCE3            1
o -p2-ss    62.7      109.60              SOURCE3            1
os-p2-s     67.3      108.47              SOURCE3            3    1.7065
p2-p2-n2    90.1       97.40              SOURCE3            1
p2-p2-p3    83.1      101.73              SOURCE3            1
p2-p2-p4    82.2      101.98              SOURCE3            1
p2-p2-p5    83.3       99.33              SOURCE3            1
p2-p2-s4    65.9       95.73              SOURCE3            1
p2-p2-s6    66.0       95.95              SOURCE3            1
p2-p2-s     69.7      111.28              SOURCE3            1
p2-p2-sh    64.9      113.94              SOURCE3            3    8.5009
p3-p2-p3    77.6      101.00              SOURCE3            1
p3-p2-s     61.5      113.28              SOURCE3            2    6.7035
p4-p2-s     63.6      103.89              SOURCE3            1
p5-p2-p5    81.5       89.40              SOURCE3            1
p5-p2-s     64.4      101.21              SOURCE3            1
pe-p2-s     69.6      106.35              SOURCE3            1
pf-p2-s     69.6      106.35              SOURCE3            1
s4-p2-s4    50.4       85.30              SOURCE3            1
s6-p2-s6    47.2       98.20              SOURCE3            1
sh-p2-sh    52.1       98.50              SOURCE3            1
s -p2-s     55.7      106.60              SOURCE3            1
s -p2-s4    49.1      105.29              SOURCE3            1
s -p2-s6    48.8      106.93              SOURCE3            1
s -p2-sh    51.5      110.73              SOURCE3            2    0.0232
s -p2-ss    50.8      114.14              SOURCE3            4    5.9223
ss-p2-ss    52.4       97.90              SOURCE3            1
br-p3-br    51.1      103.54              SOURCE3            1
br-p3-hp    33.0       96.36              SOURCE3            4    0.6701
c1-p3-c1    48.6      100.50              SOURCE3            1
c1-p3-f     66.3       96.90              SOURCE2            1
c1-p3-hp    34.8       97.67              SOURCE3            2
c2-p3-c2    47.1      101.77              SOURCE3            3
c2-p3-hp    34.1       97.85              SOURCE3            4
c3-p3-c3    47.1       99.35      SOURCE3_SOURCE5          108    0.9814
c3-p3-ca    46.9      101.94              SOURCE3            2
c3-p3-cl    54.3       99.89              SOURCE3            1
c3-p3-f     64.4       97.80              SOURCE2            1
c3-p3-hp    33.8       97.48      SOURCE3_SOURCE5           20    0.3444
c3-p3-n2    61.3       96.55              SOURCE3            2
c3-p3-n3    60.3      101.41      SOURCE3_SOURCE5           22    1.5604
c3-p3-n4    59.4       96.94              SOURCE3            6    0.4815
c3-p3-n     59.6      101.77              SOURCE3           12    2.4449
c3-p3-na    60.2      100.17              SOURCE3            4    0.0554
c3-p3-nh    59.4      104.50              SOURCE3            2
c3-p3-no    59.9       96.98              SOURCE3            2
c3-p3-o     60.0      111.67              SOURCE3           28    5.3387
c3-p3-oh    62.0       98.21              SOURCE3            2
c3-p3-os    61.7       99.53              SOURCE3            3    1.7678
c3-p3-p3    58.6       99.88      SOURCE3_SOURCE5           26    1.6230
c3-p3-p5    58.3      100.90              SOURCE3           10    2.7070
c3-p3-s4    47.8       98.88              SOURCE3            8    6.2235
c3-p3-s6    47.4      101.18              SOURCE3           12    6.4536
c3-p3-sh    47.1       98.71              SOURCE3            2
c3-p3-ss    47.1       99.37              SOURCE3            2
ca-p3-ca    47.8       99.86              SOURCE3            1
ca-p3-hp    34.3       97.50              SOURCE3            2
c -p3-c3    47.3       97.06              SOURCE3            3    1.1490
c -p3-c     46.1      100.90              SOURCE3            1
c -p3-hp    33.6       96.55              SOURCE3            6    0.5223
cl-p3-cl    62.4      102.82              SOURCE3            1
cl-p3-f     72.8       99.20              SOURCE2            1
cl-p3-hp    38.3       96.30              SOURCE3            3    0.6203
c -p3-os    67.6       81.32              SOURCE3            1
cx-p3-hp    34.0       95.20              SOURCE2            1
f -p3-f     90.4       97.40              SOURCE2            8    1.6636
f -p3-hp    48.7       96.41              SOURCE3            2
f -p3-n3    83.3      100.60              SOURCE2            1
f -p3-os    85.5       99.23      SOURCE2_SOURCE5            5    0.5316
f -p3-p3    77.7       97.20              SOURCE2            1
hp-p3-hp    26.6       95.22      SOURCE3_SOURCE5           51    2.1059
hp-p3-i     29.8       96.19              SOURCE3            4    0.6454
hp-p3-n1    47.2       92.98            HF/6-31G*            1
hp-p3-n2    43.9       98.28              SOURCE3           10    1.8860
hp-p3-n3    45.5       94.46              SOURCE3            2
hp-p3-n4    42.8       93.21              SOURCE3            2
hp-p3-n     44.5       95.15              SOURCE3            2
hp-p3-na    44.2       97.27              SOURCE3           12    0.9318
hp-p3-nh    45.6       94.10              SOURCE3            2
hp-p3-no    43.6       93.06              SOURCE3            2
hp-p3-o     48.1      101.02              SOURCE3            2
hp-p3-oh    46.2       95.95              SOURCE3            2
hp-p3-os    45.9       97.35              SOURCE3            6    2.8326
hp-p3-p2    40.6       99.11              SOURCE3           16    4.3022
hp-p3-p3    40.2       95.52              SOURCE3            4    0.0844
hp-p3-p4    40.0       95.95              SOURCE3            6    0.0489
hp-p3-p5    40.2       95.54              SOURCE3            2
hp-p3-s4    33.2       95.49              SOURCE3            2
hp-p3-s6    33.8       92.95              SOURCE3            2
hp-p3-sh    32.7       94.21              SOURCE3            2
hp-p3-ss    32.8       94.61              SOURCE3            2
i -p3-i     49.0      105.25              SOURCE3            1
n1-p3-n1    86.7       90.44            HF/6-31G*            1
n2-p3-n2    76.2      103.46              SOURCE3            1
n3-p3-n3    74.1      113.80              SOURCE3            1
n3-p3-o     80.8      107.10              SOURCE3            4
n3-p3-oh    80.9       98.36              SOURCE3            1
n4-p3-n4    72.6      100.53              SOURCE3            1
na-p3-na    75.3      106.22              SOURCE3            1
nh-p3-nh    75.7      109.11              SOURCE3            1
n -p3-n     75.6      104.58              SOURCE3            1
n -p3-o     80.3      104.99              SOURCE3            4
no-p3-no    74.8       98.33              SOURCE3            1
oh-p3-oh    79.8      104.48              SOURCE3            1
o -p3-o     81.7      122.18              SOURCE3            2    7.8556
o -p3-p3    70.1      116.74              SOURCE3           14    0.7525
o -p3-p5    73.1      107.62              SOURCE3            4
o -p3-s4    59.3      110.70              SOURCE3            4    0.7259
o -p3-s6    60.6      106.66              SOURCE3            6    3.4017
os-p3-os    81.8       99.76      SOURCE3_SOURCE5            8    1.2613
p2-p3-p2    76.7      103.58              SOURCE3            1
p3-p3-p3    73.9      105.31              SOURCE3            4    3.5864
p4-p3-p4    76.1       99.09              SOURCE3            1
p5-p3-p5    76.2       99.10              SOURCE3            1
s4-p3-s4    49.3       98.26              SOURCE3            1
s6-p3-s6    49.6       97.78              SOURCE3            1
sh-p3-sh    46.1      107.58              SOURCE3            1
s -p3-s     43.0      131.32              SOURCE3            1
ss-p3-ss    46.0      109.24              SOURCE3            1
br-p4-br    50.9      110.41              SOURCE3            1
br-p4-o     57.5      124.80              SOURCE3            1
c2-p4-c2    46.9      104.21              SOURCE3            1
c2-p4-hp    34.2       99.50              SOURCE3            2
c2-p4-o     60.5      113.59              SOURCE3            1
c3-p4-c3    46.8      102.55              SOURCE3            4    0.0192
c3-p4-n2    60.2      103.17              SOURCE3            1
c3-p4-n3    60.9      102.37              SOURCE3            1
c3-p4-n4    57.9       99.57              SOURCE3            1
c3-p4-n     60.1      103.26              SOURCE3            1
c3-p4-na    58.4      117.67              SOURCE3            5   19.0404
c3-p4-nh    60.6      102.79              SOURCE3            1
c3-p4-no    59.0       99.80              SOURCE3            3    0.2151
c3-p4-o     59.6      115.67      SOURCE3_SOURCE5           41    1.9882
c3-p4-oh    62.8       98.56              SOURCE3            2    0.4558
c3-p4-os    63.1       98.01              SOURCE3            2    0.0931
c3-p4-p2    56.8      109.27              SOURCE3            1
c3-p4-p3    57.7      103.53              SOURCE3            1
c3-p4-p4    61.5      102.12              SOURCE3            1
c3-p4-p5    57.1      104.15              SOURCE3            1
c3-p4-sh    47.2      100.17              SOURCE3            2    0.0815
c3-p4-ss    47.1      101.19              SOURCE3            1
ca-p4-ca    46.5      107.77              SOURCE3            1
ca-p4-o     61.4      111.64              SOURCE3            1
cl-p4-cl    62.2      103.51              SOURCE3            1
cl-p4-o     66.8      116.53              SOURCE3            2
hp-p4-hp    27.3       99.21              SOURCE3            4    6.4572
hp-p4-n1    45.7       99.91            HF/6-31G*            1
hp-p4-o     47.2      109.35              SOURCE3            6   10.8284
hp-p4-p3    39.3       98.96              SOURCE3            4
hp-p4-s     30.0      110.24              SOURCE3            4    4.1081
i -p4-i     51.6      113.22              SOURCE3            2    6.7916
i -p4-o     59.6      110.22              SOURCE3            4    9.7726
n1-p4-n1    81.2      100.61            HF/6-31G*            1
n1-p4-o     79.8      114.59            HF/6-31G*            1
n2-p4-n2    78.4      102.54              SOURCE3            1
n2-p4-o     76.6      120.28              SOURCE3            1
n3-p4-o     79.7      113.27              SOURCE3            1
n4-p4-o     74.2      107.61              SOURCE3            1
na-p4-o     84.7      110.60              SOURCE3            5    1.3133
nh-p4-nh    82.1       95.30              SOURCE3            1
nh-p4-o     78.6      115.86              SOURCE3            3    3.2712
n -p4-o     77.0      117.99              SOURCE3            1
no-p4-o     74.0      114.69              SOURCE3            3    0.1070
oh-p4-oh    85.2       95.71              SOURCE3            1
o -p4-o     84.0      117.22              SOURCE3            6    2.7792
o -p4-oh    80.0      117.39              SOURCE3            4    1.0083
o -p4-os    80.4      116.67              SOURCE3            4    0.6923
o -p4-p2    69.9      121.35              SOURCE3            1
o -p4-p3    70.9      114.00              SOURCE3            3    0.6663
o -p4-p4    75.9      116.43              SOURCE3            1
o -p4-p5    71.6      109.76              SOURCE3            1
o -p4-s4    54.9      112.19              SOURCE3            1
o -p4-s6    54.0      113.89              SOURCE3            1
o -p4-s     57.3      112.78              SOURCE3            2
o -p4-sh    56.7      118.09              SOURCE3            1
os-p4-os    83.5      100.34              SOURCE3            1
o -p4-ss    57.5      116.14              SOURCE3            4    1.0636
p2-p4-p2    73.2      110.71              SOURCE3            1
p3-p4-p3    70.7      114.98              SOURCE3            1
p4-p4-p4    79.7      107.38              SOURCE3            1
p5-p4-p5    72.3      107.78              SOURCE3            1
s4-p4-s4    46.2       96.24              SOURCE3            1
s6-p4-s6    44.4      102.36              SOURCE3            1
sh-p4-sh    48.5       98.81              SOURCE3            1
s -p4-s     46.1      106.30              SOURCE3            2   25.0119
ss-p4-ss    47.4      104.41              SOURCE3            1
br-p5-br    52.0      103.38              SOURCE3            1
br-p5-o     59.3      114.65              SOURCE3            3    1.0910
br-p5-oh    62.2      102.92              SOURCE3            4    0.5468
c1-p5-c1    49.1      102.89              SOURCE3            1
c1-p5-o     61.8      115.77              SOURCE3            2
c1-p5-oh    63.8      102.79              SOURCE3            2
c2-p5-c2    45.4      106.56              SOURCE3            1
c2-p5-o     60.8      109.52      SOURCE4_SOURCE5           15    2.0293
c2-p5-oh    61.7      101.69              SOURCE3            1
c2-p5-os    63.1       97.12      SOURCE3_SOURCE5            6    0.9178
c3-p5-c3    46.1      106.00      SOURCE3_SOURCE5          107    1.6965
c3-p5-hp    33.1      103.26      SOURCE4_SOURCE5           20    1.3795
c3-p5-n3    60.6      104.40      SOURCE3_SOURCE5           10    1.8148
c3-p5-o     60.5      112.50              SOURCE3           23    4.4203
c3-p5-oh    61.9      102.69      SOURCE3_SOURCE5          389    1.5370
c3-p5-os    62.5      100.77              SOURCE4           51    2.0928
c3-p5-p4    56.5      106.27              SOURCE3            1
c3-p5-s     46.7      114.40      SOURCE3_SOURCE5           36    1.0844
c3-p5-ss    45.9      105.94      SOURCE3_SOURCE5           24    1.6358
ca-p5-ca    46.8      107.90      SOURCE3_SOURCE5            5    0.5519
ca-p5-o     61.3      113.98              SOURCE3            1
ca-p5-oh    63.2      101.77              SOURCE3            1
ca-p5-os    62.6      103.75              SOURCE3            1
c -p5-c     45.4      104.16              SOURCE3            1
cl-p5-cl    62.2      103.70              SOURCE2            1
cl-p5-o     68.0      112.65      SOURCE3_SOURCE5            7    1.0635
cl-p5-oh    70.3      102.44              SOURCE3            2
c -p5-o     61.0      107.10      SOURCE4_SOURCE5           37    0.4646
c -p5-oh    61.1      102.12              SOURCE3            1
f -p5-f     92.4       92.22      SOURCE2_SOURCE5           19    1.3661
f -p5-o     85.1      112.07      SOURCE4_SOURCE5           15    0.5195
f -p5-oh    85.8      101.98              SOURCE3            2
f -p5-os    85.7      102.27      SOURCE4_SOURCE5           16    1.0230
f -p5-s     61.6      117.40              SOURCE2            1
hp-p5-hp    25.8      100.55      SOURCE3_SOURCE5           11    0.5508
hp-p5-n1    46.9      101.32            HF/6-31G*            1
hp-p5-o     45.4      115.08      SOURCE3_SOURCE5           27    1.7749
hp-p5-oh    46.0      101.57      SOURCE3_SOURCE5           16    1.3736
hp-p5-s     31.9      119.20              SOURCE2            1
i -p5-i     48.0      107.17              SOURCE3            1
i -p5-o     52.1      115.93              SOURCE3            3    0.0415
i -p5-oh    56.0      102.26              SOURCE3            4    1.9577
n1-p5-n1    86.4      101.55            HF/6-31G*            1
n1-p5-o     83.8      113.78            HF/6-31G*            1
n2-p5-n2    83.0      106.34              SOURCE3            1
n2-p5-o     83.0      113.53              SOURCE3            1
n2-p5-oh    84.1      102.40              SOURCE3            1
n3-p5-n3    80.6      103.37              SOURCE4           47    2.1009
n3-p5-nh    80.4      103.84      SOURCE4_SOURCE5           11    1.8670
n3-p5-o     80.4      114.64              SOURCE4           76    2.2728
n3-p5-oh    81.2      104.99      SOURCE3_SOURCE5           18    0.6974
n3-p5-os    82.3      102.23      SOURCE4_SOURCE5           90    2.1717
n3-p5-s     60.1      116.56      SOURCE4_SOURCE5           28    0.9342
n4-p5-n4    73.9      102.20              SOURCE3            1
n4-p5-o     77.1      109.78              SOURCE3            5    2.7519
n4-p5-oh    79.4       98.48              SOURCE3            6    0.4104
n4-p5-os    81.0       94.55              SOURCE3            2
na-p5-na    76.5      108.57              SOURCE3            1
na-p5-o     79.4      113.43              SOURCE3           11    0.8968
na-p5-oh    81.2      102.07              SOURCE3           16    1.4144
na-p5-os    80.8      103.06              SOURCE3            4    0.7463
nh-p5-nh    82.1       99.51              SOURCE3            1
nh-p5-o     80.3      114.86      SOURCE3_SOURCE5           11    1.6006
nh-p5-oh    82.0      102.91      SOURCE3_SOURCE5            6    0.9034
nh-p5-os    81.1      105.20      SOURCE3_SOURCE5            6    2.0688
n -p5-n3    79.1      104.31      SOURCE4_SOURCE5           28    1.2397
n -p5-n     78.5      103.09              SOURCE3            1
n -p5-o     79.8      112.18      SOURCE4_SOURCE5           14    1.5068
n -p5-oh    81.0      102.44              SOURCE3            4    0.0999
no-p5-no    76.3       95.68              SOURCE3            1
no-p5-o     75.9      112.75              SOURCE3            4    3.3684
no-p5-oh    78.2      101.35              SOURCE3            2
no-p5-os    78.0      101.70              SOURCE3            4    0.0565
n -p5-os    81.8      100.48              SOURCE3            2
oh-p5-oh    83.6      102.69      SOURCE3_SOURCE5          359    1.1644
oh-p5-os    83.9      101.94      SOURCE3_SOURCE5          591    1.1251
oh-p5-p2    75.1      103.53              SOURCE3            1
oh-p5-p3    74.0      103.83              SOURCE3           13    0.4303
oh-p5-p4    74.0      101.79              SOURCE3            1
oh-p5-p5    80.1      100.45              SOURCE3            1
oh-p5-s4    61.9      103.24              SOURCE3            1
oh-p5-s6    62.4      101.48              SOURCE3            1
oh-p5-s     62.1      111.30      SOURCE3_SOURCE5            8    1.1112
oh-p5-sh    61.4      101.41              SOURCE3            2
oh-p5-ss    59.8      104.09      SOURCE3_SOURCE5           23    1.4682
o -p5-o     85.5      115.80              SOURCE3           17    5.7902
o -p5-oh    81.9      115.21      SOURCE4_SOURCE5         1716    1.3221
o -p5-os    81.8      115.46      SOURCE3_SOURCE5          843    2.3835
o -p5-p2    71.9      114.60              SOURCE3            1
o -p5-p3    70.6      115.48              SOURCE3            9    2.1084
o -p5-p4    70.1      114.66              SOURCE3            1
o -p5-p5    76.4      113.44              SOURCE3            1
o -p5-s4    60.7      110.23              SOURCE3            1
o -p5-s6    60.3      111.75              SOURCE3            1
o -p5-s     61.7      116.94              SOURCE3            3    2.9506
o -p5-sh    58.5      114.56              SOURCE3            3    1.7645
os-p5-os    83.9      101.84      SOURCE4_SOURCE5          608    1.9896
os-p5-p3    74.1      103.67              SOURCE3            2
os-p5-p5    78.5      104.48              SOURCE3            1
os-p5-s4    62.1      102.52              SOURCE3            1
os-p5-s6    62.3      101.89              SOURCE3            1
o -p5-ss    57.6      114.34      SOURCE3_SOURCE5           37    1.7416
os-p5-s     60.5      117.13      SOURCE4_SOURCE5          200    0.8203
os-p5-sh    61.3      102.05      SOURCE3_SOURCE5            7    0.5915
os-p5-ss    60.3      102.48      SOURCE4_SOURCE5           70    1.4633
p2-p5-p2    74.4      107.14              SOURCE3            1
p3-p5-p3    74.0      105.23              SOURCE3            3    5.1024
p4-p5-p4    74.5      101.62              SOURCE3            1
p5-p5-p5    77.0      112.72              SOURCE3            1
s6-p5-s6    48.7      105.18              SOURCE3            1
sh-p5-sh    47.9      104.56              SOURCE3            1
sh-p5-ss    46.9      107.13              SOURCE3            1
s -p5-s     49.3      114.13              SOURCE3            1
ss-p5-ss    46.0      109.61              SOURCE3            1
cd-pc-n     66.0       90.80              SOURCE3            3    2.3423
cd-pc-na    66.4       90.18              SOURCE3           81    2.7619
cc-pd-n     66.0       90.80              SOURCE3            3
cc-pd-na    66.4       90.18              SOURCE3           81
c2-pe-ca    49.1      101.44              SOURCE3            3    0.7177
c2-pe-ce    48.9      103.01              SOURCE3            4    1.4470
c2-pe-cg    51.6      104.03              SOURCE3            3    3.8740
c2-pe-n2    69.4       94.14              SOURCE3            1
c2-pe-ne    64.7       98.70              SOURCE3           12    5.3383
c2-pe-o     63.1      115.16              SOURCE3            2    0.0149
c2-pe-p2    65.2      107.82              SOURCE3            1
c2-pe-pe    61.7      102.99              SOURCE3            9    8.2860
c2-pe-px    65.4       97.37              SOURCE3            4    0.6655
c2-pe-py    65.2       96.71              SOURCE3            4    1.2755
c2-pe-s     51.9      111.16              SOURCE3            2
c2-pe-sx    48.6       95.11              SOURCE3            4    0.2676
c2-pe-sy    47.7       95.56              SOURCE3            2    0.0462
ca-pe-n2    63.3      102.03              SOURCE3            1
ca-pe-o     62.0      106.88              SOURCE3            2    0.0018
ca-pe-p2    65.2      100.79              SOURCE3            1
ca-pe-pf    62.0       99.70              SOURCE3            2
ca-pe-s     50.6      107.93              SOURCE3            1
c -pe-c2    48.8       97.30              SOURCE3            3    0.0335
ce-pe-n2    64.0      100.55              SOURCE3            1
ce-pe-o     62.1      107.44              SOURCE3            1
ce-pe-p2    65.8       99.56              SOURCE3            1
ce-pe-s     51.3      105.54              SOURCE3            1
cg-pe-n2    68.4      101.79              SOURCE3            1
cg-pe-o     66.9      107.62              SOURCE3            1
cg-pe-p2    67.2      104.68              SOURCE3            2    5.1435
cg-pe-s     53.4      108.60              SOURCE3            4    2.6981
n2-pe-n2    85.4      108.14              SOURCE3            1
n2-pe-ne    81.0      106.80              SOURCE3            6    4.5981
n2-pe-o     83.2      115.39              SOURCE3            1
n2-pe-p2    82.7      111.60              SOURCE3            1
n2-pe-pe    76.2      109.40              SOURCE3            1
n2-pe-px    78.7      110.30              SOURCE3            3    6.0548
n2-pe-py    84.7       93.68              SOURCE3            1
n2-pe-s     66.2      114.84              SOURCE3            3    3.6512
n2-pe-sx    60.8       97.83              SOURCE3            1
n2-pe-sy    59.6       98.14              SOURCE3            1
ne-pe-o     80.0      110.24              SOURCE3            3    3.8478
ne-pe-p2    82.5      104.48              SOURCE3            2    7.1207
ne-pe-s     65.1      109.19              SOURCE3            5    3.6708
o -pe-o     82.1      119.96              SOURCE3            1
o -pe-p2    82.0      114.23              SOURCE3            1
o -pe-pe    66.1      145.96              SOURCE3            1
o -pe-px    81.0      104.37              SOURCE3            1
o -pe-py    80.3      104.49              SOURCE3            1
o -pe-s     65.8      117.42              SOURCE3            2    0.0426
o -pe-sx    58.3      106.59              SOURCE3            1
o -pe-sy    57.6      105.04              SOURCE3            1
p2-pe-pe    85.0       98.24              SOURCE3            1
p2-pe-px    83.1      108.28              SOURCE3            2    6.2959
p2-pe-py    81.7      110.87              SOURCE3            3    8.1645
p2-pe-s     68.3      111.28              SOURCE3            1
p2-pe-sx    65.5       95.73              SOURCE3            1
p2-pe-sy    64.5       95.95              SOURCE3            1
pe-pe-s     64.5      107.91              SOURCE3            2    1.5577
px-pe-s     66.5      107.62              SOURCE3            2    3.7266
py-pe-s     65.7      108.73              SOURCE3            3    5.3201
s -pe-s     43.4      178.44              SOURCE3            1
s -pe-sx    48.8      108.32              SOURCE3            2    3.0318
s -pe-sy    48.4      106.93              SOURCE3            1
c2-pf-ca    49.1      101.44              SOURCE3            3
c2-pf-cf    48.9      103.01              SOURCE3            4
c2-pf-ch    51.6      104.03              SOURCE3            3
c2-pf-n2    69.4       94.14              SOURCE3            1
c2-pf-nf    64.7       98.70              SOURCE3           12
c2-pf-o     63.1      115.16              SOURCE3            2
c2-pf-p2    65.2      107.82              SOURCE3            1
c2-pf-pf    61.7      102.99              SOURCE3            9
c2-pf-px    65.4       97.37              SOURCE3            4
c2-pf-py    65.2       96.71              SOURCE3            4
c2-pf-s     51.9      111.16              SOURCE3            2
c2-pf-sx    48.6       95.11              SOURCE3            4
c2-pf-sy    47.7       95.56              SOURCE3            2
ca-pf-n2    63.3      102.03              SOURCE3            1
ca-pf-o     62.0      106.88              SOURCE3            2
ca-pf-p2    65.2      100.79              SOURCE3            1
ca-pf-pe    62.0       99.70              SOURCE3            2
ca-pf-s     50.6      107.93              SOURCE3            1
c -pf-c2    48.8       97.30              SOURCE3            3
cf-pf-n2    64.0      100.55              SOURCE3            1
cf-pf-o     62.1      107.44              SOURCE3            1
cf-pf-p2    65.8       99.56              SOURCE3            1
cf-pf-s     51.3      105.54              SOURCE3            1
ch-pf-n2    68.4      101.79              SOURCE3            1
ch-pf-o     66.9      107.62              SOURCE3            1
ch-pf-p2    67.2      104.68              SOURCE3            2
ch-pf-s     53.4      108.60              SOURCE3            4
n2-pf-n2    85.4      108.14              SOURCE3            1
n2-pf-nf    81.0      106.80              SOURCE3            6
n2-pf-o     83.2      115.39              SOURCE3            1
n2-pf-p2    82.7      111.60              SOURCE3            1
n2-pf-pf    76.2      109.40              SOURCE3            1
n2-pf-px    78.7      110.30              SOURCE3            3
n2-pf-py    84.7       93.68              SOURCE3            1
n2-pf-s     66.2      114.84              SOURCE3            3
n2-pf-sx    60.8       97.83              SOURCE3            1
n2-pf-sy    59.6       98.14              SOURCE3            1
nf-pf-o     80.0      110.24              SOURCE3            3
nf-pf-p2    82.5      104.48              SOURCE3            2
nf-pf-s     65.1      109.19              SOURCE3            5
o -pf-o     82.1      119.96              SOURCE3            1
o -pf-p2    82.0      114.23              SOURCE3            1
o -pf-pf    66.1      145.96              SOURCE3            1
o -pf-px    81.0      104.37              SOURCE3            1
o -pf-py    80.3      104.49              SOURCE3            1
o -pf-s     65.8      117.42              SOURCE3            2
o -pf-sx    58.3      106.59              SOURCE3            1
o -pf-sy    57.6      105.04              SOURCE3            1
p2-pf-pf    85.0       98.24              SOURCE3            1
p2-pf-px    83.1      108.28              SOURCE3            2
p2-pf-py    81.7      110.87              SOURCE3            3
p2-pf-s     68.3      111.28              SOURCE3            1
p2-pf-sx    65.5       95.73              SOURCE3            1
p2-pf-sy    64.5       95.95              SOURCE3            1
pf-pf-s     64.5      107.91              SOURCE3            2
px-pf-s     66.5      107.62              SOURCE3            2
py-pf-s     65.7      108.73              SOURCE3            3
s -pf-s     43.4      178.44              SOURCE3            1
s -pf-sx    48.8      108.32              SOURCE3            2
s -pf-sy    48.4      106.93              SOURCE3            1
c3-px-ca    46.6      104.79              SOURCE3            1
c3-px-ce    46.7      104.86              SOURCE3            4    0.6354
c3-px-cf    46.7      104.86              SOURCE3            4
c3-px-ne    61.0      102.46              SOURCE3            7    1.8685
c3-px-nf    61.0      102.46              SOURCE3            7
c3-px-o     60.3      113.79      SOURCE3_SOURCE5           33    4.2352
c3-px-pe    61.1      105.73              SOURCE3           10    4.4059
c3-px-pf    61.1      105.73              SOURCE3           10
c3-px-py    58.2      103.11              SOURCE3            3    0.8680
c3-px-sx    45.5       99.55              SOURCE3            1
c3-px-sy    44.5      103.41              SOURCE3            1
ca-px-ca    46.8      104.15              SOURCE3            2    3.6168
ca-px-o     62.1      107.50              SOURCE3            5    5.7355
c -px-c3    46.3      101.72              SOURCE3            1
ce-px-ce    46.9      104.21              SOURCE3            1
ce-px-o     60.5      113.79              SOURCE3            6    0.3877
cf-px-cf    46.9      104.21              SOURCE3            1
cf-px-o     60.5      113.79              SOURCE3            6
c -px-o     58.3      114.47              SOURCE3            1
ne-px-ne    79.1      103.22              SOURCE3            2    0.6807
ne-px-o     79.3      114.13              SOURCE3           11    8.9737
nf-px-nf    79.1      103.22              SOURCE3            2
nf-px-o     79.3      114.13              SOURCE3           11
o -px-pe    76.8      116.50              SOURCE3           12    8.2925
o -px-pf    76.8      116.50              SOURCE3           12
o -px-py    71.4      114.20              SOURCE3            5    1.7165
o -px-sx    54.9      112.81              SOURCE3            3    0.8799
o -px-sy    54.6      113.54              SOURCE3            3    0.5010
pe-px-pe    79.6      110.71              SOURCE3            1
pf-px-pf    79.6      110.71              SOURCE3            1
py-px-py    73.5      107.78              SOURCE3            1
sx-px-sx    46.4       96.24              SOURCE3            1
sy-px-sy    44.8      102.36              SOURCE3            1
c3-py-n4    57.3      103.83              SOURCE3            4
c3-py-na    59.3      106.89              SOURCE3            2
c3-py-o     59.4      116.68      SOURCE3_SOURCE5           22    1.9051
c3-py-oh    62.6      100.16              SOURCE3            2
c3-py-os    61.0      105.39              SOURCE3            1
c3-py-px    57.2      106.27              SOURCE3            2
c3-py-py    56.5      109.83      SOURCE3_SOURCE5           16    1.4525
c3-py-sx    43.7      106.36              SOURCE3            4
ca-py-ca    46.3      107.55              SOURCE3            1
ca-py-o     60.6      114.33      SOURCE3_SOURCE5           20    1.3895
ca-py-oh    62.3      102.87      SOURCE4_SOURCE5           16    1.4519
ca-py-os    62.8      101.36      SOURCE3_SOURCE5           12    1.6676
c -py-c3    44.8      110.36              SOURCE3            1
c -py-c     45.8      104.20              SOURCE3            1
ce-py-ce    46.8      106.54              SOURCE3            1
ce-py-o     61.0      114.04      SOURCE3_SOURCE5           17    2.0725
ce-py-oh    62.0      104.77              SOURCE3            6    2.1852
ce-py-os    61.9      104.88      SOURCE3_SOURCE5            7    1.2571
cf-py-cf    46.8      106.54              SOURCE3            1
cf-py-o     61.0      114.04      SOURCE3_SOURCE5           12    1.5779
cf-py-oh    62.0      104.77              SOURCE3            6
cf-py-os    61.9      104.88      SOURCE3_SOURCE5            7    1.2571
c -py-o     59.5      114.00      SOURCE3_SOURCE5           17    1.4765
c -py-oh    61.1      103.22      SOURCE3_SOURCE5           16    1.4543
c -py-os    62.0      100.01      SOURCE3_SOURCE5           14    3.2269
n3-py-ne    79.4      108.76      SOURCE4_SOURCE5           30    1.0660
n4-py-o     72.9      115.58              SOURCE3            4
n4-py-py    98.9       55.10              SOURCE3            4
na-py-o     76.5      122.40              SOURCE3            2
na-py-py   105.8       50.88              SOURCE3            2
ne-py-ne    78.4      118.19      SOURCE3_SOURCE5           35    1.2083
ne-py-o     82.9      113.21              SOURCE3           15    3.8894
ne-py-oh    83.0      104.70              SOURCE3           26    2.7513
ne-py-os    81.6      108.29      SOURCE3_SOURCE5           23    1.6881
nf-py-nf    78.4      118.19      SOURCE3_SOURCE5           35    1.2083
nf-py-o     82.9      113.21              SOURCE3           15
nf-py-oh    83.0      104.70              SOURCE3           26
nf-py-os    81.6      108.29      SOURCE3_SOURCE5           23    1.6881
oh-py-oh    83.9      101.68      SOURCE3_SOURCE5           49    1.9218
oh-py-pe    79.3      104.84              SOURCE3           22    2.0337
oh-py-pf    79.3      104.84              SOURCE3           22
oh-py-px    74.2      104.30              SOURCE3            8    1.2772
oh-py-py    76.0      100.45              SOURCE3            6
oh-py-sx    57.4      100.94              SOURCE3            4
oh-py-sy    59.1      101.47              SOURCE3            6    0.2490
o -py-oh    81.6      115.83      SOURCE3_SOURCE5          105    1.8918
o -py-os    81.5      115.99      SOURCE3_SOURCE5           47    1.2146
o -py-pe    76.9      114.56              SOURCE3           12    3.6114
o -py-pf    76.9      114.56              SOURCE3           12
o -py-px    72.3      111.37              SOURCE3            5    0.3803
o -py-py    69.9      120.43              SOURCE3           16    6.0629
os-py-os    83.8      101.82      SOURCE3_SOURCE5           27    1.5502
os-py-py    74.5      104.59      SOURCE3_SOURCE5            5    0.4023
os-py-sx    56.6      103.86              SOURCE3            2
os-py-sy    58.9      102.12              SOURCE3            2
o -py-sx    53.2      118.56              SOURCE3            7    6.2976
o -py-sy    56.7      111.71              SOURCE3            5    1.1937
pe-py-pe    80.1      107.14              SOURCE3            1
pf-py-pf    80.1      107.14              SOURCE3            1
py-py-py    72.4      112.70              SOURCE3            1
py-py-sx    75.0       61.54              SOURCE3            4
sy-py-sy    45.6      105.17              SOURCE3            1
c1-s2-o     94.3      117.25              SOURCE3            1
c2-s2-n2    98.1      110.84              SOURCE3            1
c2-s2-o     94.9      114.70              SOURCE2            1
cl-s2-n1    93.0      117.70              SOURCE2            1
f -s2-n1   122.9      116.90              SOURCE2            1
n1-s2-o    128.0      108.46            HF/6-31G*            1
n2-s2-o    117.9      121.20              SOURCE2            2    0.8000
o -s2-o    118.4      116.17              SOURCE3            1
o -s2-s     91.4      118.30              SOURCE2            1
s -s2-s     74.8      115.04              SOURCE3            1
br-s4-br    74.7       98.02              SOURCE3            1
br-s4-c3    72.4       92.98              SOURCE3            1
br-s4-o     84.0      112.07              SOURCE3            1
c1-s4-c1    77.1       93.55              SOURCE3            1
c1-s4-o     94.4      110.36              SOURCE3            2
c2-s4-c2    73.1      102.29              SOURCE3            1
c2-s4-c3    74.4       94.95              SOURCE3            1
c2-s4-o     95.3      107.09              SOURCE3            1
c3-s4-c3    72.5       96.12      SOURCE3_SOURCE5           72    1.2506
c3-s4-ca    73.8       95.00              SOURCE3            1
c3-s4-f    100.0       91.70              SOURCE3            1
c3-s4-hs    53.2       90.60              SOURCE3            1
c3-s4-i     64.2       90.53              SOURCE3            1
c3-s4-n2    98.7       90.59              SOURCE3            1
c3-s4-n3    92.8       95.77      SOURCE3_SOURCE5           10    1.8721
c3-s4-n     92.4       96.07              SOURCE3            4    1.0354
c3-s4-n4    88.9       92.47              SOURCE3            1
c3-s4-na    93.2       93.07              SOURCE3           10    1.8813
c3-s4-nh    92.3       97.08              SOURCE3            1
c3-s4-no    89.7       89.53              SOURCE3            1
c3-s4-o     92.9      106.71      SOURCE3_SOURCE5          233    1.1391
c3-s4-oh    97.0       90.28      SOURCE4_SOURCE5           21    0.2709
c3-s4-os    97.2       90.06              SOURCE3            4    0.4484
c3-s4-p2    91.0       94.37              SOURCE3            1
c3-s4-p3    93.0       96.54              SOURCE3            4    1.3634
c3-s4-p4    87.8       97.40              SOURCE3            1
c3-s4-p5    93.2       99.18              SOURCE3            1
c3-s4-s4    75.5       89.50              SOURCE3            1
c3-s4-s     71.9       98.72              SOURCE3            2    0.0185
c3-s4-s6    72.3       97.48              SOURCE3            1
c3-s4-sh    71.3       94.66              SOURCE3            1
c3-s4-ss    71.1       95.31              SOURCE3            3    1.4101
ca-s4-ca    74.6       95.21              SOURCE3            1
ca-s4-o     94.5      106.63              SOURCE3            1
c -s4-c3    72.1       95.07              SOURCE3            1
c -s4-c     74.7       86.83              SOURCE3            1
cl-s4-cl    92.6       97.68              SOURCE3            1
cl-s4-o    100.5      108.34              SOURCE3            2
c -s4-o     91.6      106.17              SOURCE3            1
cx-s4-cx   102.3       48.80              SOURCE2            1
cx-s4-o     90.2      108.52               5/2017            2    1.8844
f -s4-f    137.1       92.71              SOURCE2            3    0.1490
f -s4-o    129.3      106.81              SOURCE2            2    0.0100
f -s4-s     90.8      107.50              SOURCE2            1
hs-s4-hs    42.7       87.00              SOURCE3            2    0.0202
hs-s4-n1    72.3       90.51            HF/6-31G*            1
hs-s4-o     69.7      110.27              SOURCE3            5    0.1908
i -s4-i     68.0       97.29              SOURCE3            1
i -s4-o     69.9      113.91              SOURCE3            1
n1-s4-n1   127.6       94.02            HF/6-31G*            1
n1-s4-o    122.8      110.09            HF/6-31G*            1
n2-s4-n2   133.5       90.17              SOURCE3            1
n2-s4-o    126.1      107.57              SOURCE3            1
n3-s4-n3   121.8       91.19              SOURCE3            1
n3-s4-o    117.8      110.43      SOURCE3_SOURCE5           13    1.9165
n4-s4-n4   106.4       94.61              SOURCE3            1
n4-s4-o    110.6      104.91              SOURCE3            3    0.4370
na-s4-na   112.1      103.10              SOURCE3            1
na-s4-o    116.4      109.75              SOURCE3           10    2.6919
nh-s4-nh   121.5       92.24              SOURCE3            1
nh-s4-o    119.7      107.54              SOURCE3            3    0.0401
n -s4-n    120.8       91.30              SOURCE3            1
n -s4-o    118.8      107.44      SOURCE3_SOURCE5            9    1.2433
no-s4-no   112.0       83.40              SOURCE3            1
no-s4-o    110.2      103.58              SOURCE3            3    1.5109
oh-s4-oh   120.2      100.34              SOURCE3            1
o -s4-o    127.0      114.11      SOURCE3_SOURCE5           14    2.6371
o -s4-oh   120.7      110.10      SOURCE4_SOURCE5           30    0.8834
o -s4-os   121.9      108.22      SOURCE3_SOURCE5           19    1.5128
o -s4-p2   110.6      106.77              SOURCE3            1
o -s4-p3   115.8      106.51              SOURCE3            8    4.0943
o -s4-p4   109.5      103.36              SOURCE3            1
o -s4-p5   123.8       96.95              SOURCE3            1
o -s4-s4    91.3      104.55              SOURCE3            1
o -s4-s     88.3      112.22              SOURCE3            4    2.8682
o -s4-s6    92.1      102.84              SOURCE3            1
o -s4-sh    86.7      107.51              SOURCE3            3    0.7511
os-s4-os   124.4       94.07      SOURCE3_SOURCE5            7    2.3843
o -s4-ss    86.0      109.49              SOURCE3            5    1.8509
p2-s4-p2   118.9       92.62              SOURCE3            1
p3-s4-p3   122.7       95.71              SOURCE3            2    1.2239
p5-s4-p5   126.8       93.86              SOURCE3            1
s4-s4-s4    77.0       90.17              SOURCE3            1
s4-s4-s6    77.0       90.17              SOURCE3            1
s6-s4-s6    75.6       93.52              SOURCE3            1
sh-s4-sh    69.2      102.76              SOURCE3            1
sh-s4-ss    69.3      102.64              SOURCE3            1
s -s4-s     70.5      108.08              SOURCE3            1
ss-s4-ss    71.9       95.47              SOURCE3            1
br-s6-br    77.6      101.57              SOURCE3            1
br-s6-c3    73.5       98.99              SOURCE3            1
br-s6-f     94.6      100.60              SOURCE2            1
br-s6-o     90.7      107.58              SOURCE3            6    0.3000
c1-s6-c1    75.6       99.99              SOURCE3            1
c1-s6-o     97.4      107.98      SOURCE3_SOURCE5            7    0.4450
c2-s6-c2    73.0      102.75              SOURCE3            1
c2-s6-c3    71.5      104.05              SOURCE3            1
c2-s6-o     96.5      106.58              SOURCE3            1
c3-s6-c3    70.7      103.83      SOURCE3_SOURCE5           74    2.0698
c3-s6-ca    71.7      103.17              SOURCE3            1
c3-s6-cy    73.1       94.76               5/2017           11    0.5208
c3-s6-f     98.1       95.90      SOURCE3_SOURCE5            9    2.4171
c3-s6-hs    51.1      100.62              SOURCE3            1
c3-s6-i     61.8       97.74              SOURCE3            1
c3-s6-n2    90.4      112.48      SOURCE4_SOURCE5           27    1.7086
c3-s6-n3    92.5      101.97      SOURCE4_SOURCE5          162    1.1030
c3-s6-n     90.8      103.44      SOURCE3_SOURCE5           15    0.8616
c3-s6-n4    87.7       99.40              SOURCE3            3    0.4695
c3-s6-na    91.0      102.81              SOURCE3           10    3.1256
c3-s6-nh    90.9      104.32      SOURCE4_SOURCE5           92    1.5234
c3-s6-no    86.0       99.57              SOURCE3            1
c3-s6-o     93.7      108.61      SOURCE3_SOURCE5         1062    1.0758
c3-s6-oh    94.8       98.74      SOURCE4_SOURCE5          121    0.7363
c3-s6-os    96.2       96.42      SOURCE4_SOURCE5           70    0.5868
c3-s6-p2    86.3      106.47              SOURCE3            1
c3-s6-p3    90.6      103.40              SOURCE3            3    0.8516
c3-s6-p4    84.6      104.12              SOURCE3            1
c3-s6-p5    91.6      103.46              SOURCE3            1
c3-s6-s4    72.4       98.10              SOURCE3            1
c3-s6-s     71.1      104.50              SOURCE3            1
c3-s6-s6    71.0      101.95              SOURCE3            1
c3-s6-sh    70.4      101.84              SOURCE3            1
c3-s6-ss    70.0      102.47              SOURCE3            3    1.7451
ca-s6-ca    72.6      103.08              SOURCE3            1
ca-s6-o     97.4      104.09      SOURCE4_SOURCE5          137    0.5743
c -s6-c3    70.3      101.24              SOURCE3            1
c -s6-c     69.7       99.82              SOURCE3            1
cc-s6-o     95.6      103.76      SOURCE4_SOURCE5           24    0.8201
cl-s6-cl    91.0      101.25              SOURCE3            1
cl-s6-f    105.6       99.00              SOURCE2            1
cl-s6-o    101.2      107.52      SOURCE3_SOURCE5            6    0.2106
c -s6-o     91.5      107.97              SOURCE3            1
c -s6-os    91.5      102.12              SOURCE3            1
cx-s6-cx   101.7       54.70              SOURCE2            1
cy-s6-o     91.1      110.64               5/2017           51    0.8806
f -s6-f    137.6       89.71      SOURCE2_SOURCE5           22    1.8574
f -s6-o    130.2      106.54      SOURCE3_SOURCE5            7    0.0793
hs-s6-hs    40.5       99.02              SOURCE3            2    0.0595
hs-s6-n1    77.2       97.27            HF/6-31G*            1
hs-s6-o     72.3      107.68      SOURCE3_SOURCE5           17    0.0882
i -s6-i     67.3       99.25              SOURCE3            1
i -s6-o     70.9      108.82      SOURCE3_SOURCE5            6    0.6545
n1-s6-n1   147.5       95.52            HF/6-31G*            1
n1-s6-o    137.2      107.52            HF/6-31G*            1
n2-s6-n2   132.3       98.61              SOURCE3            1
n2-s6-o    124.1      119.10      SOURCE3_SOURCE5           11    3.0533
n2-s6-oh   123.7      106.96              SOURCE3            2
n2-s6-os   126.4      103.25              SOURCE3            1
n3-s6-n3   123.0       98.44      SOURCE4_SOURCE5           16    0.3984
n3-s6-o    124.8      107.43      SOURCE3_SOURCE5          319    1.1452
n3-s6-os   124.1       99.66      SOURCE4_SOURCE5           27    0.8063
n4-s6-n4   105.7      101.85              SOURCE3            1
n4-s6-o    115.1      102.92              SOURCE3           10    1.5434
na-s6-na   119.7       98.04              SOURCE3            1
na-s6-o    123.2      105.82      SOURCE3_SOURCE5           31    0.6987
nh-s6-nh   123.7       94.56              SOURCE3            1
nh-s6-o    123.7      107.21      SOURCE3_SOURCE5          106    1.3795
n -s6-n    116.4      104.16              SOURCE3            1
n -s6-o    122.7      107.02      SOURCE3_SOURCE5           63    1.7044
no-s6-no   107.9       91.63              SOURCE3            1
no-s6-o    109.6      107.43              SOURCE3            6    1.5494
n -s6-os   122.5       99.23      SOURCE4_SOURCE5           10    0.9794
oh-s6-oh   124.7      100.34              SOURCE3            6    0.0076
oh-s6-os   127.4       96.81      SOURCE4_SOURCE5           74    0.8201
oh-s6-p2   108.7      109.67              SOURCE3            2
o -s6-o    128.2      120.05      SOURCE4_SOURCE5          971    1.8153
o -s6-oh   126.3      108.05      SOURCE3_SOURCE5          306    0.8954
o -s6-os   126.6      108.56      SOURCE3_SOURCE5          346    1.4469
o -s6-p2   111.3      106.61              SOURCE3            1
o -s6-p3   116.3      107.07              SOURCE3           22    1.0550
o -s6-p4   107.4      105.67              SOURCE3            1
o -s6-p5   118.5      106.64              SOURCE3            1
o -s6-s4    90.2      107.85              SOURCE3            1
o -s6-s     90.9      110.29              SOURCE3            6    2.2405
o -s6-s6    91.0      106.07              SOURCE3            1
o -s6-sh    89.5      106.81              SOURCE3            6    0.6292
os-s6-os   126.6       98.70              SOURCE3            1
o -s6-ss    88.8      107.43              SOURCE3           10    1.1423
p3-s6-p3   114.9      110.17              SOURCE3            4    5.3678
p5-s6-p5   120.2      104.49              SOURCE3            1
s4-s6-s4    72.4      101.99              SOURCE3            1
s4-s6-s6    77.0       90.17              SOURCE3            1
s6-s6-s6    72.0      103.29              SOURCE3            1
sh-s6-sh    70.0      106.43              SOURCE3            1
sh-s6-ss    71.1      102.64              SOURCE3            1
s -s6-s     71.4      109.34              SOURCE3            1
ss-s6-ss    71.2      101.82              SOURCE3            1
br-sh-hs    49.8       95.64              SOURCE3            1
c1-sh-hs    55.6       95.99 calculated_based_on_C  # C-SH            0
c2-sh-hs    52.8       96.79      SOURCE4_SOURCE5           12    0.5703
c3-sh-hs    51.4       96.40      SOURCE3_SOURCE5          191    0.6428
ca-sh-hs    53.2       95.50      SOURCE4_SOURCE5           44    0.8350
cc-sh-hs    53.6       95.01      SOURCE4_SOURCE5           23    1.3099
c -sh-hs    53.0       94.47      SOURCE3_SOURCE5           41    0.9733
f -sh-hs    71.4       96.50              SOURCE3            1
hs-sh-hs    42.2       93.00      SOURCE3_SOURCE5            3    0.4777
hs-sh-i     44.1       96.44              SOURCE3            1
hs-sh-n1    72.8       93.51            HF/6-31G*            1
hs-sh-n2    67.8       95.82              SOURCE3            5    3.1495
hs-sh-n     68.2       95.59              SOURCE3            4    3.9065
hs-sh-n3    67.7       95.98              SOURCE3            3    1.1735
hs-sh-n4    66.5       93.13              SOURCE3            3    0.1675
hs-sh-na    67.8       97.38              SOURCE3            9    1.0223
hs-sh-nh    66.9      101.11              SOURCE3            1
hs-sh-no    66.8       92.93              SOURCE3            1
hs-sh-o     67.5      109.23              SOURCE3            2    0.0068
hs-sh-oh    68.3       98.64              SOURCE3            2    0.0605
hs-sh-os    69.1       98.15              SOURCE3            3    0.1661
hs-sh-p2    66.1       99.12              SOURCE3           10    5.4110
hs-sh-p3    62.1       95.81              SOURCE3            3    0.4396
hs-sh-p4    63.2       94.22              SOURCE3            4    0.7605
hs-sh-p5    64.1       94.52              SOURCE3            3    0.5589
hs-sh-s     47.2      102.87              SOURCE3            2
hs-sh-s4    48.5       92.16              SOURCE3            3    1.6519
hs-sh-s6    49.5       93.83              SOURCE3            3    1.2561
hs-sh-sh    49.4       99.07              SOURCE3            2
hs-sh-ss    49.1       99.17              SOURCE3            3    0.2457
br-ss-br    77.5      102.92              SOURCE3            1
br-ss-c3    73.4       99.03              SOURCE3            1
c1-ss-c1    77.7       98.30              SOURCE2            1
c1-ss-c3    72.8      101.86      SOURCE2_SOURCE5           24    1.0923
c2-ss-c2    75.2       99.56              SOURCE3            1
c2-ss-c3    72.6      100.37              SOURCE4          100    2.3280
c2-ss-cy    76.7       89.25               5/2017           24    0.5146
c2-ss-n2    92.9      106.76              SOURCE3            1
c2-ss-na    93.8      100.51              SOURCE3            6    6.9702
c2-ss-os   100.0       89.76              SOURCE3            1
c2-ss-ss    75.7       92.26              SOURCE3            1
c3-ss-c3    71.1       99.24      SOURCE3_SOURCE5          443    1.3973
c3-ss-ca    71.1      102.10      SOURCE4_SOURCE5          393    1.3148
c3-ss-cc    72.1      100.64         CORR_SOURCE5          118    1.6668
c3-ss-cd    72.1      100.64         CORR_SOURCE5          118    1.6668
c3-ss-cl    80.0       99.40              SOURCE2            1
c3-ss-cy    72.7       94.24               5/2017           88    0.5356
c3-ss-f     95.8       97.49              SOURCE3            1
c3-ss-i     68.0      100.00              SOURCE3            1
c3-ss-n1    94.4       98.44            HF/6-31G*            1
c3-ss-n2    94.6       96.08      SOURCE3_SOURCE5           11    1.2317
c3-ss-n3    91.9       98.83              SOURCE3            3    0.2909
c3-ss-n     91.1      100.30              SOURCE3            4    0.6579
c3-ss-n4    90.3       97.79              SOURCE3            3    0.2002
c3-ss-na    92.7       96.59      SOURCE3_SOURCE5           21    1.0132
c3-ss-nh    91.3      100.63              SOURCE3            1
c3-ss-no    89.5       98.62              SOURCE3            1
c3-ss-o     92.4      106.99      SOURCE3_SOURCE5           11    1.0097
c3-ss-oh    92.9       98.28              SOURCE3            2    1.4326
c3-ss-os    92.6       98.21              SOURCE3            4    1.7097
c3-ss-p2    95.5       98.41              SOURCE3            8    0.9454
c3-ss-p3    90.9       98.70              SOURCE3            3    0.0356
c3-ss-p4    91.6       98.16              SOURCE3            4    0.1361
c3-ss-p5    90.4      100.06      SOURCE4_SOURCE5           62    1.0141
c3-ss-s4    70.6       96.37              SOURCE3            3    0.0202
c3-ss-s     70.4      101.90              SOURCE3            1
c3-ss-s6    71.6       96.76              SOURCE3            3    1.5680
c3-ss-sh    70.9      101.93              SOURCE3            1
c3-ss-ss    70.3      103.39      SOURCE4_SOURCE5          237    1.0715
ca-ss-ca    73.5       98.83      SOURCE4_SOURCE5          225    1.3938
ca-ss-cc    77.8       89.47         CORR_SOURCE5          200    1.1779
ca-ss-cd    77.8       89.47         CORR_SOURCE5          200    1.1779
ca-ss-cl    80.2      101.05              SOURCE3            1
ca-ss-n     97.4       90.99      SOURCE3_SOURCE5            5    0.5202
ca-ss-na    93.1       99.32              SOURCE3            1
ca-ss-nc    97.9       94.76              SOURCE3            1
ca-ss-nd    97.9       94.76              SOURCE3            1
ca-ss-ss    70.4      105.13      SOURCE4_SOURCE5           69    1.0007
c -ss-c2    76.5       92.43              SOURCE3            1
c -ss-c3    71.8       99.16      SOURCE3_SOURCE5          108    1.2072
c -ss-c     71.8      101.40              SOURCE3            1
c -ss-cc    75.1       94.89      SOURCE4_SOURCE5           32    1.7205
cc-ss-cc    78.0       90.24      SOURCE3_SOURCE5          652    1.5043
cc-ss-cd    77.8       90.76      SOURCE4_SOURCE5          157    1.7485
cc-ss-n     96.8       93.58      SOURCE3_SOURCE5            6    2.0175
cc-ss-na    93.8       99.33              SOURCE3           18
cc-ss-nc    99.5       93.22         CORR_SOURCE5           25    1.5563
cc-ss-os    94.7       98.81              SOURCE3            2    2.1583
cc-ss-ss    74.9       93.80         CORR_SOURCE5           31    0.9858
cd-ss-cd    78.0       90.24      SOURCE3_SOURCE5          652    1.5043
cd-ss-n     96.8       93.58      SOURCE3_SOURCE5            6    2.0175
cd-ss-na    93.8       99.33              SOURCE3           18    2.5847
cd-ss-nd    99.5       93.22         CORR_SOURCE5           25    1.5563
cd-ss-os    94.7       98.81              SOURCE3            2
cd-ss-ss    74.9       93.80         CORR_SOURCE5           31    0.9858
cl-ss-cl    90.1      103.37              SOURCE3            1
cx-ss-cx   102.2       48.30              SOURCE2            1
f -ss-f    129.7       98.30              SOURCE2            1
f -ss-ss    90.1      108.30              SOURCE2            1
i -ss-i     72.6      106.29              SOURCE3            1
n1-ss-n1   128.8       96.96            HF/6-31G*            1
n2-ss-n2   125.3       96.75              SOURCE3            1
n3-ss-n3   117.1      102.34              SOURCE3            1
n4-ss-n4   112.0      101.19              SOURCE3            1
na-ss-na   116.2      102.81              SOURCE3            1
nc-ss-nc   126.8       97.99         CORR_SOURCE5           29    0.5000
nd-ss-nd   126.8       97.99         CORR_SOURCE5           29    0.5000
nh-ss-nh   115.0      107.89              SOURCE3            1
n -ss-n    116.5      103.10              SOURCE3            1
no-ss-no   108.2      106.43              SOURCE3            1
oh-ss-oh   118.4      104.25              SOURCE3            1
o -ss-o    124.0      119.30              SOURCE2            1
o -ss-p5   114.3      106.41              SOURCE3            1
o -ss-s6    89.5      105.39              SOURCE3            1
os-ss-os   118.0      102.99              SOURCE3            1
o -ss-ss    88.2      112.70              SOURCE2            1
p2-ss-p2   127.8       99.52              SOURCE3            1
p3-ss-p3   117.2      101.67              SOURCE3            1
p5-ss-p5   126.6       87.37      SOURCE3_SOURCE5           11    1.2491
s4-ss-s4    71.7       96.08              SOURCE3            1
s4-ss-s6    70.6      101.26              SOURCE3            1
s6-ss-s6    71.2      101.81              SOURCE3            1
sh-ss-sh    71.0      107.54              SOURCE3            1
sh-ss-ss    71.2      106.53              SOURCE3            1
s -ss-s     67.9      115.04              SOURCE3            1
ss-ss-ss    70.7      107.93      SOURCE4_SOURCE5           72    1.6368
c3-sx-ca    72.2       96.64      SOURCE4_SOURCE5           41    0.4942
c3-sx-cc    73.1       95.18      SOURCE4_SOURCE5           41    0.6549
c3-sx-ce    72.9       95.29      SOURCE3_SOURCE5           10    0.5723
c3-sx-cf    72.9       95.29      SOURCE3_SOURCE5            7    0.8172
c3-sx-ne    93.4       90.06              SOURCE3            5    1.9627
c3-sx-nf    93.4       90.06              SOURCE3            5
c3-sx-o     91.9      107.52      SOURCE3_SOURCE5           84    0.7996
c3-sx-pe    91.5       94.32              SOURCE3            7    0.5547
c3-sx-pf    91.5       94.32              SOURCE3            7
c3-sx-px    88.3       96.46              SOURCE3            3    1.3351
c3-sx-py    88.2       95.67              SOURCE3            1
c3-sx-sx    67.2       91.47              SOURCE3            4    1.9919
c3-sx-sy    68.9       95.47              SOURCE3            3    2.8422
ca-sx-ca    72.9       95.75      SOURCE3_SOURCE5           14    1.8607
ca-sx-o     92.7      107.15      SOURCE4_SOURCE5           86    0.9103
c -sx-c3    72.5       92.71              SOURCE3            3    0.3095
c -sx-c     74.1       86.85              SOURCE3            1
cc-sx-o     94.3      104.81      SOURCE4_SOURCE5           45    1.5594
ce-sx-ce    73.5       94.96              SOURCE3            1
ce-sx-o     92.5      108.23      SOURCE3_SOURCE5           27    0.8358
cf-sx-cf    73.5       94.96              SOURCE3            1
cf-sx-o     92.5      108.23      SOURCE3_SOURCE5           22    0.9547
c -sx-o     90.9      106.17              SOURCE3            5    0.9477
ne-sx-ne   107.6      106.45      SOURCE3_SOURCE5            5    1.4815
ne-sx-o    114.1      109.81      SOURCE3_SOURCE5           13    1.0385
nf-sx-nf   107.6      106.45      SOURCE3_SOURCE5            5    1.4815
nf-sx-o    114.1      109.81      SOURCE3_SOURCE5            6    0.5536
o -sx-pe   111.8      106.43              SOURCE3            9    2.8345
o -sx-pf   111.8      106.43              SOURCE3            9
o -sx-px   109.1      104.77              SOURCE3            3    1.9810
o -sx-py   106.2      109.13              SOURCE3            7    5.6840
o -sx-sx    79.8      104.65              SOURCE3            6    3.0524
o -sx-sy    85.1      103.41              SOURCE3            5    0.9618
pe-sx-pe   120.1       92.62              SOURCE3            1
pf-sx-pf   120.1       92.62              SOURCE3            1
py-sx-py   133.3       69.23              SOURCE3            3   17.4143
sx-sx-sx    69.1       84.90              SOURCE3            1
sy-sx-sy    69.8       93.52              SOURCE3            1
c3-sy-ca    70.9      103.93      SOURCE4_SOURCE5          136    0.4172
c3-sy-cc    71.8      101.95      SOURCE4_SOURCE5           32    1.4362
c3-sy-ce    71.1      103.53      SOURCE3_SOURCE5           11    1.3594
c3-sy-cf    71.1      103.53      SOURCE3_SOURCE5            8    1.7429
c3-sy-ne    92.4      102.19      SOURCE3_SOURCE5           11    3.1966
c3-sy-nf    92.4      102.19      SOURCE3_SOURCE5            6    2.3703
c3-sy-o     93.8      107.85      SOURCE3_SOURCE5          283    0.5690
c3-sy-pe    85.5      106.03              SOURCE3            6    2.6117
c3-sy-pf    85.5      106.03              SOURCE3            6
c3-sy-px    85.4      103.62              SOURCE3            3    0.7078
c3-sy-py    87.5      103.39              SOURCE3            3    0.4563
c3-sy-sx    66.1      104.64              SOURCE3            3    4.6276
c3-sy-sy    67.5      100.78              SOURCE3            4    1.1633
ca-sy-ca    71.1      104.44      SOURCE4_SOURCE5           55    1.7845
ca-sy-cc    71.0      105.09      SOURCE4_SOURCE5           10    0.3628
ca-sy-n3    92.2      102.44      SOURCE4_SOURCE5          407    1.1038
ca-sy-n     90.5      105.37      SOURCE4_SOURCE5          122    1.2203
ca-sy-ne    92.5      103.01      SOURCE4_SOURCE5           36    2.1672
ca-sy-nh    90.5      105.50      SOURCE4_SOURCE5          205    1.5936
ca-sy-o     94.3      108.35      SOURCE3_SOURCE5         1362    0.6985
ca-sy-oh    93.8      101.30      SOURCE4_SOURCE5           94    0.8210
ca-sy-os    96.8       92.98              SOURCE3            1
c -sy-c3    70.4      101.25              SOURCE3            3    1.1850
c -sy-c     69.9       99.81              SOURCE3            1
cc-sy-n3    92.4      102.53         CORR_SOURCE5           35    0.5689
cc-sy-o     94.8      107.89         CORR_SOURCE5          130    0.8911
cd-sy-n3    92.4      102.53         CORR_SOURCE5           35    0.5689
cd-sy-nh    94.5       97.20      SOURCE4_SOURCE5           12    0.2429
cd-sy-o     94.8      107.89         CORR_SOURCE5          130    0.8911
ce-sy-ce    71.8      102.78              SOURCE3            1
ce-sy-o     94.4      108.38      SOURCE3_SOURCE5           66    0.9753
cf-sy-cf    71.8      102.78              SOURCE3            1
cf-sy-o     94.4      108.38      SOURCE3_SOURCE5           56    1.0516
c -sy-o     91.7      107.48      SOURCE3_SOURCE5           16    0.7996
n2-sy-o    121.9      123.53              SOURCE4            6    1.2388
n3-sy-ne   120.0      101.93      SOURCE4_SOURCE5           15    1.4395
n3-sy-o    123.4      107.13      SOURCE4_SOURCE5          863    1.1609
na-sy-na   119.4       98.04              SOURCE3            1
nc-sy-nc   132.6       98.04              SOURCE3            2
nd-sy-nd   132.6       98.04              SOURCE3            2
ne-sy-ne   122.9       98.62              SOURCE3            1
ne-sy-o    123.2      109.65      SOURCE3_SOURCE5          101    1.9902
nf-sy-nf   122.9       98.62              SOURCE3            1
nf-sy-o    123.2      109.65      SOURCE3_SOURCE5           87    1.9451
nh-sy-o    123.1      106.23      SOURCE4_SOURCE5          319    1.7353
n -sy-o    122.2      107.54      SOURCE4_SOURCE5          155    1.8699
o -sy-o    126.4      121.41      SOURCE3_SOURCE5          734    0.8526
o -sy-oh   126.0      106.68      SOURCE3_SOURCE5          166    0.5588
o -sy-os   123.1      107.52      SOURCE4_SOURCE5           38    1.6656
o -sy-pe   109.5      106.90              SOURCE3           12    1.4524
o -sy-pf   109.5      106.90              SOURCE3           12
o -sy-px   108.1      106.17              SOURCE3            6    0.7059
o -sy-py   111.2      106.67              SOURCE3           10    0.6478
o -sy-sx    84.0      106.33              SOURCE3           10    2.0456
o -sy-sy    84.2      106.19              SOURCE3           12    0.1754
py-sy-py   112.3      104.49              SOURCE3            1
sx-sy-sx    66.8      101.99              SOURCE3            1
sy-sy-sy    66.5      103.29              SOURCE3            1
c2-c1-cf    60.0      179.05      SOURCE4_SOURCE5            9    0.3913
c3-c1-ch    57.7      178.43      SOURCE4_SOURCE5           95    0.5682
nf-c1-s     73.6      175.82      SOURCE4_SOURCE5           15    0.2067
br-c2-cf    64.3      121.53      SOURCE4_SOURCE5           11    0.7009
cd-c2-h4    49.8      119.85      SOURCE4_SOURCE5           16    0.8001
cd-c2-nh    86.6      123.12      SOURCE4_SOURCE5           17    1.2171
cd-c2-o     91.4      123.59      SOURCE4_SOURCE5            6    0.0560
cf-c2-cl    72.1      123.47      SOURCE4_SOURCE5           30    1.0225
cf-c2-h4    49.7      122.31      SOURCE4_SOURCE5          145    1.6214
cf-c2-na    86.1      124.17      SOURCE4_SOURCE5            6    1.9423
cf-c2-nh    87.8      120.71      SOURCE4_SOURCE5          150    2.3947
cf-c2-no    86.1      119.65      SOURCE4_SOURCE5            5    0.9817
cf-c2-o     92.0      123.37      SOURCE4_SOURCE5            9    1.0481
cf-c2-oh    88.6      123.13      SOURCE4_SOURCE5           62    1.7479
cf-c2-os    88.0      122.80      SOURCE4_SOURCE5           98    2.2743
h4-c2-nf    64.9      119.51      SOURCE4_SOURCE5           42    1.6302
h5-c2-nf    64.7      119.85      SOURCE4_SOURCE5           27    1.3790
nf-c2-os   114.2      118.76              SOURCE4            5
nf-c2-ss    82.2      120.51      SOURCE4_SOURCE5           23    2.4188
n -c2-nf   109.3      125.34      SOURCE4_SOURCE5           15    1.5591
ca-c3-cf    65.6      112.21      SOURCE4_SOURCE5           93    1.2595
cd-c3-cx    65.7      112.40               5/2017            1
c -c3-cf    65.5      111.89      SOURCE4_SOURCE5           59    1.5769
cd-c3-hx    47.6      111.01      SOURCE4_SOURCE5           10    0.7123
cd-c3-n2    84.6      110.31      SOURCE4_SOURCE5           21    0.5628
cd-c3-n4    81.5      115.58      SOURCE4_SOURCE5            6    1.1723
cd-c3-na    83.6      113.15      SOURCE4_SOURCE5           10    0.6466
cd-c3-p5    79.5      116.23      SOURCE4_SOURCE5            6    0.7766
cf-c3-cf    65.8      111.47      SOURCE4_SOURCE5           35    0.5985
cf-c3-n     84.3      110.22      SOURCE4_SOURCE5           10    1.0919
cf-c3-oh    85.0      111.19      SOURCE4_SOURCE5           57    1.5702
cf-c3-os    85.4      109.50      SOURCE4_SOURCE5           55    1.8883
cf-c3-ss    63.3      110.72      SOURCE4_SOURCE5           12    1.7025
cd-ca-cq    66.0      124.30      SOURCE4_SOURCE5           10    0.6423
cf-ca-na    84.1      119.92      SOURCE4_SOURCE5           29    0.5242
ch-ca-cq    67.3      121.53      SOURCE4_SOURCE5           12    0.1831
cl-ca-cq    71.7      120.39      SOURCE4_SOURCE5           34    0.5366
cq-ca-f     88.8      119.42      SOURCE4_SOURCE5           30    0.2799
cq-ca-h4    48.4      120.09      SOURCE4_SOURCE5           35    0.4098
cq-ca-na    90.7      108.79      SOURCE4_SOURCE5          349    0.5003
cq-ca-nb    86.4      123.58      SOURCE4_SOURCE5           79    0.8527
cq-ca-nh    85.7      121.56      SOURCE4_SOURCE5           19    0.6123
cq-ca-oh    86.6      120.85      SOURCE4_SOURCE5           29    1.4592
cq-ca-ss    66.0      111.17      SOURCE4_SOURCE5           16    2.4162
ca-c -nf    85.3      114.71      SOURCE4_SOURCE5            9    0.7464
br-cd-c     65.2      116.28      SOURCE4_SOURCE5           24    1.3164
br-cd-cd    63.4      124.05      SOURCE4_SOURCE5           23    1.9356
br-cd-cc    63.7      124.23      SOURCE4_SOURCE5           84    2.2845
br-cd-na    80.6      121.58      SOURCE4_SOURCE5           13    0.9881
ca-cd-cf    64.3      127.01      SOURCE4_SOURCE5           27    1.6430
ca-cd-nh    84.3      122.13      SOURCE4_SOURCE5           11    2.0536
cd-c -cf    66.4      115.57      SOURCE4_SOURCE5            8    1.2130
cd-cd-f     88.4      119.19      SOURCE4_SOURCE5           19    1.0481
c -cd-ch    67.0      117.88      SOURCE4_SOURCE5           19    0.6396
cd-cd-sy    61.1      128.25      SOURCE4_SOURCE5           12    0.8482
cc-cd-f     89.6      121.19      SOURCE4_SOURCE5           54    0.6386
cc-cd-no    82.9      128.69      SOURCE4_SOURCE5          197    1.4212
c -cd-f     87.8      116.98      SOURCE4_SOURCE5           33    0.4384
ch-cd-na    84.9      122.61      SOURCE4_SOURCE5            7    1.0826
ch-cd-ss    63.8      120.73      SOURCE4_SOURCE5           15    0.9326
cd-c -h4    47.6      114.83      SOURCE4_SOURCE5           20    0.4400
cl-cd-na    90.5      121.12      SOURCE4_SOURCE5           25    0.9015
cl-cd-ss    71.9      119.85      SOURCE4_SOURCE5           16    0.8775
c -cd-nf    84.5      119.88              SOURCE4            6
cd-c -s     64.0      126.28      SOURCE4_SOURCE5           57    2.2083
cd-c -ss    64.4      112.40      SOURCE4_SOURCE5           32    1.0830
cx-cd-nc    85.6      119.81               5/2017            2
cx-cd-os    85.4      118.07      SOURCE4_SOURCE5           13    0.0898
cc-c -cx    65.4      117.59               5/2017            1
cc-c -nc    86.5      113.75      SOURCE4_SOURCE5           14    0.0860
cf-c -cx    65.0      117.91               5/2017           13    0.7631
cf-c -h4    47.2      114.89      SOURCE4_SOURCE5           94    0.4993
cf-c -ss    64.8      110.49      SOURCE4_SOURCE5            8    0.5728
na-cd-no   105.3      124.59      SOURCE4_SOURCE5          114    0.8160
na-cd-oh   111.7      117.48      SOURCE4_SOURCE5           23    1.0304
na-cd-sx    79.7      117.02      SOURCE4_SOURCE5           19    0.3766
na-cd-sy    79.5      120.46      SOURCE4_SOURCE5            8    1.7069
nd-cd-no   106.9      121.73      SOURCE4_SOURCE5           10    0.8384
nc-cd-nc   110.8      128.07      SOURCE4_SOURCE5           10    0.4198
nc-cd-nf   107.8      129.01      SOURCE4_SOURCE5           13    1.6879
nc-cd-no   108.2      122.75      SOURCE4_SOURCE5           64    0.2909
nc-cd-sh    79.2      124.97      SOURCE4_SOURCE5           13    0.8081
nc-cd-sx    76.8      127.74      SOURCE4_SOURCE5           19    0.3234
nc-cd-sy    79.3      123.03      SOURCE4_SOURCE5           20    1.2273
nf-cd-ss    81.7      117.03      SOURCE4_SOURCE5           10    0.2421
n -cd-n2   112.9      119.42      SOURCE4_SOURCE5           13    0.1189
no-cd-os   109.1      117.55      SOURCE4_SOURCE5           82    0.2764
no-cd-ss    79.7      121.06      SOURCE4_SOURCE5           23    0.2526
ca-cc-cf    66.7      124.90      SOURCE4_SOURCE5           32    1.6591
ca-cc-na    83.6      123.45              SOURCE4           39
cd-cc-cg    67.1      125.79      SOURCE4_SOURCE5           54    1.7418
cd-cc-cy    66.4      121.68               5/2017            4    2.0175
cd-cc-nd    88.1      123.82      SOURCE4_SOURCE5           14    0.3678
cc-cc-cy    64.6      124.39               5/2017            2    0.0292
cf-cc-nc    86.6      123.98      SOURCE4_SOURCE5            5    2.4219
c -cc-h4    47.1      118.19      SOURCE4_SOURCE5            8    0.2226
na-cc-nh   110.8      117.28      SOURCE4_SOURCE5           54    1.7570
na-cc-ss    83.7      111.46              SOURCE4           20
nc-cc-nc   107.6      125.70      SOURCE4_SOURCE5           18    0.6787
oh-cc-os   115.4      111.61      SOURCE4_SOURCE5            6    1.1909
c2-cf-cl    72.1      119.76      SOURCE4_SOURCE5           38    1.3369
c2-cf-h4    49.2      124.55      SOURCE4_SOURCE5           32    1.8945
c2-cf-n1    91.3      118.23      SOURCE4_SOURCE5           11    1.2780
c2-cf-na    87.2      119.19      SOURCE4_SOURCE5            5    0.8452
c2-cf-oh    88.0      123.70      SOURCE4_SOURCE5           17    1.7138
c3-cf-ch    66.0      117.22      SOURCE4_SOURCE5           26    1.7890
c3-cf-ne    84.4      120.68      SOURCE4_SOURCE5            7    2.0560
c3-cf-nh    82.7      119.56      SOURCE4_SOURCE5            5    1.0524
ca-cf-cf    65.7      119.54      SOURCE4_SOURCE5           18    1.9239
ca-cf-cl    72.2      114.59      SOURCE4_SOURCE5            8    0.9719
ca-cf-h4    47.0      116.99      SOURCE4_SOURCE5          181    1.0407
ca-cf-nh    85.5      115.58      SOURCE4_SOURCE5          147    1.1060
ca-cf-os    85.8      115.91      SOURCE4_SOURCE5           17    1.5899
ca-cf-ss    63.4      117.52      SOURCE4_SOURCE5            9    1.2901
c -cf-ca    65.5      118.28      SOURCE4_SOURCE5           17    1.7879
cd-cf-cc    65.3      130.61      SOURCE4_SOURCE5           19    0.8270
c -cf-cf    65.2      120.98      SOURCE4_SOURCE5           37    2.3876
c -cf-ch    66.5      118.42      SOURCE4_SOURCE5           34    1.0602
cd-cf-h4    47.9      115.68      SOURCE4_SOURCE5           48    0.8279
c -cf-cl    71.8      115.47      SOURCE4_SOURCE5           19    1.2383
cd-cf-nh    85.3      118.05      SOURCE4_SOURCE5           13    1.6005
c -cf-cy    74.7       88.44      SOURCE4_SOURCE5           34    1.2419
cf-cf-cl    71.6      117.22      SOURCE4_SOURCE5           23    1.1321
cf-cf-oh    86.7      116.85      SOURCE4_SOURCE5           19    1.5331
ce-cf-cy    62.2      137.58      SOURCE4_SOURCE5           18    1.4229
ce-cf-h4    49.3      122.95      SOURCE4_SOURCE5           18    1.1766
ce-cf-n1    90.5      119.94      SOURCE4_SOURCE5            7    1.8420
ce-cf-nh    87.3      121.38      SOURCE4_SOURCE5           27    1.6583
ch-cf-n2    87.9      121.14      SOURCE4_SOURCE5            8    0.9418
c -cf-oh    86.2      115.76      SOURCE4_SOURCE5           15    2.2145
c -cf-os    86.1      114.67      SOURCE4_SOURCE5           26    2.3740
h4-cf-n1    64.9      116.64      SOURCE4_SOURCE5           12    0.5604
h4-cf-nf    62.2      115.65      SOURCE4_SOURCE5           12    1.7190
n2-cf-os   114.2      117.95      SOURCE4_SOURCE5           13    0.4519
n2-cf-ss    81.5      117.23              SOURCE4            6
nf-cf-nh   111.3      113.64      SOURCE4_SOURCE5           29    1.5167
ne-cf-nh   112.3      119.27      SOURCE4_SOURCE5           17    1.8891
ca-ce-cd    64.6      130.88      SOURCE4_SOURCE5           29    1.2258
c -ce-cc    66.1      117.82      SOURCE4_SOURCE5           19    0.9022
c -ce-n2    88.2      114.41      SOURCE4_SOURCE5            8    1.4615
h4-ce-nf    64.3      120.56      SOURCE4_SOURCE5           33    0.8495
c1-ch-cd    58.9      178.61      SOURCE4_SOURCE5            7    0.3553
ch-cg-cg    60.6      179.58      SOURCE4_SOURCE5           48    0.3197
n -c -nf   113.6      110.26      SOURCE4_SOURCE5           15    1.6743
ca-cq-na    86.5      119.50      SOURCE4_SOURCE5           38    0.8587
nb-cq-nb   110.0      125.79      SOURCE4_SOURCE5            6    0.6645
cd-cx-hc    47.5      114.33               5/2017            9    0.7607
cf-cy-h2    45.9      117.40      SOURCE4_SOURCE5           21    0.5798
cf-cy-n     94.2       87.94      SOURCE4_SOURCE5           24    0.2234
cf-cy-ss    60.5      120.54      SOURCE4_SOURCE5           21    2.1971
cd-n2-na    91.8      109.24      SOURCE4_SOURCE5           14    1.5712
cd-n2-nh    88.7      118.47      SOURCE4_SOURCE5            7    1.6660
c3-n4-cd    64.4      111.04      SOURCE4_SOURCE5           11    1.9847
c3-na-cq    65.4      119.62      SOURCE4_SOURCE5           10    0.5495
ca-na-cq    67.0      120.86      SOURCE4_SOURCE5           38    1.4370
cd-na-cf    64.7      126.61      SOURCE4_SOURCE5            8    0.5158
cq-nb-nb    86.9      120.96      SOURCE4_SOURCE5           20    0.6372
c -n -cf    63.5      131.38      SOURCE4_SOURCE5          225    1.7874
ca-nc-nd    92.5      108.34      SOURCE4_SOURCE5           14    0.2755
c2-nf-ch    70.2      123.23      SOURCE4_SOURCE5           27    1.1966
c -nf-sy    65.6      116.43      SOURCE4_SOURCE5           10    2.0084
c3-nh-ce    65.1      120.12      SOURCE4_SOURCE5           32    2.1639
cd-nh-n2    85.5      120.09      SOURCE4_SOURCE5           16    0.9182
cd-nh-sy    63.0      122.52      SOURCE4_SOURCE5           37    1.3342
cf-nh-sy    65.3      113.39      SOURCE4_SOURCE5            8    1.1060
hn-n -nd    62.3      115.42      SOURCE4_SOURCE5           24    0.7584
cd-no-o     87.7      117.49      SOURCE4_SOURCE5          426    0.5387
n3-py-nf    79.4      108.76      SOURCE4_SOURCE5           18    1.1434
cd-s6-o     95.6      103.76      SOURCE4_SOURCE5           15    0.9562
cd-sh-hs    53.6       95.01      SOURCE4_SOURCE5           15    1.4000
c -ss-cd    75.1       94.89      SOURCE4_SOURCE5           18    1.2231
c3-sx-cd    73.1       95.18      SOURCE4_SOURCE5           24    0.6543
cd-sx-o     94.3      104.81      SOURCE4_SOURCE5           28    1.4279
c3-sy-cd    71.8      101.95      SOURCE4_SOURCE5           20    1.3784
ca-sy-cd    71.0      105.09      SOURCE4_SOURCE5            5    0.3628
ca-sy-nf    92.5      103.01      SOURCE4_SOURCE5           25    2.4137
cc-sy-nh    94.5       97.20      SOURCE4_SOURCE5            6    0.2429
n3-sy-nf   120.0      101.93      SOURCE4_SOURCE5           10    1.4898
cl-py-ne    67.2      109.16              SOURCE5           79    0.9726
ce-ce-nh    85.8      116.41              SOURCE5           70    1.9262
cp-ca-os    87.9      116.91              SOURCE5           38    1.2997
ca-cc-ca    65.3      122.94              SOURCE5           37    2.3284
h1-c3-i     39.3      103.88              SOURCE5           43    0.8359
h4-c2-h4    37.6      117.92              SOURCE5           46    1.0787
c -ss-ss    72.8       97.68              SOURCE5           29    1.7788
f -py-ne    83.7      108.60              SOURCE5           47    0.7739
ca-nh-ce    65.0      127.74              SOURCE5           32    0.9569
ce-cx-cx    64.2      118.62               5/2017           40    1.7472
py-ne-py   111.0      121.41              SOURCE5           34    1.5196
c -cd-ss    63.0      121.97              SOURCE5           29    2.1476
s -p5-ss    46.4      116.67              SOURCE5           27    1.1060
cx-c3-nh    86.6      103.86               5/2017           29    2.2522
cc-cc-cl    72.0      119.99              SOURCE5           43    1.9574
cd-na-cx    66.4      116.39               5/2017           14    0.5535
h1-cy-nh    61.8      110.00               5/2017            2    1.8569
h5-c -os    64.0      113.09              SOURCE5           20    0.1826
c2-c3-n4    81.9      113.64              SOURCE5           18    2.3563
c2-cx-c3    65.2      115.48               5/2017           22    1.1986
c3-c2-cx    64.8      117.87               5/2017           20    2.2886
br-cx-cx    62.7      119.04               5/2017           21    0.7114
cc-cf-ch    68.2      122.27              SOURCE5           30    0.9028
c3-c3-sx    63.1      110.50              SOURCE5           14    1.4461
ca-cy-hc    46.4      114.53               5/2017           17    1.6221
cx-c1-n1    74.2      178.25               5/2017           17    0.8798
cl-py-cl    61.6      101.95              SOURCE5           12    0.7596
c2-ce-cx    66.4      122.74               5/2017           23    1.5745
c3-c -cx    64.6      116.04               5/2017           14    1.1793
cf-cc-os    87.2      123.07              SOURCE5           15    1.3662
cd-cd-cl    72.0      119.99              SOURCE5           43    1.9574
c3-py-ca    46.1      107.27              SOURCE5           20    1.8136
c3-c3-py    80.6      111.57              SOURCE5           14    1.9142
c3-py-s     46.2      113.85              SOURCE5           14    0.3847
ca-c -cx    64.9      117.66               5/2017           20    1.5268
ce-ce-os    86.8      115.19              SOURCE5           15    2.1777
c3-n4-cx    62.6      117.29              SOURCE5           15    0.3164
h4-ce-sy    42.6      115.00              SOURCE5           20    1.1588
hx-cy-n4    60.5      106.00               5/2017            2    0.1412
cy-no-o     84.2      116.83               5/2017           17    1.1181
cc-cd-cx    66.1      124.15               5/2017           10    1.8770
ca-nb-na    87.3      118.78              SOURCE5           10    0.6408
cl-c3-cy    71.1      111.89               5/2017           12    0.7377
f -c2-h4    66.2      112.05              SOURCE5           13    0.7763
ca-py-s     46.0      116.31              SOURCE5           11    1.2602
cl-c3-cx    71.6      110.76               5/2017            9    1.3315
ca-nh-cy    64.7      123.81               5/2017            2    2.0914
cy-cy-no    79.8      115.43               5/2017           15    1.0848
ce-n1-n1    77.6      177.62              SOURCE5           10    0.5740
cy-cy-hx    45.0      115.92               5/2017            9    1.5918
ce-n -hn    48.1      113.83              SOURCE5           11    1.3642
c3-cx-cu    64.0      120.91               5/2017           11    0.4272
cf-cf-ne    86.6      120.79              SOURCE5            9    1.8014
f -p5-na    88.7       89.26              SOURCE5           12    1.2991
h4-ce-nh    62.3      115.58              SOURCE5           10    0.8050
ne-c -s     82.1      124.23              SOURCE5            9    1.7990
ca-os-py    83.0      123.31              SOURCE5           12    0.8994
cf-ce-cl    71.4      121.94              SOURCE5           20    1.2372
cy-cy-n4    81.5      110.88               5/2017            4    0.7688
na-cc-sh    79.2      122.95              SOURCE5            9    1.1542
nb-na-o    113.4      118.13              SOURCE5           11    0.6838
c -cx-n3    83.0      116.37               5/2017            2    0.1235
cd-cy-hc    48.3      107.20               5/2017            8    0.5300
f -c3-no   111.1      107.76              SOURCE5           11    0.3179
ce-cd-na    86.0      124.93              SOURCE5            9    0.9918
cq-cp-cq    69.7      108.02              SOURCE5           24    0.5633
os-py-s     59.8      116.22              SOURCE5           11    0.4580
c -c3-cy    65.4      110.88               5/2017            9    1.4172
cy-c2-ha    45.8      118.59               5/2017            5    1.8406
cp-cq-cp    69.7      108.02              SOURCE5           24    0.5633
cx-cu-cx    90.2       63.19               5/2017           12    0.2140
cu-c2-ha    50.4      121.49               5/2017           12    0.1524
cd-ce-cg    68.2      122.27              SOURCE5           30    0.9028
cf-ne-ne    87.9      113.17              SOURCE5           15    1.6715
c3-c2-no    82.8      115.94              SOURCE5            9    0.9963
f -cy-f    120.2      108.56               5/2017            9    1.2393
c2-cy-hc    46.9      112.80               5/2017           10    0.5936
c3-c2-cy    64.2      117.99               5/2017           10    1.8958
c -ce-h4    46.7      118.08              SOURCE5            8    2.4522
cf-cc-n     86.2      124.20              SOURCE5           10    0.8706
cd-cc-i     60.1      124.28              SOURCE5           14    1.7120
ce-cf-cl    71.4      121.94              SOURCE5           20    1.2372
cl-c3-p5    92.5      109.52              SOURCE5            9    0.8307
c2-c3-no    83.7      107.19              SOURCE5            9    0.5470
ce-nf-nf    87.9      113.17              SOURCE5           15    1.6715
c1-c3-cx    66.5      112.35               5/2017           11    0.3186
ce-c3-h2    46.9      112.27              SOURCE5            9    0.2011
na-cd-na   115.9      106.60              SOURCE5           10    1.3968
cx-cx-n4    80.4      118.73               5/2017            2    0.1804
c1-cx-hc    48.4      114.86               5/2017            6    0.1269
cg-ca-nb    87.9      116.87              SOURCE5           10    0.6088
ce-c2-f     90.0      122.62              SOURCE5           11    1.4117
cp-ca-cq    71.0      111.52              SOURCE5            8    0.0849
cl-py-nf    67.2      109.16              SOURCE5           79    0.9726
ca-c3-cy    65.2      112.32               5/2017            7    0.8064
ch-cd-nd    85.0      123.03              SOURCE5            7    0.2371
h1-cy-ss    41.6      111.82               5/2017            1
h5-cc-n2    64.0      123.28              SOURCE5            5    1.2554
cc-na-cy    64.0      126.88               5/2017            8    1.2393
c -c3-no    83.4      106.99              SOURCE5            8    1.0618
c3-py-c3    46.1      105.72              SOURCE5           10    2.4094
hx-c3-n3    60.7      111.73              SOURCE5           10    0.1463
cf-cf-nh    85.8      116.41              SOURCE5           70    1.9262
c3-n3-py    81.5      118.27              SOURCE5            8    1.5513
h5-c2-os    64.7      110.95              SOURCE5            9    1.4177
cc-c3-ce    66.3      110.89              SOURCE5            7    2.0183
n4-c3-p5   104.1      106.09              SOURCE5           10    1.7975
ne-cd-ss    79.5      126.00              SOURCE5            6    1.6775
na-cd-ne   111.3      122.47              SOURCE5            7    2.4448
cl-c3-h3    48.7      107.66              SOURCE5           10    0.1942
h5-c -s     44.0      123.51              SOURCE5            6    0.5125
cf-ce-ss    63.7      120.95              SOURCE5           15    1.8784
c3-c2-f     87.7      113.28              SOURCE5            8    1.0861
h4-c2-oh    64.5      114.61              SOURCE5            8    1.2250
ne-ce-nf   108.3      127.96              SOURCE5           10    1.2321
cc-n -cd    67.1      121.05              SOURCE5            7    0.3580
f -py-f     90.4       97.51              SOURCE5            5    0.2281
n -cc-os   110.4      119.02              SOURCE5            8    1.4066
cq-cp-nb    85.9      120.01              SOURCE5           14    1.1266
c -c -s     64.0      121.31              SOURCE5            8    0.9033
cf-ce-os    88.4      120.23              SOURCE5            8    2.3122
br-ce-c2    64.2      120.52              SOURCE5            8    0.4148
cp-nb-na    87.5      118.11              SOURCE5            5    0.5760
n -s6-oh   123.3       97.30              SOURCE5            8    0.9381
cd-c3-h2    47.7      110.47              SOURCE5           12    1.1111
nb-ca-sy    81.3      115.73              SOURCE5            6    0.4033
na-sy-o    123.0      105.30              SOURCE5            5    1.0811
hx-cx-hx    38.0      115.77               5/2017            9    0.0901
cd-cf-ne    86.1      122.39              SOURCE5            7    1.4919
h5-c -oh    65.3      109.49              SOURCE5            7    0.3600
cy-n -cy    71.4       94.55              SOURCE5            5    0.6286
br-c3-no    81.1      106.96              SOURCE5            6    2.2092
c2-ss-s4    73.2       92.42              SOURCE5            8    0.4009
c3-nh-o     85.5      117.53              SOURCE5            7    1.0041
br-cc-ss    65.7      120.06              SOURCE5            6    0.2609
c -ce-ss    64.5      113.23              SOURCE5            6    1.9344
c3-n -n3    82.1      117.56              SOURCE5            6    2.4546
h5-ca-na    62.5      115.80              SOURCE5            8    0.4738
n2-nh-oh   106.3      117.89              SOURCE5            6    0.2008
c2-c3-p5    80.8      112.22              SOURCE5            6    0.6523
c3-cx-nh    86.2      106.88               5/2017            1
c2-cc-ss    62.7      127.48              SOURCE5            6    0.3389
c -ca-na    84.3      117.81              SOURCE5            7    2.2477
cl-c2-n2    91.8      121.45              SOURCE5            8    0.8251
n2-s4-ne   122.2      104.29              SOURCE5            8    0.9503
nc-c -s     82.1      124.47              SOURCE5            7    1.3793
o -sy-ss    85.1      107.59              SOURCE5            7    2.0694
c2-ce-ss    63.0      123.86              SOURCE5            5    1.0553
c3-cx-ca    64.5      117.01               5/2017            6    1.1320
cc-cc-nf    87.3      121.68              SOURCE5            7    1.9093
ca-nd-cd    73.4      104.24              SOURCE5            8    0.2625
cc-n2-oh    89.3      113.25              SOURCE5            7    1.6484
ca-os-sy    63.8      118.01              SOURCE5            8    2.0392
hx-c3-p5    54.8      107.59              SOURCE5            7    1.8329
ca-ce-n     83.3      118.99              SOURCE5            8    0.3821
h4-ce-sx    41.7      115.27              SOURCE5            5    0.1053
c3-ce-ne    83.8      116.23              SOURCE5            5    1.2988
c1-n1-ce    61.7      176.87              SOURCE5            7    0.6686
c3-n2-cd    67.9      117.01              SOURCE5            6    1.8279
cc-c3-h2    47.7      110.47              SOURCE5           12    1.1111
ca-ce-cg    67.2      116.47              SOURCE5            5    1.0847
c2-cc-na    86.7      123.27              SOURCE5            6    1.9888
ca-c3-s4    63.9      109.52              SOURCE5            7    1.3239
n2-cf-nf   111.8      120.69              SOURCE5            6    1.4522
ce-cf-ss    63.7      120.95              SOURCE5           15    1.8784
c3-cx-ss    62.4      114.17               5/2017            4    0.0523
nh-ce-nh   108.6      119.71              SOURCE5            6    0.4946
cd-c -ne    87.0      112.22              SOURCE5            6    0.1806
na-c3-ss    82.9      103.15              SOURCE5            8    0.3361
cf-cf-os    86.8      115.19              SOURCE5           15    2.1777
cx-c3-h2    46.4      114.01               5/2017            8    0.8649
cv-ss-cy    79.2       82.62              SOURCE5            8    0.2654
ss-cy-ss    63.5      109.96               5/2017            1
ce-cx-os    82.8      117.21              SOURCE5            6    1.3466
nb-ca-ne   109.0      121.41              SOURCE5            6    1.6965
br-ca-nb    81.7      116.35              SOURCE5            5    0.4508
c3-nh-os    84.4      110.37              SOURCE5            6    2.4123
c2-nh-p5    81.1      125.90              SOURCE5            6    1.8594
br-ca-cp    63.6      121.39              SOURCE5            7    0.3403
cc-ce-cc    67.2      116.17              SOURCE5            6    0.4089
c3-nh-s6    63.9      116.49              SOURCE5            6    0.5375
cx-c3-na    82.4      114.78               5/2017            7    1.7481
ca-os-p3    85.6      110.46              SOURCE5            5    0.0025
ce-cf-sy    62.9      123.19              SOURCE5            5    0.3760
ca-n2-n1    92.5      118.48              SOURCE5            5    0.1464
cd-cd-no    82.3      125.95              SOURCE5            5    2.2787
na-n2-os   113.1      104.34              SOURCE5            6    0.3185
ce-c3-f     88.3      110.31              SOURCE5            6    0.9204
cx-cc-na    82.0      127.21               5/2017            7    2.0873
n -n2-na   113.9      106.04              SOURCE5            6    0.3975
c3-cf-cc    67.1      117.43              SOURCE5            5    2.0116
ca-na-cy    63.6      128.06               5/2017            7    0.2603
h1-c3-py    54.3      109.38              SOURCE5            7    0.4767
cy-s6-cy    75.5       86.77               5/2017            5    1.5405
ce-ce-s4    63.6      119.12              SOURCE5            6    0.0093
c3-p3-cy    45.4      103.85               5/2017            6    0.6245
h2-cx-os    62.4      113.42               5/2017            2    0.0119
c -c -ce    64.6      115.44              SOURCE5            5    1.0373
ce-cy-h1    46.2      115.49               5/2017            5    0.2559
cx-c3-ss    64.8      105.42               5/2017            7    0.4078
cg-ce-ss    63.7      118.19              SOURCE5            5    1.0760
br-cy-cy    61.8      119.27               5/2017            6    1.4624
c -cy-cl    71.0      112.18               5/2017            5    2.4165
c -cx-n     82.8      117.59               5/2017            1
br-c3-f     82.5      109.62              SOURCE5            7    0.6251
c3-n4-cy    63.5      112.48               5/2017            4    0.1362
ce-cv-ss    62.4      132.71               5/2017            1
cc-cd-i     60.2      124.28              SOURCE5           14    1.7120
c2-ss-ca    73.0      102.78              SOURCE5            5    0.7426
c -cx-ce    64.8      116.84               5/2017            7    1.2393
cy-nh-cy    71.5       93.31              SOURCE5            6    0.3047
cx-c -h4    46.5      115.38               5/2017            7    0.1819
c -n4-c3    64.0      108.76              SOURCE5            7    1.5097
f -cy-py    99.6      113.19               5/2017            8    0.9744
n2-c3-ss    80.4      109.39              SOURCE5            5    1.4343
c3-ss-cf    71.4      101.28              SOURCE5            6    2.4411
ce-cy-hc    46.3      114.84               5/2017            5    0.4991
br-cc-nc    82.5      116.25              SOURCE5            5    0.0824
h3-c3-n     61.3      109.88              SOURCE5            6    0.7497
ca-ne-cd    67.6      123.67              SOURCE5            5    2.0742
cx-n -cy    65.0      116.21              SOURCE5            6    0.4758
cl-c3-s4    71.5      111.99              SOURCE5            6    1.5116
cp-cq-nb    85.9      120.01              SOURCE5           14    1.1266
cc-cd-o     86.7      136.06              SOURCE5            5    0.5251
hx-cy-hx    38.6      110.80               5/2017            5    0.4155
cc-na-sy    61.9      125.17              SOURCE5            5    1.1548
h1-cy-na    62.9      106.38               5/2017            5    0.0918
h4-cf-sy    42.6      115.00              SOURCE5           20    1.1588
c -p5-c3    44.4      111.28              SOURCE5            6    2.1227
ca-c -nc    84.5      117.03              SOURCE5            5    0.2959
c3-os-sy    63.9      115.05              SOURCE5            5    0.9975
cd-ne-sy    65.4      120.78              SOURCE5            5    1.2762
cx-ca-nb    85.6      116.90               5/2017            5    0.8439
nc-ss-ss    93.8       97.44              SOURCE5            6    0.0880
hp-p5-os    45.6      103.08              SOURCE5            5    0.8064
ca-n -oh    84.3      115.62              SOURCE5            5    1.0474
c3-s6-ne    91.3      108.19              SOURCE5            5    0.2914
c1-cx-h1    48.4      114.80               5/2017            5    0.4789
na-c3-oh   109.8      108.59              SOURCE5            6    1.4542
n -nc-nd   109.8      119.88              SOURCE5            5    0.1982
c3-na-nb    85.2      113.14              SOURCE5            5    0.4557
ne-c -os   113.5      112.01              SOURCE5            5    1.9012
br-ce-ce    65.0      115.22              SOURCE5            6    0.2328
cc-c2-oh    91.1      115.18              SOURCE5            6    0.1517
c1-cx-os    86.1      115.61               5/2017            1
nc-cc-os   109.6      121.72              SOURCE5            5    2.3919
br-ce-cf    63.9      121.60              SOURCE5            5    1.8246
cy-c3-f     87.2      111.48               5/2017            5    0.6981
h5-ce-ne    62.7      113.65              SOURCE5            5    0.5892
n3-py-n3    79.0      104.56              SOURCE5            5    0.5659
br-cc-ca    62.5      126.64              SOURCE5            5    0.3204
f -c3-na   113.0      110.41              SOURCE5            5    0.7067
cc-c3-s4    63.4      112.00              SOURCE5            5    0.1216
ce-cf-sx    64.7      112.97              SOURCE5            5    1.7021
cc-cc-i     59.7      125.79              SOURCE5            5    1.4784
c -cg-ch    58.7      176.69              SOURCE5            5    0.2913
ce-c3-hx    47.2      110.88              SOURCE5            5    0.3335
cd-na-cy    64.1      126.49               5/2017            5    0.1565
br-c3-c2    63.7      111.17              SOURCE5            5    1.2445
ce-ce-cg    68.2      114.64              SOURCE5            5    0.4759
cl-cd-nd    90.6      121.29              SOURCE5            5    0.8123
n -ca-na   109.1      117.17              SOURCE5            5    0.3934
cx-cd-nd    83.7      121.60               5/2017            5    0.1341
cl-p5-os    69.5      104.53              SOURCE5            5    0.1303
cx-ss-cy    73.8       91.64               5/2017            5    0.0761
cc-cg-ch    59.3      177.06              SOURCE5            5    0.7516
cc-sy-oh    92.8      104.12              SOURCE5            5    0.3761
cq-ca-os    87.9      116.91              SOURCE5           38    1.2997
ca-cd-ca    65.3      122.94              SOURCE5           37    2.3284
f -py-nf    83.7      108.60              SOURCE5           47    0.7739
ca-nh-cf    65.0      127.74              SOURCE5           32    0.9569
cf-cx-cx    61.4      130.33               5/2017            1
py-nf-py   111.0      121.41              SOURCE5           34    1.5196
c -cc-ss    63.0      121.97              SOURCE5           29    2.1476
cc-na-cx    64.9      121.86               5/2017            1
c2-cf-cx    65.1      127.65               5/2017            2    2.2681
ce-cd-os    87.2      123.07              SOURCE5           15    1.3662
cd-cc-cx    64.8      130.46               5/2017            3    2.8385
cf-n1-n1    77.6      177.62              SOURCE5           10    0.5740
cf-n -hn    48.1      113.83              SOURCE5           11    1.3642
ce-ce-nf    86.6      120.79              SOURCE5            9    1.8014
cf-no-o     86.0      118.22              SOURCE5           11    0.7792
h4-cf-nh    62.3      115.58              SOURCE5           10    0.8050
nf-c -s     82.1      124.23              SOURCE5            9    1.7990
na-cd-sh    79.2      122.95              SOURCE5            9    1.1542
cc-cy-hc    48.7      107.00               5/2017            4    0.5882
cf-cc-na    86.0      124.93              SOURCE5            9    0.9918
c -cf-h4    46.7      118.08              SOURCE5            8    2.4522
ce-cd-n     86.2      124.20              SOURCE5           10    0.8706
cf-c3-h2    46.9      112.27              SOURCE5            9    0.2011
na-cc-na   115.9      106.60              SOURCE5           10    1.3968
ch-ca-nb    87.9      116.87              SOURCE5           10    0.6088
cf-c2-f     90.0      122.62              SOURCE5           11    1.4117
cg-cc-nc    85.0      123.03              SOURCE5            7    0.2371
h5-cd-n2    64.0      123.28              SOURCE5            5    1.2554
cd-c3-cf    66.3      110.89              SOURCE5            7    2.0183
nf-cc-ss    79.5      126.00              SOURCE5            6    1.6775
na-cc-nf   111.3      122.47              SOURCE5            7    2.4448
nf-cf-ne   108.3      127.96              SOURCE5           10    1.2321
n -cd-os   110.4      119.02              SOURCE5            8    1.4066
ce-cf-os    88.4      120.23              SOURCE5            8    2.3122
br-cf-c2    64.2      120.52              SOURCE5            8    0.4148
cq-nb-na    87.5      118.11              SOURCE5            5    0.5760
cc-ce-nf    86.1      122.39              SOURCE5            7    1.4919
cf-s4-ss    74.5       88.65              SOURCE5            8    0.4156
br-cd-ss    65.7      120.06              SOURCE5            6    0.2609
c -cf-ss    64.5      113.23              SOURCE5            6    1.9344
c2-cd-ss    62.7      127.48              SOURCE5            6    0.3389
n2-s4-nf   122.2      104.29              SOURCE5            8    0.9503
nd-c -s     82.1      124.47              SOURCE5            7    1.3793
c2-cf-ss    63.0      123.86              SOURCE5            5    1.0553
cd-cd-ne    87.3      121.68              SOURCE5            7    1.9093
ca-nc-cc    73.4      104.24              SOURCE5            8    0.2625
cd-n2-oh    89.3      113.25              SOURCE5            7    1.6484
ca-cf-n     83.3      118.99              SOURCE5            8    0.3821
h4-cf-sx    41.7      115.27              SOURCE5            5    0.1053
c3-cf-nf    83.8      116.23              SOURCE5            5    1.2988
c1-n1-cf    61.7      176.87              SOURCE5            7    0.6686
c3-n2-cc    67.9      117.01              SOURCE5            6    1.8279
ca-cf-ch    67.2      116.47              SOURCE5            5    1.0847
c2-cd-na    86.7      123.27              SOURCE5            6    1.9888
n2-ce-ne   111.8      120.69              SOURCE5            6    1.4522
nh-cf-nh   108.6      119.71              SOURCE5            6    0.4946
cc-c -nf    87.0      112.22              SOURCE5            6    0.1806
cf-cx-os    82.8      117.21              SOURCE5            6    1.3466
nb-ca-nf   109.0      121.41              SOURCE5            6    1.6965
br-ca-cq    63.6      121.39              SOURCE5            7    0.3403
cd-cf-cd    67.2      116.17              SOURCE5            6    0.4089
cf-ce-sy    62.9      123.19              SOURCE5            5    0.3760
cc-cc-no    82.3      125.95              SOURCE5            5    2.2787
cf-c3-f     88.3      110.31              SOURCE5            6    0.9204
cx-cd-na    81.8      127.21              SOURCE5            7    2.0873
c3-ce-cd    67.1      117.43              SOURCE5            5    2.0116
cf-cf-s4    63.6      119.12              SOURCE5            6    0.0093
c -c -cf    64.6      115.44              SOURCE5            5    1.0373
cf-cy-h1    46.2      115.49              SOURCE5            5    0.2559
ch-cf-ss    63.7      118.19              SOURCE5            5    1.0760
cf-cv-ss    61.9      130.09              SOURCE5            7    2.1973
c -cx-cf    65.0      116.84              SOURCE5            7    1.2393
c3-ss-ce    71.4      101.28              SOURCE5            6    2.4411
cf-cy-hc    46.4      114.84              SOURCE5            5    0.4991
br-cd-nd    82.5      116.25              SOURCE5            5    0.0824
ca-nf-cc    67.6      123.67              SOURCE5            5    2.0742
cd-cc-o     86.7      136.06              SOURCE5            5    0.5251
cd-na-sy    61.9      125.17              SOURCE5            5    1.1548
ca-c -nd    84.5      117.03              SOURCE5            5    0.2959
cc-nf-sy    65.4      120.78              SOURCE5            5    1.2762
nd-ss-ss    93.8       97.44              SOURCE5            6    0.0880
c3-s6-nf    91.3      108.19              SOURCE5            5    0.2914
n -nd-nc   109.8      119.88              SOURCE5            5    0.1982
nf-c -os   113.5      112.01              SOURCE5            5    1.9012
br-cf-cf    65.0      115.22              SOURCE5            6    0.2328
cd-c2-oh    91.1      115.18              SOURCE5            6    0.1517
nd-cd-os   109.6      121.72              SOURCE5            5    2.3919
br-cf-ce    63.9      121.60              SOURCE5            5    1.8246
h5-cf-nf    62.7      113.65              SOURCE5            5    0.5892
br-cd-ca    62.5      126.64              SOURCE5            5    0.3204
cd-c3-s4    63.4      112.00              SOURCE5            5    0.1216
cf-ce-sx    64.7      112.97              SOURCE5            5    1.7021
cd-cd-i     59.8      125.79              SOURCE5            5    1.4784
c -ch-cg    58.7      176.69              SOURCE5            5    0.2913
cf-c3-hx    47.2      110.88              SOURCE5            5    0.3335
cf-cf-ch    68.2      114.64              SOURCE5            5    0.4759
cl-cc-nc    90.6      121.29              SOURCE5            5    0.8123
cx-cc-nc    83.6      123.10               5/2017            4    0.0212
cd-ch-cg    59.3      177.06              SOURCE5            5    0.7516
cd-sy-oh    92.8      104.12              SOURCE5            5    0.3761
cx-cx-op   116.4       59.10               5/2017          788    0.5911
h1-cx-op    60.8      114.93               5/2017          521    0.5578
c3-cx-op    82.7      115.83               5/2017          437    1.2206
nj-c -o    108.3      133.06               5/2017          375    1.1853
c -nj-cy    73.1       94.02               5/2017          400    0.9271
h1-cx-np    59.2      116.75               5/2017          251    1.3313
cx-op-cx    89.1       61.76               5/2017          272    0.2227
cy-cy-nj    92.3       88.64               5/2017          298    0.3546
cy-c -nj    92.8       91.68               5/2017          255    0.2693
h1-cx-nm    59.8      116.40               5/2017          183    1.0171
h1-cy-nj    60.4      111.56               5/2017          189    0.5925
ce-nj-cy    66.5      111.65               5/2017          212    2.1008
c -nj-ce    62.9      131.56               5/2017          192    1.3241
c -ce-nj    83.3      118.53               5/2017          191    1.4551
cx-cx-np   114.7       59.60               5/2017          200    0.1764
c3-cy-nj    85.8      104.19               5/2017          184    0.6089
c2-ce-nj    90.5      110.33               5/2017          122    1.5095
h2-cy-nj    59.6      114.54               5/2017          125    0.6756
cx-cx-nm   115.7       59.12               5/2017          126    0.4262
nj-cy-ss    81.6      105.14               5/2017           96    0.4378
c -cx-op    83.6      114.98               5/2017          121    2.4675
cx-np-cx    89.0       60.75               5/2017           90    0.2619
cx-np-p5    80.8      119.47               5/2017          102    1.2691
h1-c3-nj    62.0      108.52               5/2017           74    0.7997
h1-cy-nq    59.4      114.39               5/2017           47    0.4222
c -nj-c3    63.3      127.60               5/2017           58    2.0671
c3-nj-cy    64.4      117.18               5/2017           64    1.3258
cx-nm-cx    89.0       62.00               5/2017           53    0.5675
c3-c3-nj    85.2      106.94               5/2017           62    0.9453
cf-ce-nj    91.2      108.32               5/2017           69    0.7305
c -c3-nj    84.4      110.19               5/2017           63    1.0059
cc-nm-cx    64.2      122.67               5/2017           54    1.1105
c3-np-cx    64.5      116.39               5/2017           56    0.8663
h1-c3-np    61.2      109.97               5/2017           36    1.5352
c3-cx-np    81.9      115.87               5/2017           44    2.6976
cy-cy-nq    92.0       88.75               5/2017           40    0.4361
ca-cy-cy    63.4      116.81               5/2017           39    5.3567
ce-c2-cx    66.9      122.46               5/2017           37    2.7509
np-p5-o     78.8      116.36               5/2017           35    0.7533
ca-nm-cx    64.6      123.62               5/2017           34    0.6428
cy-cy-oq    91.7       90.56               5/2017           31    0.6765
c2-cx-op    83.5      116.86               5/2017           32    0.8978
h1-c3-nq    61.9      108.57               5/2017           28    0.8533
h1-cy-oq    61.2      110.42               5/2017           23    0.6967
c3-cy-oq    83.0      112.52               5/2017           28    1.0753
c3-nq-cy    63.8      118.65               5/2017           24    0.7845
cx-cx-n     82.1      119.02               5/2017           29    1.3890
np-p5-np    79.9      101.22               5/2017           23    1.3244
cd-cc-nm    86.3      120.02               5/2017           27    3.1659
c -cc-nm    83.3      120.41               5/2017           22    3.3026
nj-s6-o    122.1      107.52               5/2017           23    1.5874
ce-cy-nj    94.0       87.89               5/2017           24    0.2234
ce-c -nj    96.3       90.02               5/2017           19    0.1956
h1-cy-nn    59.6      113.90               5/2017           24    0.5436
nb-ca-nm   112.3      116.81               5/2017           22    0.1535
cd-nm-cx    64.3      125.63               5/2017           26    2.3547
cy-nq-cy    72.2       90.89               5/2017           23    0.5650
cx-np-hn    47.5      109.82               5/2017           18    1.2179
c3-c3-np    83.6      110.44               5/2017           18    0.8305
cl-p5-nq    67.7      106.00               5/2017           20   15.5183
n3-p5-np    79.8      103.46               5/2017           14    1.1022
hx-c3-nk    60.5      107.16               5/2017           14    0.7090
c3-c3-nq    83.4      111.33               5/2017           13    1.0980
cy-nq-hn    46.0      115.35               5/2017           16    0.5918
o -c -oq   111.9      128.02               5/2017           15    0.2268
s -p5-sq    45.7      116.54               5/2017           16    1.0313
c3-nk-cx    62.7      117.29               5/2017           15    0.3164
hx-cx-nk    58.9      114.50               5/2017           17    0.1111
ca-ca-nn    86.4      121.30               5/2017           11    0.6025
ca-cx-op    82.7      118.22               5/2017           12    0.7181
cy-oq-cy    72.0       91.64               5/2017           14    0.9476
ne-py-np    79.3      108.52               5/2017           10    0.9768
cx-np-py    80.1      121.75               5/2017           10    1.0295
h1-cx-ni    58.8      116.04               5/2017           11    0.8697
h2-cy-sq    41.5      112.70               5/2017           16    0.2934
c -oq-cy    74.0       91.81               5/2017           13    0.1118
nj-cy-s6    82.4      103.04               5/2017           12    0.8707
ce-c3-cx    67.0      107.13               5/2017           12    4.2613
cy-c -oq    92.0       94.76               5/2017           13    0.2487
ca-ca-nm    86.3      120.92               5/2017            8    1.4000
n -p5-np    78.2      104.63               5/2017           14    0.8228
cx-cx-ss    61.8      117.07               5/2017            9    0.9216
hx-cy-nl    58.5      112.25               5/2017           10    1.2745
c -ce-cx    65.3      116.79               5/2017           15    4.1498
ca-nn-cy    63.2      127.19               5/2017           12    1.0510
ce-cf-nj    91.2      108.88               5/2017           14    1.2299
cy-cy-nn    92.2       88.52               5/2017            9    0.2046
c -cf-nj    84.0      117.12               5/2017           11    0.9941
cf-nj-cy    67.0      110.67               5/2017           14    1.2434
c -nj-cf    63.4      130.17               5/2017            7    1.2980
np-p5-s     59.6      117.02               5/2017           13    0.6701
cy-nj-s6    60.1      128.33               5/2017           13    3.9962
c -nj-s6    61.5      126.24               5/2017           11    1.8391
cx-cx-nj    84.0      112.80               5/2017           14    3.3617
cc-cd-nm    86.4      123.63               5/2017            9    0.6628
c -cd-nm    86.4      115.12               5/2017           10    0.4572
c2-ce-cy    62.8      135.24               5/2017           12    3.3796
c3-cy-nq    81.6      114.92               5/2017           11    1.5228
nj-cy-os   110.5      106.30               5/2017           11    1.3753
ce-cy-cy    71.7       91.26               5/2017            9    7.6322
cy-cy-i     57.8      124.59               5/2017            9    0.2685
ce-ce-cx    67.2      112.11               5/2017           11    3.1246
c2-nm-cx    64.2      123.62               5/2017            6    1.7105
cl-p5-nn    68.5      106.11               5/2017           10   15.4157
c3-p5-sq    44.7      107.60               5/2017            8    0.0032
cy-n4-hn    46.4      108.23               5/2017            9    1.9124
c -cx-np    82.1      116.84               5/2017            8    1.3308
c -cx-c     64.3      119.01               5/2017           10    3.0316
c3-cy-cv    63.3      118.55               5/2017            6    3.1192
c -ce-cv    67.1      121.01               5/2017            6    2.5795
c3-cy-ce    63.3      119.10               5/2017            9    3.7569
nj-s6-oh   123.0       97.30               5/2017            8    0.9381
ce-c2-cy    66.8      120.23               5/2017            8    3.6606
c -ni-cx    65.7      112.89               5/2017            7    0.8204
cx-cx-ni   113.5       60.20               5/2017            8    0.4477
cx-cx-nk   113.1       60.33               5/2017            8    0.0491
cy-nj-cy    71.1       94.55               5/2017            5    0.6286
c -cy-n3    80.1      119.34               5/2017            8    2.9850
h1-cy-sq    41.5      112.68               5/2017            2    1.2615
ca-ca-nj    85.9      120.06               5/2017            6    0.2939
cy-cy-nl    90.3       89.92               5/2017            7    0.3940
c3-cy-ca    64.8      113.57               5/2017            7    3.4595
sq-p5-sq    48.8       92.54               5/2017            8    0.2614
p5-sq-p5   123.5       87.45               5/2017            8    0.2687
cy-cy-nh    81.3      116.16               5/2017            7    2.5407
cx-c3-f     88.3      109.76               5/2017            4    0.4674
ca-cx-ca    66.5      112.09               5/2017            6    3.7075
cy-nl-cy    68.5       95.59               5/2017            5   11.0123
cv-sq-cy    79.2       82.62               5/2017            8    0.2654
c3-cx-nm    81.9      116.90               5/2017            6    0.9555
cd-cd-cx    65.8      121.16               5/2017            6    4.7037
ce-cx-op    82.8      117.21               5/2017            6    1.3466
cx-cx-oh    83.5      117.53               5/2017            4    1.0877
cl-cy-sq    70.9      113.25               5/2017            4    0.0097
cl-cy-cl    82.1      108.77               5/2017            4    0.1710
nh-p5-np    79.8      103.23               5/2017            5    1.6959
h2-cy-h2    38.2      112.44               5/2017            3    1.1599
c -nj-cx    62.7      130.44               5/2017            7    1.5990
f -cy-s4    79.0      111.78               5/2017            4    0.6672
cy-nl-hn    44.5      116.49               5/2017            5    1.4191
cy-cv-cy    72.0       92.49               5/2017            3    0.5396
c3-nq-p5    76.6      130.03               5/2017            4    2.7758
c2-cv-cy    63.2      133.90               5/2017            4    1.1682
cy-nn-cy    71.4       93.31               5/2017            6    0.3047
cu-c3-hc    48.4      109.32               5/2017            4    0.4822
o -p5-oq    80.7      111.64               5/2017            4    0.0067
f -cy-p3   100.9      113.48               5/2017            4    2.6052
cx-nj-cy    64.7      116.21               5/2017            6    0.4758
c -cx-nj    81.2      120.99               5/2017            6    1.4325
br-cx-br    68.5      111.35               5/2017            4    0.3227
c2-c3-nj    88.1      102.04               5/2017            6    0.5829
cy-nj-hn    43.5      130.43               5/2017            4    0.5564
c -nj-hn    45.5      130.69               5/2017            4    0.3898
c3-cx-ce    64.2      117.74               5/2017            5    3.5091
c3-os-cx    66.2      114.88               5/2017            4    1.0718
c -os-cx    67.0      118.28               5/2017            6    1.6217
c -c -cx    65.3      111.89               5/2017            5    7.1774
cx-c2-n2    85.6      121.33               5/2017            5    3.6391
ce-cx-h1    46.7      115.28               5/2017            3    0.6480
c3-c3-nk    81.6      112.67               5/2017            4    0.2516
op-cx-os   107.9      116.08               5/2017            5    0.4632
c2-cy-oh    85.6      110.66               5/2017            4    0.5730
ce-cv-sq    62.0      129.66               5/2017            6    2.0748
cy-p3-cy    49.9       83.91               5/2017            2
p3-cy-p3   109.6       94.01               5/2017            4    0.2418
cx-cx-i     58.3      123.50               5/2017            4    0.4266
ce-c2-nm    85.0      127.27               5/2017            4    0.2044
c3-c2-nm    82.7      119.45               5/2017            4    0.2888
c -cy-oq    92.8       88.79               5/2017            4    0.5710
cx-no-o     85.0      116.76               5/2017            3    0.1846
cx-cx-h2    45.1      122.75               5/2017            4    0.8649
cy-s4-o     89.7      106.89               5/2017            3    0.4570
sq-cy-sq    68.4       94.68               5/2017            3    0.8226
cv-cx-cx    61.0      131.57               5/2017            4    0.1609
nj-p5-nj    74.1      109.62               5/2017            3   15.3647
cl-cx-op    89.7      115.62               5/2017            3    0.0331
h2-cy-na    62.8      106.55               5/2017            4    0.3463
na-cy-oq   107.1      112.79               5/2017            3    0.0982
h2-cy-oq    60.9      111.49               5/2017            4    0.3504
ce-cv-cy    63.1      132.80               5/2017            4    4.6817
c1-cy-cy    64.7      115.83               5/2017            4    1.9538
c -cy-nj    81.3      114.64               5/2017            3    0.5131
cu-c2-h4    50.6      120.84               5/2017            3    0.5974
c -cy-nq    81.5      113.64               5/2017            5    0.6718
c3-cy-cl    69.9      116.52               5/2017            4
cc-c2-cx    67.7      118.69               5/2017            4    0.1767
c -cd-cx    65.0      120.91               5/2017            4    1.7956
c3-c -nj    82.9      117.49               5/2017            4    1.3145
cx-nk-cx    88.5       59.34               5/2017            4    0.0214
c -nj-ca    62.9      133.65               5/2017            3    0.9513
c3-nk-c3    62.8      116.24               5/2017            3    0.6640
ni-c -o    110.1      124.76               5/2017            3    0.0955
c3-cx-n2    82.1      116.51               5/2017            3    2.8045
cx-ni-cx    88.9       59.59               5/2017            4    0.6966
cx-c2-oh    85.4      118.33               5/2017            2    0.1221
c -cx-nm    82.6      116.38               5/2017            3    1.0348
cy-sq-cy    80.7       76.10               5/2017            2    0.0046
cx-c2-cx    66.3      114.57               5/2017            4    0.4023
c -cy-c     64.5      110.83               5/2017            2    3.0933
cy-cy-sq    68.9       91.32               5/2017            4    0.0870
hx-c3-nl    60.0      108.77               5/2017            2    0.1223
h2-cx-op    60.5      116.29               5/2017            3    0.4885
c1-cx-op    84.4      117.68               5/2017            4    0.2200
cg-c1-cx    58.4      178.74               5/2017            3    0.0281
cu-c2-na    85.6      127.64               5/2017            3    0.1334
cy-cy-n2    81.2      117.74               5/2017            4    0.8366
ca-nj-cy    62.1      129.62               5/2017            3    2.4722
ca-cy-nj    81.6      116.76               5/2017            3    0.2183
ca-cy-h1    47.4      109.93               5/2017            2    0.0136
np-py-np    78.7      104.50               5/2017            3    0.3387
c3-cy-p5    77.7      115.52               5/2017            4    0.7727
h1-cy-n2    61.4      114.25               5/2017            3    0.0152
sq-p5-ss    45.6      108.61               5/2017            2
c2-n2-cy    69.4      116.81               5/2017            3    0.1182
n3-cy-p3   100.3      109.52               5/2017            4    3.8573
c3-cy-p3    77.1      115.86               5/2017            4    0.4668
cx-c2-nh    83.5      120.58               5/2017            3    1.4728
op-op-p5   140.1       60.28               5/2017            3    0.0474
f -cy-s6    81.0      112.88               5/2017            4    0.4681
o -p5-op    78.8      124.06               5/2017            3    0.2749
c -c -nj    83.0      115.09               5/2017            2
no-cy-no   105.4      106.55               5/2017            3    0.0285
cv-cy-f     85.5      116.68               5/2017            2    1.1227
c -cx-c2    65.0      117.67               5/2017            3    0.9514
c2-os-cy    68.9      110.05               5/2017            3    0.0809
h2-cx-sp    41.5      115.60               5/2017            4
ce-cx-ce    66.4      111.50               5/2017            2
ca-os-cy    66.1      118.86               5/2017            3    0.0683
h2-cy-s4    39.8      113.54               5/2017            3    5.3672
ca-c -cy    66.9      106.90               5/2017            3    0.0144
n3-p5-sq    58.0      104.94               5/2017            4
n -c -nj   111.4      113.89               5/2017            3    0.2740
cf-c3-cx    66.6      108.48               5/2017            2    4.7226
cx-np-sy    63.2      115.47               5/2017            3    0.1653
c -nj-cl    68.8      125.57               5/2017            4    0.0280
c -nj-c     71.2      104.62               5/2017            3   19.7506
nj-c -nj   122.6       92.54               5/2017            3    4.5162
cx-cx-n2    81.5      119.32               5/2017            2    0.3408
nq-p5-nq    88.0       80.37               5/2017            4    0.2774
p5-nq-p5   113.4       99.63               5/2017            4    0.2774
ca-nn-p5    80.2      129.96               5/2017            4    1.0405
c3-p5-nj    59.0      105.57               5/2017            2    6.1936
c3-nj-p5    74.0      136.28               5/2017            2    0.2518
c -nj-p5    90.1       93.58               5/2017            2    1.7014
n4-cy-p3    97.2      114.86               5/2017            2
hx-cy-p3    51.0      114.01               5/2017            4    0.2613
cf-cc-sq    61.4      130.11               5/2017            2    0.8984
ce-cy-cl    70.9      114.18               5/2017            3    3.2837
cl-np-cx    69.0      115.01               5/2017            2    0.2658
s6-cy-s6    69.2       92.46               5/2017            4    0.0205
c1-c1-cx    58.5      179.60               5/2017            3    0.0811
c -cy-c2    64.2      114.90               5/2017            2    2.7878
cv-cy-h1    46.0      116.15               5/2017            3    0.4810
sq-cv-sq    69.7      100.69               5/2017            3    0.0408
br-cy-c     63.4      113.79               5/2017            3    1.7521
c3-nl-cy    62.9      114.43               5/2017            2    3.7174
cy-c1-n1    73.4      178.19               5/2017            3    0.4447
c -cy-f     86.2      111.98               5/2017            2    2.6644
cx-s6-o     92.4      107.88               5/2017            2    0.4105
c2-cy-oq    84.4      110.47               5/2017            3    0.9895
np-p5-os    82.2      100.36               5/2017            2    2.0470
c3-c3-cu    65.6      112.97               5/2017            2    0.0195
c3-cu-cu    60.8      152.33               5/2017            3    0.0138
c3-cu-cx    59.6      143.11               5/2017            2    0.0114
cx-np-p3    79.7      117.31               5/2017            3    0.2774
ca-p3-cy    45.2      106.43               5/2017            2    0.0001
cy-py-s     45.0      114.96               5/2017            4
ca-py-cy    44.4      109.38               5/2017            4
np-s6-o    118.9      106.89               5/2017            2    2.5256
cu-cx-f     85.0      123.08               5/2017            4
cy-cc-na    81.1      127.40               5/2017            2    0.0024
c -cy-n2    82.6      114.44               5/2017            2    0.2400
nm-cx-os   106.5      117.51               5/2017            2    0.0344
cl-cx-nm    89.1      116.53               5/2017            2    0.1279
c3-n -cx    65.6      115.34               5/2017            2    0.4336
cx-cx-no    81.2      116.74               5/2017            1
cf-sx-cy    75.6       87.56               5/2017            2    0.0390
cy-sx-o     91.5      106.72               5/2017            2    0.3476
h2-cy-sx    42.6      105.10               5/2017            2    0.1610
nj-cy-sx    80.9      105.88               5/2017            2    0.0913
cy-cy-sx    59.1      123.17               5/2017            1
ce-cy-s6    61.0      118.02               5/2017            2    0.0022
c -cx-ca    65.4      115.24               5/2017            1
np-sy-o    120.8      108.49               5/2017            1
cy-p5-n3    57.6      111.83               5/2017            2
cf-c2-cx    65.1      129.35               5/2017            1
c -cx-cv    74.1       89.36               5/2017            2    0.1403
cx-cx-s4    60.3      118.38               5/2017            1
ca-ss-cy    71.9       99.29               5/2017            1
cv-ce-cy    74.8       94.77               5/2017            1
c -cy-cv    63.8      115.56               5/2017            1
c3-c -cy    63.5      116.20               5/2017            2    0.0213
cl-cy-f     93.6      111.16               5/2017            2
c2-nh-cy    65.9      119.23               5/2017            1
c1-ce-cy    63.1      136.04               5/2017            2    0.0507
c2-cy-cl    73.0      107.79               5/2017            2    0.0195
c -cx-c1    68.0      110.46               5/2017            2    0.0118
c -cy-n4    83.6      105.79               5/2017            1
cx-n4-hn    46.1      111.43               5/2017            1
c3-ce-cv    65.1      125.26               5/2017            2    0.0413
cy-nj-os    79.3      125.33               5/2017            1
c -nj-os    81.4      125.79               5/2017            1
ce-ce-cy    73.8       92.04               5/2017            2
cx-p5-o     61.9      107.77               5/2017            2    1.0659
c3-cy-f     85.3      116.11               5/2017            2
cx-p5-oh    62.9       99.62               5/2017            2    0.1413
cx-cx-p5    78.2      120.29               5/2017            1
c2-cy-c3    66.3      108.95               5/2017            1
ce-cy-oq    85.4      107.57               5/2017            2    0.9131
c3-c2-cv    65.2      127.33               5/2017            2    0.0282
cv-c2-ha    51.1      117.19               5/2017            2    0.0186
c1-c2-cx    67.3      123.69               5/2017            2    0.0388
c1-cx-c3    66.8      112.87               5/2017            2
cy-nh-hn    46.9      116.45               5/2017            1
cx-ce-n2    83.0      126.72               5/2017            2    0.1048
cx-cx-s6    61.1      118.42               5/2017            1
ce-n2-cx    71.4      107.29               5/2017            1
ce-c -cy    73.1       89.99               5/2017            2    0.0125
cl-c2-cx    72.9      114.93               5/2017            2    0.1831
c3-c3-cv    66.3      109.22               5/2017            1
cy-c3-nh    83.1      111.89               5/2017            2    0.0368
h1-cx-i     39.1      107.64               5/2017            1
cy-c3-no    80.3      114.72               5/2017            2    0.1964
c -cx-cl    71.5      113.26               5/2017            2    0.0899
br-c3-cy    63.9      109.90               5/2017            2    0.2523
c1-cx-np    83.8      116.64               5/2017            2    0.8442
cv-cv-nh    84.8      131.88               5/2017            2    3.8189
cy-cv-nh    78.4      134.23               5/2017            2    1.7020
ca-cx-n2    82.2      118.59               5/2017            2
o -s6-sp    86.9      116.39               5/2017            2
o -s6-op   124.0      113.41               5/2017            2
c2-c3-nq    83.5      113.46               5/2017            1
n3-c3-np   109.5      106.35               5/2017            2    3.6335
h2-c3-np    61.6      108.74               5/2017            2    2.5491
cy-nq-nq    90.9       89.21               5/2017            2    0.1168
c3-s6-cx    70.0      103.52               5/2017            2    0.9319
c3-cx-s6    62.8      111.43               5/2017            2    3.0093
ca-p3-cx    45.5      105.28               5/2017            2    0.0086
hc-cx-p3    52.0      109.32               5/2017            2    0.0135
cx-cx-p3   101.6       67.04               5/2017            1
c2-cx-p3    77.5      115.96               5/2017            2    0.0286
c3-cx-n     81.8      118.56               5/2017            1
ce-nm-cx    64.5      122.65               5/2017            2    0.1606
ca-cx-n3    83.5      115.37               5/2017            2    3.8559
ne-sy-np   118.2      102.64               5/2017            1
h1-cx-n2    60.3      115.09               5/2017            2    1.3606
c3-s6-np    92.2       96.37               5/2017            1
nj-os-s6    84.2      112.22               5/2017            2    1.9469
op-np-s6    80.0      107.06               5/2017            2    1.4278
cx-np-s6    63.4      109.23               5/2017            2    2.9273
cx-np-op   114.1       57.60               5/2017            1
cx-op-np   111.2       60.26               5/2017            2    0.1701
np-cx-op   144.0       62.25               5/2017            2    0.2842
ca-cx-np    84.1      111.74               5/2017            1
ne-cv-sq    78.2      130.58               5/2017            2    3.9481
cx-c2-n     88.7      105.90               5/2017            2    1.9664
n -c -ni   112.5      108.96               5/2017            2    1.0016
cy-s4-os    89.8       99.89               5/2017            2
cy-s4-cy    77.5       77.06               5/2017            2    6.0783
s4-cy-s6    66.6       96.33               5/2017            2
cy-c3-cy    70.1       96.03               5/2017            2
op-p5-op   110.1       58.98               5/2017            2    0.5147
nh-p5-op    79.4      109.75               5/2017            1
hn-nl-hn    38.3      114.25               5/2017            2    0.1940
c -cy-nl    82.5      108.19               5/2017            2    3.6695
c -cy-hx    46.7      108.37               5/2017            1
cy-cc-nd    83.6      123.93               5/2017            2    0.0382
c1-cv-cy    63.5      134.78               5/2017            1
h2-cx-nm    58.9      120.16               5/2017            1
cl-cx-h2    48.7      109.56               5/2017            2    0.9176
c3-cx-sp    61.7      117.95               5/2017            2    0.2577
h1-cx-sp    41.9      113.87               5/2017            1
cx-cx-sp    82.6       66.15               5/2017            1
cy-cy-sy    61.1      116.36               5/2017            2    0.7368
cy-sy-o     91.6      109.31               5/2017            2    0.3216
c3-s4-cy    72.9       90.94               5/2017            2    0.4605
nj-cy-s4    77.9      109.36               5/2017            2    1.2804
c1-cx-n3    84.5      116.77               5/2017            2
c3-s4-cx    71.6       95.81               5/2017            2    0.0898
c -cy-ca    65.5      109.95               5/2017            2    3.2201
ce-os-cx    70.2      106.77               5/2017            2
cx-c -s     63.5      126.27               5/2017            2    1.8035
cy-ca-nb    84.1      118.93               5/2017            1
cl-cx-n2    89.2      116.42               5/2017            2    0.1700
c3-cx-cl    70.7      115.01               5/2017            2    0.9036
cl-cy-p3    89.4      113.21               5/2017            2    0.6632
cl-cy-p5    89.4      114.53               5/2017            2    3.2198
c1-cx-c1    68.5      113.23               5/2017            1
nn-p5-nn    91.9       79.92               5/2017            2
p5-nn-p5   117.9      100.08               5/2017            2
cp-ca-cx    69.6      108.27               5/2017            2    0.1673
ce-cv-cx    63.1      134.57               5/2017            2    1.2860
cc-sq-cc    81.7       80.38               5/2017            2    0.1168
sq-cc-sq    69.4       99.62               5/2017            2    0.1606
ca-cy-cl    72.1      110.44               5/2017            2    0.0111
c3-cy-nl    80.6      114.62               5/2017            2    0.5512
sq-cy-ss    62.6      113.15               5/2017            2    1.3344
cx-c3-py    83.6      104.34               5/2017            1
cy-s4-nq   101.5       76.85               5/2017            2
nq-s4-o    116.8      114.17               5/2017            2
c3-nq-s4    61.0      124.45               5/2017            2
cy-nq-no    80.8      123.23               5/2017            1
nq-no-o    114.1      117.13               5/2017            2    0.0089
ce-cu-cx    92.8       65.87               5/2017            2    1.1024
cu-ce-cx    93.9       62.58               5/2017            2    0.8974
ca-ce-cu    60.3      155.34               5/2017            1
cv-cy-nj    94.3       87.16               5/2017            2    0.0068
ca-ce-cx    59.3      142.12               5/2017            2    0.8654
ce-cx-cu    98.7       51.55               5/2017            2    0.2050
cy-s6-nj   103.3       77.53               5/2017            2    0.0220
c3-cy-s6    61.0      117.31               5/2017            2    1.6097
c2-cy-os    87.7      104.91               5/2017            2    0.0532
c3-cy-nn    80.9      117.09               5/2017            1
h1-cx-oh    63.3      111.16               5/2017            2    2.1291
cc-cx-op    84.0      116.69               5/2017            1
c -c3-np    83.7      111.18               5/2017            2    0.3155
cx-os-p5    83.1      121.49               5/2017            1
oq-cy-oq   118.8       90.73               5/2017            2    0.2180
cy-cd-nd    83.8      118.88               5/2017            2    0.3763
cx-c -ne    85.6      112.89               5/2017            2    3.0729
oq-cy-os   109.8      108.91               5/2017            2    1.6832
ce-cx-cf    68.1      106.30               5/2017            2    0.2737
cf-cx-op    81.8      120.46               5/2017            2    0.3089
cf-cf-cx    69.5      105.06               5/2017            1
cv-cu-cx    61.6      149.42               5/2017            1
cx-sp-sp    95.8       54.12               5/2017            2
br-c2-cx    65.7      113.08               5/2017            2    0.6246
cy-cy-n1    82.0      115.36               5/2017            1
c -cx-f     87.2      113.85               5/2017            2    0.1033
c -cx-cy    73.5       89.45               5/2017            2    3.2844
c3-cy-cx    64.9      112.55               5/2017            2    1.4880
c3-p5-np    60.2      104.48               5/2017            2    0.0144
cy-p5-s     45.6      116.63               5/2017            2
np-p3-ss    60.2       98.78               5/2017            2    3.2750
cy-cy-p5    89.4       86.58               5/2017            2
cy-cv-n2    80.6      132.92               5/2017            2    2.7922
c1-c3-cy    66.8      110.29               5/2017            1
oq-p5-oq    87.3       85.53               5/2017            2
p5-oq-p5   117.7       94.45               5/2017            1
cx-cx-n1    82.0      122.22               5/2017            2    2.3482
cd-cx-h1    47.8      112.90               5/2017            2    0.0019
cd-cx-np    80.5      123.31               5/2017            2
c2-cx-cd    66.2      115.40               5/2017            2    0.2042
cx-op-op   110.3       56.13               5/2017            1
s4-cy-sq    68.1       92.38               5/2017            2    0.0006
c3-cy-s4    64.3      100.56               5/2017            2    0.0091
c3-cy-h2    45.2      118.37               5/2017            1
c3-cy-sq    64.2      106.21               5/2017            2    0.0145
cx-c2-os    85.7      116.34               5/2017            2    3.6043
cy-c3-s6    65.3      106.22               5/2017            2
cy-py-cy    49.3       83.53               5/2017            2
py-cy-py   106.6       96.47               5/2017            2
cl-cy-cv    71.0      113.53               5/2017            2    0.7703
cl-c2-cv    72.6      122.17               5/2017            2    0.6394
cx-np-os    83.7      110.33               5/2017            2    1.1321
c -cy-oh    86.7      104.48               5/2017            1
c3-cy-oh    84.8      110.75               5/2017            2    1.5973
c3-nh-cy    64.1      119.55               5/2017            2    3.3739
c3-p5-op    60.3      107.93               5/2017            2    0.1775
ca-ce-cy    67.0      110.27               5/2017            2   19.5804
ca-cy-ce    69.3      100.40               5/2017            2   16.4058
cx-cu-f     78.9      146.47               5/2017            2
cu-cu-f     83.5      150.20               5/2017            2
c1-cy-hc    49.2      108.46               5/2017            1
n3-py-np    77.8      107.41               5/2017            1
cy-c3-n     88.5       98.88               5/2017            1
n2-ce-nm   109.9      124.51               5/2017            1
ce-ce-nm    84.6      119.01               5/2017            1
ca-ne-cv    68.1      124.70               5/2017            1
c2-cx-ni    85.5      107.88               5/2017            1
c -nj-nq    91.4       95.27               5/2017            1
ca-nj-nq    79.6      125.44               5/2017            1
cy-nq-nj    92.6       87.97               5/2017            1
hn-nq-nj    60.9      106.36               5/2017            1
c3-cy-no    80.1      116.41               5/2017            1
c -cy-sy    63.4      108.13               5/2017            1
ca-sy-cy    69.6      105.32               5/2017            1
h2-cx-np    59.3      116.40               5/2017            1
ca-cx-h2    46.7      116.36               5/2017            1
c3-ss-cx    68.5      107.07               5/2017            1
cd-c3-cy    65.3      112.94               5/2017            1
c1-cx-ss    62.8      115.61               5/2017            1
c -cx-s4    63.5      106.85               5/2017            1
cx-c3-s6    66.0      104.37               5/2017            1
c2-c1-cv    60.2      179.30               5/2017            1
cx-c2-f     88.9      112.57               5/2017            1
ce-n2-nj    89.0      115.30               5/2017            1
cy-nj-n2    77.2      133.72               5/2017            1
c -nj-n2    80.6      129.93               5/2017            1
cx-sp-cx   103.6       47.47               5/2017            1
op-s6-sp   120.4       58.92               5/2017            1
op-sp-s6   128.1       48.17               5/2017            1
s6-op-sp    78.4       72.91               5/2017            1
ce-cy-s4    59.5      118.23               5/2017            1
cx-cy-nj    93.6       87.93               5/2017            1
cx-cy-h2    44.4      123.72               5/2017            1
cx-cy-s6    61.3      116.63               5/2017            1
cx-c -nj    95.5       90.16               5/2017            1
cd-c -cy    64.3      117.42               5/2017            1
c -nj-c1    64.0      134.58               5/2017            1
c1-nj-cy    62.8      131.60               5/2017            1
cy-c3-i     59.7      115.35               5/2017            1
cg-c1-nj    76.4      179.85               5/2017            1
br-cy-c3    63.0      115.71               5/2017            1
cx-c3-cy    69.8       97.58               5/2017            1
br-cy-cx    62.4      118.03               5/2017            1
c3-cx-cy    69.6       98.40               5/2017            1
cc-c3-cy    65.2      113.36               5/2017            1
c1-cy-oh    89.5      105.02               5/2017            1
c3-nh-cx    63.0      124.94               5/2017            1
cl-c -cx    71.3      112.60               5/2017            1
nj-c3-os   110.4      107.76               5/2017            1
cv-p3-n3    59.7      106.66               5/2017            1
cy-p3-n3    57.0      110.11               5/2017            1
cv-p3-cy    52.7       79.26               5/2017            1
cl-p5-cv    51.0      121.62               5/2017            1
cl-p5-cy    51.4      109.94               5/2017            1
cv-p5-n3    60.1      117.63               5/2017            1
cv-p5-cy    52.3       86.14               5/2017            1
cl-cv-p3    88.3      126.70               5/2017            1
cl-cv-p5    90.7      129.39               5/2017            1
p3-cv-p5   113.7      103.91               5/2017            1
p3-cy-p5   112.1       90.63               5/2017            1
h1-cx-p5    53.1      114.46               5/2017            1
op-cx-p5   101.5      114.21               5/2017            1
ca-cy-oq    83.3      113.13               5/2017            1
c -cy-ce    64.4      113.62               5/2017            1
cf-ss-cx    71.7      100.73               5/2017            1
no-cx-op   104.5      115.78               5/2017            1
ce-cy-os    84.2      113.17               5/2017            1
h2-cx-no    59.8      110.83               5/2017            1
op-cx-s6    79.8      111.21               5/2017            1
ce-cu-os    80.9      152.34               5/2017            1
cx-cu-os    79.0      140.68               5/2017            1
c3-os-cu    67.5      115.62               5/2017            1
cy-os-p5    80.4      128.86               5/2017            1
sp-cx-sp    79.7       71.77               5/2017            1
ca-sy-np    91.9      101.17               5/2017            1
ni-c -ni   109.7      110.35               5/2017            1
c1-c3-nj    86.0      110.55               5/2017            1
cy-cy-s4    58.0      122.92               5/2017            1
br-cy-br    67.9      111.77               5/2017            1
c1-cx-ce    64.4      123.15               5/2017            1
ce-cx-no    81.2      117.03               5/2017            1
c1-cx-cu    64.9      123.96               5/2017            1
cu-cx-no    82.0      117.44               5/2017            1
c1-cx-no    84.8      111.51               5/2017            1
cx-cu-ha    42.9      141.93               5/2017            1
ce-cu-ha    45.4      153.29               5/2017            1
c -oq-cv    74.9       90.77               5/2017            1
cx-c -oq    94.7       93.03               5/2017            1
cx-cv-oq    93.6       91.01               5/2017            1
cu-cv-oq    84.7      126.39               5/2017            1
cu-cv-cx    62.1      142.60               5/2017            1
cy-ce-n2    81.5      129.87               5/2017            1
na-cc-nm   107.1      121.71               5/2017            1
nd-cc-nm   106.5      128.30               5/2017            1
cx-c -cy    72.3       90.96               5/2017            1
cx-cy-cx    64.3      115.08               5/2017            1
c3-ss-cv    72.5      101.05               5/2017            1
sq-cv-ss    62.5      127.72               5/2017            1
ce-cy-sq    70.8       87.80               5/2017            1
cy-p5-cy    51.5       80.34               5/2017            1
c3-cy-ss    63.4      108.69               5/2017            1
c -cx-no    83.2      111.53               5/2017            1
cy-c2-o     85.2      122.78               5/2017            1
ce-c -oq    95.6       92.92               5/2017            1
s4-cy-s4    66.1       94.86               5/2017            1
s4-nq-s4    65.8      109.31               5/2017            1
br-cy-oq    80.6      112.77               5/2017            1
br-c3-cx    63.8      110.58               5/2017            1
cl-cx-f     92.9      113.42               5/2017            1
cy-os-no    83.0      114.10               5/2017            1
nj-c -os   113.9      110.38               5/2017            1
f -cx-os   112.8      115.27               5/2017            1
c2-cy-nq    80.8      118.88               5/2017            1
cx-c3-p5    80.4      112.94               5/2017            1
n3-cx-oh   110.1      111.48               5/2017            1
cx-c3-no    85.3      102.42               5/2017            1
c3-nl-c3    64.8      108.92               5/2017            1
c3-cy-hx    46.5      111.70               5/2017            1
c3-c3-nl    81.1      113.93               5/2017            1
cl-c2-cy    69.9      123.60               5/2017            1
ca-cc-cy    62.9      128.96               5/2017            1
cf-ce-cx    69.4      111.99               5/2017            1
cc-n -cy    66.1      120.06               5/2017            1
ce-cx-n2   126.8       49.50               5/2017            1
c -cx-n2    82.8      116.10               5/2017            1
nb-ca-nn   111.5      119.11               5/2017            1
cy-n3-s6    64.4      117.44               5/2017            1
br-cy-h1    42.9      106.03               5/2017            1
c3-cx-oh    83.7      115.84               5/2017            1
c3-cx-cc    65.6      115.28               5/2017            1
ca-c3-np    84.1      110.86               5/2017            1
cy-c3-na    81.9      115.21               5/2017            1
np-c3-np   110.9      103.87               5/2017            1
cl-cv-cv    69.1      133.87               5/2017            1
cl-cv-cy    67.4      131.66               5/2017            1
cv-cv-os    85.3      130.42               5/2017            1
cy-cv-os    78.3      134.37               5/2017            1
c2-cy-cv    64.1      117.51               5/2017            1
cv-os-p5    82.1      126.68               5/2017            1
c3-nq-nq    82.1      111.23               5/2017            1
c3-nh-cv    64.4      124.63               5/2017            1
hn-nq-nq    59.4      106.94               5/2017            1
cx-c2-ne    87.3      116.30               5/2017            1
cv-nh-hn    49.6      114.59               5/2017            1
cv-nh-n2    86.6      117.39               5/2017            1
cc-os-cy    65.7      120.91               5/2017            1
cx-ce-n1    84.1      122.09               5/2017            1
cv-nh-o     89.9      115.74               5/2017            1
cc-cx-h1    47.3      116.98               5/2017            1
cc-cc-cx    66.9      118.16               5/2017            1
c2-cy-ce    64.4      116.90               5/2017            1
ce-cy-oh    84.2      113.87               5/2017            1
cx-p3-cx    67.4       45.87               5/2017            1
cc-ce-nj    85.3      115.31               5/2017            1
cy-ce-n1    86.5      113.97               5/2017            1
ce-cy-n1    85.8      108.60               5/2017            1
c1-n1-cy    57.7      179.35               5/2017            1
c -op-cx    95.6       57.80               5/2017            1
cx-c -op   109.0       72.05               5/2017            1
o -c -op   110.4      137.49               5/2017            1
c3-c -ni    83.4      114.01               5/2017            1
c -ne-cu    70.1      118.64               5/2017            1
cu-cx-op   125.9       51.95               5/2017            1
cx-cu-ne    75.8      158.18               5/2017            1
ne-cu-op   110.3      133.54               5/2017            1
cx-cu-op   113.8       68.28               5/2017            1
cy-c -s     63.1      124.50               5/2017            1
cu-op-cx    94.1       59.77               5/2017            1
cd-cx-op    84.0      115.97               5/2017            1
c -cx-cd    64.7      119.27               5/2017            1
c3-cv-cy    59.2      138.62               5/2017            1
c3-cv-ce    64.9      127.59               5/2017            1
os-cy-os   112.3      107.01               5/2017            1
c3-os-nj    84.8      110.39               5/2017            1
cy-c3-ss    62.0      114.66               5/2017            1
c -cx-oh    80.1      128.25               5/2017            1
ce-cx-oh    81.0      125.60               5/2017            1
ca-c3-nk    81.3      115.36               5/2017            1
cy-cx-op    82.3      116.61               5/2017            1
ch-c -cx    66.4      115.27               5/2017            1
cy-cx-h1    46.1      114.75               5/2017            1
cx-cy-nq    81.4      115.83               5/2017            1
cx-cy-h1    47.2      109.34               5/2017            1
np-p3-np    79.8       95.24               5/2017            1
h2-cy-nq    59.0      115.82               5/2017            1
nq-cy-os   106.0      115.12               5/2017            1
cv-n2-os    90.9      109.54               5/2017            1
c3-s6-nj    92.2      100.02               5/2017            1
cy-c2-nh    83.3      118.62               5/2017            1
cy-c2-n2    83.4      124.85               5/2017            1
c2-cy-ca    64.5      116.61               5/2017            1
c -sq-cy    80.9       76.78               5/2017            1
cc-n -cx    65.9      120.69               5/2017            1
c3-nj-cx    61.0      132.94               5/2017            1
nj-c -oq   123.0       93.75               5/2017            1
nj-cx-op   102.1      125.92               5/2017            1
nj-cx-oq   120.6       90.20               5/2017            1
cx-cx-oq    79.9      125.67               5/2017            1
op-cx-oq   105.4      119.09               5/2017            1
c -oq-cx    76.4       87.79               5/2017            1
c3-os-np    84.6      107.95               5/2017            1
n -cx-op   108.1      113.29               5/2017            1
c2-cx-ce    68.5      105.95               5/2017            1
cu-c2-n     86.0      126.56               5/2017            1
c -cy-ss    60.6      118.39               5/2017            1
c1-n1-cx    59.2      177.15               5/2017            1
n1-cx-op   107.8      117.37               5/2017            1
ca-cy-nh    84.4      111.09               5/2017            1
cy-n3-sy    62.4      122.88               5/2017            1
op-cx-op   140.9       66.60               5/2017            1
ca-ce-cv    63.2      137.31               5/2017            1
c1-cx-ni    83.6      115.91               5/2017            1
c2-cy-c2    65.3      114.06               5/2017            1
c1-c3-nq    85.3      112.05               5/2017            1
c1-c3-nk    85.0      108.99               5/2017            1
cy-c -ss    62.5      115.55               5/2017            1
nj-cy-sh    78.8      114.00               5/2017            1
h2-cy-sh    42.4      109.40               5/2017            1
cy-cy-sh    61.0      117.83               5/2017            1
cy-sh-hs    52.2       93.94               5/2017            1
c1-cy-cl    74.3      106.10               5/2017            1
c1-cy-cv    65.0      117.74               5/2017            1
n3-cx-p5   100.7      115.88               5/2017            1
o -c -sq    75.1      132.86               5/2017            1
c -cx-cu    65.0      118.78               5/2017            1
ca-cx-f     88.1      111.96               5/2017            1
c2-cy-f     89.1      108.45               5/2017            1
cy-c2-f     86.1      117.19               5/2017            1
c2-cx-nm    83.8      114.54               5/2017            1
cy-c -sq    68.6       94.13               5/2017            1
c1-cy-oq    86.2      109.67               5/2017            1
c1-cy-c3    66.9      110.22               5/2017            1
op-cx-s4    78.5      111.64               5/2017            1
c3-cx-s4    60.8      115.92               5/2017            1
ca-os-cx    70.1      106.92               5/2017            1
""")

gaff_dihedrals = dedent("""
X -c -c -X    4    1.200       180.000           2.000
X -c -c1-X    2    0.000       180.000           2.000
X -c -cg-X    2    0.000       180.000           2.000      same as X-c-c1-X
X -c -ch-X    2    0.000       180.000           2.000
X -c -c2-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -cu-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -cv-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -ce-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -cf-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -c3-X    6    0.000       180.000           2.000      JCC, 7, (1986), 230
X -c -cx-X    6    0.000       180.000           2.000      JCC, 7, (1986), 230
X -c -cy-X    6    0.000       180.000           2.000      JCC, 7, (1986), 230
X -c -ca-X    4    4.000       180.000           2.000      optimized by Junmei Wang, Jan-2013
X -c -cc-X    4   11.500       180.000           2.000      statistic value
X -c -cd-X    4   11.500       180.000           2.000      statistic value
X -c -n -X    4   10.000       180.000           2.000      AA,NMA (no c-n3, c-n4, c-nh)
X -c -n2-X    2    8.300       180.000           2.000      double bond, same as X-c2-n2-X
X -c -nc-X    2    8.00        180.000           2.000      same as X-C-NC-X
X -c -nd-X    2    8.00        180.000           2.000      same as X-C-NC-X
X -c -ne-X    2    0.400       180.000           2.000      single bond
X -c -nf-X    2    0.400       180.000           2.000      single bond
X -c -na-X    4    5.800       180.000          -2.000
X -c -na-X    4    1.400       180.000           4.000
X -c -no-X    4    1.800       180.000           2.000
X -c -oh-X    2    4.600       180.000           2.000      Junmei et al, 1999
X -c -os-X    2    5.400       180.000           2.000      Junmei et al, 1999
X -c -p2-X    2   13.300       180.000           2.000      double bond, same as X-c2-p2-X
X -c -pc-X    2    4.000       180.000           2.000      estimated
X -c -pd-X    2    4.000       180.000           2.000      estimated
X -c -pe-X    2    0.000       180.000           2.000      single bond
X -c -pf-X    2    0.000       180.000           2.000      single bond
X -c -p3-X    4    6.200       180.000           2.000
X -c -p4-X    4    5.400       180.000           2.000
X -c -px-X    4    5.400       180.000           2.000
X -c -p5-X    4    4.000         0.000           2.000
X -c -py-X    4    4.000         0.000           2.000
X -c -sh-X    2    4.500       180.000           2.000
X -c -ss-X    2    6.200       180.000           2.000
X -c -s4-X    4    0.800       180.000           2.000
X -c -sx-X    4    0.800       180.000           2.000
X -c -s6-X    6    3.000         0.000           2.000
X -c -sy-X    6    3.000         0.000           2.000
X -c1-c1-X    1    0.000       180.000           2.000      for both triple and single bonds
X -c1-cg-X    1    0.000       180.000           2.000      for both triple and single bonds
X -c1-ch-X    1    0.000       180.000           2.000      for both triple and single bonds
X -cg-cg-X    1    0.000       180.000           2.000      for both triple and single bonds
X -ch-ch-X    1    0.000       180.000           2.000      for both triple and single bonds
X -cg-ch-X    1    0.000       180.000           2.000      for both triple and single bonds
X -c1-c2-X    2    0.000       180.000           2.000
X -c1-c3-X    3    0.000       180.000           2.000
X -c1-ca-X    2    0.000       180.000           2.000
X -c1-cc-X    2    0.000       180.000           2.000
X -c1-cd-X    2    0.000       180.000           2.000
X -c1-ce-X    2    0.000       180.000           2.000
X -c1-cf-X    2    0.000       180.000           2.000
X -c1-cu-X    2    0.000       180.000           2.000
X -c1-cv-X    2    0.000       180.000           2.000
X -c1-cx-X    3    0.000       180.000           2.000
X -c1-cy-X    3    0.000       180.000           2.000
X -c1-n -X    2    0.000       180.000           2.000
X -c1-n2-X    1    0.000       180.000           2.000
X -c1-n3-X    2    0.000       180.000           2.000
X -c1-n4-X    3    0.000       180.000           2.000
X -c1-na-X    2    0.000       180.000           2.000
X -c1-nb-X    2    0.000       180.000           2.000
X -c1-nc-X    2    0.000       180.000           2.000
X -c1-nd-X    2    0.000       180.000           2.000
X -c1-ne-X    2    0.000       180.000           2.000
X -c1-nf-X    2    0.000       180.000           2.000
X -c1-nh-X    2    0.000       180.000           2.000
X -c1-no-X    2    0.000       180.000           2.000
X -c1-oh-X    1    0.000       180.000           2.000
X -c1-os-X    1    0.000       180.000           2.000
X -c1-p2-X    1    0.000       180.000           2.000
X -c1-pb-X    1    0.000       180.000           2.000
X -c1-pc-X    1    0.000       180.000           2.000
X -c1-pd-X    1    0.000       180.000           2.000
X -c1-pe-X    1    0.000       180.000           2.000
X -c1-pf-X    1    0.000       180.000           2.000
X -c1-p3-X    2    0.000       180.000           2.000
X -c1-p4-X    2    0.000       180.000           2.000
X -c1-px-X    2    0.000       180.000           2.000
X -c1-p5-X    3    0.000       180.000           2.000
X -c1-py-X    3    0.000       180.000           2.000
X -c1-s2-X    1    0.000       180.000           2.000
X -c1-sh-X    1    0.000       180.000           2.000
X -c1-ss-X    1    0.000       180.000           2.000
X -c1-s4-X    2    0.000       180.000           2.000
X -c1-sx-X    2    0.000       180.000           2.000
X -c1-s6-X    3    0.000       180.000           2.000
X -c1-sy-X    3    0.000       180.000           2.000
X -c2-c2-X    4   26.600       180.000           2.000      c2=c2 double bond, intrpol.bsd.on C6H6
X -c2-ce-X    4   26.600       180.000           2.000      c2=c2 double bond, intrpol.bsd.on C6H6
X -c2-cf-X    4   26.600       180.000           2.000      c2=c2 double bond, intrpol.bsd.on C6H6
X -ce-cf-X    4   26.600       180.000           2.000      c2=c2 double bond, intrpol.bsd.on C6H6
X -ce-ce-X    4    4.000       180.000           2.000      c2-c2 single bond, parm99
X -cf-cf-X    4    4.000       180.000           2.000      c2-c2 single bond, parm99
X -cc-cd-X    4   16.000       180.000           2.000      statistic value of parm94
X -cc-cc-X    4   16.000       180.000           2.000      statistic value of parm94
X -cd-cd-X    4   16.000       180.000           2.000      statistic value of parm94
X -c2-c3-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c2-ca-X    4    2.800       180.000           2.000      optimized by Junmei Wang, March 2013
X -c2-n -X    4    2.600       180.000           2.000
X -c2-n2-X    2    8.300       180.000           2.000      double bond, parm99
X -c2-ne-X    2    8.300       180.000           2.000      double bond, parm99
X -c2-nf-X    2    8.300       180.000           2.000      double bond, parm99
X -ce-ne-X    2    1.600       180.000           2.000      single bond
X -cf-nf-X    2    1.600       180.000           2.000      single bond
X -c2-nc-X    2    9.500       180.000           2.000      statistic value from parm94
X -c2-nd-X    2    9.500       180.000           2.000      statistic value from parm94
X -cc-nd-X    2    9.500       180.000           2.000      statistic value from parm94
X -cd-nc-X    2    9.500       180.000           2.000      statistiv value from parm94
X -cc-nc-X    2    9.500       180.000           2.000      statistic value from parm94
X -cd-nd-X    2    9.500       180.000           2.000      statistiv value from parm94
X -c2-n3-X    4    1.200       180.000           2.000      intrpol.
X -c2-n4-X    6    0.000       180.000           3.000      intrpol.
X -c2-na-X    4    2.500       180.000           2.000
X -cc-na-X    4    6.800       180.000           2.000      statistic value from parm94
X -cd-na-X    4    6.800       180.000           2.000      statistic value from parm94
X -c2-nh-X    4    2.700       180.000           2.000
X -c2-no-X    4    3.000       180.000           2.000
X -c2-oh-X    2    2.100       180.000           2.000      parm99
X -c2-os-X    2    2.100       180.000           2.000      parm99
X -c2-p2-X    2   13.300       180.000           2.000      double bond
X -c2-pe-X    2   13.300       180.000           2.000      double bond
X -c2-pf-X    2   13.300       180.000           2.000      double bond
X -ce-pf-X    2   13.300       180.000           2.000      double bond
X -ce-pe-X    2    1.900       180.000           2.000      single bond
X -cf-pf-X    2    1.900       180.000           2.000      single bond
X -c2-pc-X    2    9.500       180.000           2.000      estimated
X -c2-pd-X    2    9.500       180.000           2.000      estimated
X -cc-pc-X    2    9.500       180.000           2.000      estimated
X -cc-pd-X    2    9.500       180.000           2.000      estimated
X -cd-pc-X    2    9.500       180.000           2.000      estimated
X -cd-pd-X    2    9.500       180.000           2.000      estimated
X -c2-p3-X    4    1.800       180.000           2.000
X -c2-p4-X    4   26.600       180.000           2.000      c2=p4 double bond !!!
X -ce-p4-X    4   26.600       180.000           2.000      c2=p4 double bond !!!
X -cf-p4-X    4   26.600       180.000           2.000      c2=p4 double bond !!!
X -c2-px-X    4    1.300         0.000           2.000
X -ce-px-X    4    1.300         0.000           2.000
X -cf-px-X    4    1.300         0.000           2.000
X -c2-p5-X    6   39.900       180.000           2.000      c2=p5 double bond !!!
X -ce-p5-X    6   39.900       180.000           2.000      c2=p5 double bond !!!
X -cf-p5-X    6   39.900       180.000           2.000      c2=p5 double bond !!!
X -c2-py-X    6    8.600       180.000           2.000
X -ce-py-X    6    8.600       180.000           2.000
X -cf-py-X    6    8.600       180.000           2.000
X -c2-sh-X    2    1.000       180.000           2.000
X -c2-ss-X    2    2.200       180.000           2.000
X -c2-s4-X    4   26.600       180.000           2.000      c2=s4 double bond  !!!
X -ce-s4-X    4   26.600       180.000           2.000      c2=s4 double bond  !!!
X -cf-s4-X    4   26.600       180.000           2.000      c2=s4 double bond  !!!
X -c2-sx-X    4    2.400         0.000           2.000
X -ce-sx-X    4    2.400         0.000           2.000
X -cf-sx-X    4    2.400         0.000           2.000
X -c2-s6-X    6   39.900       180.000           2.000      c2=s6 double bond  !!!
X -ce-s6-X    6   39.900       180.000           2.000      c2=s6 double bond  !!!
X -cf-s6-X    6   39.900       180.000           2.000      c2=s6 double bond  !!!
X -c2-sy-X    6    7.600       180.000           2.000
X -ce-sy-X    6    7.600       180.000           2.000
X -cf-sy-X    6    7.600       180.000           2.000
X -c3-c3-X    9    1.400         0.000           3.000      JCC,7,(1986),230
X -cx-cx-X    9    1.400         0.000           3.000      same as X-c3-c3-X
X -cy-cy-X    9    1.400         0.000           3.000      same as X-c3-c3-X
X -c3-ca-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c3-n -X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -cx-n -X    6    0.000         0.000           2.000      same as X-c3-n-X
X -cy-n -X    6    0.000         0.000           2.000      same as X-c3-n-X
X -c3-n2-X    6    0.000         0.000           3.000      JCC,7,(1986),230
X -c3-ne-X    6    0.000         0.000           3.000      JCC,7,(1986),230
X -c3-nf-X    6    0.000         0.000           3.000      JCC,7,(1986),230
X -c3-n3-X    6    1.800         0.000           3.000      Junmei et al, 1999
X -c3-n4-X    9    1.400         0.000           3.000      JCC,7,(1986),230
X -c3-na-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c3-nh-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c3-no-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c3-oh-X    3    0.500         0.000           3.000      JCC,7,(1986),230
X -c3-os-X    3    1.150         0.000           3.000      JCC,7,(1986),230
X -c3-p2-X    3    0.800       180.000           2.000
X -c3-pe-X    3    0.800       180.000           2.000
X -c3-pf-X    3    0.800       180.000           2.000
X -c3-p3-X    6    0.800         0.000           3.000
X -c3-p4-X    6    0.800         0.000           3.000
X -c3-px-X    6    0.800         0.000           3.000
X -c3-p5-X    9    0.200         0.000           3.000
X -c3-py-X    9    0.200         0.000           3.000
X -c3-sh-X    3    0.750         0.000           3.000      JCC,7,(1986),230
X -c3-ss-X    3    1.000         0.000           3.000      JCC,7,(1986),230
X -c3-s4-X    6    1.200         0.000           3.000
X -c3-sx-X    6    1.200         0.000           3.000
X -c3-s6-X    9    1.300         0.000           3.000
X -c3-sy-X    9    1.300         0.000           3.000
X -c3-cc-X    6    0.000         0.000           3.000      same as X-c3-ca-X
X -c3-cd-X    6    0.000         0.000           3.000      same as X-c3-ca-X
X -ca-ca-X    4   14.500       180.000           2.000      intrpol.bsd.on C6H6
X -ca-cp-X    4   14.500       180.000           2.000      intrpol.bsd.on C6H6
X -ca-cq-X    4   14.500       180.000           2.000      intrpol.bsd.on C6H6
X -cp-cp-X    4    4.000       180.000           2.000      estimated, intrpol.
X -cq-cq-X    4    4.000       180.000           2.000      estimated, intrpol.
X -ca-n -X    4    1.800       180.000           2.000
X -ca-n2-X    2    0.000       180.000           3.000
X -ca-ne-X    2    0.000       180.000           3.000
X -ca-nf-X    2    0.000       180.000           3.000
X -ca-n4-X    4    7.000         0.000           2.000
X -ca-na-X    4    1.200       180.000           2.000
X -ca-nb-X    2    9.60        180.0             2.000      same as X-CA-NC-X
X -ca-nc-X    2    9.60        180.0             2.000      same as X-CA-NC-X
X -ca-nd-X    2    9.60        180.0             2.000      same as X-CA-NC-X
X -ca-nh-X    4    4.200       180.000           2.000
X -cc-nh-X    4    4.200       180.000           2.000      same as X-ca-nh-X
X -cd-nh-X    4    4.200       180.000           2.000      same as X-ca-nh-X
X -ca-no-X    4    2.400       180.000           2.000
X -ca-oh-X    2    1.800       180.000           2.000      Junmei et al, 99
X -ca-os-X    2    1.800       180.000           2.000      same as X-ca-oh-X
X -ca-p2-X    2    1.200       180.000           2.000
X -ca-pe-X    2    1.200       180.000           2.000      same as X-ca-p2-X
X -ca-pf-X    2    1.200       180.000           2.000      same as X-ca-p2-X
X -ca-pc-X    2    9.600       180.000           2.000      estimated, intrpol
X -ca-pd-X    2    9.600       180.000           2.000      estimated, intrpol
X -ca-p3-X    4    0.000       180.000           2.000
X -ca-p4-X    4    2.100       180.000           2.000
X -ca-px-X    4    2.100       180.000           2.000      estimated, same as X-ca-p4-X
X -ca-p5-X    6    8.800       180.000           2.000
X -ca-py-X    6    8.800       180.000           2.000      estimated, same as X-ca-p5-X
X -ca-sh-X    2    0.000       180.000           2.000
X -ca-ss-X    2    0.800       180.000           2.000
X -ca-s4-X    4    1.200         0.000           2.000
X -ca-sx-X    4    1.200         0.000           2.000      estimated, same as X-ca-s4-X
X -ca-s6-X    6    7.800       180.000           2.000
X -ca-sy-X    6    7.800       180.000           2.000      estimated, same as X-ca-s6-X
X -n -cc-X    4    6.600       180.000           2.000      statistic value from parm94
X -n -cd-X    4    6.600       180.000           2.000      statistic value from parm94
X -n -n -X    4    4.600         0.000           2.000
X -n -n2-X    2    0.800         0.000           2.000
X -n -ne-X    2    0.800         0.000           2.000
X -n -nf-X    2    0.800         0.000           2.000
X -n -n3-X    4    4.300         0.000           2.000
X -n -n4-X    4    3.800         0.000           2.000
X -n -na-X    4    2.800         0.000           2.000
X -n -nc-X    2    9.600       180.000           2.000      estimated, intrpol.
X -n -nd-X    2    9.600       180.000           2.000      estimated, intrpol.
X -n -nh-X    4    4.400         0.000           2.000
X -n -no-X    4    5.500       180.000           2.000
X -n -oh-X    2    3.000         0.000           2.000
X -n -os-X    2    2.200         0.000           2.000
X -n -p2-X    2    2.000       180.000           2.000
X -n -pe-X    2    2.000       180.000           2.000
X -n -pf-X    2    2.000       180.000           2.000      estimated, intrpol.
X -n -pc-X    2    9.600       180.000           2.000      estimated, intrpol.
X -n -pd-X    2    9.600       180.000           2.000
X -n -p3-X    4    9.000         0.000           2.000
X -n -p4-X    4    1.300         0.000           2.000
X -n -px-X    4    1.300         0.000           2.000
X -n -p5-X    6   13.200       180.000           2.000
X -n -py-X    6   13.200       180.000           2.000
X -n -sh-X    2    2.200         0.000           2.000
X -n -ss-X    2    3.000         0.000           2.000
X -n -s4-X    4    6.000         0.000           3.000
X -n -sx-X    4    6.000         0.000           3.000
X -n -s6-X    6    6.600       180.000           2.000
X -n -sy-X    6    6.600       180.000           2.000
X -n1-c2-X    2    0.000       180.000           2.000
X -n1-c3-X    3    0.000       180.000           2.000
X -n1-ca-X    2    0.000       180.000           2.000
X -n1-cc-X    2    0.000       180.000           2.000
X -n1-cd-X    2    0.000       180.000           2.000
X -n1-ce-X    2    0.000       180.000           2.000
X -n1-cf-X    2    0.000       180.000           2.000
X -n1-cu-X    2    0.000       180.000           2.000
X -n1-cv-X    2    0.000       180.000           2.000
X -n1-cx-X    3    0.000       180.000           2.000
X -n1-cy-X    3    0.000       180.000           2.000
X -n1-n -X    2    0.000       180.000           2.000
X -n1-n1-X    1    0.000       180.000           2.000
X -n1-n2-X    1    0.000       180.000           2.000
X -n1-n3-X    2    0.000       180.000           2.000
X -n1-n4-X    3    0.000       180.000           2.000
X -n1-na-X    2    0.000       180.000           2.000
X -n1-nb-X    2    0.000       180.000           2.000
X -n1-nc-X    2    0.000       180.000           2.000
X -n1-nd-X    2    0.000       180.000           2.000
X -n1-ne-X    2    0.000       180.000           2.000
X -n1-nf-X    2    0.000       180.000           2.000
X -n1-nh-X    2    0.000       180.000           2.000
X -n1-no-X    2    0.000       180.000           2.000
X -n1-oh-X    1    0.000       180.000           2.000
X -n1-os-X    1    0.000       180.000           2.000
X -n1-p2-X    1    0.000       180.000           2.000
X -n1-pb-X    1    0.000       180.000           2.000
X -n1-pc-X    1    0.000       180.000           2.000
X -n1-pd-X    1    0.000       180.000           2.000
X -n1-pe-X    1    0.000       180.000           2.000
X -n1-pf-X    1    0.000       180.000           2.000
X -n1-p3-X    2    0.000       180.000           2.000
X -n1-p4-X    2    0.000       180.000           2.000
X -n1-px-X    2    0.000       180.000           2.000
X -n1-p5-X    3    0.000       180.000           2.000
X -n1-py-X    3    0.000       180.000           2.000
X -n1-s2-X    1    0.000       180.000           2.000
X -n1-sh-X    1    0.000       180.000           2.000
X -n1-ss-X    1    0.000       180.000           2.000
X -n1-s4-X    2    0.000       180.000           2.000
X -n1-sx-X    2    0.000       180.000           2.000
X -n1-s6-X    3    0.000       180.000           2.000
X -n1-sy-X    3    0.000       180.000           2.000
X -n2-n2-X    1    3.000       180.000          -2.000      double bond
X -n2-n2-X    1    2.800         0.000           1.000      double bond
X -n2-ne-X    1    3.000       180.000          -2.000      double bond
X -n2-ne-X    1    2.800         0.000           1.000      double bond
X -n2-nf-X    1    3.000       180.000          -2.000      double bond
X -n2-nf-X    1    2.800         0.000           1.000      double bond
X -ne-nf-X    1    3.000       180.000          -2.000      double bond
X -ne-nf-X    1    2.800         0.000           1.000      double bond
X -ne-ne-X    1    1.200       180.000           2.000      single bond, intrpol
X -nf-nf-X    1    1.200       180.000           2.000      single bond, intrpol
X -nc-nc-X    1    4.000       180.000           2.000      estimated, intrpol
X -nd-nd-X    1    4.000       180.000           2.000      estimated, intrpol
X -nc-nd-X    1    4.000       180.000           2.000      estimated, intrpol
X -n2-nc-X    1    3.000       180.000          -2.000      same as X-n2-n2-X
X -n2-nc-X    1    2.800         0.000           1.000
X -n2-nd-X    1    3.000       180.000          -2.000      same as X-n2-n2-X
X -n2-nd-X    1    2.800         0.000           1.000
X -n2-n3-X    2   12.200       180.000           2.000
X -ne-n3-X    2   12.200       180.000           2.000
X -nf-n3-X    2   12.200       180.000           2.000
X -n2-n4-X    3   24.000       180.000           2.000
X -ne-n4-X    3   24.000       180.000           2.000
X -nf-n4-X    3   24.000       180.000           2.000
X -n2-na-X    2    3.400       180.000           2.000
X -ne-na-X    2    3.400       180.000           2.000
X -nf-na-X    2    3.400       180.000           2.000
X -na-nc-X    2    9.600       180.000           2.000      estimated, intrpol.
X -na-nd-X    2    9.600       180.000           2.000      estimated, intrpol.
X -n2-nh-X    2    5.600       180.000           2.000
X -ne-nh-X    2    5.600       180.000           2.000
X -nf-nh-X    2    5.600       180.000           2.000
X -n2-no-X    2    1.500       180.000           2.000
X -ne-no-X    2    1.500       180.000           2.000
X -nf-no-X    2    1.500       180.000           2.000
X -n2-oh-X    1    3.200       180.000           2.000
X -ne-oh-X    1    3.200       180.000           2.000
X -nf-oh-X    1    3.200       180.000           2.000
X -n2-os-X    1    3.000       180.000           2.000
X -ne-os-X    1    3.000       180.000           2.000
X -nf-os-X    1    3.000       180.000           2.000
X -nc-os-X    1    4.800       180.000           2.000      estimated, intrpol.
X -nc-ss-X    1    4.800       180.000           2.000      estimated, intrpol.
X -n2-p2-X    1    5.400       180.000           2.000      estimated, intrpol.
X -n2-pe-X    1    5.400       180.000           2.000      estimated, intrpol.
X -n2-pf-X    1    5.400       180.000           2.000      estimated, intrpol.
X -ne-pf-X    1    5.400       180.000           2.000      estimated, intrpol.
X -n2-pc-X    1    5.400       180.000           2.000      estimated, intrpol.
X -n2-pd-X    1    5.400       180.000           2.000      estimated, intrpol.
X -nc-p2-X    1    5.400       180.000           2.000      estimated, intrpol.
X -nd-p2-X    1    5.400       180.000           2.000      estimated, intrpol.
X -nc-pc-X    1    6.600       180.000           2.000      estimated, intrpol.
X -nd-pd-X    1    6.600       180.000           2.000      estimated, intrpol.
X -nd-pc-X    1    6.600       180.000           2.000      estimated, intrpol.
X -nc-pd-X    1    6.600       180.000           2.000      estimated, intrpol.
X -ne-pe-X    1    0.600         0.000           1.000      single bond
X -nf-pf-X    1    0.600         0.000           1.000      single bond
X -n2-p3-X    2    4.200       180.000           2.000
X -n2-p4-X    2   13.300       180.000           2.000      estimated  !!!
X -ne-p4-X    2   13.300       180.000           2.000      estimated  !!!
X -nf-p4-X    2   13.300       180.000           2.000      estimated  !!!
X -n2-p5-X    3   20.000       180.000           2.000      estimated  !!!
X -ne-p5-X    3    3.000       180.000           3.000
X -nf-p5-X    3    3.000       180.000           3.000
X -ne-px-X    3    3.000       180.000           3.000
X -nf-px-X    3    3.000       180.000           3.000
X -n2-sh-X    1    2.100       180.000           2.000
X -ne-sh-X    1    2.100       180.000           2.000
X -nf-sh-X    1    2.100       180.000           2.000
X -n2-ss-X    1    2.800       180.000          -2.000
X -n2-ss-X    1    1.300       180.000           1.000
X -ne-ss-X    1    2.800       180.000          -2.000
X -ne-ss-X    1    1.300       180.000           1.000
X -nf-ss-X    1    2.800       180.000          -2.000
X -nf-ss-X    1    1.300       180.000           1.000
X -n2-s4-X    2   13.300       180.000           2.000      estimated !!!
X -ne-sx-X    2    3.000       180.000           3.000
X -nf-sx-X    2    3.000       180.000           3.000
X -n2-s6-X    3   20.000       180.000           2.000      estimated  !!!
X -ne-sy-X    3    1.500       180.000          -3.000
X -ne-sy-X    3   20.400       180.000           1.000
X -nf-sy-X    3    1.500       180.000          -3.000
X -nf-sy-X    3   20.400       180.000           1.000
X -n3-n3-X    4    9.000         0.000           2.000
X -n3-n4-X    6    1.500         0.000           3.000
X -n3-na-X    4    6.400         0.000           2.000
X -n3-nh-X    4    7.600         0.000           2.000
X -n3-no-X    4   16.000       180.000           2.000
X -n3-oh-X    1    2.200         0.000           2.000
X -n3-os-X    1    1.800         0.000           2.000
X -n3-p2-X    2    6.400       180.000           2.000
X -n3-pe-X    2    6.400       180.000           2.000
X -n3-pf-X    2    6.400       180.000           2.000
X -n3-p3-X    4    9.400         0.000           2.000
X -n3-p4-X    4    8.400       180.000           2.000
X -n3-px-X    4    8.400       180.000           2.000
X -n3-p5-X    6   18.000       180.000           2.000
X -n3-py-X    6   18.000       180.000           2.000
X -n3-sh-X    1    3.100         0.000           2.000
X -n3-ss-X    1    2.600         0.000           2.000
X -n3-s4-X    4   15.000         0.000           2.000
X -n3-sx-X    4   15.000         0.000           2.000
X -n3-s6-X    6   18.800         0.000           2.000
X -n3-sy-X    6   18.800         0.000           2.000
X -n4-n4-X    9    1.700         0.000           3.000
X -n4-na-X    6    1.400         0.000           3.000
X -n4-nh-X    6    1.100         0.000           3.000
X -n4-no-X    6    0.500       180.000           3.000
X -n4-oh-X    3    1.000         0.000           3.000
X -n4-os-X    3    1.700         0.000           3.000
X -n4-p2-X    3    0.500       180.000           3.000
X -n4-pe-X    3    0.500       180.000           3.000
X -n4-pf-X    3    0.500       180.000           3.000
X -n4-p3-X    6    0.900         0.000           3.000
X -n4-p4-X    4    0.200         0.000           3.000
X -n4-px-X    4    0.200         0.000           3.000
X -n4-p5-X    9    0.800         0.000           3.000
X -n4-py-X    9    0.800         0.000           3.000
X -n4-sh-X    3    2.000         0.000           3.000
X -n4-ss-X    3    1.000         0.000           3.000
X -n4-s4-X    6    1.700         0.000           3.000
X -n4-sx-X    6    1.700         0.000           3.000
X -n4-s6-X    9    1.200         0.000           3.000
X -n4-sy-X    9    1.200         0.000           3.000
X -na-na-X    4    3.600         0.000           2.000
X -na-nh-X    4    4.800         0.000           2.000
X -na-no-X    4   24.000       180.000           2.000
X -na-oh-X    2    2.000         0.000           2.000
X -na-os-X    2    1.300         0.000           2.000
X -na-p2-X    1    1.000       180.000           2.000
X -na-pe-X    1    1.000       180.000           2.000
X -na-pf-X    1    1.000       180.000           2.000
X -na-p3-X    4    5.800         0.000           2.000
X -na-p4-X    4    4.400         0.000           3.000
X -na-px-X    4    4.400         0.000           3.000
X -na-p5-X    6    5.000       180.000           2.000
X -na-py-X    6    5.000       180.000           2.000
X -na-sh-X    2    3.600         0.000           2.000
X -na-ss-X    2   15.600         0.000           2.000
X -na-s4-X    4    4.200         0.000           2.000
X -na-sx-X    4    4.200         0.000           2.000
X -na-s6-X    6   22.000       180.000           2.000
X -na-sy-X    6   22.000       180.000           2.000
X -nh-nh-X    4    7.200       180.000           3.000
X -nh-no-X    4   10.200       180.000           2.000
X -nh-oh-X    2    3.000         0.000           2.000
X -nh-os-X    2    3.000         0.000           1.000
X -nh-p2-X    2    2.800       180.000           2.000
X -nh-pe-X    2    2.800       180.000           2.000
X -nh-pf-X    2    2.800       180.000           2.000
X -nh-p3-X    4    9.400         0.000           2.000
X -nh-p4-X    4    4.700         0.000           3.000
X -nh-px-X    4    4.700         0.000           3.000
X -nh-p5-X    6    4.800         0.000           2.000
X -nh-py-X    6    4.800         0.000           2.000
X -nh-sh-X    2    3.200         0.000           2.000
X -nh-ss-X    2    4.200         0.000           2.000
X -nh-s4-X    4    3.000         0.000          -2.000
X -nh-s4-X    4    0.400       180.000           3.000
X -nh-sx-X    4    3.000         0.000          -2.000
X -nh-sx-X    4    0.400       180.000           3.000
X -nh-s6-X    6    0.600       180.000           2.000
X -nh-sy-X    6    0.600       180.000           2.000
X -no-no-X    4    1.600       180.000          -4.000
X -no-no-X    4    7.200       180.000           2.000
X -no-oh-X    2    7.800       180.000           2.000
X -no-os-X    2    6.000       180.000           2.000
X -no-p2-X    1    0.300       180.000           2.000
X -no-pe-X    1    0.300       180.000           2.000
X -no-pf-X    1    0.300       180.000           2.000
X -no-p3-X    4    7.600       180.000           2.000
X -no-p4-X    4    2.300       180.000           2.000
X -no-px-X    4    2.300       180.000           2.000
X -no-p5-X    6   14.400         0.000          -2.000
X -no-p5-X    6    2.400         0.000           3.000
X -no-py-X    6   14.400         0.000          -2.000
X -no-py-X    6    2.400         0.000           3.000
X -no-sh-X    2    4.600       180.000           2.000
X -no-ss-X    2    5.400       180.000           2.000
X -no-s4-X    4   10.400       180.000           2.000
X -no-sx-X    4   10.400       180.000           2.000
X -no-s6-X    6    2.000         0.000           2.000
X -no-sy-X    6    2.000         0.000           2.000
X -oh-oh-X    1    1.600         0.000           2.000
X -oh-os-X    1    1.600         0.000           2.000
X -oh-p2-X    1    1.500       180.000           2.000
X -oh-pe-X    1    1.500       180.000           2.000
X -oh-pf-X    1    1.500       180.000           2.000
X -oh-p3-X    2    0.800       180.000           3.000
X -oh-p4-X    2    1.400         0.000           1.000
X -oh-px-X    2    1.400         0.000           1.000
X -oh-p5-X    3    1.600         0.000           3.000
X -oh-py-X    3    1.600         0.000           3.000
X -oh-sh-X    1    2.400         0.000           2.000
X -oh-ss-X    1    2.400         0.000           2.000
X -oh-s4-X    2   10.000         0.000           1.000
X -oh-sx-X    2   10.000         0.000           1.000
X -oh-s6-X    3   28.500       180.000           1.000
X -oh-sy-X    3   28.500       180.000           1.000
X -os-os-X    1    1.000         0.000           1.000
X -os-ss-X    1    2.200         0.000           2.000
X -os-sh-X    1    1.800         0.000           2.000
X -os-s4-X    2    3.300         0.000           3.000
X -os-sx-X    2    3.300         0.000           3.000
X -os-s6-X    3    3.600       180.000           2.000
X -os-sy-X    3    3.600       180.000           2.000
X -os-p2-X    1    3.000       180.000          -2.000
X -os-p2-X    1    2.000       180.000           1.000
X -os-pe-X    1    3.000       180.000          -2.000
X -os-pe-X    1    2.000       180.000           1.000
X -os-pf-X    1    3.000       180.000          -2.000
X -os-pf-X    1    2.000       180.000           1.000
X -os-p3-X    2    4.400         0.000           2.000
X -os-p4-X    2    2.100       180.000           2.000
X -os-px-X    2    2.100       180.000           2.000
X -os-p5-X    3    2.400         0.000           2.000
X -os-py-X    3    2.400         0.000           2.000
X -p2-p2-X    1    6.600       180.000           2.000      estimated, intrpol.
X -p2-pe-X    1    6.600       180.000           2.000      estimated, intrpol.
X -p2-pf-X    1    6.600       180.000           2.000      estimated, intrpol.
X -p2-pc-X    1    6.600       180.000           2.000      estimated, intrpol.
X -p2-pd-X    1    6.600       180.000           2.000      estimated, intrpol.
X -pe-pe-X    1    1.200       180.000           2.000      single bond
X -pf-pf-X    1    1.200       180.000           2.000      single bond
X -pc-pc-X    1    7.200       180.000           2.000      estimated, intrpol.
X -pd-pd-X    1    7.200       180.000           2.000      estimated, intrpol.
X -pc-pd-X    1    7.200       180.000           2.000      estimated, intrpol.
X -p2-p3-X    2    2.400         0.000           1.000
X -pe-p3-X    2    2.400         0.000           1.000
X -pf-p3-X    2    2.400         0.000           1.000
X -p2-p4-X    2   13.300       180.000           2.000      estimated  !!!
X -pe-px-X    2    4.900         0.000           2.000
X -pf-px-X    2    4.900         0.000           2.000
X -p2-p5-X    3   20.000       180.000           2.000      estimated  !!!
X -pe-py-X    3    5.700         0.000           1.000
X -pf-py-X    3    5.700         0.000           1.000
X -p2-sh-X    1    1.400       180.000           2.000
X -pe-sh-X    1    1.400       180.000           2.000
X -pf-sh-X    1    1.400       180.000           2.000
X -p2-ss-X    1    1.400       180.000           2.000
X -pe-ss-X    1    1.400       180.000           2.000
X -pf-ss-X    1    1.400       180.000           2.000
X -p2-s4-X    2   13.300       180.000           2.000       estimated !!!
X -pe-sx-X    2    3.000         0.000           2.000
X -pf-sx-X    2    3.000         0.000           2.000
X -p2-s6-X    3   20.000       180.000           2.000       estimated !!!
X -pe-sy-X    3    1.200       180.000           3.000
X -pf-sy-X    3    1.200       180.000           3.000
X -p3-p3-X    4    2.000         0.000           3.000
X -p3-p4-X    4    3.600         0.000           1.000
X -p3-px-X    4    3.600         0.000           1.000
X -p3-p5-X    6   11.000       180.000           2.000
X -p3-py-X    6   11.000       180.000           2.000
X -p3-sh-X    2    9.200         0.000           2.000
X -p3-ss-X    2    2.300         0.000           3.000
X -p3-s4-X    4   15.400         0.000           2.000
X -p3-sx-X    4   15.400         0.000           2.000
X -p3-s6-X    6    1.600         0.000           3.000
X -p3-sy-X    6    1.600         0.000           3.000
X -p4-p4-X    4   26.600       180.000           2.000      estimated   !!!
X -px-px-X    4    5.800       180.000           2.000
X -p4-p5-X    6   39.900       180.000           2.000      estimated   !!!
X -px-py-X    6    1.900       180.000           2.000
X -p4-s4-X    4   26.600       180.000           2.000      estimated   !!!
X -px-sx-X    4    3.400         0.000           1.000
X -p4-s6-X    6   39.900       180.000           2.000      estimated   !!!
X -px-sy-X    6    0.700         0.000           3.000
X -p4-sh-X    2    0.500       180.000           1.000
X -px-sh-X    2    0.500       180.000           1.000
X -p4-ss-X    2    1.200       180.000           2.000
X -px-ss-X    2    1.200       180.000           2.000
X -p5-p5-X    9   60.000       180.000           2.000      estimated   !!!
X -py-py-X    9    5.400         0.000           2.000
X -p5-sh-X    3    0.900         0.000           3.000
X -py-sh-X    3    0.900         0.000           3.000
X -p5-ss-X    3   11.400       180.000           2.000
X -py-ss-X    3   11.400       180.000           2.000
X -p5-s4-X    6   40.000       180.000           2.000      estimated  !!!
X -py-sx-X    6    1.600         0.000           3.000
X -p5-s6-X    9   60.000       180.000           2.000      estimated  !!!
X -py-sy-X    9    2.500         0.000           3.000
X -sh-sh-X    1    5.600         0.000           3.000
X -sh-ss-X    1    5.300         0.000           3.000
X -sh-s4-X    2    1.400         0.000           3.000
X -sh-sx-X    2    1.400         0.000           3.000
X -sh-s6-X    3   14.000       180.000           2.000
X -sh-sy-X    3   14.000       180.000           2.000
X -ss-ss-X    1    0.000         0.000           3.000
X -ss-s4-X    2    0.600         0.000           3.000
X -ss-sx-X    2    0.600         0.000           3.000
X -ss-s6-X    3    9.200       180.000           2.000
X -ss-sy-X    3    9.200       180.000           2.000
X -s4-s4-X    4   26.600       180.000           2.000       estimated !!!
X -sx-sx-X    4    2.500         0.000           3.000
X -s4-s6-X    6   40.000       180.000           2.000       estimated !!!
X -sx-sy-X    6   26.000       180.000           2.000
X -s6-s6-X    9   60.000       180.000           2.000       estimated !!!
X -sy-sy-X    9    1.400       180.000           2.000
X -cf-pe-X    2   13.300       180.000           2.00       NEW
X -nd-os-X    1    4.800       180.000           2.00       NEW
X -nd-ss-X    1    4.800       180.000           2.00       NEW
X -nf-pe-X    1    5.400       180.000           2.00       NEW
c2-ne-p5-o    1    0.000         0.0            -3.         TorType=1
c2-ne-p5-o    1    2.300         0.0             1.         TorType=1
c2-nf-p5-o    1    0.000         0.0            -3.         TorType=1
c2-nf-p5-o    1    2.300         0.0             1.         TorType=1
ce-ne-p5-o    1    0.000         0.0            -3.         TorType=1
ce-ne-p5-o    1    2.300         0.0             1.         TorType=1
ce-nf-p5-o    1    0.000         0.0            -3.         TorType=1
ce-nf-p5-o    1    2.300         0.0             1.         TorType=1
cf-ne-p5-o    1    0.000         0.0            -3.         TorType=1
cf-ne-p5-o    1    2.300         0.0             1.         TorType=1
cf-nf-p5-o    1    0.000         0.0            -3.         TorType=1
cf-nf-p5-o    1    2.300         0.0             1.         TorType=1
hn-n -c -o    1    2.500       180.0            -2.         JCC,7,(1986),230 TorType=1
hn-n -c -o    1    2.000         0.0             1.         J.C.cistrans-NMA DE TorType=1
c3-n3-p5-o    1    3.000       180.0            -2.         TorType=1
c3-n3-p5-o    1    2.300         0.0             3.         TorType=1
oh-p5-os-c3   1    0.250         0.0            -3.         JCC,7,(1986),230 TorType=1
oh-p5-os-c3   1    1.200         0.0             2.         gg&gt ene.631g*/mp2 TorType=1
h1-c3-c -o    1    0.800         0.0            -1.         Junmei et al, 1999 TorType=1
h1-c3-c -o    1    0.080       180.0             3.         Junmei et al, 1999 TorType=1
ho-oh-c -o    1    2.300       180.0            -2.         Junmei et al, 1999 TorType=1
ho-oh-c -o    1    1.900         0.0             1.         Junmei et al, 1999 TorType=1
c2-c2-c -o    1    2.175       180.0            -2.         Junmei et al, 1999 TorType=1
c2-c2-c -o    1    0.300         0.0             3.         Junmei et al, 1999 TorType=1
c3-c3-os-c    1    0.383         0.0            -3.         Junmei et al, 1999 TorType=1
c3-c3-os-c    1    0.800       180.0             1.         Junmei et al, 1999 TorType=1
c3-os-c3-na   1    0.383         0.0            -3.         parm98.dat, TC,PC,PAK TorType=1
c3-os-c3-na   1    0.650         0.0             2.         Piotr et al. TorType=1
o -c -os-c3   1    2.700       180.0            -2.         Junmei et al, 1999 TorType=1
o -c -os-c3   1    1.400       180.0             1.         Junmei et al, 1999 TorType=1
os-c3-na-c2   1    0.000       000.0            -2.         parm98, TC,PC,PAK TorType=1
os-c3-na-c2   1    2.500         0.0             1.         parm98, TC,PC,PAK TorType=1
h1-c3-c3-os   1    0.000         0.0            -3.         Junmei et al, 1999 TorType=1
h1-c3-c3-os   1    0.250         0.0             1.         Junmei et al, 1999 TorType=1
h1-c3-c3-oh   1    0.000         0.0            -3.         Junmei et al, 1999 TorType=1
h1-c3-c3-oh   1    0.250         0.0             1.         Junmei et al, 1999 TorType=1
h1-c3-c3-f    1    0.000         0.0            -3.         Junmei et al, 1999 TorType=1
h1-c3-c3-f    1    0.190         0.0             1.         Junmei et al, 1999 TorType=1
h1-c3-c3-cl   1    0.000         0.0            -3.         Junmei et al, 1999 TorType=1
h1-c3-c3-cl   1    0.250         0.0             1.         Junmei et al, 1999 TorType=1
h1-c3-c3-br   1    0.000         0.0            -3.         Junmei et al, 1999 TorType=1
h1-c3-c3-br   1    0.550         0.0             1.         Junmei et al, 1999 TorType=1
hc-c3-c3-os   1    0.000         0.0            -3.         Junmei et al, 1999 TorType=1
hc-c3-c3-os   1    0.250         0.0             1.         Junmei et al, 1999 TorType=1
c3-n4-c3-ca   1    0.156         0.0            -3.         Junmei, 2015 TorType=1
c3-n4-c3-ca   1    0.700         0.0             2.         Junmei, 2015 TorType=1
oh-c3-c3-n4   1    0.144         0.0            -3.         Junmei, 2015 TorType=1
oh-c3-c3-n4   1    1.300         0.0             2.         Junmei, 2015 TorType=1
c3-c3-n4-c3   1    0.156         0.0             3.         Junmei, 2015 TorType=1
c3-c -os-p5   1    2.700       180.0            -2.         Junmei, 2015 TorType=1
c3-c -os-p5   1    2.000       180.0             1.         Junmei, 2015 TorType=1
c -os-p5-o    1    0.800         0.0            -2.         Junmei, 2015 TorType=1
c -os-p5-o    1    1.100         0.0            -1.         Junmei, 2015 TorType=1
c -os-p5-o    1    0.500       180.0             3.         Junmei, 2015 TorType=1
c3-c3-os-p5   1    0.383         0.0            -3.         Junmei, 2015 TorType=1
c3-c3-os-p5   1    3.950       180.0             1.         Junmei, 2015 TorType=1
c3-os-p5-o    1    0.800         0.0            -2.         Junmei, 2015 TorType=1
c3-os-p5-o    1    0.550         0.0             3.         Junmei, 2015 TorType=1
ca-ca-os-p5   1    1.750       180.0             2.         Junmei, 2015 TorType=1
ca-os-p5-o    1    0.800       180.0            -2.         Junmei, 2015 TorType=1
ca-os-p5-o    1    0.100         0.0             3.         Junmei, 2015 TorType=1
br-c3-c3-br   1    0.500         0.000          -3          m9 GA AUE=0.9626 RMSE=1.1958 TorType=2
br-c3-c3-br   1    1.820         0.000           1          m9 GA AUE=0.9626 RMSE=1.1958 TorType=2
c -n -c2-c2   1    1.570       180.000          -2          c25 GA AUE=0.3367 RMSE=0.3900 TorType=2
c -n -c2-c2   1    1.530       180.000           1          c25 GA AUE=0.3367 RMSE=0.3900 TorType=2
c3-ss-c2-c2   1    1.280       180.000          -2          c39 GA AUE=0.3908 RMSE=0.4760 TorType=2
c3-ss-c2-c2   1    1.200       180.000           3          c39 GA AUE=0.3908 RMSE=0.4760 TorType=2
c3-c2-c2-c3   1    5.290       180.000          -2          c22 GA AUE=2.0091 RMSE=3.0745 TorType=2
c3-c2-c2-c3   1    0.400       180.000           1          c22 GA AUE=2.0091 RMSE=3.0745 TorType=2
c3-c3-c3-c3   1    0.130         0.000          -3          c42  GA AUE=0.2975 RMSE=0.3306 TorType=2
c3-c3-c3-c3   1    0.290       180.000          -2          c42 GA AUE=0.2720 RMSE=0.3206 TorType=2
c3-c3-c3-c3   1    0.110         0.000           1          c42 GA AUE=0.2720 RMSE=0.3206 TorType=2
n -c -c3-c3   1    0.000       180.000          -4          p20 GA AUE=0.5445 RMSE=0.7015 TorType=2
n -c -c3-c3   1    0.710       180.000           2          p20 GA AUE=0.5445 RMSE=0.7015 TorType=2
c3-os-c3-c3   1    0.240         0.000          -3          p29 GA AUE=0.4256 RMSE=0.5201 TorType=2
c3-os-c3-c3   1    0.160         0.000           2          p29 GA AUE=0.4256 RMSE=0.5201 TorType=2
ca-nh-n3-c3   1    1.120         0.000           2          c115 SS AUE=2.2848 RMSE=2.9445 TorType=2
hs-sh-ss-c3   1    1.600         0.000          -3          c223 GA AUE=0.7163 RMSE=0.8348 TorType=2
hs-sh-ss-c3   1    2.810         0.000           2          c223 GA AUE=0.7163 RMSE=0.8348 TorType=2
ho-oh-nh-ca   1    1.430         0.000          -1          c156 GA AUE=0.4441 RMSE=0.5406 TorType=2
ho-oh-nh-ca   1    0.500         0.000           2          c156 GA AUE=0.4441 RMSE=0.5406 TorType=2
cl-c3-c3-cl   1    0.500         0.000          -3          m8 GA AUE=0.9322 RMSE=1.0556 TorType=2
cl-c3-c3-cl   1    0.930         0.000           1          m8 GA AUE=0.9322 RMSE=1.0556 TorType=2
c -n -c3-c3   1    0.100       180.000          -4          p19 GA AUE=0.2882 RMSE=0.4031 TorType=2
c -n -c3-c3   1    0.170         0.000          -3          p19 GA AUE=0.2882 RMSE=0.4031 TorType=2
c -n -c3-c3   1    1.020       180.000           1          p19 GA AUE=0.2882 RMSE=0.4031 TorType=2
c2-p2-n -c    1    1.480       180.000          -2          c88 GA AUE=0.5049 RMSE=0.6214 TorType=2
c2-p2-n -c    1    2.150       180.000           1          c88 GA AUE=0.5049 RMSE=0.6214 TorType=2
f -c3-c3-f    1    1.000         0.000          -3          m7 GA AUE=1.3130 RMSE=1.6963 TorType=2
f -c3-c3-f    1    0.640       180.000           1          m7 GA AUE=1.3130 RMSE=1.6963 TorType=2
hc-c3-c2-c2   1    0.360       180.000          -3          c23 GA AUE=0.0738 RMSE=0.0893 TorType=2
hc-c3-c2-c2   1    1.470         0.000           1          c23 GA AUE=0.0738 RMSE=0.0893 TorType=2
hc-c3-c3-br   1    0.210         0.000          -3          m5 GA AUE=0.2036 RMSE=0.2389 TorType=2
hc-c3-c3-br   1    0.080         0.000           1          m5 GA AUE=0.2036 RMSE=0.2389 TorType=2
hc-c3-c3-c3   1    0.080         0.000           3          m2 SS AUE=0.2468 RMSE=0.2989 TorType=2
hc-c3-c3-cl   1    0.220         0.000          -3          m4 GA AUE=0.1732 RMSE=0.2055 TorType=2
hc-c3-c3-cl   1    0.250       180.000           1          m4 GA AUE=0.1732 RMSE=0.2055 TorType=2
hc-c3-c3-f    1    0.220         0.000          -3          m3 GA AUE=0.0868 RMSE=0.1021 TorType=2
hc-c3-c3-f    1    1.970       180.000           1          m3 GA AUE=0.0868 RMSE=0.1021 TorType=2
hc-c3-c3-hc   1    0.120         0.000           3          m1 SS AUE=0.2420 RMSE=0.2944 TorType=2
hc-c3-c3-oh   1    0.180         0.000          -3          m11 GA AUE=0.1021 RMSE=0.1307 TorType=2
hc-c3-c3-oh   1    0.510         0.000           1          m11 GA AUE=0.1021 RMSE=0.1307 TorType=2
n -c -c3-n    1    0.100       180.000          -1          p17 GA AUE=0.9129 RMSE=1.0401 TorType=2
n -c -c3-n    1    2.120       180.000           2          p17 GA AUE=0.9129 RMSE=1.0401 TorType=2
oh-c3-c3-os   1    1.010         0.000          -3          suger5ring,suger6ring GA AUE=0.6597 RMSE=0.8978 TorType=2
oh-c3-c3-os   1    0.000         0.000          -2          suger5ring,suger6ring GA AUE=0.6597 RMSE=0.8978 TorType=2
oh-c3-c3-os   1    0.020       180.000           1          suger5ring,suger6ring GA AUE=0.6597 RMSE=0.8978 TorType=2
os-p5-os-c3   1    0.000         0.000          -3          c191 GA AUE=0.2324 RMSE=0.3542 TorType=2
os-p5-os-c3   1    2.610         0.000           2          c191 GA AUE=0.2324 RMSE=0.3542 TorType=2
c3-n -c -c3   1    0.260       180.000          -2          c5 GA AUE=0.9706 RMSE=1.2796 TorType=2
c3-n -c -c3   1    0.500         0.000           1          c5 GA AUE=0.9706 RMSE=1.2796 TorType=2
c3-os-c -c3   1    1.580       180.000          -1          c13 GA AUE=0.2469 RMSE=0.2990 TorType=2
c3-os-c -c3   1    3.180       180.000          -2          c13 GA AUE=0.2469 RMSE=0.2990 TorType=2
c3-os-c -c3   1    0.730         0.000           3          c13 GA AUE=0.2469 RMSE=0.2990 TorType=2
hs-sh-c -c3   1    1.080       180.000          -2          c18 GA AUE=0.2126 RMSE=0.3029 TorType=2
hs-sh-c -c3   1    1.920       180.000           1          c18 GA AUE=0.2126 RMSE=0.3029 TorType=2
os-c3-os-c3   1    0.000       180.000          -3          cococ,lactose2,t12 GA AUE=0.8913 RMSE=1.4261 TorType=2
os-c3-os-c3   1    1.240         0.000          -2
os-c3-os-c3   1    0.970       180.000           1
c3-ss-ss-c3   1    3.150         0.000          -2          c226,p2 GA AUE=0.4785 RMSE=0.5249 TorType=2
c3-ss-ss-c3   1    0.890         0.000           3          c226,p2 GA AUE=0.4785 RMSE=0.5249
o -c -c3-hc   1    0.830         0.000          -1          CH3COO,CH3COOH GA AUE=0.0144 RMSE=0.0193 TorType=2
o -c -c3-hc   1    0.040       180.000           3
ho-oh-c3-c3   1    0.000         0.000           3          m19 SS AUE=0.1539 RMSE=0.2110 TorType=2
oh-c3-c3-oh   1    0.900         0.000          -3          p5,ch2oh2 GA AUE=0.9894 RMSE=1.1930 TorType=2
oh-c3-c3-oh   1    1.130         0.000           2          p5,ch2oh2 GA AUE=0.9894 RMSE=1.1930 TorType=2
os-c3-c3-os   1    0.000         0.000          -3          p28,suger5ring,suger6ring,coccoc GA AUE=1.1750 RMSE=1.6708 TorType=2
os-c3-c3-os   1    0.000       180.000          -2
os-c3-c3-os   1    0.170       180.000           1
c1-c1-c3-c1   1    0.000         0.000           2          t5 SS AUE=0.0048 RMSE=0.0058  TorType=3
c2-c2-c3-c2   1    0.112         0.000           2          t4 SS AUE=0.5917 RMSE=0.7276 TorType=3
c2-ce-ca-ca   1    0.505       180.000           2          add6f SS AUE=0.2273 RMSE=0.3302 TorType=3
c2-ce-ce-c3   1    0.500       180.000           2          set1_2 SS AUE=0.6541 RMSE=0.8643 TorType=3
c2-cf-cd-cc   1    0.500       180.000           2          add6d SS AUE=0.3708 RMSE=0.4956 TorType=3
c2-n2-c3-n2   1    1.570       180.000          -2          t14 GA AUE=1.3428 RMSE=1.6221 TorType=3
c2-n2-c3-n2   1    2.730       180.000           1          t14 GA AUE=1.3428 RMSE=1.6221 TorType=3
c2-n2-na-cd   1    1.575       180.000           2          c99 SS AUE=0.2455 RMSE=0.3271 TorType=3
c2-n2-n -c    1    2.790       180.000           1          c80 SS AUE=2.1704 RMSE=2.7351 TorType=3
c2-n2-nh-c2   1    1.200         0.000           2          set3_6 SS AUE=1.7161 RMSE=2.4147 TorType=3
c2-ne-ca-ca   1    0.495         0.000           3          c63 SS AUE=1.1301 RMSE=1.4142 TorType=3
c2-ne-ce-c2   1    0.170       180.000           2          c26 SS AUE=0.7462 RMSE=0.9083 TorType=3
c2-ne-ce-c3   1    0.820         0.000           2          set1_6 SS AUE=0.2966 RMSE=0.4200 TorType=3
c2-nh-c2-c2   1    0.980       180.000           2          set3_2 SS AUE=0.5762 RMSE=0.7682 TorType=3
c2-nh-c2-c3   1    3.140       180.000           2          set3_26 SS AUE=0.5612 RMSE=0.7360 TorType=3
c2-nh-c3-h1   1    0.400         0.000           3          set3_3 SS AUE=0.2455 RMSE=0.3092 TorType=3
c2-nh-ca-ca   1    0.550       180.000           2          set3_4 SS AUE=0.8992 RMSE=1.3720 TorType=3
c2-nh-nh-c2   1    2.930         0.000           3          set3_24 SS AUE=2.3906 RMSE=3.0117 TorType=3
c2-p2-c3-p2   1    2.070       180.000           1          t18 SS AUE=0.4761 RMSE=0.6635 TorType=3
c2-p2-n4-hn   1    0.000       180.000           3          c133 SS AUE=0.2623 RMSE=0.3265 TorType=3
c2-p2-na-cc   1    1.830       180.000           2          c146 SS AUE=0.3236 RMSE=0.3673 TorType=3
c2-p2-nh-c2   1    1.330       180.000           2          set3_14 SS AUE=0.4660 RMSE=0.7730 TorType=3
c2-p2-nh-c3   1    2.400       180.000           2          c119 SS AUE=1.0662 RMSE=1.4725 TorType=3
c2-p2-nh-ca   1    1.880       180.000           1          c158 SS AUE=1.5854 RMSE=1.8810 TorType=3
c2-pe-ca-ca   1    1.065       180.000           2          c71 SS AUE=0.2838 RMSE=0.3291 TorType=3
c2-pe-ce-c2   1    0.825       180.000           2          c34 SS AUE=0.3082 RMSE=0.3467 TorType=3
c2-pe-ce-c3   1    3.640       180.000           1          set1_14 SS AUE=0.2869 RMSE=0.3329 TorType=3
c2-pe-ne-c2   1    0.290         0.000           1          c104 SS AUE=0.4118 RMSE=0.5379 TorType=3
c2-pe-pe-c2   1    0.680       180.000           2          c196 SS AUE=0.2486 RMSE=0.3241 TorType=3
c3-c2-nh-ca   1    1.160       180.000          -2          set1_10 GA AUE=0.3625 RMSE=0.5970 TorType=3
c3-c2-nh-ca   1    1.880         0.000           1          set1_10 GA AUE=0.3625 RMSE=0.5970 TorType=3
c3-c3-c3-hc   1    0.080         0.000           3          t2 SS AUE=0.2507 RMSE=0.3027 TorType=3
c3-c3-cc-ca   1    0.082         0.000           3          p3 SS AUE=0.4586 RMSE=0.5633 TorType=3
c3-c3-n -c    1    0.650       180.000          -4          sialic2 GA AUE=1.1541 RMSE=1.2847 TorType=3
c3-c3-n -c    1    0.030       180.000          -3          sialic2 GA AUE=1.1541 RMSE=1.2847 TorType=3
c3-c3-n -c    1    2.260         0.000           1          sialic2 GA AUE=1.1541 RMSE=1.2847 TorType=3
c3-c -c3-c3   1    0.332       180.000           2          p10 SS AUE=0.3226 RMSE=0.4401 TorType=3
c3-c -ce-c3   1    4.110         0.000           2          set3_25 SS AUE=0.6933 RMSE=1.1187 TorType=3
c3-ce-ce-c3   1    0.500       180.000           2          set3_22 SS AUE=1.0809 RMSE=1.3455 TorType=3
c3-n2-c2-c3   1   10.370       180.000           2          c7 SS AUE=1.1629 RMSE=1.3902 TorType=3
c3-n3-n3-c3   1    2.310         0.000           2          c112 SS AUE=0.8815 RMSE=1.0390 TorType=3
c3-n3-nh-c2   1    1.355         0.000           2          set3_7 SS AUE=1.4104 RMSE=1.6750 TorType=3
c3-n4-ca-ca   1    1.495         0.000           2          c65 SS AUE=0.2872 RMSE=0.3575 TorType=3
c3-n4-n4-c3   1    0.244         0.000           3          c127 SS AUE=0.6207 RMSE=0.7993 TorType=3
c3-nh-c2-c2   1    0.950       180.000          -2          c27 GA AUE=0.7690 RMSE=1.0440 TorType=3
c3-nh-c2-c2   1    1.120       180.000           3          c27 GA AUE=0.7690 RMSE=1.0440 TorType=3
c3-nh-c2-c3   1    2.495       180.000           2          set1_7 SS AUE=0.8853 RMSE=1.2321 TorType=3
c3-os-c2-c2   1    2.520       180.000          -2          c33 GA AUE=0.9155 RMSE=1.0796 TorType=3
c3-os-c2-c2   1    2.000       180.000           1          c33 GA AUE=0.9155 RMSE=1.0796 TorType=3
c3-os-c2-c3   1    4.790       180.000           2          set1_13 SS AUE=0.9973 RMSE=1.5097 TorType=3
c3-os-c3-h1   1    0.337         0.000           3          c52 SS AUE=0.2706 RMSE=0.3300 TorType=3
c3-os-ca-ca   1    1.610       180.000           2          c70 SS AUE=0.3151 RMSE=0.3580 TorType=3
c3-os-n2-c2   1    2.200       180.000          -2          c103 SS AUE=1.2430 RMSE=1.4817 TorType=3
c3-os-n2-c2   1    0.900       180.000           3          c103 SS AUE=1.2430 RMSE=1.4817 TorType=3
c3-os-n3-c3   1    0.840         0.000           2          c118 SS AUE=0.7374 RMSE=0.9683 TorType=3
c3-os-n4-c3   1    0.620       180.000           3          c132 SS AUE=0.8090 RMSE=0.9444 TorType=3
c3-os-na-cc   1    0.190         0.000           2          c145 SS AUE=0.2720 RMSE=0.3305 TorType=3
c3-os-n -c    1    0.420         0.000           2          c87 SS AUE=0.3019 RMSE=0.3567 TorType=3
c3-os-nh-c2   1    1.150         0.000           1          set3_13 SS AUE=0.9655 RMSE=1.1845 TorType=3
c3-os-nh-ca   1    0.500         0.000           1          c157 SS AUE=0.8647 RMSE=1.0585 TorType=3
c3-os-no-o    1    2.515       180.000           2          c168 SS AUE=0.3706 RMSE=0.4248 TorType=3
c3-os-oh-ho   1    1.010         0.000           2          c178 SS AUE=0.2810 RMSE=0.3796 TorType=3
c3-os-os-c3   1    0.380         0.000           1          c187 SS AUE=0.4838 RMSE=0.6593 TorType=3
c3-os-p2-c2   1    2.940       180.000          -2          c188 GA AUE=0.3661 RMSE=0.4565 TorType=3
c3-os-p2-c2   1    1.850       180.000           1          c188 GA AUE=0.3661 RMSE=0.4565 TorType=3
c3-p3-c2-c2   1    0.297         0.000           2          c35 SS AUE=1.0902 RMSE=1.4763 TorType=3
c3-p3-c2-c3   1    0.950       180.000           2          set1_15 SS AUE=0.4182 RMSE=0.4905 TorType=3
c3-p3-ca-ca   1    0.177       180.000           2          c72 SS AUE=0.2797 RMSE=0.3319 TorType=3
c3-p3-n2-c2   1    5.000       180.000           2          c105 SS AUE=0.8649 RMSE=1.0889 TorType=3
c3-p3-n3-c3   1    2.850         0.000           2          c120 SS AUE=0.8776 RMSE=1.2067 TorType=3
c3-p3-n4-c3   1    0.067         0.000           3          c134 SS AUE=0.1760 RMSE=0.2433 TorType=3
c3-p3-na-cc   1    1.025         0.000           2          c147 SS AUE=0.2741 RMSE=0.3331 TorType=3
c3-p3-n -c    1    1.830         0.000           2          c89 SS AUE=0.9690 RMSE=1.3708 TorType=3
c3-p3-nh-c2   1    1.850         0.000           2          set3_15 SS AUE=0.8611 RMSE=0.9832 TorType=3
c3-p3-no-o    1    1.400       180.000           2          c170 SS AUE=0.5082 RMSE=0.5728 TorType=3
c3-p3-oh-ho   1    0.240       180.000           3          c180 SS AUE=0.9983 RMSE=1.2838 TorType=3
c3-p3-p2-c2   1    0.200         0.000           1          c197 SS AUE=0.5014 RMSE=0.7016 TorType=3
c3-p3-p3-c3   1    0.375         0.000           3          c204 SS AUE=0.8032 RMSE=0.9405 TorType=3
c3-p4-n3-c3   1    1.778       180.000           2          c121 SS AUE=1.1246 RMSE=1.4091 TorType=3
c3-p4-n4-hn   1    0.005         0.000           3          c135 SS AUE=0.2627 RMSE=0.3254 TorType=3
c3-p4-na-cc   1    1.000         0.000          -3          c148 GA AUE=0.9954 RMSE=1.1119 TorType=3
c3-p4-na-cc   1    0.640       180.000           2          c148 GA AUE=0.9954 RMSE=1.1119 TorType=3
c3-p4-nh-c2   1    0.900         0.000           1          set3_16 SS AUE=1.0315 RMSE=1.1976 TorType=3
c3-p4-nh-ca   1    0.000       180.000          -3          c160 GA AUE=1.0676 RMSE=1.4622 TorType=3
c3-p4-nh-ca   1    0.840       180.000           2          c160 GA AUE=1.0676 RMSE=1.4622 TorType=3
c3-p4-os-c3   1    0.600       180.000           2          c190 SS AUE=0.5663 RMSE=0.6640 TorType=3
c3-p4-p3-c3   1    1.400         0.000           1          c205 SS AUE=0.7593 RMSE=0.9141 TorType=3
c3-px-ca-ca   1    0.432       180.000           2          c73 SS AUE=0.4755 RMSE=0.6108 TorType=3
c3-px-c -c3   1    0.000         0.000          -2          c16 GA AUE=1.0361 RMSE=1.3175 TorType=3
c3-px-c -c3   1    0.580       180.000           1          c16 GA AUE=1.0361 RMSE=1.3175 TorType=3
c3-px-ce-c2   1    1.130         0.000           2          c36 SS AUE=1.2444 RMSE=1.6024 TorType=3
c3-px-ce-c3   1    0.810       180.000           2          set1_16 SS AUE=0.9969 RMSE=1.2788 TorType=3
c3-px-ne-c2   1    0.610         0.000          -3          c106 GA AUE=1.6606 RMSE=2.1207 TorType=3
c3-px-ne-c2   1    1.440         0.000           1          c106 GA AUE=1.6606 RMSE=2.1207 TorType=3
c3-px-pe-c2   1    1.565         0.000           2          c198 SS AUE=1.0967 RMSE=1.2917 TorType=3
c3-s4-c3-h1   1    0.117         0.000           3          c59 SS AUE=0.2210 RMSE=0.2792 TorType=3
c3-s4-n3-c3   1    3.100         0.000           2          c125 SS AUE=1.3654 RMSE=1.8896 TorType=3
c3-s4-n4-c3   1    0.200         0.000           3          c139 SS AUE=0.7713 RMSE=0.9400 TorType=3
c3-s4-na-cc   1    0.550         0.000           2          c152 SS AUE=0.5159 RMSE=0.7408 TorType=3
c3-s4-nh-c2   1    0.235       180.000          -2          set3_20 GA AUE=1.5742 RMSE=1.9736 TorType=3
c3-s4-nh-c2   1    0.500         0.000          -3          set3_20 GA AUE=1.5742 RMSE=1.9736 TorType=3
c3-s4-nh-c2   1    1.302         0.000           1          set3_20 GA AUE=1.5742 RMSE=1.9736 TorType=3
c3-s4-no-o    1    1.130       180.000           2          c175 SS AUE=0.7753 RMSE=0.8760 TorType=3
c3-s4-oh-ho   1    0.000       180.000           1          c185 SS AUE=1.7272 RMSE=2.1061 TorType=3
c3-s4-os-c3   1    1.310       180.000           1          c194 SS AUE=0.9618 RMSE=1.1506 TorType=3
c3-s4-p3-c3   1    2.220         0.000           2          c209 SS AUE=1.9189 RMSE=2.5861 TorType=3
c3-s4-sh-hs   1    0.000         0.000          -3          c224 GA AUE=1.1511 RMSE=1.3863 TorType=3
c3-s4-sh-hs   1    0.560       180.000           2          c224 GA AUE=1.1511 RMSE=1.3863 TorType=3
c3-s4-ss-c3   1    0.050         0.000           3          c227 SS AUE=0.7707 RMSE=0.9378 TorType=3
c3-s6-c3-h1   1    0.089         0.000           3          c60 SS AUE=0.0648 RMSE=0.0808 TorType=3
c3-s6-n3-c3   1    3.610         0.000           2          c126 SS AUE=1.8933 RMSE=2.6424 TorType=3
c3-s6-n4-c3   1    1.470         0.000           1          c140 SS AUE=0.2994 RMSE=0.3260 TorType=3
c3-s6-na-cc   1    3.938       180.000           2          c153 SS AUE=0.8118 RMSE=1.0393 TorType=3
c3-s6-n -c    1    0.768       180.000           2          c95 SS AUE=0.4645 RMSE=0.6488 TorType=3
c3-s6-nh-c2   1    0.667         0.000           2          set3_21 SS AUE=1.6191 RMSE=2.2150 TorType=3
c3-s6-no-o    1    0.348         0.000           2          c176 SS AUE=0.2701 RMSE=0.3306 TorType=3
c3-s6-oh-ho   1   11.690       180.000           1          c186 SS AUE=0.6401 RMSE=0.8081 TorType=3
c3-s6-os-c3   1    0.533       180.000           2          c195 SS AUE=0.9691 RMSE=1.1571 TorType=3
c3-s6-p3-c3   1    0.183         0.000           3          c210 SS AUE=0.5556 RMSE=0.6476 TorType=3
c3-s6-sh-hs   1    4.317       180.000           2          c225 SS AUE=1.0170 RMSE=1.0970 TorType=3
c3-s6-ss-c3   1    2.400       180.000           2          c228 SS AUE=0.8201 RMSE=1.0146 TorType=3
c3-ss-c2-c3   1    2.025       180.000           2          set1_19 SS AUE=0.5269 RMSE=0.6098 TorType=3
c3-ss-c3-c3   1    0.167         0.000           3          p9 SS AUE=0.4614 RMSE=0.5750 TorType=3
c3-ss-c3-h1   1    0.220         0.000           3          c58 SS AUE=0.2551 RMSE=0.3303 TorType=3
c3-ss-ca-ca   1    0.750       180.000           2          c76 SS AUE=0.2509 RMSE=0.3297 TorType=3
c3-ss-n2-c2   1    1.350       180.000          -2          c109 GA AUE=0.6324 RMSE=0.7825 TorType=3
c3-ss-n2-c2   1    1.380       180.000           1          c109 GA AUE=0.6324 RMSE=0.7825 TorType=3
c3-ss-n3-c3   1    2.680         0.000           2          c124 SS AUE=1.0072 RMSE=1.2488 TorType=3
c3-ss-n4-c3   1    0.390         0.000           3          c138 SS AUE=0.3868 RMSE=0.4909 TorType=3
c3-ss-n -c    1    0.500         0.000           2          c93 SS AUE=0.5560 RMSE=0.7560 TorType=3
c3-ss-nh-c2   1    1.100         0.000           2          set3_19 SS AUE=0.9372 RMSE=1.1240 TorType=3
c3-ss-no-o    1    2.295       180.000           2          c174 SS AUE=0.3406 RMSE=0.3839 TorType=3
c3-ss-oh-ho   1    2.130         0.000           2          c184 SS AUE=0.2806 RMSE=0.3277 TorType=3
c3-ss-os-c3   1    1.740         0.000           2          c193 SS AUE=0.5504 RMSE=0.6616 TorType=3
c3-ss-p2-c2   1    2.970       180.000           2          c201 SS AUE=0.8463 RMSE=1.2678 TorType=3
c3-ss-p3-c3   1    3.750         0.000           2          c208 SS AUE=0.5096 RMSE=0.5972 TorType=3
c3-ss-p4-c3   1    0.570       180.000           2          c214 SS AUE=0.7214 RMSE=0.9325 TorType=3
c3-sx-ca-ca   1    0.640         0.000           2          c77 SS AUE=0.6566 RMSE=0.8245 TorType=3
c3-sx-ce-c2   1    1.460         0.000          -2          c40 GA AUE=1.8189 RMSE=2.2140 TorType=3
c3-sx-ce-c2   1    1.500       180.000           3          c40 GA AUE=1.8189 RMSE=2.2140 TorType=3
c3-sx-ce-c3   1    1.500         0.000          -3          set1_20 GA AUE=2.1436 RMSE=3.2053 TorType=3
c3-sx-ce-c3   1    4.160         0.000          -2          set1_20 GA AUE=2.1436 RMSE=3.2053 TorType=3
c3-sx-ce-c3   1    3.100       180.000           1          set1_20 GA AUE=2.1436 RMSE=3.2053 TorType=3
c3-sx-ne-c2   1    1.000       180.000          -3          c110 GA AUE=1.5150 RMSE=1.7663 TorType=3
c3-sx-ne-c2   1    1.900       180.000           1          c110 GA AUE=1.5150 RMSE=1.7663 TorType=3
c3-sx-pe-c2   1    4.190         0.000           2          c202 SS AUE=2.6033 RMSE=3.2866 TorType=3
c3-sx-px-c3   1    2.670         0.000           1          c215 SS AUE=0.8306 RMSE=1.0179 TorType=3
c3-sx-sx-c3   1    2.920         0.000           1          c229 SS AUE=2.7179 RMSE=3.6787 TorType=3
c3-sx-sy-c3   1    4.940       180.000           2          c230 SS AUE=1.7022 RMSE=1.9951 TorType=3
c3-sy-ca-ca   1    1.220       180.000           2          c78 SS AUE=0.2941 RMSE=0.3313 TorType=3
c3-sy-ce-c2   1    0.935       180.000           2          c41 SS AUE=0.9708 RMSE=1.2822 TorType=3
c3-sy-ce-c3   1    0.640         0.000          -3          set1_21 GA AUE=0.6383 RMSE=0.7388 TorType=3
c3-sy-ce-c3   1    0.333       180.000          -2          set1_21 GA AUE=0.6383 RMSE=0.7388 TorType=3
c3-sy-ce-c3   1    1.040       180.000           1          set1_21 GA AUE=0.6383 RMSE=0.7388 TorType=3
c3-sy-ne-c2   1    0.340       180.000          -3          c111 GA AUE=0.2248 RMSE=0.3231 TorType=3
c3-sy-ne-c2   1    7.467       180.000           1          c111 GA AUE=0.2248 RMSE=0.3231 TorType=3
c3-sy-pe-c2   1    0.237       180.000           3          c203 SS AUE=0.3743 RMSE=0.4294 TorType=3
c3-sy-px-c3   1    0.062         0.000           3          c216 SS AUE=0.6353 RMSE=0.7537 TorType=3
c3-sy-sy-c3   1    0.378         0.000           2          c231 SS AUE=1.1799 RMSE=1.3634 TorType=3
ca-c3-c3-c    1    0.100         0.000           3          p22 SS AUE=0.8008 RMSE=1.0051 TorType=3
ca-c3-c3-n    1    0.210         0.000           3          p16 SS AUE=0.6330 RMSE=0.8053 TorType=3
ca-ca-c3-ca   1    0.000       180.000           2          t1 SS AUE=0.1988 RMSE=0.2606 TorType=3
ca-ca-ce-c2   1    0.618       180.000           2          c24 SS AUE=0.2364 RMSE=0.3330 TorType=3
ca-ca-ce-c3   1    0.540       180.000           2          set1_4 SS AUE=0.2602 RMSE=0.3333 TorType=3
ca-ca-os-c    1    0.650       180.000           2          t35b SS AUE=0.2491 RMSE=0.3333 TorType=3
ca-cf-ce-ca   1    8.510       180.000           2          add6b SS AUE=4.0000 RMSE=5.4296 TorType=3
ca-c -os-c3   1    2.685       180.000           2          t36b SS AUE=1.2217 RMSE=1.4489 TorType=3
ca-cp-cp-ca   1    0.795       180.000           2          c61 SS AUE=0.2914 RMSE=0.3303 TorType=3
ca-nh-c2-c2   1    1.920       180.000           1          c30 SS AUE=0.8599 RMSE=1.1406 TorType=3
ca-nh-n2-c2   1    1.370       180.000          -3          c100 GA AUE=2.0208 RMSE=2.4869 TorType=3
ca-nh-n2-c2   1    2.000         0.000          -2          c100 GA AUE=2.0208 RMSE=2.4869 TorType=3
ca-nh-n2-c2   1    0.000       180.000           1          c100 GA AUE=2.0208 RMSE=2.4869 TorType=3
ca-nh-n4-c3   1    0.100         0.000           3          c129 SS AUE=1.1901 RMSE=1.4071 TorType=3
ca-nh-na-cd   1    0.700         0.000           2          c142 SS AUE=0.5118 RMSE=0.8838 TorType=3
ca-nh-n -c    1    0.605         0.000           2          c84 SS AUE=1.2184 RMSE=1.3197 TorType=3
ca-nh-nh-c2   1    1.490         0.000           3          set3_10 SS AUE=2.7548 RMSE=3.5233 TorType=3
ca-nh-nh-ca   1    4.590         0.000           1          c154 SS AUE=3.6427 RMSE=5.6136 TorType=3
ca-nh-no-o    1    0.620       180.000           2          c155 SS AUE=1.3263 RMSE=1.9039 TorType=3
ca-nh-p3-c3   1    1.940       180.000          -2          c159 GA AUE=0.8724 RMSE=1.1678 TorType=3
ca-nh-p3-c3   1    0.540         0.000           3          c159 GA AUE=0.8724 RMSE=1.1678 TorType=3
ca-nh-p5-os   1    0.467         0.000           2          c161 SS AUE=0.8323 RMSE=0.9798 TorType=3
ca-nh-s4-c3   1    1.245         0.000          -2          c164 GA AUE=1.5450 RMSE=1.8592 TorType=3
ca-nh-s4-c3   1    0.225         0.000           3          c164 GA AUE=1.5450 RMSE=1.8592 TorType=3
ca-nh-s6-c3   1    1.930         0.000           3          c165 SS AUE=0.7711 RMSE=0.9257 TorType=3
ca-nh-ss-c3   1    1.290       180.000          -2          c163 GA AUE=0.9564 RMSE=1.5597 TorType=3
ca-nh-ss-c3   1    1.190       180.000           1          c163 GA AUE=0.9564 RMSE=1.5597 TorType=3
ca-nh-sy-ca   1    0.100       180.000          -2          add6a SS AUE=0.6854 RMSE=0.9512 TorType=3
ca-nh-sy-ca   1    0.990         0.000           3          add6a SS AUE=0.6854 RMSE=0.9512 TorType=3
ca-os-c -o    1    1.275       180.000           2          t35a SS AUE=1.2481 RMSE=1.5211 TorType=3
c -c3-c3-n    1    0.210         0.000           3          p26 SS AUE=1.0437 RMSE=1.3000 TorType=3
c -c3-n -c    1    0.390       180.000          -2          p18 GA AUE=0.4030 RMSE=0.5768 TorType=3
c -c3-n -c    1    0.640         0.000           1          p18 GA AUE=0.4030 RMSE=0.5768 TorType=3
cc-na-c2-c2   1    0.728       180.000           2          c29 SS AUE=0.2592 RMSE=0.3329 TorType=3
cc-na-c2-c3   1    1.125       180.000           2          set1_9 SS AUE=0.3784 RMSE=0.4839 TorType=3
cc-na-ca-ca   1    0.603       180.000           2          c66 SS AUE=0.2705 RMSE=0.3328 TorType=3
cc-na-na-cd   1    0.400         0.000           2          c141 SS AUE=0.5320 RMSE=0.6402 TorType=3
cc-na-nh-c2   1    0.700         0.000           2          set3_9 SS AUE=0.7727 RMSE=0.9375 TorType=3
cc-n -c -c3   1    0.500       180.000           2          set2_9 SS AUE=0.2224 RMSE=0.3240 TorType=3
cd-cc-c3-c3   1    0.157       180.000           3          p1 SS AUE=0.2727 RMSE=0.3320 TorType=3
cd-na-c3-na   1    0.023         0.000           2          t16 SS AUE=0.2606 RMSE=0.3332 TorType=3
c -n -c2-c3   1    1.510       180.000           1          set1_5 SS AUE=0.6699 RMSE=0.8754 TorType=3
c -n -c3-n    1    2.080         0.000           2          t17 SS AUE=0.8425 RMSE=1.0798 TorType=3
c -n -ca-ca   1    0.950       180.000           2          c62 SS AUE=0.8788 RMSE=0.9694 TorType=3
c -n -n -c    1    3.000       180.000          -2          c79 GA AUE=1.1290 RMSE=1.3734 TorType=3
c -n -n -c    1    2.490         0.000           1          c79 GA AUE=1.1290 RMSE=1.3734 TorType=3
c -n -nh-c2   1    0.600         0.000           2          set3_5 SS AUE=0.7968 RMSE=0.8909 TorType=3
c -os-c -c3   1    1.980       180.000           1          set3_29 SS AUE=0.2568 RMSE=0.3303 TorType=3
cz-nh-c3-c3   1    0.248       180.000           2          p11 SS AUE=0.2819 RMSE=0.3532 TorType=3
h1-c3-n2-c2   1    0.165       180.000           3          c45 SS AUE=0.6984 RMSE=0.9045 TorType=3
h1-c3-n3-c3   1    0.225         0.000           3          c46 SS AUE=0.2936 RMSE=0.3481 TorType=3
h1-c3-na-cc   1    0.000       180.000           2          c48 SS AUE=0.0685 RMSE=0.0813 TorType=3
h1-c3-n -c    1    0.000       180.000           2          c44 SS AUE=0.1670 RMSE=0.1874 TorType=3
h1-c3-nh-ca   1    0.332         0.000           2          c49 SS AUE=1.0901 RMSE=1.3252 TorType=3
h1-c3-no-o    1    0.000       180.000           2          c50 SS AUE=0.0210 RMSE=0.0225 TorType=3
h1-c3-os-p5   1    0.217         0.000           3          c56 SS AUE=0.3987 RMSE=0.4985 TorType=3
hc-c3-c2-c3   1    0.310         0.000           2          set1_3 SS AUE=0.6796 RMSE=0.8466 TorType=3
hc-c3-c3-i    1    0.210         0.000           3          m6 SS AUE=0.3234 RMSE=0.3857 TorType=3
hc-c3-c3-n3   1    0.100         0.000           3          m12 SS AUE=0.1396 RMSE=0.1646 TorType=3
hc-c3-ca-ca   1    0.000       180.000           2          c43 SS AUE=0.0203 RMSE=0.0347 TorType=3
hc-c3-p2-c2   1    0.933       180.000           2          c53 SS AUE=0.3657 RMSE=0.4529 TorType=3
hc-c3-p3-c3   1    0.145         0.000           3          c54 SS AUE=0.2605 RMSE=0.3289 TorType=3
hc-c3-p4-c3   1    0.050         0.000           3          c55 SS AUE=0.1589 RMSE=0.2005 TorType=3
hn-n3-c3-c3   1    0.217         0.000           3          m20 SS AUE=0.7039 RMSE=0.8271 TorType=3
hn-n4-c2-c2   1    0.082       180.000           3          c28 SS AUE=0.6341 RMSE=0.7948 TorType=3
hn-n4-c2-c3   1    0.087         0.000           3          set1_8 SS AUE=0.2828 RMSE=0.3296 TorType=3
hn-n4-c3-hx   1    0.109         0.000           3          c47 SS AUE=0.2716 RMSE=0.3296 TorType=3
hn-n4-n2-c2   1    8.663       180.000           2          c98 SS AUE=0.3876 RMSE=0.4783 TorType=3
hn-n4-n3-c3   1    0.188         0.000           3          c113 SS AUE=0.3464 RMSE=0.4155 TorType=3
hn-n4-na-cd   1    0.150         0.000           3          c128 SS AUE=0.1276 RMSE=0.1509 TorType=3
hn-n4-n -c    1    1.445         0.000           2          c82 SS AUE=0.4066 RMSE=0.5885 TorType=3
hn-n4-nh-c2   1    0.213         0.000           3          set3_8 SS AUE=0.2620 RMSE=0.3316 TorType=3
hn-nh-na-cd   1    0.802         0.000           2          c114 SS AUE=0.2869 RMSE=0.3676 TorType=3
ho-oh-c2-c2   1    1.120       180.000           2          c32 SS AUE=0.2661 RMSE=0.3303 TorType=3
ho-oh-c2-c3   1    1.510       180.000           1          set1_12 SS AUE=1.5331 RMSE=1.7625 TorType=3
ho-oh-c3-h1   1    0.113         0.000           3          c51 SS AUE=0.2631 RMSE=0.3230 TorType=3
ho-oh-ca-ca   1    0.835       180.000           2          c69 SS AUE=0.2718 RMSE=0.3256 TorType=3
ho-oh-n2-c2   1    2.370       180.000           2          c102 SS AUE=0.3163 RMSE=0.3944 TorType=3
ho-oh-n3-c3   1    1.230         0.000           2          c117 SS AUE=0.7804 RMSE=0.9479 TorType=3
ho-oh-n4-c3   1    0.340         0.000           3          c131 SS AUE=0.4375 RMSE=0.5350 TorType=3
ho-oh-na-cc   1    0.440         0.000           2          c144 SS AUE=0.2865 RMSE=0.3255 TorType=3
ho-oh-nh-c2   1    0.850         0.000           2          set3_12 SS AUE=0.6311 RMSE=0.7217 TorType=3
ho-oh-no-o    1    1.360       180.000           2          c167 SS AUE=0.2872 RMSE=0.3226 TorType=3
ho-oh-oh-ho   1    1.210         0.000           2          c177 SS AUE=0.6716 RMSE=0.7402 TorType=3
ho-oh-p2-c2   1    1.410       180.000           2          c179 SS AUE=0.6083 RMSE=0.8611 TorType=3
ho-oh-p4-c3   1    0.830       180.000           1          c181 SS AUE=0.8966 RMSE=1.0772 TorType=3
ho-oh-p5-o    1    0.367         0.000           3          c182 SS AUE=0.8891 RMSE=1.0397 TorType=3
hs-sh-c2-c2   1    0.640       180.000           2          c38 SS AUE=0.5356 RMSE=0.6146 TorType=3
hs-sh-c2-c3   1    1.460       180.000           1          set1_18 SS AUE=1.6292 RMSE=1.8635 TorType=3
hs-sh-c3-h1   1    0.143         0.000           3          c57 SS AUE=0.2676 RMSE=0.3251 TorType=3
hs-sh-ca-ca   1    0.105       180.000           2          c75 SS AUE=0.2588 RMSE=0.3299 TorType=3
hs-sh-n2-c2   1    1.910       180.000           2          c108 SS AUE=0.5066 RMSE=0.9568 TorType=3
hs-sh-n3-c3   1    3.340         0.000           2          c123 SS AUE=1.0521 RMSE=1.3809 TorType=3
hs-sh-n4-c3   1    0.500         0.000           3          c137 SS AUE=1.0514 RMSE=1.3202 TorType=3
hs-sh-na-cc   1    1.255         0.000           2          c150 SS AUE=0.2920 RMSE=0.3622 TorType=3
hs-sh-nh-c2   1    0.795         0.000           2          set3_18 SS AUE=1.0130 RMSE=1.2554 TorType=3
hs-sh-no-o    1    1.300       180.000           2          c173 SS AUE=0.2229 RMSE=0.2551 TorType=3
hs-sh-oh-ho   1    2.010         0.000           2          c183 SS AUE=0.2853 RMSE=0.3308 TorType=3
hs-sh-os-c3   1    1.850         0.000           2          c192 SS AUE=0.4441 RMSE=0.5536 TorType=3
hs-sh-p2-c2   1    0.890       180.000           2          c200 SS AUE=0.2562 RMSE=0.3521 TorType=3
hs-sh-p3-c3   1    3.600         0.000           2          c207 SS AUE=0.5012 RMSE=0.6062 TorType=3
hs-sh-p4-c3   1    0.585       180.000           1          c213 SS AUE=1.2130 RMSE=1.4705 TorType=3
hs-sh-p5-os   1    2.890         0.000          -2          c218 GA AUE=0.8635 RMSE=1.2959 TorType=3
hs-sh-p5-os   1    1.290         0.000           1          c218 GA AUE=0.8635 RMSE=1.2959 TorType=3
hs-sh-sh-hs   1    2.640         0.000           2          c222 SS AUE=0.2962 RMSE=0.3759 TorType=3
n2-c2-c3-c2   1    0.558       180.000           2          t9 SS AUE=0.7685 RMSE=0.9760 TorType=3
n3-c3-c3-c3   1    0.210         0.000           3          p8 SS AUE=0.4096 RMSE=0.5005 TorType=3
n3-c3-c3-ca   1    0.100         0.000           3          m16 SS AUE=0.8325 RMSE=1.0411 TorType=3
n3-c3-n3-hn   1    1.750         0.000           2          t13 SS AUE=0.6939 RMSE=0.8306 TorType=3
n4-c3-c3-c3   1    0.210         0.000           3          p12 SS AUE=0.5399 RMSE=0.6216 TorType=3
n4-c3-n4-hn   1    0.100         0.000           3          t26 SS AUE=0.0245 RMSE=0.0373 TorType=3
n -c3-c3-c3   1    0.100         0.000           3          p23 SS AUE=0.2641 RMSE=0.3317 TorType=3
nh-c3-c3-c3   1    0.210         0.000           3          p13 SS AUE=0.8361 RMSE=0.9491 TorType=3
o -c -c3-c3   1    0.270       180.000           2          p14 SS AUE=0.2361 RMSE=0.3321 TorType=3
oh-c3-c3-c3   1    0.210         0.000           3          p7 SS AUE=0.6517 RMSE=0.7713 TorType=3
oh-c3-c3-c    1    0.210         0.000           3          p25 SS AUE=0.3653 RMSE=0.6406 TorType=3
oh-c3-c3-n    1    0.101         0.000           3          p24 SS AUE=0.9998 RMSE=1.2475 TorType=3
oh-c3-oh-ho   1    1.570         0.000           2          t11 SS AUE=0.6180 RMSE=0.8544 TorType=3
o -no-c2-c2   1    0.398       180.000           2          c31 SS AUE=0.2143 RMSE=0.3292 TorType=3
o -no-c2-c3   1    0.660       180.000           2          set1_11 SS AUE=0.2915 RMSE=0.3323 TorType=3
o -no-c3-no   1    5.020       180.000           2          t15 SS AUE=0.7609 RMSE=0.9238 TorType=3
o -no-ca-ca   1    0.700       180.000           2          c68 SS AUE=0.2638 RMSE=0.3293 TorType=3
o -no-cd-cc   1    1.075       180.000           2          add6e SS AUE=0.2138 RMSE=0.3290 TorType=3
o -no-n2-c2   1    1.030       180.000           2          c101 SS AUE=0.3306 RMSE=0.4189 TorType=3
o -no-n3-c3   1    2.170       180.000           2          c116 SS AUE=2.5004 RMSE=3.2115 TorType=3
o -no-n4-c3   1    1.250       180.000           2          c130 SS AUE=0.1901 RMSE=0.4144 TorType=3
o -no-na-cc   1    1.090       180.000           2          c143 SS AUE=0.5033 RMSE=0.6912 TorType=3
o -no-nh-c2   1    0.000       180.000           2          set3_11 SS AUE=2.0620 RMSE=2.8356 TorType=3
o -no-no-o    1    0.150       180.000          -4          c166 GA AUE=0.3903 RMSE=0.4419 TorType=3
o -no-no-o    1    1.450       180.000           2          c166 GA AUE=0.3903 RMSE=0.4419 TorType=3
o -no-p2-c2   1    0.990       180.000           2          c169 SS AUE=0.2765 RMSE=0.3321 TorType=3
o -no-p4-c3   1    0.502       180.000           2          c171 SS AUE=0.3449 RMSE=0.3960 TorType=3
o -py-ne-c2   1    0.900       180.000          -3          c107 GA AUE=0.4990 RMSE=0.6000 TorType=3
o -py-ne-c2   1    2.460         0.000           1          c107 GA AUE=0.4990 RMSE=0.6000 TorType=3
o -s4-c3-s4   1    1.340       180.000           1          t25 SS AUE=1.1411 RMSE=1.4982 TorType=3
o -s6-c3-s6   1    0.092         0.000           3          t24 SS AUE=0.4257 RMSE=0.4949 TorType=3
os-c -c3-c    1    2.000       180.000          -2          t42 GA AUE=0.4321 RMSE=0.5299 TorType=3
os-c -c3-c    1    1.850       180.000           1          t42 GA AUE=0.4321 RMSE=0.5299 TorType=3
os-p3-os-c3   1    2.040         0.000           2          c189 SS AUE=1.0926 RMSE=1.3514 TorType=3
os-p5-n3-c3   1    5.000       180.000           2          c122 SS AUE=2.8241 RMSE=3.6042 TorType=3
os-p5-n4-c3   1    0.143         0.000           3          c136 SS AUE=0.4630 RMSE=0.6433 TorType=3
os-p5-na-cc   1    2.180       180.000           2          c149 SS AUE=0.6556 RMSE=0.9113 TorType=3
os-p5-nh-c2   1    0.500         0.000           2          set3_17 SS AUE=0.9578 RMSE=1.1771 TorType=3
os-p5-no-o    1    2.733         0.000          -2          c172 GA AUE=0.6484 RMSE=0.8206 TorType=3
os-p5-no-o    1    0.317         0.000           3          c172 GA AUE=0.6484 RMSE=0.8206 TorType=3
os-p5-p3-c3   1    2.005       180.000           2          c206 SS AUE=1.1482 RMSE=1.4324 TorType=3
os-p5-ss-c3   1    4.467       180.000           2          c219 SS AUE=0.9050 RMSE=1.1227 TorType=3
os-py-ca-ca   1    1.800       180.000           2          c74 SS AUE=0.8528 RMSE=1.0796 TorType=3
os-py-ce-c2   1    1.767       180.000           2          c37 SS AUE=0.8275 RMSE=1.0644 TorType=3
os-py-ce-c3   1    4.200       180.000           2          set1_17 SS AUE=0.9222 RMSE=1.1571 TorType=3
os-py-pe-c2   1    2.567         0.000           1          c199 SS AUE=0.6931 RMSE=0.8807 TorType=3
os-py-py-c3   1    0.386         0.000           2          c212 SS AUE=0.6618 RMSE=0.8385 TorType=3
os-py-py-os   1    0.387         0.000           2          c217 SS AUE=0.6636 RMSE=1.0913 TorType=3
os-py-sx-c3   1    0.348         0.000           3          c220 SS AUE=0.6436 RMSE=0.8137 TorType=3
os-py-sy-c3   1    2.860         0.000          -2          c221 GA AUE=1.1694 RMSE=1.4143 TorType=3
os-py-sy-c3   1    0.380         0.000           1          c221 GA AUE=1.1694 RMSE=1.4143 TorType=3
p3-c3-p3-hp   1    0.215         0.000           3          t19 SS AUE=1.0811 RMSE=1.2418 TorType=3
s -c -c3-c    1    0.332       180.000           2          t10 SS AUE=0.9021 RMSE=1.2368 TorType=3
sh-c3-c3-n    1    0.210         0.000           3          p4 SS AUE=1.1296 RMSE=1.3941 TorType=3
sh-c3-sh-hs   1    0.083         0.000           3          t22 SS AUE=0.4554 RMSE=0.5406 TorType=3
ss-c3-ss-c3   1    0.497         0.000           3          t23 SS AUE=0.5714 RMSE=0.8553 TorType=3
c3-c3-ca-ca   1    0.245       180.000           2          m15,m17 SS AUE=0.2499 RMSE=0.3414 TorType=3
c3-c3-c -o    1    0.030       180.000          -2          sialic1,t37,t41 GA AUE=0.7374 RMSE=0.9897 TorType=3
c3-c3-c -o    1    0.550       180.000          -3
c3-c3-c -o    1    0.740         0.000           1
c3-c3-os-c3   1    0.910         0.000          -3          lactose1,ccoc GA AUE=1.5236 RMSE=2.4206 TorType=3
c3-c3-os-c3   1    1.000         0.000          -2
c3-c3-os-c3   1    0.000         0.000           1
ca-ca-c -o    1    0.5225      180.000           2          phcooh,t36a SS AUE=0.2702 RMSE=0.3317 TorType=3
o -c -c3-c    1    1.360         0.000          -1          t6,t7,t8 GA AUE=0.3790 RMSE=0.4991 TorType=3
o -c -c3-c    1    0.180       180.000           3
os-c3-c -o    1    0.630       180.000          -2          iduronic2,t39,t40 GA AUE=1.0545 RMSE=1.4852 TorType=3
os-c3-c -o    1    1.000       180.000          -3
os-c3-c -o    1    0.080         0.000           1
c2-ce-cs-c3   1    2.180         0.000           2          set2_2 SS AUE=0.8412 RMSE=1.0280  TorType=3
c2-ce-c -c3   1    2.970         0.000           2          c2 SS AUE=0.5377 RMSE=0.6518 TorType=3
c2-ce-ce-c2   1    0.500       180.000           2          c232,t3 SS AUE=0.7154 RMSE=0.9564 TorType=3
c2-n -c -c3   1    0.770       180.000           1          set3_1 SS AUE=1.1124 RMSE=1.4578 TorType=3
c2-n -cs-c3   1    2.833       180.000           2          set3_27 SS AUE=0.3805 RMSE=0.4661 TorType=3
c2-ne-c -c3   1    2.080       180.000           1          c6 SS AUE=0.4876 RMSE=0.8222 TorType=3
c2-ne-cs-c3   1    4.670       180.000           1          set2_6 SS AUE=1.2531 RMSE=1.5945 TorType=3
c2-pe-c -c3   1    1.750       180.000           1          c14 SS AUE=1.0447 RMSE=1.2490 TorType=3
c2-pe-cs-c3   1    2.960       180.000           1          set2_14 SS AUE=0.8598 RMSE=1.0604 TorType=3
c3-cs-cs-c3   1    0.455       180.000           2          set3_23 SS AUE=0.7278 RMSE=1.0389 TorType=3
c3-c -c -c3   1    0.512       180.000           2          c1 SS AUE=0.2443 RMSE=0.3313 TorType=3
c3-c -cs-c3   1    0.800       180.000           2          set2_1 SS AUE=1.0068 RMSE=1.3922 TorType=3
c3-c -n -ca   1    0.750       180.000          -2          c10 GA AUE=1.0418 RMSE=1.1578 TorType=3
c3-c -n -ca   1    0.500         0.000           3          c10 GA AUE=1.0418 RMSE=1.1578 TorType=3
c3-cs-n -ca   1    3.913       180.000           2          set2_10 SS AUE=1.3234 RMSE=1.7703 TorType=3
c3-n7-c3-c3   1    0.020       180.000          -3          m13 GA AUE=0.3404 RMSE=0.4405 TorType=3
c3-n7-c3-c3   1    0.050         0.000           2          m13 GA AUE=0.3404 RMSE=0.4405 TorType=3
c3-n3-c3-c3   1    0.580         0.000          -3          m14 GA AUE=0.4298 RMSE=0.5205 TorType=3
c3-n3-c3-c3   1    0.280       180.000           2          m14 GA AUE=0.4298 RMSE=0.5205 TorType=3
c3-n -cs-c3   1    2.000       180.000          -2          set2_7 GA AUE=0.7571 RMSE=0.9582 TorType=3
c3-n -cs-c3   1    2.310         0.000           1          set2_7 GA AUE=0.7571 RMSE=0.9582 TorType=3
c3-nu-ca-ca   1    0.550       180.000           2          c67 SS AUE=0.5825 RMSE=0.8345 TorType=3
c3-nh-ca-ca   1    0.733       180.000           2          c64 SS AUE=0.6264 RMSE=0.7797 TorType=3
c3-os-cs-c3   1    0.120         0.000          -1          set2_13 GA AUE=0.2180 RMSE=0.2948 TorType=3
c3-os-cs-c3   1    3.470       180.000          -2          set2_13 GA AUE=0.2180 RMSE=0.2948 TorType=3
c3-os-cs-c3   1    0.730         0.000           3          set2_13 GA AUE=0.2180 RMSE=0.2948 TorType=3
c3-p3-c -c3   1    1.538       180.000           2          c15 SS AUE=0.3737 RMSE=0.4391 TorType=3
c3-p3-cs-c3   1    2.050       180.000           2          set2_15 SS AUE=0.4669 RMSE=0.6407 TorType=3
c3-ss-c -c3   1    2.100       180.000           2          c19 SS AUE=0.9147 RMSE=1.1012 TorType=3
c3-ss-cs-c3   1    3.585       180.000           2          set2_19 SS AUE=0.3546 RMSE=0.4561 TorType=3
c3-sx-c -c3   1    0.950         0.000          -2          c20 GA AUE=1.4077 RMSE=1.8160 TorType=3
c3-sx-c -c3   1    1.460       180.000           1          c20 GA AUE=1.4077 RMSE=1.8160 TorType=3
c3-sx-cs-c3   1    0.000       180.000          -2          set2_20 GA AUE=1.3014 RMSE=1.5331 TorType=3
c3-sx-cs-c3   1    0.820       180.000           1          set2_20 GA AUE=1.3014 RMSE=1.5331 TorType=3
c3-sy-cs-c3   1    0.167         0.000           2          set2_21 SS AUE=0.4320 RMSE=0.5527 TorType=3
c3-sy-c -c3   1    0.833         0.000           2          c21 SS AUE=1.1437 RMSE=1.4496 TorType=3
ca-ca-c -c3   1    0.552       180.000           2          c4 SS AUE=0.2254 RMSE=0.3313 TorType=3
ca-ca-cs-c3   1    0.630       180.000           2          set2_4 SS AUE=0.2690 RMSE=0.3277 TorType=3
c -c3-c3-c3   1    0.100         0.000           3          p15,p21 SS AUE=0.6594 RMSE=0.8092 TorType=3
c -n -cs-c3   1    0.570         0.000           2          set2_5 SS AUE=1.0844 RMSE=1.5574 TorType=3
c -n -c -c3   1    0.000       180.000          -2          set3_28 GA AUE=1.6503 RMSE=2.2241 TorType=3
c -n -c -c3   1    1.720       180.000           1          set3_28 GA AUE=1.6503 RMSE=2.2241 TorType=3
hc-c3-c -c3   1    0.000         0.000           2          c3 SS AUE=0.0845 RMSE=0.1001 TorType=3
hc-c3-cs-c3   1    0.665         0.000           2          set2_3 SS AUE=0.5619 RMSE=0.7242 TorType=3
hn-n4-c -c3   1    1.025       180.000          -2          c8 GA AUE=0.2852 RMSE=0.3192 TorType=3
hn-n4-c -c3   1    0.365       180.000           4          c8 GA AUE=0.2852 RMSE=0.3192 TorType=3
hn-n4-cs-c3   1    0.950       180.000          -2          set2_8 GA AUE=0.7027 RMSE=0.8556 TorType=3
hn-n4-cs-c3   1    0.745         0.000           4          set2_8 GA AUE=0.7027 RMSE=0.8556 TorType=3
ho-oh-c -c3   1    1.780       180.000           2          c12 SS AUE=0.3293 RMSE=0.3814 TorType=3
ho-oh-cs-c3   1    2.920       180.000           2          set2_12 SS AUE=0.3286 RMSE=0.4081 TorType=3
hs-sh-cs-c3   1    2.690       180.000          -2          set2_18 GA AUE=0.2516 RMSE=0.2978 TorType=3
hs-sh-cs-c3   1    1.390       180.000           1          set2_18 GA AUE=0.2516 RMSE=0.2978 TorType=3
o -n -c -c3   1    0.370       180.000           2          c11 SS AUE=0.3392 RMSE=0.4173 TorType=3
o -n -cs-c3   1    0.520         0.000           2          set2_11 SS AUE=0.2859 RMSE=0.3263 TorType=3
o -p5-c3-p5   1    2.590       180.000          -2          t20 GA AUE=1.4330 RMSE=1.6847 TorType=3
o -p5-c3-p5   1    3.170         0.000           1          t20 GA AUE=1.4330 RMSE=1.6847 TorType=3
os-py-c -c3   1    2.370         0.000           2          c17 SS AUE=1.1966 RMSE=1.4736 TorType=3
os-py-cs-c3   1    0.500         0.000           2          set2_17 SS AUE=0.8458 RMSE=1.0943 TorType=3
""")

gaff_impropers = ("""
X -o -c -o          1.1          180.          2.           JCC,7,(1986),230
X -X -c -o          10.5         180.          2.           JCC,7,(1986),230
X -X -ca-ha         1.1          180.          2.           bsd.on C6H6 nmodes
X -X -n -hn         1.1          180.          2.           JCC,7,(1986),230
X -X -n2-hn         1.1          180.          2.           JCC,7,(1986),230
X -X -na-hn         1.1          180.          2.           JCC,7,(1986),230
X -c3-n -c3         1.1          180.          2.           JCC,7,(1986),230
X -n2-ca-n2         10.5         180.          2.           JCC,7,(1986),230
c -c2-c2-c3         1.1          180.          2.           dac guess, 9/94
c -ca-ca-c3         1.1          180.          2.           dac guess, 9/94
c -c3-n -hn         1.1          180.          2.           Junmei et al.1999
c -c3-n -o          1.1          180.          2.           Junmei et al.1999
c2-c2-na-c3         1.1          180.          2.
c2-c -c2-c3         1.1          180.          2.
c2-c3-c2-hc         1.1          180.          2.           Junmei et al.1999
c2-c3-ca-hc         1.1          180.          2.           Junmei et al.1999
c2-hc-c -o          1.1          180.          2.           Junmei et al.1999
c3-o -c -oh         1.1          180.          2.
c3-c2-c2-n2         1.1          180.          2.
c3-c2-c2-na         1.1          180.          2.
c3-ca-ca-n2         1.1          180.          2.
c3-ca-ca-na         1.1          180.          2.
ca-ca-ca-c2         1.1          180.          2.
ca-ca-ca-c3         1.1          180.          2.
ca-ca-ca-f          1.1          180.          2.           Junmei et al.1999
ca-ca-ca-cl         1.1          180.          2.           Junmei et al.1999
ca-ca-ca-br         1.1          180.          2.           Junmei et al.1999
ca-ca-ca-i          1.1          180.          2.           Junmei et al.1999
ca-ca-c -oh         1.1          180.          2.           (not used in tyr!)
ca-ca-na-c3         1.1          180.          2.
ca-c -ca-c3         1.1          180.          2.
ca-hc-c -o          1.1          180.          2.           Junmei et al.1999
ca-n2-ca-n2         1.1          180.          2.           dac, 10/94
hc-o -c -oh         1.1          180.          2.           Junmei et al.1999
hc-o -c -os         1.1          180.          2.
n2-c2-ca-n2         1.1          180.          2.           dac guess, 9/94
n2-ca-ca-n2         1.1          180.          2.           dac guess, 9/94
na-n2-ca-n2         1.1          180.          2.           dac, 10/94
""")

# hw  ow  0000.     0000.                                4.  flag for fast water

# MOD4      RE
gaff_LJ_params = dedent("""
  hc          1.4593  0.0208
  ha          1.4735  0.0161
  hn          0.6210  0.0100
  ho          0.3019  0.0047
  hs          0.6112  0.0124
  hp          0.6031  0.0144
  o           1.7107  0.1463
  os          1.7713  0.0726
  op          1.7713  0.0726
  oq          1.7713  0.0726
  oh          1.8200  0.0930
  c3          1.9069  0.1078
  c2          1.8606  0.0988
  c1          1.9525  0.1596
  n           1.7852  0.1636
  s           1.9825  0.2824
  p2          2.0732  0.2295
  f           1.7029  0.0832
  cl          1.9452  0.2638
  br          2.0275  0.3932
  i           2.1558  0.4955
  n1          1.8372  0.1098
  n2          1.8993  0.0941
  n3          1.8886  0.0858
  na          1.7992  0.2042
  nh          1.7903  0.2150
  n+          1.6028  0.7828
  n9          2.2700  0.0095
  h1          1.3593  0.0208
  h2          1.2593  0.0208
  h3          1.1593  0.0208
  hx          1.0593  0.0208
  h4          1.4235  0.0161
  h5          1.3735  0.0161
  cx          1.9069  0.1078
  cy          1.9069  0.1078
  c           1.8606  0.0988
  cs          1.8606  0.0988
  ca          1.8606  0.0988
  cc          1.8606  0.0988
  cd          1.8606  0.0988
  ce          1.8606  0.0988
  cf          1.8606  0.0988
  cp          1.8606  0.0988
  cq          1.8606  0.0988
  cz          1.8606  0.0988
  cg          1.9525  0.1596
  ch          1.9525  0.1596
  cu          1.8606  0.0988
  cv          1.8606  0.0988
  nb          1.8993  0.0941
  nc          1.8993  0.0941
  nd          1.8993  0.0941
  ne          1.8993  0.0941
  nf          1.8993  0.0941
  no          1.8886  0.0858
  n7          1.9686  0.0522
  n8          2.0486  0.0323
  n4          1.4028  3.8748
  nx          1.4528  2.5453
  ny          1.5028  1.6959
  nz          1.5528  1.1450
  ns          1.8352  0.1174
  nt          1.8852  0.0851
  nu          1.8403  0.1545
  nv          1.8903  0.1120
  ni          1.7852  0.1636
  nj          1.7852  0.1636
  nk          1.4528  2.5453
  nl          1.4528  2.5453
  nm          1.7903  0.2150
  nn          1.7903  0.2150
  np          1.8886  0.0858
  nq          1.8886  0.0858
  n5          1.9686  0.0522
  n6          1.9686  0.0522
  s2          1.9825  0.2824
  s4          1.9825  0.2824
  s6          1.9825  0.2824
  sx          1.9825  0.2824
  sy          1.9825  0.2824
  sh          1.9825  0.2824
  ss          1.9825  0.2824
  sp          1.9825  0.2824
  sq          1.9825  0.2824
  p3          2.0732  0.2295
  p4          2.0732  0.2295
  p5          2.0732  0.2295
  pb          2.0732  0.2295
  px          2.0732  0.2295
  py          2.0732  0.2295
  pc          2.0732  0.2295
  pd          2.0732  0.2295
  pe          2.0732  0.2295
  pf          2.0732  0.2295
 """)

# END
#
# ----------------------------------------------------------------------------
# Equilibrium  Sources
# SOURCE1
# Authors: Frank H. Allen, Olga Kennard and David G. Watson
# Title: Tables of Bond lengths determined by X-ray and neutron
# diffraction. Part 1. Bond lengths in organic compounds
# Journal: J. Chem. Soc. Perkin Trans. II 1987, S1-S19
#
# SOURCE2
# Authors: Harmony, M. D.; Laurie, V. W.; Kuczkowski, R. L.; Schwendeman,
# R. H.; Ramsay, D. A.; Lovas, F. J.; Lafferty, W. J.; Maki, A. G.
# Title: Molecular structures of gas-phase polyatomic molecules determined
# by spectroscopic methods
# Journal: J. Phys. Chem. Ref. Data, Vol 8, 1979, 619
#
# SOURCE3
# Optimized geometries at MP2/6-31G* level
#
# SOURCE4
# Optimized geometries at B3LYP/6-31G* level (15,000 molecules)
#
# SOURCE5
# Optimized geometries at B3LYP/6-31G* level (30,000 molecules)
# ---------------------------------------------------------------------------
# Bond stretching parameter format
# atom_type  force_constant   equ. length  source_ID occurrence rmsd
# xx-yy          581.1           1.288      SOURCE1     103    0.0100
# ---------------------------------------------------------------------------
# atom_type  force_constant   equ. angle   source_ID   occurrence   rmsd
# xx-yy-zz      35.450          103.620     SOURCE3         3      0.7078
# ---------------------------------------------------------------------------
# aa-bb-cc-dd 4    2.000         0.000 2	set2_17	SS AUE=0.8458 RMSE=1.0943 TorType=3
# |           |    |             |     |     |    |           |   |         |
# atom_type   |    force_constant|     Vterm |    Opt_methods |   |    Torsional_Type
# multiplicity       phase    model_cmpd          Prediction_Error
#
# TorType=1: parameter comes from gaff
# TorType=2: parameter introduced in gaff, but updated
# TorType=3: parameter newly introduced
# Opt_method=SS: systematic search
# Opt_method=GA: genetic algorithm
# ---------------------------------------------------------------------------
# Version gaff2.1
# van der Waals:  redeveloped to reproduce both high-level ab initio interaction
# energies and experimental pure liquid properties.
# Reference bond lengthes and angles:  updated based on the statistics of more
# than 30,000 geometries optimized at at least B3LYP/6-31G* level.
# Bond length and bond angle force constants: redeveloped to reproduce vibrational
# frequencies of more than 600 molecules. The AUE and RMSE of more
# than 22000 frequencies is 51 and 67 cm-1, respectively.
# Torsional angle parameters:  developed to reproduce ab initio rotation profiles
# (MP2/aug-cc-pVTZ) for 400 most common model compounds including
# some PTM residues. The average RMS errors of reproducing ab
# initio rotation profiles is 0.94 kcal/mol
# !!!Suggestions/criticisms/comments are always welcome !!!
# ----------------------------------------------------------------------------
# Version gaff2.11
# Updates to GAFF 2.11, May, 2017:
# added new atom types for n3/n4/n/nh/os/ss in RG3 and RG4
# updated bond length/angle parameters involved by the newly introduced atom types
# ----------------------------------------------------------------------------
