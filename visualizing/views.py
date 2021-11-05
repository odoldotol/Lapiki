from django.shortcuts import render

import matplotlib.pyplot as plt
plt.switch_backend('Agg')


def save_main_piechart(raitio, labels, id, nameing):
    try:
        explode=[]
        for i in raitio:
            explode = explode + [0.07]
        plt.pie(raitio, labels=labels, autopct='%.2f%%', pctdistance=1.2, labeldistance=0.5, startangle=90, textprops={'color':"w"}, counterclock=False, explode=explode)
        plt.savefig(f'./static/img/visualizing/{id}_main_{nameing}.png', dpi=200, bbox_inches='tight', facecolor='#000000')
        plt.clf()
    except:
        return False
    return True