# %%

import sqlite3

# Create / connect to database file
conn = sqlite3.connect("happy_child_peds.db")
cur = conn.cursor()

cur.executescript("""
PRAGMA foreign_keys = ON;

-- ============================================
-- DROP TABLES (reverse dependency order)
-- ============================================
DROP TABLE IF EXISTS IMMUNIZATION_EVENT;
DROP TABLE IF EXISTS CLINICAL_ENCOUNTER;
DROP TABLE IF EXISTS VACCINE_LOT;
DROP TABLE IF EXISTS STAFF_CLINIC;
DROP TABLE IF EXISTS PROVIDER;
DROP TABLE IF EXISTS NURSE;
DROP TABLE IF EXISTS PATIENT_GUARDIAN;
DROP TABLE IF EXISTS PATIENT;
DROP TABLE IF EXISTS GUARDIAN;
DROP TABLE IF EXISTS STAFF;
DROP TABLE IF EXISTS CLINIC;
DROP TABLE IF EXISTS VACCINE;

-- ============================================
-- DDL: CREATE TABLES
-- ============================================

-- VACCINE
CREATE TABLE VACCINE (
    vaccine_id INTEGER PRIMARY KEY,
    cvx_code TEXT UNIQUE NOT NULL,
    vaccine_name TEXT NOT NULL,
    recommended_min_age_months INTEGER,
    recommended_max_age_years INTEGER
);

-- CLINIC
CREATE TABLE CLINIC (
    clinic_id INTEGER PRIMARY KEY,
    clinic_name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    phone_number TEXT
);

-- STAFF (base table for nurses and providers)
CREATE TABLE STAFF (
    staff_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role TEXT NOT NULL,           -- 'NURSE' or 'PROVIDER'
    email TEXT,
    phone_number TEXT
);

-- GUARDIAN
CREATE TABLE GUARDIAN (
    guardian_id INTEGER PRIMARY KEY,
    gfirst_name TEXT NOT NULL,
    glast_name TEXT NOT NULL,
    relationship_to_child TEXT,
    phone_number TEXT,
    email TEXT,
    primary_language TEXT,
    preferred_communication_method TEXT,
    has_legal_consent_authority INTEGER
);

-- PATIENT
CREATE TABLE PATIENT (
    patient_id INTEGER PRIMARY KEY,
    pfirst_name TEXT NOT NULL,
    plast_name TEXT NOT NULL,
    birthdate TEXT NOT NULL,
    sex TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    primary_clinic_id INTEGER,
    is_active_patient INTEGER,
    FOREIGN KEY (primary_clinic_id) REFERENCES CLINIC(clinic_id)
);

-- PATIENT_GUARDIAN (M:N link)
CREATE TABLE PATIENT_GUARDIAN (
    patient_guardian_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    guardian_id INTEGER NOT NULL,
    relationship_type TEXT,
    is_primary_contact INTEGER,
    consent_notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES PATIENT(patient_id),
    FOREIGN KEY (guardian_id) REFERENCES GUARDIAN(guardian_id)
);

-- NURSE (1:1 with STAFF where role='NURSE')
CREATE TABLE NURSE (
    staff_id INTEGER PRIMARY KEY,
    license_number TEXT NOT NULL,
    nurse_type TEXT,
    FOREIGN KEY (staff_id) REFERENCES STAFF(staff_id)
);

-- PROVIDER (1:1 with STAFF where role='PROVIDER')
CREATE TABLE PROVIDER (
    staff_id INTEGER PRIMARY KEY,
    npi_number TEXT NOT NULL,
    specialty TEXT,
    FOREIGN KEY (staff_id) REFERENCES STAFF(staff_id)
);

-- STAFF_CLINIC (M:N staff↔clinic)
CREATE TABLE STAFF_CLINIC (
    staff_clinic_id INTEGER PRIMARY KEY,
    staff_id INTEGER NOT NULL,
    clinic_id INTEGER NOT NULL,
    FOREIGN KEY (staff_id) REFERENCES STAFF(staff_id),
    FOREIGN KEY (clinic_id) REFERENCES CLINIC(clinic_id)
);

-- VACCINE_LOT
CREATE TABLE VACCINE_LOT (
    vaccine_lot_id INTEGER PRIMARY KEY,
    vaccine_id INTEGER NOT NULL,
    mvx_code TEXT NOT NULL,
    lot_number TEXT NOT NULL,
    expiration_date TEXT,
    ndc_code TEXT,
    FOREIGN KEY (vaccine_id) REFERENCES VACCINE(vaccine_id)
);

-- CLINICAL_ENCOUNTER
CREATE TABLE CLINICAL_ENCOUNTER (
    encounter_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    clinic_id INTEGER NOT NULL,
    encounter_date TEXT NOT NULL,
    encounter_type TEXT,
    reason_for_visit TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES PATIENT(patient_id),
    FOREIGN KEY (clinic_id) REFERENCES CLINIC(clinic_id)
);

-- IMMUNIZATION_EVENT
CREATE TABLE IMMUNIZATION_EVENT (
    immunization_event_id INTEGER PRIMARY KEY,
    encounter_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    vaccine_lot_id INTEGER NOT NULL,
    administration_date TEXT NOT NULL,
    administering_staff_id INTEGER NOT NULL,
    site_of_administration TEXT,
    route TEXT,
    dose_number INTEGER,
    refusal_reason TEXT,
    notes TEXT,
    FOREIGN KEY (encounter_id) REFERENCES CLINICAL_ENCOUNTER(encounter_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT(patient_id),
    FOREIGN KEY (vaccine_lot_id) REFERENCES VACCINE_LOT(vaccine_lot_id),
    FOREIGN KEY (administering_staff_id) REFERENCES STAFF(staff_id)
);

-- ============================================
-- INSERT DATA
-- ============================================

-- VACCINE (10 rows)
INSERT INTO VACCINE (vaccine_id, cvx_code, vaccine_name,
                     recommended_min_age_months, recommended_max_age_years)
VALUES
(1,  '08',  'Hepatitis B',                        0,   18),
(2,  '20',  'DTaP',                               2,    7),
(3,  '10',  'Polio (IPV)',                        2,   18),
(4,  '48',  'Hib',                                2,    5),
(5,  '133', 'Pneumococcal conjugate (PCV13)',     2,    5),
(6,  '03',  'MMR',                               12,   18),
(7,  '21',  'Varicella',                         12,   18),
(8,  '83',  'Hepatitis A',                       12,   18),
(9,  '116', 'Rotavirus',                          2,    1),
(10, '62',  'HPV',                                9,   26);

-- CLINIC (10 rows)
INSERT INTO CLINIC (clinic_id, clinic_name, address, city, state, zip, phone_number)
VALUES
(1, 'Happy Child Pediatrics - Salt Lake', '123 Main St',    'Salt Lake City', 'UT', '84101', '801-555-0101'),
(2, 'Happy Child Pediatrics - Provo',     '456 Center St',  'Provo',          'UT', '84601', '801-555-0102'),
(3, 'Happy Child Pediatrics - Ogden',     '789 Canyon Rd',  'Ogden',          'UT', '84401', '801-555-0103'),
(4, 'Happy Child Pediatrics - St George', '15 Red Rock Dr', 'St George',      'UT', '84770', '801-555-0104'),
(5, 'Happy Child Pediatrics - Logan',     '22 Valley Ln',   'Logan',          'UT', '84321', '801-555-0105'),
(6, 'Happy Child Pediatrics - Sandy',     '9000 State St',  'Sandy',          'UT', '84070', '801-555-0106'),
(7, 'Happy Child Pediatrics - Lehi',      '200 Tech Way',   'Lehi',           'UT', '84043', '801-555-0107'),
(8, 'Happy Child Pediatrics - Murray',    '300 Hospital Rd','Murray',         'UT', '84107', '801-555-0108'),
(9, 'Happy Child Pediatrics - Draper',    '777 Eagle Rd',   'Draper',         'UT', '84020', '801-555-0109'),
(10,'Happy Child Pediatrics - Park City', '50 Summit Ave',  'Park City',      'UT', '84060', '801-555-0110');

-- STAFF (20 rows: 10 nurses, 10 providers)
INSERT INTO STAFF (staff_id, first_name, last_name, role, email, phone_number)
VALUES
-- Nurses 1–10
(1,  'Emily',   'Clark',    'NURSE',    'eclark@hcpeds.org',    '801-555-0201'),
(2,  'Megan',   'Stone',    'NURSE',    'mstone@hcpeds.org',    '801-555-0202'),
(3,  'Sarah',   'Hill',     'NURSE',    'shill@hcpeds.org',     '801-555-0203'),
(4,  'Lily',    'Nguyen',   'NURSE',    'lnguyen@hcpeds.org',   '801-555-0204'),
(5,  'Rachel',  'Lopez',    'NURSE',    'rlopez@hcpeds.org',    '801-555-0205'),
(6,  'Hannah',  'Brown',    'NURSE',    'hbrown@hcpeds.org',    '801-555-0206'),
(7,  'Ava',     'Thompson', 'NURSE',    'athompson@hcpeds.org', '801-555-0207'),
(8,  'Olivia',  'King',     'NURSE',    'oking@hcpeds.org',     '801-555-0208'),
(9,  'Jenna',   'Scott',    'NURSE',    'jscott@hcpeds.org',    '801-555-0209'),
(10, 'Maria',   'White',    'NURSE',    'mwhite@hcpeds.org',    '801-555-0210'),
-- Providers 11–20
(11, 'Daniel',  'Roberts',  'PROVIDER', 'droberts@hcpeds.org',  '801-555-0301'),
(12, 'Nathan',  'Brooks',   'PROVIDER', 'nbrooks@hcpeds.org',   '801-555-0302'),
(13, 'Jacob',   'Price',    'PROVIDER', 'jprice@hcpeds.org',    '801-555-0303'),
(14, 'Sophia',  'Mitchell', 'PROVIDER', 'smitchell@hcpeds.org', '801-555-0304'),
(15, 'Ethan',   'Rivera',   'PROVIDER', 'erivera@hcpeds.org',   '801-555-0305'),
(16, 'Noah',    'Young',    'PROVIDER', 'nyoung@hcpeds.org',    '801-555-0306'),
(17, 'Chloe',   'Ward',     'PROVIDER', 'cward@hcpeds.org',     '801-555-0307'),
(18, 'Logan',   'Foster',   'PROVIDER', 'lfoster@hcpeds.org',   '801-555-0308'),
(19, 'Aiden',   'Gonzalez', 'PROVIDER', 'agonzalez@hcpeds.org', '801-555-0309'),
(20, 'Grace',   'Parker',   'PROVIDER', 'gparker@hcpeds.org',   '801-555-0310');

-- GUARDIAN (10 rows)
INSERT INTO GUARDIAN (guardian_id, gfirst_name, glast_name, relationship_to_child,
                      phone_number, email, primary_language,
                      preferred_communication_method, has_legal_consent_authority)
VALUES
(1,  'Laura',  'Anderson', 'Mother', '801-555-0401', 'laura.anderson@example.com',  'English', 'PHONE', 1),
(2,  'Michael','Anderson', 'Father', '801-555-0402', 'michael.anderson@example.com','English', 'EMAIL', 1),
(3,  'Priya',  'Patel',    'Mother', '801-555-0403', 'priya.patel@example.com',     'Hindi',   'SMS',   1),
(4,  'Raj',    'Patel',    'Father', '801-555-0404', 'raj.patel@example.com',       'Hindi',   'PHONE', 1),
(5,  'Erin',   'Smith',    'Mother', '801-555-0405', 'erin.smith@example.com',      'English', 'EMAIL', 1),
(6,  'Carlos', 'Garcia',   'Father', '801-555-0406', 'carlos.garcia@example.com',   'Spanish', 'SMS',   1),
(7,  'Anna',   'Lee',      'Mother', '801-555-0407', 'anna.lee@example.com',        'English', 'PHONE', 1),
(8,  'David',  'Lee',      'Father', '801-555-0408', 'david.lee@example.com',       'English', 'EMAIL', 1),
(9,  'Fatima', 'Hassan',   'Mother', '801-555-0409', 'fatima.hassan@example.com',   'Arabic',  'SMS',   1),
(10, 'Omar',   'Hassan',   'Father', '801-555-0410', 'omar.hassan@example.com',     'Arabic',  'PHONE', 1);

-- PATIENT (10 rows)
INSERT INTO PATIENT (patient_id, pfirst_name, plast_name, birthdate, sex,
                     address, city, state, zip, primary_clinic_id, is_active_patient)
VALUES
(1,  'Eli',      'Anderson', '2018-03-15', 'M', '101 Oak St',   'Salt Lake City','UT','84101', 1, 1),
(2,  'Sophie',   'Anderson', '2020-07-20', 'F', '101 Oak St',   'Salt Lake City','UT','84101', 1, 1),
(3,  'Arjun',    'Patel',    '2016-11-05', 'M', '55 Maple Rd',  'Provo',         'UT','84601', 2, 1),
(4,  'Mira',     'Patel',    '2019-01-25', 'F', '55 Maple Rd',  'Provo',         'UT','84601', 2, 1),
(5,  'Liam',     'Smith',    '2015-09-10', 'M', '700 Elm Dr',   'Ogden',         'UT','84401', 3, 1),
(6,  'Ava',      'Smith',    '2017-02-18', 'F', '700 Elm Dr',   'Ogden',         'UT','84401', 3, 1),
(7,  'Mateo',    'Garcia',   '2021-05-30', 'M', '88 Cedar Ln',  'St George',     'UT','84770', 4, 1),
(8,  'Isabella', 'Garcia',   '2014-12-02', 'F', '88 Cedar Ln',  'St George',     'UT','84770', 4, 1),
(9,  'Noah',     'Lee',      '2013-06-08', 'M', '12 Pine Ct',   'Logan',         'UT','84321', 5, 1),
(10, 'Layla',    'Hassan',   '2019-09-22', 'F', '900 Birch St', 'Salt Lake City','UT','84101', 1, 1);

-- PATIENT_GUARDIAN (10 rows)
INSERT INTO PATIENT_GUARDIAN (patient_guardian_id, patient_id, guardian_id,
                              relationship_type, is_primary_contact, consent_notes)
VALUES
(1,  1, 1, 'Mother', 1, 'Primary contact'),
(2,  1, 2, 'Father', 0, 'Joint legal custody'),
(3,  2, 1, 'Mother', 1, 'Primary contact'),
(4,  2, 2, 'Father', 0, 'Joint legal custody'),
(5,  3, 3, 'Mother', 1, 'Prefers SMS reminders'),
(6,  3, 4, 'Father', 0, NULL),
(7,  4, 3, 'Mother', 1, NULL),
(8,  5, 5, 'Mother', 1, NULL),
(9,  6, 6, 'Father', 1, NULL),
(10, 10,9, 'Mother', 1, 'Recent move; confirm address');

-- NURSE (10 rows – staff 1–10)
INSERT INTO NURSE (staff_id, license_number, nurse_type)
VALUES
(1,  'RN12345',  'RN'),
(2,  'RN23456',  'RN'),
(3,  'RN34567',  'RN'),
(4,  'RN45678',  'RN'),
(5,  'RN56789',  'RN'),
(6,  'RN67890',  'RN'),
(7,  'RN78901',  'RN'),
(8,  'RN89012',  'RN'),
(9,  'RN90123',  'RN'),
(10, 'RN01234',  'RN');

-- PROVIDER (10 rows – staff 11–20)
INSERT INTO PROVIDER (staff_id, npi_number, specialty)
VALUES
(11, '1111111111', 'Pediatrics'),
(12, '2222222222', 'Pediatrics'),
(13, '3333333333', 'Pediatrics'),
(14, '4444444444', 'Pediatrics'),
(15, '5555555555', 'Pediatrics'),
(16, '6666666666', 'Pediatrics'),
(17, '7777777777', 'Pediatrics'),
(18, '8888888888', 'Pediatrics'),
(19, '9999999999', 'Pediatrics'),
(20, '1010101010', 'Pediatrics');

-- STAFF_CLINIC (10 rows)
INSERT INTO STAFF_CLINIC (staff_clinic_id, staff_id, clinic_id)
VALUES
(1,  1, 1),
(2,  2, 1),
(3,  3, 2),
(4,  4, 3),
(5,  5, 4),
(6, 11, 1),
(7, 12, 2),
(8, 13, 3),
(9, 14, 4),
(10, 15, 5);

-- VACCINE_LOT (10 rows)
INSERT INTO VACCINE_LOT (vaccine_lot_id, vaccine_id, mvx_code, lot_number,
                          expiration_date, ndc_code)
VALUES
(1,  1,  'MER', 'HBV123A', '2026-01-31', '00006-4093-02'),
(2,  2,  'GSK', 'DTAP45B', '2025-12-31', '58160-0814-52'),
(3,  3,  'SAN', 'IPV789C', '2027-03-15', '49281-860-10'),
(4,  4,  'MER', 'HIB456D', '2025-09-30', '00006-4893-01'),
(5,  5,  'PFZ', 'PCV13E',  '2026-06-30', '00005-1971-01'),
(6,  6,  'MER', 'MMR001F', '2026-04-30', '00006-4681-00'),
(7,  7,  'MER', 'VAR777G', '2025-11-30', '00006-4827-01'),
(8,  8,  'GSK', 'HEPA88H', '2027-01-31', '58160-0817-52'),
(9,  9,  'MER', 'ROTA55I', '2025-08-31', '00006-4047-41'),
(10, 10, 'MER', 'HPV99J',  '2028-12-31', '00006-4121-02');

-- CLINICAL_ENCOUNTER (10 rows)
INSERT INTO CLINICAL_ENCOUNTER (encounter_id, patient_id, clinic_id,
                                encounter_date, encounter_type,
                                reason_for_visit, notes)
VALUES
(1, 1, 1, '2025-01-10', 'Well visit',    '4-year well child',       'Doing well; due for DTaP and IPV.'),
(2, 2, 1, '2025-02-05', 'Vaccine visit', 'Catch-up vaccines',       'Parent requested review of schedule.'),
(3, 3, 2, '2025-01-20', 'Sick visit',    'Fever and cough',         'Likely viral; no RSV testing needed.'),
(4, 3, 2, '2025-03-15', 'Vaccine visit', 'Routine immunizations',   'Discussed Hib and PCV boosters.'),
(5, 4, 2, '2025-04-01', 'Well visit',    '2-year well child',       'Growth tracking normal.'),
(6, 5, 3, '2025-01-25', 'Vaccine visit', 'MMR and Varicella',       'Provided VIS and answered questions.'),
(7, 6, 3, '2025-02-12', 'Well visit',    '8-year well child',       'Discussed upcoming HPV eligibility.'),
(8, 7, 4, '2025-03-05', 'Vaccine visit', 'Rotavirus dose',          'No contraindications noted.'),
(9, 8, 4, '2025-03-22', 'Sick visit',    'Ear pain',                'No vaccines given.'),
(10,9, 5, '2025-04-10', 'Vaccine visit', 'HPV initiation',          'Guardian hesitant but agreed.');

-- IMMUNIZATION_EVENT (10 rows)
INSERT INTO IMMUNIZATION_EVENT (immunization_event_id, encounter_id, patient_id,
                                vaccine_lot_id, administration_date,
                                administering_staff_id, site_of_administration,
                                route, dose_number, refusal_reason, notes)
VALUES
(1,  1, 1, 2,  '2025-01-10', 1,  'Left thigh',  'IM',   4, NULL,
 'DTaP booster given without issue.'),
(2,  1, 1, 3,  '2025-01-10', 1,  'Right thigh', 'IM',   4, NULL,
 'IPV booster administered.'),
(3,  2, 2, 4,  '2025-02-05', 2,  'Left thigh',  'IM',   3, NULL,
 'Hib booster; mild anxiety, tolerated.'),
(4,  2, 2, 5,  '2025-02-05', 2,  'Right thigh', 'IM',   3, NULL,
 'PCV13 booster.'),
(5,  4, 3, 4,  '2025-03-15', 3,  'Left thigh',  'IM',   3, NULL,
 'Hib dose complete.'),
(6,  5, 4, 1,  '2025-04-01', 4,  'Right thigh', 'IM',   3, NULL,
 'HepB catch-up; guardian counseled on schedule.'),
(7,  6, 5, 6,  '2025-01-25', 5,  'Left arm',    'IM',   1, NULL,
 'MMR first dose; VIS provided.'),
(8,  6, 5, 7,  '2025-01-25', 5,  'Right arm',   'IM',   1, NULL,
 'Varicella first dose.'),
(9,  8, 7, 9,  '2025-03-05', 6,  'Oral',        'ORAL', 2, NULL,
 'Rotavirus second dose.'),
(10,10,9,10, '2025-04-10', 7,  'Left arm',     'IM',   1,
 'Religious exemption previously noted but rescinded',
 'HPV dose 1; documented prior hesitancy.');
""")

