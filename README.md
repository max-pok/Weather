# Weather service for linux

## Authors:
--------
* Maxim Pokidaylo
* Adir Atia
* Vitaly Nechayuk

## Description:
Weather TCP Server + Client - Detailed weather around the world.
The server can be used at any time through the bash as long as it runs.
Gives detailed and updated weather information according to the entered location.

Version: 1.0

## System requirements
 * Internet connection
 * Linux/Unix-based operation system
 * Python package installed (version 2.7.1 optimal)

## Installation
1. Put the following files in your root directory (HOME):
   * `Makefile`
   * `t.py`
   * `weather_tcpserver.py`
   * `weather`
   * `service.service`
2. Enter the command `make install` in the bash (root).

## Activation & Use
1. Enter the command `make run` in the bash (root).
2. Enter the command `./weather + [LOCATION]` in format of [City, CPA (optional)].
   Examples: `./weather Houston, US`
             `./weather Tel Aviv`
             `./weather washington`

##### IMPORTANT: 
* The location must be entered according to the required format and with legit city name and CPA. Otherwise exception will be thrown.
* CPA is optional, though recommended (due to similar city names in different countries).
* If the location is not legit, a default location will be activated instead.
* If the location is not entered, a default location will be activated instead.
  (Default location: Beer-Sheva, IL)
  
## Uninstall
Enter the command `make clean` in the bash (root).

#### CPA - Country Postal Abbreviations
AF = Afghanistan
AL = Albania
DZ = Algeria
AX = Aland Islands
AS = American Samoa
AI = Anguilla
AD = Andorra
AO = Angola
AN = Antilles - Netherlands
AG = Antigua and Barbuda
AQ = Antarctica
AR = Argentina
AM = Armenia
AU = Australia
AT = Austria
AW = Aruba
AZ = Azerbaijan
BA = Bosnia and Herzegovina
BB = Barbados
BD = Bangladesh
BE = Belgium
BF = Burkina Faso
BG = Bulgaria
BH = Bahrain
BI = Burundi
BJ = Benin
BM = Bermuda
BN = Brunei Darussalam
BO = Bolivia
BR = Brazil
BS = Bahamas
BT = Bhutan
BV = Bouvet Island
BW = Botswana
BV = Belarus
BZ = Belize
KH = Cambodia
CM = Cameroon
CA = Canada
CV = Cape Verde
CF = Central African Republic
TD = Chad
CL = Chile
CN = China
CX = Christmas Island
CC = Cocos (Keeling) Islands
CO = Colombia
CG = Congo
CI = Cote D'Ivoire (Ivory Coast)
CK = Cook Islands
CR = Costa Rica
HR = Croatia (Hrvatska)
CU = Cuba
CY = Cyprus
CZ = Czech Republic
CD = Democratic Republic of the Congo
DJ = Djibouti
DK = Denmark
DM = Dominica
DO = Dominican Republic
EC = Ecuador
EG = Egypt
SV = El Salvador
TP = East Timor
EE = Estonia
GQ = Equatorial Guinea
ER = Eritrea
ET = Ethiopia
FI = Finland
FJ = Fiji
FK = Falkland Islands (Malvinas)
FM = Federated States of Micronesia
FO = Faroe Islands
FR = France
FX = France, Metropolitan
GF = French Guiana
PF = French Polynesia
GA = Gabon
GM = Gambia
DE = Germany
GH = Ghana
GI = Gibraltar
GB = Great Britain (UK)
GD = Grenada
GE = Georgia
GR = Greece
GL = Greenland
GN = Guinea
GP = Guadeloupe
GS = S. Georgia and S. Sandwich Islands
GT = Guatemala
GU = Guam
GW = Guinea-Bissau
GY = Guyana
HK = Hong Kong
HM = Heard Island and McDonald Islands
HN = Honduras
HT = Haiti
HU = Hungary
ID = Indonesia
IE = Ireland
IL = Israel
IN = India
IO = British Indian Ocean Territory
IQ = Iraq
IR = Iran
IT = Italy
JM = Jamaica
JO = Jordan
JP = Japan
KE = Kenya
KG = Kyrgyzstan
KI = Kiribati
KM = Comoros
KN = Saint Kitts and Nevis
KP = Korea (North)
KR = Korea (South)
KW = Kuwait
KY = Cayman Islands
KZ = Kazakhstan
LA = Laos
LB = Lebanon
LC = Saint Lucia
LI = Liechtenstein
LK = Sri Lanka
LR = Liberia
LS = Lesotho
LT = Lithuania
LU = Luxembourg
LV = Latvia
LY = Libya
MK = Macedonia
MO = Macao
MG = Madagascar
MY = Malaysia
ML = Mali
MW = Malawi
MR = Mauritania
MH = Marshall Islands
MQ = Martinique
MU = Mauritius
YT = Mayotte
MT = Malta
MX = Mexico
MA = Morocco
MC = Monaco
MD = Moldova
MN = Mongolia
MM = Myanmar
MP = Northern Mariana Islands
MS = Montserrat
MV = Maldives
MZ = Mozambique
NA = Namibia
NC = New Caledonia
NE = Niger
NF = Norfolk Island
NG = Nigeria
NI = Nicaragua
NL = Netherlands
NO = Norway
NP = Nepal
NR = Nauru
NU = Niue
NZ = New Zealand (Aotearoa)
OM = Oman
PA = Panama
PE = Peru
PG = Papua New Guinea
PH = Philippines
PK = Pakistan
PL = Poland
PM = Saint Pierre and Miquelon
CS = Serbia and Montenegro
PN = Pitcairn
PR = Puerto Rico
PS = Palestinian Territory
PT = Portugal
PW = Palau
PY = Paraguay
QA = Qatar
RE = Reunion
RO = Romania
RU = Russian Federation
RW = Rwanda
SA = Saudi Arabia
WS = Samoa
SH = Saint Helena
VC = Saint Vincent and the Grenadines
SM = San Marino
ST = Sao Tome and Principe
SN = Senegal
SC = Seychelles
SL = Sierra Leone
SG = Singapore
SK = Slovakia
SI = Slovenia
SB = Solomon Islands
SO = Somalia
ZA = South Africa
ES = Spain
SD = Sudan
SR = Suriname
SJ = Svalbard and Jan Mayen
SE = Sweden
CH = Switzerland
SY = Syria
SU = USSR (former)
SZ = Swaziland
TW = Taiwan
TZ = Tanzania
TJ = Tajikistan
TH = Thailand
TL = Timor-Leste
TG = Togo
TK = Tokelau
TO = Tonga
TT = Trinidad and Tobago
TN = Tunisia
TR = Turkey
TM = Turkmenistan
TC = Turks and Caicos Islands
TV = Tuvalu
UA = Ukraine
UG = Uganda
AE = United Arab Emirates
UK = United Kingdom
US = United States
UM = United States Minor Outlying Islands
UY = Uruguay
UZ = Uzbekistan
VU = Vanuatu
VA = Vatican City State
VE = Venezuela
VG = Virgin Islands (British)
VI = Virgin Islands (U.S.)
VN = Viet Nam
WF = Wallis and Futuna
EH = Western Sahara
YE = Yemen
YU = Yugoslavia (former)
ZM = Zambia
ZR = Zaire (former)
ZW = Zimbabwe

