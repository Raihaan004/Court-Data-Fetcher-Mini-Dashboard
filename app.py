from flask import Flask, render_template, request
import database
import scraper
import datetime
import os

app = Flask(__name__)

# List of all case types from the provided HTML
all_case_types = [
    'ADMIN.REPORT', 'ARB.A.', 'ARB. A. (COMM.)', 'ARB.P.', 'BAIL APPLN.', 'CA', 
    'CA (COMM.IPD-CR)', 'C.A.(COMM.IPD-GI)', 'C.A.(COMM.IPD-PAT)', 'C.A.(COMM.IPD-PV)', 
    'C.A.(COMM.IPD-TM)', 'CAVEAT(CO.)', 'CC(ARB.)', 'CCP(CO.)', 'CCP(REF)', 'CEAC', 
    'CEAR', 'CHAT.A.C.', 'CHAT.A.REF', 'CMI', 'CM(M)', 'CM(M)-IPD', 'C.O.', 'CO.APP.', 
    'CO.APPL.(C)', 'CO.APPL.(M)', 'CO.A(SB)', 'C.O.(COMM.IPD-CR)', 'C.O.(COMM.IPD-GI)', 
    'C.O.(COMM.IPD-PAT)', 'C.O. (COMM.IPD-TM)', 'CO.EX.', 'CONT.APP.(C)', 'CONT.CAS(C)', 
    'CONT.CAS.(CRL)', 'CO.PET.', 'C.REF.(O)', 'CRL.A.', 'CRL.L.P.', 'CRL.M.C.', 
    'CRL.M.(CO.)', 'CRL.M.I.', 'CRL.O.', 'CRL.O.(CO.)', 'CRL.REF.', 'CRL.REV.P.', 
    'CRL.REV.P.(MAT.)', 'CRL.REV.P.(NDPS)', 'CRL.REV.P.(NI)', 'C.R.P.', 'CRP-IPD', 
    'C.RULE', 'CS(COMM)', 'CS(OS)', 'CS(OS) GP', 'CUSAA', 'CUS.A.C.', 'CUS.A.R.', 
    'CUSTOM A.', 'DEATH SENTENCE REF.', 'DEMO', 'EDC', 'EDR', 'EFA(COMM)', 'EFA(OS)', 
    'EFA(OS)  (COMM)', 'EFA(OS)(IPD)', 'EL.PET.', 'ETR', 'EX.F.A.', 'EX.P.', 'EX.S.A.', 
    'FAO', 'FAO (COMM)', 'FAO-IPD', 'FAO(OS)', 'FAO(OS) (COMM)', 'FAO(OS)(IPD)', 
    'GCAC', 'GCAR', 'GTA', 'GTC', 'GTR', 'I.A.', 'I.P.A.', 'ITA', 'ITC', 'ITR', 'ITSA', 
    'LA.APP.', 'LPA', 'MAC.APP.', 'MAT.', 'MAT.APP.', 'MAT.APP.(F.C.)', 'MAT.CASE', 
    'MAT.REF.', 'MISC. APPEAL(PMLA)', 'OA', 'OCJA', 'O.M.P.', 'O.M.P. (COMM)', 
    'OMP (CONT.)', 'O.M.P. (E)', 'O.M.P. (E) (COMM.)', 'O.M.P.(EFA)(COMM.)', 
    'OMP (ENF.) (COMM.)', 'O.M.P.(I)', 'O.M.P.(I) (COMM.)', 'O.M.P. (J) (COMM.)', 
    'O.M.P. (MISC.)', 'O.M.P.(MISC.)(COMM.)', 'O.M.P.(T)', 'O.M.P. (T) (COMM.)', 
    'O.REF.', 'RC.REV.', 'RC.S.A.', 'RERA APPEAL', 'REVIEW PET.', 'RFA', 'RFA(COMM)', 
    'RFA-IPD', 'RFA(OS)', 'RFA(OS)(COMM)', 'RF(OS)(IPD)', 'RSA', 'SCA', 'SDR', 'SERTA', 
    'ST.APPL.', 'STC', 'ST.REF.', 'SUR.T.REF.', 'TEST.CAS.', 'TR.P.(C)', 'TR.P.(C.)', 
    'TR.P.(CRL.)', 'VAT APPEAL', 'W.P.(C)', 'W.P.(C)-IPD', 'WP(C)(IPD)', 'W.P.(CRL)', 
    'WTA', 'WTC', 'WTR'
]


def init_db():
    """Initializes the database and creates the table if it doesn't exist."""
    if not os.path.exists('queries.db'):
        conn = database.create_connection()
        if conn is not None:
            try:
                database.create_table(conn)
                print("Database 'queries.db' created and table initialized.")
            finally:
                conn.close()
        else:
            print("Error! Could not create the database connection.")

# Call the init_db function once when the app starts
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        case_year = request.form['case_year']

        data = scraper.fetch_case_data(case_type, case_number, case_year)
        
        conn = None
        try:
            conn = database.create_connection()
            if conn:
                query_details = (case_type, case_number, case_year, datetime.datetime.now(), str(data))
                database.log_query(conn, query_details)
        except Exception as e:
            print(f"Database logging failed: {e}")
        finally:
            if conn:
                conn.close()

        if "error" in data:
            return render_template('index.html', error=data["error"], case_types=all_case_types)

        return render_template('results.html', data=data)
    
    # For GET request, just show the form with the case types
    return render_template('index.html', case_types=all_case_types)

if __name__ == '__main__':
    app.run(debug=True)