conn.commit()
conn.close()



# %%
#print out patient information table to verify data inserted correctly

conn = sqlite3.connect("happy_child_peds.db")
cur = conn.cursor()

cur.execute("SELECT * FROM PATIENT")
rows = cur.fetchall()

for row in rows:
    print(row)

# %%
#use pandas to make it look nice
import pandas as pd

# connect to your database
conn = sqlite3.connect("happy_child_peds.db")

# load patient table into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM patient", conn)

# display the table
print(df)

# %%
#run queries to answer the following questions: 
#1. Give a list of phone numbers of guardians whose children have not yet had the flu vaccine this year so they can be sent a text reminder to come in. 
#2. For #1, find the primary language of the guardian so the text message will be in the right language. 
#3. Note any and all refusals. List the name of the provider as well as the reason for refusal. 
#4. See which clinic has given the most vaccines. 
#5. A parent is requesting a vaccination record for their child's school registration. Please retrieve all vaccines given to Eli Anderson and the date they were each administered. 
#6. A child, Mira Patel, has had an adverse reaction to a vaccine. Get the vaccine name, ID, administration date, lot number, and administering provider. 

# %%
#1. Give a list of phone numbers of guardians whose children have not yet had the flu vaccine this year so they can be sent a text reminder to come in. 
import sqlite3
import pandas as pd

