# Entradas del usuario
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
tarifa_hora = float(input("Ingrese la tarifa por hora: "))

# Calcular salario bruto
salario_bruto = horas_trabajadas * tarifa_hora

# Calcular descuentos de salud y pensión (4% + 4%)
salud = salario_bruto * 0.04
pension = salario_bruto * 0.04
total_descuentos = salud + pension

# Calcular impuesto a la renta
impuesto_renta = 0

if salario_bruto > 100_000_000:
    impuesto_renta = 0.04 * (salario_bruto - 100_000_000)
elif salario_bruto > 50_000_000:
    impuesto_renta = 0.03 * (salario_bruto - 50_000_000)
elif salario_bruto > 10_000_000:
    impuesto_renta = 0.02 * (salario_bruto - 10_000_000)

# Calcular salario neto
salario_neto = salario_bruto - total_descuentos - impuesto_renta

# Mostrar resultados
print(f"\nSalario bruto: ${salario_bruto:,.2f}")
print(f"Descuento salud: ${salud:,.2f}")
print(f"Descuento pensión: ${pension:,.2f}")
print(f"Impuesto a la renta: ${impuesto_renta:,.2f}")
print(f"Salario neto: ${salario_neto:,.2f}")