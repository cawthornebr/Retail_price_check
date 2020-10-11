from pandas import DataFrame
import pandas as pd

def page_data(url_list):

    y = url_list.split('mainEntity')

    list1 = y[1].split('@type":"Product')

    #get ratings
    ratings = []

    for i in range(0,len(list1)):

        newsss = list1[i].split('\n')

        for i in newsss:

            i.strip()

            if "ratingValue" in i:

                strip_string = (i.strip().replace("'","").replace("\"",""))

                if len(strip_string) < 25:

                    ratings.append(strip_string[13:-1])
    
    #get review count
    review_count = []

    for i in range(0,len(list1)):

        newsss = list1[i].split('\n')

        for i in newsss:

            i.strip()

            if "reviewCount" in i:

                strip_string = (i.strip().replace("'","").replace("\"",""))

                if len(strip_string) < 20:

                    review_count.append(strip_string[13:-1])
    
    #get best rating
    bestRating = []

    for i in range(0,len(list1)):

        newsss = list1[i].split('\n')

        for i in newsss:

            i.strip()

            if "bestRating" in i:

                strip_string = (i.strip().replace("'","").replace("\"",""))

                if len(strip_string) < 15:

                    bestRating.append(strip_string[12:-1])
    
    #get worst rating
    worstRating = []

    for i in range(0,len(list1)):

        newsss = list1[i].split('\n')

        for i in newsss:

            i.strip()

            if "worstRating" in i:

                strip_string = (i.strip().replace("'","").replace("\"",""))

                if len(strip_string) < 15:

                    worstRating.append(strip_string[13:])

    #get sku
    sku = []
    for i in range(0,len(list1)):
        newsss = list1[i].split('\n')
        for i in newsss:
            i.strip()
            if "sku" in i:
                strip_string = (i.strip().replace("'","").replace("\"",""))
                if len(strip_string) < 20:
                    sku.append(strip_string[5:-1])

    #get brand name
    brand = []

    for i in range(0,len(list1)):

        newsss = list1[i].split('\n')

        for i in newsss:

            i.strip()

            if "brand" in i:

                strip_string = (i.strip().replace("'","").replace("\"",""))

                if len(strip_string) < 30:

                    brand.append(strip_string[7:])

    #get price
    price = []

    for i in range(0,len(list1)):

        newsss = list1[i].split('\n')

        for i in newsss:

            i.strip()

            if "price" in i:

                strip_string = (i.strip().replace("'","").replace("\"",""))

                if len(strip_string) < 15:
                    
                    price.append(float(strip_string[6:-1]))
    
    # put lists in df
    df = DataFrame(list(zip(price, brand,sku,worstRating,bestRating,review_count,ratings)),
            columns = ['price','brand','sku','worst_rating','best_rating','review_count','avg_ratings'])
    
    pd.options.display.float_format = '${0:,.2f}'.format

    df = df.sort_values(by=['brand'])
    
    return(df)