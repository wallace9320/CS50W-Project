document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('all').onclick = () => load_quiz('all');
    document.getElementById('made').onclick = () => load_quiz('created');
    document.getElementById('answered').onclick = () => load_quiz('answered');

    document.getElementById('search-by-username').onclick = () => search_quiz('username');
    document.getElementById('search-by-title').onclick = () => search_quiz('title');

    document.getElementById('input-by-username').onkeyup = () => enable('username');
    document.getElementById('input-by-title').onkeyup = () => enable('title');

    load_quiz('all');

});


function load_quiz(type) {
    document.getElementById('list-of-quizzes').innerHTML = "";
    const quiz_heading = document.getElementById('quiz-heading');
    if (type === 'all') quiz_heading.innerHTML = "All Quizzes";
    else if (type === 'created') quiz_heading.innerHTML = "Quizzes Created by You";
    else if (type === 'answered') quiz_heading.innerHTML = "Quizzes Completed by You";
    fetch(`/display/${type}`)
    .then(response => response.json())
    .then(quizzes => {
        quizzes.forEach(add_quiz);
    })
}


function search_quiz(type) {
    document.getElementById("search-by-username").disabled = true;
    document.getElementById("search-by-title").disabled = true;

    document.getElementById('list-of-quizzes').innerHTML = "";
    const quiz_heading = document.getElementById('quiz-heading');
    let keyword = "";
    if (type === 'username') {
        const username = document.getElementById('input-by-username').value;
        quiz_heading.innerHTML = `Search Results by Username: ${username}`;
        keyword = username;
    }
    else if (type === 'title') {
        const title = document.getElementById('input-by-title').value;
        quiz_heading.innerHTML = `Search Results by Title: ${title}`;
        keyword = title;
    }
    document.getElementById('input-by-username').value = "";
    document.getElementById('input-by-title').value = "";
    fetch(`/search/${type}/${keyword}`)
    .then(response => response.json())
    .then(quizzes => {
        quizzes.forEach(add_quiz)
    })
}


function add_quiz(content) {
    const quiz = document.createElement('div');
    quiz.className = "form-group one-box";

    const current_user = document.getElementById('current-user').innerHTML;

    const title = document.createElement('strong');
    title.innerHTML = content.title;
    const owner = document.createElement('p');
    owner.innerHTML = `By ${content.owner} at ${content.timestamp}`;

    quiz.appendChild(title);
    quiz.appendChild(owner);

    if (content.owner !== current_user) {
        const link_attempt_or_view = document.createElement('a');
        if (content.answered.includes(current_user)) {
            link_attempt_or_view.innerHTML = "View Your Results";
            link_attempt_or_view.href = `result/${content.id}`;
        }
        else {
            link_attempt_or_view.innerHTML = "Attempt Quiz";
            link_attempt_or_view.href = `attempt/${content.id}`;
        }
        link_attempt_or_view.style = "margin-right: 20px;";
        quiz.appendChild(link_attempt_or_view);
    }

    const link_view_others = document.createElement('a');
    link_view_others.innerHTML = "View Results by All Users";
    link_view_others.href = `otherresult/${content.id}`;
    quiz.appendChild(link_view_others);

    document.getElementById('list-of-quizzes').append(quiz);
}


function enable(type) {
    if (document.getElementById(`input-by-${type}`).value === "") { 
        document.getElementById(`search-by-${type}`).disabled = true; 
    } else { 
        document.getElementById(`search-by-${type}`).disabled = false;
    }
}