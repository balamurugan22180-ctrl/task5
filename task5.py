rain_cloudy = 30
rain_clear = 10
no_rain_cloudy = 20
no_rain_clear = 40

total = rain_cloudy + rain_clear + no_rain_cloudy + no_rain_clear
rain_days = rain_cloudy + rain_clear
no_rain_days = no_rain_cloudy + no_rain_clear

print("Dataset (number of days)")
print(f"{'':<10}{'Cloudy':>8}{'Clear':>8}")
print(f"{'Rain':<10}{rain_cloudy:>8}{rain_clear:>8}")
print(f"{'Not Rain':<10}{no_rain_cloudy:>8}{no_rain_clear:>8}")
print("Total days:", total)
print()

p_rain = rain_days / total
p_no_rain = no_rain_days / total

print("Prior probabilities")
print(f"P(Rain)     = {rain_days}/{total} = {p_rain:.4f}")
print(f"P(Not Rain) = {no_rain_days}/{total} = {p_no_rain:.4f}")
print()

p_cloudy_given_rain = rain_cloudy / rain_days
p_cloudy_given_no_rain = no_rain_cloudy / no_rain_days

print("Conditional probabilities")
print(f"P(Cloudy | Rain)     = {rain_cloudy}/{rain_days} = {p_cloudy_given_rain:.4f}")
print(f"P(Cloudy | Not Rain) = {no_rain_cloudy}/{no_rain_days} = {p_cloudy_given_no_rain:.4f}")
print()

p_cloudy = p_cloudy_given_rain * p_rain + p_cloudy_given_no_rain * p_no_rain

print("Evidence")
print(f"P(Cloudy) = {p_cloudy_given_rain:.4f} * {p_rain:.4f} + {p_cloudy_given_no_rain:.4f} * {p_no_rain:.4f} = {p_cloudy:.4f}")
print()

p_rain_given_cloudy = (p_cloudy_given_rain * p_rain) / p_cloudy
p_no_rain_given_cloudy = (p_cloudy_given_no_rain * p_no_rain) / p_cloudy

print("Bayes' Theorem")
print(f"P(Rain | Cloudy)     = {p_cloudy_given_rain:.4f} * {p_rain:.4f} / {p_cloudy:.4f} = {p_rain_given_cloudy:.4f}")
print(f"P(Not Rain | Cloudy) = {p_cloudy_given_no_rain:.4f} * {p_no_rain:.4f} / {p_cloudy:.4f} = {p_no_rain_given_cloudy:.4f}")
print()

print("Comparison")
if p_rain_given_cloudy > p_no_rain_given_cloudy:
    prediction = "Rain"
    print(f"{p_rain_given_cloudy:.4f} > {p_no_rain_given_cloudy:.4f}")
else:
    prediction = "Not Rain"
    print(f"{p_no_rain_given_cloudy:.4f} >= {p_rain_given_cloudy:.4f}")

print()
print("Predicted weather for a cloudy day:", prediction)