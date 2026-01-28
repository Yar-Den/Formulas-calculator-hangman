from flask import Flask, render_template, request, session
from physica import topics
from words import words

import random
import re


app = Flask(__name__)
app.secret_key = 'secret-key'

@app.route('/')
def index():
    return render_template('index.html', topics=topics)


@app.route('/topic/<topic_id>')
def topic(topic_id):
    topic = topics.get(topic_id)
    if not topic:
        return "Тема не найдена", 404
    return render_template('topic.html', topic=topic)


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    active_tab = request.args.get('tab', 'arithmetic')

    arithmetic_expr = None
    arithmetic_result = None
    arithmetic_error = None

    selected_topic_key = None
    selected_topic = None
    selected_formula = None
    formula_result = None
    formula_error = None

    if request.method == 'POST':
        active_tab = request.form.get('tab', active_tab)

        if active_tab == 'arithmetic':
            arithmetic_expr = request.form.get('expression', '')

            try:
                arithmetic_result = eval(arithmetic_expr)
            except Exception:
                arithmetic_error = "Ошибка вычисления"

        elif active_tab == 'physics':
            selected_topic_key = request.form.get('topic_id')
    
            if selected_topic_key in topics:
                selected_topic = topics[selected_topic_key]
    
            formula_id = request.form.get('formula_id')
    
            if selected_topic and formula_id:
                for f in selected_topic['formulas']:
                    if f['id'] == formula_id:
                        selected_formula = f
                        break
    
            if selected_formula and request.form.get('calculate'):
                try:
                    values = {}
                    for var in selected_formula['vars']:
                        values[var] = float(request.form.get(var))
    
                    formula_result = eval(
                        selected_formula['python'],
                        {},
                        values
                    )
                except Exception:
                    formula_error = "Ошибка расчёта формулы"
    return render_template(
        'calculator.html',
        active_tab=active_tab,

        arithmetic_expr=arithmetic_expr,
        arithmetic_result=arithmetic_result,
        arithmetic_error=arithmetic_error,

        topics=topics,
        selected_topic_key=selected_topic_key,
        selected_topic=selected_topic,
        selected_formula=selected_formula,
        formula_result=formula_result,
        formula_error=formula_error
    )


@app.route('/hangman', methods=['GET', 'POST'])
def hangman():
    if 'word' not in session:
        session['word'] = random.choice(words)
        session['guessed'] = []
        session['errors'] = 0
        session['xp'] = session.get('xp', 0)
        session['hint_used'] = False

    word = session['word']
    guessed = session['guessed']
    errors = session['errors']
    xp = session['xp']

    message = None
    error_message = None

    if request.method == 'POST':
        letter = request.form.get('letter', '').lower().strip()

        # Проверка на корректность ввода
        if not re.fullmatch(r'[а-яё]', letter):
            error_message = "Введите одну букву русского алфавита"
        elif letter in guessed:
            error_message = "Вы уже угадали эту букву"
        else:
            guessed.append(letter)

            if letter not in word:
                errors += 1
            else:
                xp += 5

    # Подсказка
    if request.args.get('hint') == '1':
        if session.get('hint_used'):
            error_message = "Подсказка уже использована"
        elif xp < 10:
            error_message = "Недостаточно опыта для подсказки"
        else:
            hidden_letters = [letter for letter in set(word) if letter not in guessed]
            hint_letter = random.choice(hidden_letters)
            guessed.append(hint_letter)
            xp -= 10
            session['hint_used'] = True
            error_message = f"Подсказка: открыта буква «{hint_letter.upper()}»"

    # Победа
    if all(letter in guessed for letter in word):
        message = "🤘😎🤘Вы выиграли!), вам добавилось 20 опыта"
        xp += 20
        session.clear()
        session['xp'] = xp

    # Проигрыш
    if errors >= 6:
        message = f"😥Вы проиграли(. Загаданное слово: {word}, у вас отнялось 10 опыта"
        session.clear()
        if xp >= 10:
            xp -= 10
        else:
            xp = 0
        session['xp'] = xp
    
    session['guessed'] = guessed
    session['errors'] = errors
    session['xp'] = xp

    display_word = [letter if letter in guessed else '•' for letter in word]
    word_display = ' '.join(display_word)
    
    return render_template(
        'hangman.html',
        word_display=word_display,
        errors=errors,
        guessed=guessed,
        message=message,
        error_message=error_message,
        xp=xp
    )

