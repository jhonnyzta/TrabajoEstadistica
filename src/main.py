from matplotlib import pyplot as plt
from graphics import *
from files import *
from extra import *
import os



def order(data):
    position_data = desv_est_mues(data)
    q1, q2, q3 = kuartil(data)
    dict_return = {'mean': position_data[0], 'std_dev': position_data[1],
                                'quartil': [q1,q2,q3]}
    return dict_return

def data_processed(args):
    new_data = {}
    for country in args.keys():
        new_data[country] = {'urban': {'men': {}, 'women': {}}, 'rural': {'men': {}, 'women': {}}}
        for i in args[country].keys():
            labels = i.split('_')
            datas = args[country][i]
            new_data[country][labels[0]][labels[1]] = order(datas)
            #box_plot(country, new_data[country][labels[0]][labels[1]], args[country][i], i)

    return new_data

archivo = os.path.join(os.path.dirname(__file__), '..', 'data', "imc.csv")

dirgraphs = os.path.join(os.path.dirname(__file__), '..', 'graphics')

data = read_data(archivo)

# Labels
headers = data.pop(0)

data_by_country = create_set_data(data)

processed_data = data_processed(data_by_country)


complement_data = {}
countries = data_by_country.keys()
for i in countries:
    complement_data[i] = complete_data(i)
    data_men = data_by_country[i]['urban_men']
    data_women = data_by_country[i]['urban_women']
    #bar_graph(i, data_men, data_women, 'urban')
    data_men = data_by_country[i]['rural_men']
    data_women = data_by_country[i]['rural_women']
    #bar_graph(i, data_men, data_women, 'rural')
    key_format = {
        "country" : i,
        "men_urban": processed_data[i]['urban']['men'],
        "women_urban": processed_data[i]['urban']['women'],
        "men_rural": processed_data[i]['rural']['men'],
        "women_rural": processed_data[i]['rural']['women'],
    }
    #make_md(key_format)

#global data
global_dic = {}
for i in countries:
    global_dic[i] = {"Men": [], "Women": [], 'Global': []}
    urban_men = data_by_country[i]['urban_men']
    rural_men = data_by_country[i]['urban_men']
    urban_women = data_by_country[i]['urban_women']
    rural_women = data_by_country[i]['urban_women']
    dates = complement_data[i]
    
    for index in zip(urban_men, rural_men, urban_women, rural_women, dates.keys()):
        bmi_men = index[0]*dates[index[4]]['Urban']+index[1]*dates[index[4]]['Rural']
        bmi_women = index[2]*dates[index[4]]['Urban']+index[3]*dates[index[4]]['Rural']
        bmi_global = bmi_men*dates[index[4]]['Men']+bmi_women*dates[index[4]]['Women']
        global_dic[i]['Men'].append(bmi_men)
        global_dic[i]['Women'].append(bmi_women)
        global_dic[i]['Global'].append(bmi_global)

for i in global_dic.keys():
    data1 = global_dic[i]['Men']
    data2 = global_dic[i]['Women']
    bar_graph(i, data1, data2, 'global')
    mean_men = desv_est_mues(data1)[0]
    mean_women = desv_est_mues(data2)[0]
    total_bar_plot(i, ['Men', 'Women'], [mean_men, mean_women], 'means')

groups = {'Andina': [
    'Colombia',
    'Ecuador',
    'Venezuela',
    'Peru',
    'Bolivia'
    ],
    "Sur": [
        "Argentina",
        "Paraguay",
        "Uruguay",
        "Chile"
    ],
    "Amazonas": [
        "Brazil",
        "Guyana",
        "Suriname"
    ]}

groups_compare = {}

for i in groups.keys():
    groups_compare[i] = {'mean': 0,
                         'men': 0,
                         'women': 0,
                         'urban': 0,
                         'rural': 0,
                         'population':0}
    mean, population, urban, rural = 0, 0 , 0, 0
    for j in groups[i].keys():
        population += complement_data[j]['Populati<on']
        