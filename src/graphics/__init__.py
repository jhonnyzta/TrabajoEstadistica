from matplotlib import pyplot as plt
import os

dirgraphs = os.path.join(os.path.dirname(__file__), '../..', 'graphics')

def median_data(args):
    args.sort()
    lenght = len(args)
    position = lenght // 2
    if lenght % 2 == 0:
        median = (args[position - 1] + args[position]) / 2
        return median
    median = args[position]
    return median

def desv_est_mues(args):
    sum_values = 0
    sum_square_values = 0
    n = len(args) - 1
    for i in args:
        sum_values += i
        sum_square_values += i ** 2
    mean = sum_values / (n+1)
    variance = sum_square_values / n -2 * sum_values * mean / n + (n+1) * mean**2 / n
    desv_esta = variance**0.5
    return mean, desv_esta

def kuartil(args):
    args.sort()
    q1p = int(len(args)*0.25)
    q3p = int(len(args)*0.75)
    Q1 = args[q1p]
    Q2 = median_data(args)
    Q3 = args[q3p]
    return Q1, Q2, Q3

def bar_graph(label, args, args2, etiqueta):
    directory = f'{dirgraphs}/{label}'
    if not os.path.exists(directory):
        os.makedirs(directory)
    rango = list(range(1,len(args)+1))
    min_value = min(min(args), min(args2))
    max_value = max(max(args), max(args2))
    
    plt.bar(rango, args2, color = 'orange', label='Mujeres')
    plt.bar(rango, args, color='blue', label='Hombres', alpha=0.8)
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.xlabel('Conjunto de datos')
    plt.ylabel('Valor')
    plt.title('Gráfico de barras')
    plt.ylim(min_value - 2, max_value+1)
    plt.savefig(f'{directory}/barras_{etiqueta}.png',bbox_inches='tight', dpi=150)
    plt.clf()

def total_bar_plot(label, labels, data, name):
    directory = f'{dirgraphs}/{label}'
    plt.bar(labels, data)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{directory}/graph_{name}.png')
    plt.clf()

def box_plot(label, dic_values, data, gender):
    directory = f'{dirgraphs}/{label}'
    if not os.path.exists(directory):
        os.makedirs(directory)
    q1 = dic_values['quartil'][0]
    q3 = dic_values['quartil'][2]
    iqr = q3 - q1
    lower_whisker = q1 - 1.5 * iqr
    uppper_whisker = q3 + 1.5 * iqr
    plt.boxplot([data], whis=[lower_whisker, uppper_whisker], showmeans=True)
    plt.title('Diagrama de Bigotes con Cuartiles')
    plt.ylabel('Valores')
    plt.xlabel('Datos')
    plt.savefig(f'{directory}/bigotes_{gender}.png',bbox_inches='tight', dpi=150)
    plt.clf()
    return True

def bar_sex_plot(label, data_mean):
    directory = f'{dirgraphs}/{label}'
    labels = ['Hombres', 'Mujeres']
    plt.bar(labels, data_mean)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{directory}/bar_sex.png')
    plt.clf()