# Connect to  SQLite DB
#flu vaccine_id's are 140','141','150','153'
conn = sqlite3.connect("happy_child_peds.db")

query = """
SELECT DISTINCT
    g.gfirst_name AS guardian_first_name,
    g.glast_name AS guardian_last_name,
    g.phone_number
FROM GUARDIAN g
JOIN PATIENT_GUARDIAN pg 
    ON g.guardian_id = pg.guardian_id
JOIN PATIENT p 
    ON pg.patient_id = p.patient_id
WHERE p.patient_id NOT IN (
        SELECT DISTINCT ie2.patient_id
        FROM IMMUNIZATION_EVENT ie2
        JOIN VACCINE_LOT vl2 ON ie2.vaccine_lot_id = vl2.vaccine_lot_id
        JOIN VACCINE v2 ON vl2.vaccine_id = v2.vaccine_id
        WHERE v2.cvx_code IN ('140','141','150','153')
          AND strftime('%Y', ie2.administration_date) = strftime('%Y','now')
    )
AND g.phone_number IS NOT NULL;
"""

df = pd.read_sql_query(query, conn)

conn.close()

df

# %%
#2. For #1, find the primary language of the guardian so the text message will be in the right language. 
conn = sqlite3.connect("happy_child_peds.db")

query = """SELECT DISTINCT
    g.gfirst_name       AS guardian_first_name,
    g.glast_name        AS guardian_last_name,
    g.phone_number,
    g.primary_language
FROM GUARDIAN g
JOIN PATIENT_GUARDIAN pg 
    ON g.guardian_id = pg.guardian_id
JOIN PATIENT p 
    ON pg.patient_id = p.patient_id
WHERE p.patient_id NOT IN (
        SELECT DISTINCT ie2.patient_id
        FROM IMMUNIZATION_EVENT ie2
        JOIN VACCINE_LOT vl2 
            ON ie2.vaccine_lot_id = vl2.vaccine_lot_id
        JOIN VACCINE v2 
            ON vl2.vaccine_id = v2.vaccine_id
        WHERE v2.cvx_code IN ('140','141','150','153')   -- flu vaccine CVX codes
          AND strftime('%Y', ie2.administration_date) = strftime('%Y','now')
    )
  AND g.phone_number IS NOT NULL;
  """

