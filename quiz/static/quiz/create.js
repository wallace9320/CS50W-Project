let count = 3;

document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('add-question').onclick = () => add_question();
    document.getElementById('remove-question').onclick = () => remove_question();

});


function add_question() {

    count++;
    document.getElementById('no-of-questions').value = count;

    if (count >= 4) document.getElementById('remove-question').className = "btn btn-info btn-create"
    if (count >= 5) document.getElementById('add-question').className = "btn btn-info btn-create hidden"

    const new_question = document.createElement('div');
    new_question.className = "form-group one-box";
    new_question.id = count;

    const label = document.createElement('span');
    label.innerHTML = `Question ${count}:`;

    const question = document.createElement('input');
    question.className = "form-group form-control";
    question.name = `${count}-question`;
    question.placeholder = "Question";

    const option1 = document.createElement('input');
    option1.className = "form-group form-control";
    option1.name = `${count}-option-1`;
    option1.placeholder = "Option 1";
    const option2 = document.createElement('input');
    option2.className = "form-group form-control";
    option2.name = `${count}-option-2`;
    option2.placeholder = "Option 2";
    const option3 = document.createElement('input');
    option3.className = "form-group form-control";
    option3.name = `${count}-option-3`;
    option3.placeholder = "Option 3";
    const option4 = document.createElement('input');
    option4.className = "form-group form-control";
    option4.name = `${count}-option-4`;
    option4.placeholder = "Option 4";

    const dropdownlabel = document.createElement('span');
    dropdownlabel.innerHTML = "Correct Answer: ";

    const dropdown = document.createElement('select');
    dropdown.name = `${count}-select`;

    const dropdown1 = document.createElement('option');
    dropdown1.value = "1";
    dropdown1.innerHTML = "Option 1";
    const dropdown2 = document.createElement('option');
    dropdown2.value = "2";
    dropdown2.innerHTML = "Option 2";
    const dropdown3 = document.createElement('option');
    dropdown3.value = "3";
    dropdown3.innerHTML = "Option 3";
    const dropdown4 = document.createElement('option');
    dropdown4.value = "4";
    dropdown4.innerHTML = "Option 4";

    dropdown.appendChild(dropdown1);
    dropdown.appendChild(dropdown2);
    dropdown.appendChild(dropdown3);
    dropdown.appendChild(dropdown4);

    new_question.appendChild(label);
    new_question.appendChild(question);
    new_question.appendChild(option1);
    new_question.appendChild(option2);
    new_question.appendChild(option3);
    new_question.appendChild(option4);
    new_question.appendChild(dropdownlabel);
    new_question.appendChild(dropdown);

    document.querySelector('.questions').append(new_question);

}


function remove_question() {

    document.getElementById(count).remove();

    count--;
    document.getElementById('no-of-questions').value = count;

    if (count <= 3) document.getElementById('remove-question').className = "btn btn-info btn-create hidden";
    if (count <= 4) document.getElementById('add-question').className = "btn btn-info btn-create";

}