holidays = ['New Year', 'Republic Day', 'Holi', 'God Friday', 'Independence Day', 'Diwali', 'Eid']
holidays[4] = "Good Friday"
holidays.append("Eid")
holidays.append("Makar Sankranti")
holidays.append("Gandhi Jayanti")
holidays.append("Christmas")
holidays.remove("Eid")
holidays.remove("Independence Day")
holidays.clear()
print(holidays)
