import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from Tools.scripts.generate_re_casefix import alpha
from fontTools.diff import color

# создание данных
# x = np.linspace(1, 50, 50)
# np.random.seed(1)
# y = np.random.randint(0, 20, 50)

# plt.plot(x, y)
# plt.plot(x + 10, y + 10)
#
# plt.legend(["Legend1", "Legend2"],
#            loc="upper center",  # 1) изменение положения (default="best")
#            fontsize=12,  # 2) рамера шрифта
#            labelspacing=6.7,  # 3) изменение расстояния между легендами
#            ncol=2 # 4) изменение кол-ва столбцов в легенде
#            )
# plt.show()
# plt.close()

# 5) единая легенда для все подзаголовках
# figure, axes = plt.subplots(1, 2)
#
# axes[0].plot(x, y,  label="Линия 1")
# axes[1].plot(x + 5, y + 5, label="Линия 2")
#
# handles, labels = [], []
# for ax in axes:
#     h, l = ax.get_legend_handles_labels()
#     handles += h
#     labels  += l
#
# figure.legend(handles, labels, loc="upper center")
#
# plt.show()

# 6) Как вручную добавить легенду с цветной рамкой на фигуру Matplotlib?
# figure, axes = plt.subplots()
# axes.plot(x, y)
# axes.plot(x * 2, y * 2)
#
# red_patch = mpatches.Patch(color="blue", label="Группа А")
# blue_patch = mpatches.Patch(color="black", label="Группа Б")
#
# figure.legend(
#     handles=[red_patch, blue_patch],
#     edgecolor="green",
#     bbox_to_anchor=(0.9, 0.88), # 7) меняем расположение легенды
#     frameon=False # 8) Удаление границы
# )
#
# plt.show()


# ПРО ЛИНИИ

# 1 Горизонтальная линия
# plt.axhline(y = 0.5, color = 'red')
# plt.show()

# 2 Разные горизонтальные линии
# plt.axhline(y=0.8, color="red", linestyle="-",  linewidth=2)
# plt.axhline(y=0.4, color="green", linestyle="--", linewidth=1.5)
# plt.axhline(y=0.2, color="black", linestyle=":",  linewidth=3)
# plt.show()

# 3 Вертикальная линия
# plt.axvline(x=10, color="red", linestyle="-")
# plt.show()

# 4 Разные вертикальные линии
# plt.axvline(x=3, color="green",  linestyle="--", linewidth=1.5)
# plt.axvline(x=5, color="blue",   linestyle=":",  linewidth=3)
# plt.axvline(x=7, color="purple", linestyle="-.", linewidth=1)
# plt.show()

# 5 Изменить непрозрачность строки
# plt.axhline(y=1, color="red", linestyle="-", alpha=0.3)
# plt.axhline(y=2, color="red", linestyle="-", alpha=1.0)
# plt.show()

# 6 Изменить толщину линии
# plt.axhline(y=0.5, color="red", linewidth=5)
# plt.axvline(x=5,   color="blue", linewidth=10)
# plt.show()

# 7 Заливка между линиями
# plt.axhline(y=0.5, color="red", linestyle="-")
# plt.axhline(y=-0.5, color="green", linestyle="-")
# plt.axhspan(-0.5, 0.5, color="yellow")
# plt.show()

# ПРО ГИСТОГРАММЫ

# 1 Горизонтальная гистограмма
# dataset = pd.read_csv("data/housing_market_dataset.csv")
# type_counts = dataset["Тип здания"].value_counts()
# plt.barh(type_counts.index, type_counts.values)
# plt.show()

# 2 Отобразить значение каждого столбца
# dataset = pd.read_csv("data/housing_market_dataset.csv")
# type_counts = dataset["Тип здания"].value_counts()
# bars = plt.bar(type_counts.index, type_counts.values)
# plt.bar_label(bars)
# plt.show()

# 3 Аннотировать столбцы
# dataset = pd.read_csv("data/housing_market_dataset.csv")
# type_counts = dataset["Тип здания"].value_counts()
#
# figure, axes = plt.subplots()
# bars = axes.bar(type_counts.index, type_counts.values)
#
# for bar in bars:
#     height = bar.get_height()
#     axes.annotate(
#         f"{height}",
#         xy=(bar.get_x() + bar.get_width() / 2, height),
#         xytext=(0, 2),
#         textcoords="offset points",
#         fontsize=10,
#         ha="center",
#         va="bottom",
#     )
# plt.show()

# 4 Аннотирование сгруппированных столбцов
# dataset = pd.read_csv("data/housing_market_dataset.csv")
# cross_table = pd.crosstab(dataset["Тип здания"], dataset["Класс жилья"])
#
# axe = cross_table.plot.bar(figsize=(15, 5), ylabel="Количество", rot=0)
# for container in axe.containers:
#     axe.bar_label(container, padding=2, fontsize=8)
#
# axe.legend(title="Класс жилья")
# plt.show()

# 5 Столбчатая диаграмма по убыванию
# dataset = pd.read_csv("data/housing_market_dataset.csv")
# house_class = (dataset["Класс жилья"]
#                .value_counts()
#                .sort_values(ascending=False))
# house_class.plot.bar(figsize=(8, 5), rot=0, ylabel="Количество")
# plt.show()

