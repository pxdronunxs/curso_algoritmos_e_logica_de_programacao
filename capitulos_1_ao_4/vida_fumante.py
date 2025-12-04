cigarros_por_dia = int(input("Informe a quantidade de baseados fumados por dia: "))
anos_que_fuma = float(input("Há quantos anos é maconheiro: "))
dias = anos_que_fuma * 365
total_cigarros = dias * cigarros_por_dia
total_minutos = total_cigarros * 10
total_horas = total_minutos / 60
total_dias = total_horas / 24

print(f"O total de dias perdidos é: {total_dias:.2f}")
