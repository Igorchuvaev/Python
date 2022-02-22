import json

profit_dict = {}
average_profit = {}
companies = 0
profits = 0
with open("unit7.txt", encoding="utf-8") as unit7_file:
    for item in unit7_file:
        company_info = item.split()
        # print(company_info)
        profit_info = int(company_info[2]) - int(company_info[3])
        # print(profit_info)
        profit_dict[company_info[0]] = profit_info
        # print(profit_info)
        if profit_info >= 0:
            companies += 1
            profits += profit_info
            # print(companies,profits)
average_profit["profit"] = profits/companies
# print(profit_dict)
# print(average_profit)
with open("unit7.json", "w") as info_json:
    json.dump([profit_dict, average_profit], info_json)


