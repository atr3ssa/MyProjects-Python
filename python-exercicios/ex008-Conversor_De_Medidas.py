print("===== Conversor de Medidas =====")
dist_metros= float(input("Distância em METROS: "))
print("A medida de {} corresponde a: \n {:.0f} km \n {:.0f} hm \n {:.0f} dam \n {:.0f} dm \n {:.0f} cm \n {:.0f} mm".format(dist_metros,(dist_metros/1000),(dist_metros/100), (dist_metros/10), (dist_metros*10), (dist_metros*100), (dist_metros*1000)))
