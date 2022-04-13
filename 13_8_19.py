kolvo_biletov = int(input("Сколько вы хотите приобрести билетов: "))
summa_za_bilety = 0

for i in range(kolvo_biletov):
  age = int(input(f"Сообщите пожалуйста возраст обладателя {i+1}-го билета: "))
  
  if 0 <= age < 18:
    continue
  elif 18 <= age < 25:
    summa_za_bilety += 990
  elif age > 25:
    summa_za_bilety += 1390
  
summa_k_oplate = summa_za_bilety

if kolvo_biletov >= 3:
  summa_k_oplate = int(summa_za_bilety - summa_za_bilety*0.1)
print (f"Сумма к оплате за все билеты составит: {summa_k_oplate} руб.")