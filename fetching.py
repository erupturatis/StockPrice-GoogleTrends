
def fetch_google_trends(stock_name:str)->list:
    request = "https://trends.google.com/trends/api/widgetdata/multiline?hl=en-US&tz=-120&req=%7B%22time%22:%222021-12-20+2022-03-20%22,%22resolution%22:%22DAY%22,%22locale%22:%22en-US%22,%22comparisonItem%22:%5B%7B%22geo%22:%7B%22country%22:%22US%22%7D,%22complexKeywordsRestriction%22:%7B%22keyword%22:%5B%7B%22type%22:%22ENTITY%22,%22value%22:%22%2Fm%2F02vx4%22%7D%5D%7D%7D%5D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:0%7D%7D&token=APP6_UEAAAAAYjjAwhEUe3P3oAkv_aKDJ9F922Inv3Ju&tz=-120"
    pass

def fetch_stocks(stock_name:str)->list:
    pass


fetch_google_trends("football")