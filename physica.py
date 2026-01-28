topics = {
    "mechanics": {
        "title": "Механика",
        "theory": """
        <p>Механика — раздел физики, изучающий движение тел.</p>
        <p>Она описывает, как изменяется положение тел во времени и почему это происходит.</p>
        """,
        "formulas": [
            {
                "id": "speed",
                "name": "Скорость",
                "latex": "v = \\frac{s}{t}",
                "python": "s / t",
                "vars": ["s", "t"],
                "result_name": "v",
                "description": "Скорость — путь, делённый на время"
            },
            {
                "id": "acceleration",
                "name": "Ускорение",
                "latex": "a = \\frac{v - v_0}{t}",
                "python": "(v - v0) / t",
                "vars": ["v", "v0", "t"],
                "result_name": "a",
                "description": "Ускорение — изменение скорости за время"
            }
        ],
        "examples": [
            {
                "name": "Расчёт скорости",
                "desc": "Автомобиль проезжает 100 метров за 20 секунд. Найти скорость.",
                "solution": "v = \\frac{100}{20} = 5 \\text{ м/с}"
            },
            {
                "name": "Расчёт ускорения",
                "desc": "Скорость изменилась с 5 до 15 м/с за 4 секунды.",
                "solution": "a = \\frac{15 - 5}{4} = 2.5 \\text{ м/с}^2"
            }
        ]
    },

    "optics": {
        "title": "Оптика",
        "theory": "<p>Оптика изучает свет и его свойства.</p>",
        "formulas": [
            {
                "id": "refraction",
                "name": "Закон преломления",
                "latex": "n = \\frac{c}{v}",
                "python": "c / v",
                "vars": ["c", "v"],
                "result_name": "n",
                "description": "Показатель преломления"
            }
        ],
        "examples": [
            {
                "name": "Преломление света",
                "desc": "Скорость света в среде 2·10⁸ м/с.",
                "solution": "n = \\frac{3·10^8}{2·10^8} = 1.5"
            }
        ]
    },

    "electricity": {
        "title": "Электричество",
        "theory": "<p>Раздел физики, изучающий электрические явления.</p>",
        "formulas": [
            {
                "id": "ohm",
                "name": "Закон Ома",
                "latex": "I = \\frac{U}{R}",
                "python": "U / R",
                "vars": ["U", "R"],
                "result_name": "I",
                "description": "Сила тока"
            }
        ],
        "examples": [
            {
                "name": "Закон Ома",
                "desc": "Напряжение 12 В, сопротивление 6 Ом.",
                "solution": "I = \\frac{12}{6} = 2 \\text{ А}"
            }
        ]
    }
}
