setup_template="""\\begindata
INPUT_DATA_TYPE   = 'ELEMENTS'
OUTPUT_SPK_TYPE   = 5
OBJECT_ID         = {object_id}
OBJECT_NAME       = '{object_name}'
CENTER_ID         = {center_id}
CENTER_NAME       = 'SOLAR_SYSTEM_BARYCENTER'
CENTER_GM	  = {center_gm}
REF_FRAME_NAME    = 'J2000'
TIME_WRAPPER      = '# ETSECONDS'
PRODUCER_ID       = 'Bryan Lunt'
DATA_ORDER        = 'EPOCH RP E INC NOD PER MEAN SKIP'
INPUT_DATA_UNITS  = ('ANGLES=DEGREES' 'DISTANCES=km')
DATA_DELIMITER    = ' '
LINES_PER_RECORD  = 2
IGNORE_FIRST_LINE = 3
LEAPSECONDS_FILE  = '../naif0007.tls'
PCK_FILE          = '../gravity.tpc'
SEGMENT_ID        = 'SPK_ELEMENTS_05'
TLE_STOP_PAD	  = '18250 days'
\\begintext"""

ephemeris_template="""Test: {object_id} relative to {center_id} in frame J2000. GM= {center_gm}
JD, RP, ECC, INC, LNODE, ARGP, M0, T0
-------------------------------------
2000 JAN 01 00:00:00
{rad_periapsis_km} {eccentricity} {inclination} {longitude_of_ascending_node} {argument_of_periapsis} {mean_anomaly_at_epoch} -657287949.8
"""


ephemeris_template_header="""Test: {object_id} relative to {center_id} in frame J2000. GM= {center_gm}
JD, RP, ECC, INC, LNODE, ARGP, M0, T0
-------------------------------------
"""
ephemeris_data_line="""{time_in_seconds}
{rad_periapsis_km} {eccentricity} {inclination} {longitude_of_ascending_node} {argument_of_periapsis} {mean_anomaly_at_epoch} -657287949.8
"""
