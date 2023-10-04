def main():

    f = open('temps.txt')
    
    temps = []
    for line in f:
        line = line.strip()
        line = line.split(' ')
        d = {'temp':line[0],"unit":line[1]}
        temps.append(d)

    for temp in temps:
        print("Temperature:{temp} | Unit:{unit}".format(**temp))
       # print("Temperature:{} | Unit:{}".format(temp['temp']))

main()