# ТОЧЕЧНЫЕ ДИАГРАММЫ
# 1 Добавить легенду к точечной диаграмме
# hours_study = np.array([0, 1, 1, 2, 4, 5, 6, 8, 10, 12, 24])
# grades = np.array([55, 60, 63, 66, 70, 86, 87, 89, 90, 98, 100])
#
# plt.scatter(hours_study, grades, label="Study")
# plt.xlabel("Время учения")
# plt.ylabel("Баллы")
# plt.legend()
# plt.show()

# 2 Соединить точки рассеивания
# hours_study = np.array([0, 1, 1, 2, 4, 5, 6, 8, 10, 12, 24])
# grades = np.array([55, 60, 63, 66, 70, 86, 87, 89, 90, 98, 100])
#
# plt.scatter(hours_study, grades, label="Study")
# plt.plot(hours_study, grades, color="red", linewidth=1)
#
# plt.xlabel("Время учения")
# plt.ylabel("Баллы")
#
# plt.legend()
# plt.show()

# 3 Разные цвета
# hours_study = np.array([0, 1, 1, 2, 4])
# grades = np.array([55, 60, 63, 66, 70])
# colors = ["red", "blue", "green", "#FF8C00", "purple"]
#
# plt.scatter(hours_study, grades,
#             label="Study",
#             c=colors,
#             s=67) # 4 Увеличить размер точек
#
# plt.xlabel("Время учения")
# plt.ylabel("Баллы")
#
# plt.legend()
# plt.show()

# КРУГОВАЯ ДИАГРАММА
# 1 Создать круговую диаграмму
# categories = np.array(["Juniors", "Middles", "Seniors", "Teamleads"])
# counts = np.array([20, 13, 3, 1])
# plt.pie(counts,
#         labels=categories,
#         explode=[0, 0, 0, 0.2],  # 3 смещение клинаб
#         wedgeprops={ # установка границ для клиньев
#             "edgecolor": "black",
#             "linewidth": 0.5,
#             "linestyle": "-"
#         })
# plt.show()

# ВОПРОСЫ ПРО ГРАФИКИ
# x = np.linspace(1, 50, 50)
# y = np.random.randint(0, 20, 50)
#
# plt.figure(
#     facecolor="gray", # 5) Цвет всей фигуры
#     figsize=(8, 6)) # 10) Изменить размер фигруы при
# # создании либо для существующей
# # fig = plt.gcf()
# # fig.set_size_inches(12, 4)
# plt.plot(x, y,
#          alpha=0.4, # 1) настройка прозрачности
#          color=np.random.rand(3)) # 2) настройка цвета 6) случайный цвет
# plt.title("Заголовок",fontsize=16) # 3) Настройка шрифта заголовка
#
# plt.xlabel("Ось X", fontsize=14) # 4) Настройка шрифта для оси
# plt.ylabel("Ось Y", fontsize=14)
# plt.tick_params(axis="both", labelsize=12) # 4.1/12) Настройка шрифта меток
#
# plt.text(0, 10, "текст внутри", fontsize=12) # 7) Текст внутри графика
# plt.figtext(0.2, 0.01, "подпись внизу фигуры") # 8) текст внутри фигуры
#
# plt.show()

# 9 Изменить размер цветовой панели
# data = np.random.rand(10, 10)
# figure, axe = plt.subplots()
# image = axe.imshow(data)
#
# plt.colorbar(image, ax=axe,
#              shrink=0.7, # длина относительно axe
#              aspect=20 # чем больше значение тем уже
#              )
# plt.show()

# 11) Добавление легенды с цветной рамкой
# figure, axe = plt.subplots()
# data = np.linspace(0, 20, 20)
# axe.plot(data, label="Линия")
#
# leg = axe.legend()
# leg.get_frame().set_facecolor("gray")
# leg.get_frame().set_edgecolor("red")
#
# plt.show()

# 13) Скрыть метки
# figure, axe = plt.subplots()
#
# x = np.linspace(1, 50, 50)
# y = np.random.randint(0, 20, 50)
#
# axe.plot(x, y)
#
# # Убирает цифры с меток
# axe.tick_params(axis="x", labelbottom=False)
# axe.tick_params(axis="y", labelleft=False)
#
# # Убирает тики и цифрф
# axe.set_xticks([])
# axe.set_yticks([])
#
# plt.show()

# 14) Настроить положение меток осей
# figure, axe = plt.subplots()
#
# x = np.linspace(1, 50, 50)
# y = np.random.randint(0, 20, 50)
#
# axe.plot(x, y)
#
# axe.set_xlabel("Метка X", loc="right")
# axe.set_ylabel("Метка Y", loc="top")
#
# plt.show()

# 15) Скрыть ось, границы и пробелы
figure, axe = plt.subplots()

x = np.linspace(1, 50, 50)
y = np.random.randint(0, 20, 50)

axe.plot(x, y)

# Скрыть ось целиком
axe.set_axis_off()

# Убрать пробелы внутри фигуры
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Убрать поля при сохранении
#figure.savefig("no_padding.png", bbox_inches="tight", pad_inches=0)

plt.show()