df = pd.read_sql_query(query, conn)

conn.close()

df

# %%
#3. Note any and all refusals. List the name of the provider as well as the reason for refusal. 
conn = sqlite3.connect("happy_child_peds.db")

query = """SELECT
    p.pfirst_name  AS patient_first_name,
    p.plast_name   AS patient_last_name,
    s.first_name   AS provider_first_name,
    s.last_name    AS provider_last_name,
    v.vaccine_name,
    ie.refusal_reason
FROM IMMUNIZATION_EVENT ie
JOIN PATIENT p
    ON ie.patient_id = p.patient_id
JOIN STAFF s
    ON ie.administering_staff_id = s.staff_id
JOIN VACCINE_LOT vl
    ON ie.vaccine_lot_id = vl.vaccine_lot_id
JOIN VACCINE v
    ON vl.vaccine_id = v.vaccine_id
WHERE ie.refusal_reason IS NOT NULL
  AND ie.refusal_reason <> '';
    """

df = pd.read_sql_query(query, conn)

conn.close()

df

# %%
#4. See which clinic has given the most vaccines. 
conn = sqlite3.connect("happy_child_peds.db")

query ="""
SELECT
    c.clinic_id,
    c.clinic_name,
    COUNT(ie.immunization_event_id) AS vaccine_count
FROM IMMUNIZATION_EVENT ie
JOIN CLINICAL_ENCOUNTER ce
    ON ie.encounter_id = ce.encounter_id
JOIN CLINIC c
    ON ce.clinic_id = c.clinic_id
GROUP BY
    c.clinic_id,
    c.clinic_name
ORDER BY
    vaccine_count DESC;
    """
    
