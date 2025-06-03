document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('quiz-form');
    const results = document.getElementById('results');

    const correctAnswers = {
        q1: 'c',
        q2: 'b',
        q3: 'b'
    };

    const explanations = {
        q1: 'Pythonban egyszerű értékadással hozunk létre változót, például x = 5.',
        q2: 'A for ciklus sorozatokat jár be elemről elemre.',
        q3: 'Függvényt a def kulcsszó segítségével definiálunk.'
    };

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        results.innerHTML = '';
        let score = 0;
        let total = Object.keys(correctAnswers).length;

        for (let key in correctAnswers) {
            const question = document.getElementById(key);
            const selected = form.elements[key].value;
            if (selected === correctAnswers[key]) {
                score++;
            } else {
                const wrongDiv = document.createElement('div');
                wrongDiv.className = 'wrong';
                wrongDiv.textContent = `A(z) ${key} válasz helytelen. Helyes válasz: ${correctAnswers[key].toUpperCase()}. ${explanations[key]}`;
                results.appendChild(wrongDiv);
            }
        }

        const scoreDiv = document.createElement('div');
        scoreDiv.textContent = `Eredmény: ${score} / ${total}`;
        results.appendChild(scoreDiv);
    });
});
