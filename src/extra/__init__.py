import os
dir_file = os.path.join(os.path.dirname(__file__), '../..', 'data')

def read_data(file):
    with open(file, 'r') as f:
        lineas = f.readlines()
    data = [i.strip().split() for i in lineas]
    data = [[x if x.isalpha() else float(x) for x in row] for row in data]
    return data

def complete_data(arg):
    file_open = f"{dir_file}/{arg}.csv"
    data = read_data(file_open)
    data.pop(0)
    dic_data = {}
    for row in data:
        men_porc = round(row[1]/row[3],3)
        women_porc = round(row[2]/row[3],3)
        rural_porc = round(row[4]/100,3)
        urban_porc = round(1-rural_porc,3)
        total_population = row[3]
        dic_data[row[0]] = {
            "Men": men_porc,
            "Women": women_porc,
            "Rural": rural_porc,
            "Urban": urban_porc,
            "Population": total_population
        }
    return dic_data

def create_set_data(data):
    data_by_country = {}
    for row in data:
        country = row[0]
        gender = row[1]
        urban = row[3]
        rural = row[4]

        if country not in data_by_country:
            data_by_country[country] = {'urban_men': [], 'urban_women': [],
                                    'rural_men': [], 'rural_women': []}

        if gender == 'Men':
            data_by_country[country]['urban_men'].append(urban)
            data_by_country[country]['rural_men'].append(rural)
        elif gender == 'Women':
            data_by_country[country]['urban_women'].append(urban)
            data_by_country[country]['rural_women'].append(rural)
    return data_by_country

