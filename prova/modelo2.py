import os,matplotlib.pyplot,requests
import pandas as pd

def baixar_arquivo(url,endereco):
    response = requests.get(url, stream=True)
    if response.status_code == requests.codes.OK:
        with open(endereco+os.path.basename(url.split("?")[0]), 'wb') as novo_arquivo:
                for parte in response.iter_content(chunk_size=256):
                    novo_arquivo.write(parte)
    else:
        response.raise_for_status()

def delta(x):
    return int(x[x.size-1]) - int(x[x.size-2])

def media(x):
    return int(x[len(x)-1]) - int(x[len(x)-2]) / 2

def abrirArquivo(path):
    # with open(path,'r') as confirmed:
    #     leitor=csv.DictReader(confirmed,delimiter=',')
    #     for coluna in leitor:
    #         if coluna['Country/Region'] == 'Brazil':
    #             coluna3 = coluna
    # x=[]
    # for e in coluna3.values():
    #     x.append(e)
    # return x
    leitor = pd.read_csv(path)
    leitor = leitor.loc[leitor['Country/Region'] == 'Brazil']
    leitor.drop('Province/State', inplace=True, axis=1)
    leitor.drop('Country/Region', inplace=True, axis=1)
    leitor.drop('Lat', inplace=True, axis=1)
    leitor.drop('Long', inplace=True, axis=1)
    return leitor.to_numpy()

def kUm1(x1, x3):
    return k21 * x3 - (k11+k31)*x1

def kDois1(x1,x3, k1):
    return k21 * (x3+k1/2) - (k11+k31)*(x1+k1/2)

def kTres1(x1, x3, k2):
    return k21 * (x3+k2/2) - (k11+k31)*(x1+k2/2)

def kQuatro1(x1, x3, k3):
    return k21 * (x3+k3) - (k11+k31)*(x1+k3)

def kUm2(x1):
    return k11 * x1

def kDois2(x1, k1):
    return k11 * (x1+k1/2)

def kTres2(x1, k2):
    return k11 * (x1+k2/2)

def kQuatro2(x1, k3):
    return k11 * (x1+k3)

def kUm3(x1,x3):
    return -1 * k21 * x3 + k31 * x1

def kDois3(x1,x3, k1):
    return -1 * k21 * (x3+k1/2) + k31 * (x1+k1/2)

def kTres3(x1,x3, k2):
    return -1 * k21 * (x3+k2/2) + k31 * (x1+k2/2)

def kQuatro3(x1,x3, k3):
    return -1 * k21 * (x3+k3) + k31 * (x1+k3)

url=["https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"]

for i in range(0,3):
    baixar_arquivo(url[i],'dados/')
    
dados_confirmed = 'dados/time_series_covid19_confirmed_global.csv'
dados_deaths= 'dados/time_series_covid19_deaths_global.csv'
dados_recovered= 'dados/time_series_covid19_recovered_global.csv'

brasil_confirmed = abrirArquivo(dados_confirmed)
brasil_deaths = abrirArquivo(dados_deaths)
brasil_recovered = abrirArquivo(dados_recovered)

casos = 209000000 * 0.7 - brasil_confirmed.item((0,brasil_confirmed.size-1))

k31=brasil_confirmed.mean()
k11=brasil_deaths.mean()
k21=brasil_recovered.mean()

#k31 = delta(brasil_confirmed) / casos
#k11 = media(brasil_deaths)
#k21 = media(brasil_recovered)

h = 1
t = 0

rk11 = 0
rk12 = 0
rk13 = 0

rk21 = 0
rk22 = 0
rk23 = 0

rk31 = 0
rk32 = 0
rk33 = 0

rk41 = 0
rk42 = 0
rk43 = 0

x1= brasil_confirmed.item(brasil_confirmed.size-1)
x2= brasil_deaths.item(brasil_deaths.size-1)
x3= casos

auxX1 = 0
auxX2 = 0
auxX3 = 0
erro = 0

matplotlib.pyplot.ioff()
graphT = []
graphX1 = []
graphX2 = []

while t < 70:
    auxX1 = x1
    auxX2 = x2
    auxX3 = x3

    rk11 = h*kUm1(x1,x3)
    rk21 = h*kUm2(x1)
    rk31 = h*kUm3(x1,x3)

    rk12 = h*kDois1(x1,x3, rk11)
    rk22 = h*kDois2(x1, rk21)
    rk32 = h*kDois3(x1,x3, rk31)

    rk13 = h*kTres1(x1,x3, rk12)
    rk23 = h*kTres2(x1, rk22)
    rk33 = h*kTres3(x1,x3, rk32)

    rk14 = h*kQuatro1(x1,x3, rk13)
    rk24 = h*kQuatro2(x1, rk23)
    rk34 = h*kQuatro3(x1,x3, rk33)

    print(f't:{t} || C:{x1} || M:{x2}')

    graphT.append(t)
    graphX1.append(x1)
    graphX2.append(x2)

    x1 = x1 + (rk11 + 2 * rk12 + 2 * rk13 + rk14)/6
    x2 = x2 + (rk21 + 2 * rk22 + 2 * rk23 + rk24)/6
    x3 = x3 + (rk31 + 2 * rk32 + 2 * rk33 + rk34)/6

    erro = (x1 - auxX1) / auxX1 + (x2 - auxX2) / auxX2 + (x3 - auxX3) / auxX3
    t = t + h
    

matplotlib.pyplot.plot(graphT,graphX1,label='C(t)')
matplotlib.pyplot.plot(graphT,graphX2,label='M(t)')
matplotlib.pyplot.xlabel('tempo (t)')
matplotlib.pyplot.ylabel('valores (C(t) M(t)')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()