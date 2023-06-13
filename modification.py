import pandas as pd
import tabula


def countrywise(pdfs):
    countrywise_dicts = []
    pdf_path = "bhadra-2079.pdf"
    df = tabula.read_pdf(pdf_path, pages = 'all')
   
    month = pdfs.split('-')[0].title()
    year = pdfs.split('-')[-1]
    
    serial_number = [s for s in (df[0]['Unnamed: 0'][1:]).iloc[1:]]
    country = [s for s in (df[0]['Unnamed: 1'][1:]).iloc[1:]]
    recruiting_agency = [t.split() for t in (df[0]['Unnamed: 2'][2:]).iloc[0:]]
    countrywise = [c.split() for c in (df[0][f'Countrywise Labour Approval for {month} {year}'][2:]).iloc[0:]]
    
    try:
        total_without_reentry = [t.split() for t in (df[0]['Unnamed: 6'][2:]).iloc[0:]]
        total_with_reentry = [t.split() for t in (df[0]['Unnamed: 5'][2:]).iloc[0:]]
    except Exception as e:
        total_without_reentry = [t.split() for t in (df[0]['Unnamed: 5'][2:]).iloc[0:]]
        total_with_reentry = [t.split() for t in (df[0]['Unnamed: 4'][2:]).iloc[0:]]
        

    datas = {
        'Countrywise Labour Approval for Bhadra 2079': {
            'S.N': serial_number,
            'Country': country,
            'Recruiting Agency': {
                'Male': [male[0] for male in recruiting_agency],
                'FeMale': [female[1] for female in recruiting_agency],
                'Total': [total[2] for total in recruiting_agency],
            },
            'Individual-New': {
                'Male': [male[0] for male in countrywise],
                'Female': [female[1] for female in countrywise],
                'Total': [total[2] for total in countrywise],
            },
            'G-to-G': {
                'Male': [male[3] for male in countrywise],
                'Female': [female[4] for female in countrywise],
                'Total': [total[5] for total in countrywise],
            },
            'Individual-ReEntry': {
            'Male': [male[6] for male in countrywise],  
            'Female': [female[7] for female in countrywise],  
            'Total': [total[8] for total in countrywise],  
            },
            'Total with ReEntry': {
            'Male': [male[0] for male in total_with_reentry],  
            'Female': [female[1] for female in total_with_reentry],  
            'Total': [total[2] for total in total_with_reentry],  
            },
            'Total without ReEntry': {
            'Male': [male[0] for male in total_without_reentry],  
            'Female': [female[1] for female in total_without_reentry],  
            'Total': [total[2] for total in total_without_reentry],  
            },
        }
    }
    countrywise_dicts.append(datas)
    return countrywise_dicts

pdf_names = 'bhadra-2079'
df = pd.DataFrame(countrywise(pdf_names))
df.to_json(f'{pdf_names}.csv', indent = 4)