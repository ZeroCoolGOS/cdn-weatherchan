# function
def displayPage2():
    # ===================== Screen 2 =====================
    # text forecast for 5 days - page 1 of 3
    #print(time.strftime("%H:%M.") + prog + ver + ".WEATHER_PAGE-display page " + str(PageNum))   

    # pull text forecasts from env_canada
    wsum_day1 = textwrap.wrap(ec_en_wpg.conditions["text_summary"]["value"].upper(), 35)
    wsum_day2 = textwrap.wrap(ec_en_wpg.daily_forecasts[1]["period"].upper() + ".." + ec_en_wpg.daily_forecasts[1]["text_summary"].upper(), 35)
    wsum_day3 = textwrap.wrap(ec_en_wpg.daily_forecasts[2]["period"].upper() + ".." + ec_en_wpg.daily_forecasts[2]["text_summary"].upper(), 35)
    wsum_day4 = textwrap.wrap(ec_en_wpg.daily_forecasts[3]["period"].upper() + ".." + ec_en_wpg.daily_forecasts[3]["text_summary"].upper(), 35)    
    wsum_day5 = textwrap.wrap(ec_en_wpg.daily_forecasts[4]["period"].upper() + ".." + ec_en_wpg.daily_forecasts[4]["text_summary"].upper(), 35)
    wsum_day6 = textwrap.wrap(ec_en_wpg.daily_forecasts[5]["period"].upper() + ".." + ec_en_wpg.daily_forecasts[5]["text_summary"].upper(), 35)   
    
    # build text_forecast string
    global text_forecast
    text_forecast = wsum_day1 + linebreak + wsum_day2 + linebreak + wsum_day3 + linebreak + wsum_day4 + linebreak + wsum_day5 + linebreak + wsum_day6

    # create 8 lines of text
    s1 = "WINNIPEG CITY FORECAST 2".center(35," ")
    s2 = (text_forecast[0]).center(35," ") if len(text_forecast) >= 1 else " "
    s3 = (text_forecast[1]).center(35," ") if len(text_forecast) >= 2 else " "
    s4 = (text_forecast[2]).center(35," ") if len(text_forecast) >= 3 else " "
    s5 = (text_forecast[3]).center(35," ") if len(text_forecast) >= 4 else " "
    s6 = (text_forecast[4]).center(35," ") if len(text_forecast) >= 5 else " "
    s7 = (text_forecast[5]).center(35," ") if len(text_forecast) >= 6 else " "
    s8 = (text_forecast[6]).center(35," ") if len(text_forecast) >= 7 else " "