df = pd.read_sql_query(query, conn)

conn.close()

df

# %%
#5. A parent is requesting a vaccination record for their child's school registration. Please retrieve all vaccines given to Eli Anderson and the date they were each administered. 
conn = sqlite3.connect("happy_child_peds.db")

query = """
SELECT
    v.vaccine_name,
    ie.administration_date
FROM PATIENT p
JOIN IMMUNIZATION_EVENT ie
    ON p.patient_id = ie.patient_id
JOIN VACCINE_LOT vl
    ON ie.vaccine_lot_id = vl.vaccine_lot_id
JOIN VACCINE v
    ON vl.vaccine_id = v.vaccine_id
WHERE p.pfirst_name = 'Eli'
  AND p.plast_name = 'Anderson'
ORDER BY ie.administration_date;
"""

df = pd.read_sql_query(query, conn)
conn.close()

df

# %%
#6. A child,Mira Patel , has had an adverse reaction to a vaccine. Get the vaccine name, ID, administration date, lot number, and administering provider. 

conn = sqlite3.connect("happy_child_peds.db")

query = """
SELECT
    v.vaccine_name,
    v.vaccine_id,
    ie.administration_date,
    vl.lot_number,
    s.first_name AS provider_first_name,
    s.last_name  AS provider_last_name
FROM PATIENT p
JOIN IMMUNIZATION_EVENT ie
    ON p.patient_id = ie.patient_id
JOIN VACCINE_LOT vl
    ON ie.vaccine_lot_id = vl.vaccine_lot_id
JOIN VACCINE v
    ON vl.vaccine_id = v.vaccine_id
JOIN STAFF s
    ON ie.administering_staff_id = s.staff_id
WHERE p.pfirst_name = 'Mira'
  AND p.plast_name = 'Patel'
ORDER BY date(ie.administration_date) DESC
LIMIT 1;
"""

df = pd.read_sql_query(query, conn)
conn.close()

print(df)



