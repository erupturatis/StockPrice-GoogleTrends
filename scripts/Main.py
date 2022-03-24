from webscrapping.google_trends import GoogleTrendsRequest

def calculate_correlation()->int:
    pass


def main():
    # does correlation for fixed variables
    trends_requester = GoogleTrendsRequest()
    trends_requester.test_request()

if __name__ == "__main__":
    main()