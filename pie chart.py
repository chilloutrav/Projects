import matplotlib.pyplot as plt
data = {"Python":29,
"javascript":26,
"java":21,
"C":17,
"C++":11}
colors = ['orange', 'green','cyan','skyblue','yellow']
highligh = (0,0.2,0,0,0)

nationalities = ['American', 'German', 'French', 'Other']
students = [60,23,21,34]

pairs = zip(students, nationalities)
pairs = sorted(list(pairs))
students, nationalities = zip(*pairs)






plt.pie(list(data.values()), explode=highligh, colors=colors, autopct='%.2f%%', shadow=True, startangle=90,)
plt.axis('equal')
plt.title("Whatever the fuck i am doing")
plt.show()

