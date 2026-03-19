let questionCount = parseInt(document.getElementById('question_count').value) || 0;

function renumber() {
    const boxes = document.querySelectorAll('.question-box');
    questionCount = boxes.length;
    document.getElementById('question_count').value = questionCount;

    boxes.forEach((box, qi) => {
        const qNum = qi + 1;
        box.id = `question-${qNum}`;
        box.querySelector('h3').textContent = `Question ${qNum}`;
        box.querySelector('.question-prompt').name = `question_${qNum}_prompt`;
        box.querySelector('.option-count').name = `question_${qNum}_option_count`;

        const options = box.querySelectorAll('.options-container > div');
        box.querySelector('.option-count').value = options.length;

        options.forEach((opt, oi) => {
            const oNum = oi + 1;
            opt.querySelector('input[type="text"]').name = `question_${qNum}_option_${oNum}`;
            const radio = opt.querySelector('input[type="radio"]');
            radio.name = `question_${qNum}_correct`;
            radio.value = oNum;
        });
    });
}

function addQuestion() {
    const container = document.getElementById('questions-container');
    const div = document.createElement('div');
    div.className = 'question-box';
    div.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0;"></h3>
            <button type="button" onclick="removeQuestion(this)" style="color:red;">✕ Remove</button>
        </div>
        <label>Question Text:</label>
        <textarea class="question-prompt" name="prompt_placeholder" rows="2" placeholder="Enter question..."></textarea>
        <div class="options-container"></div>
        <input type="hidden" name="option_count_placeholder" value="0" class="option-count" />
        <button type="button" onclick="addOption(this)" style="margin-top:8px;">+ Add Option</button>
    `;
    container.appendChild(div);
    renumber();
    addOption(div.querySelector('button[onclick="addOption(this)"]'));
    addOption(div.querySelector('button[onclick="addOption(this)"]'));
}

function removeQuestion(btn) {
    btn.closest('.question-box').remove();
    renumber();
}

function addOption(btn) {
    const box = btn.closest('.question-box');
    const optionsContainer = box.querySelector('.options-container');
    const div = document.createElement('div');
    div.style = 'display:flex; align-items:center; gap:10px; margin-top:6px;';
    div.innerHTML = `
        <input type="text" name="placeholder" placeholder="Option text" style="flex:1;" />
        <label style="white-space:nowrap;">
            <input type="radio" name="placeholder_correct" value="0" /> Correct
        </label>
        <button type="button" onclick="removeOption(this)" style="color:red;">✕</button>
    `;
    optionsContainer.appendChild(div);
    renumber();
}

function removeOption(btn) {
    btn.closest('div').remove();
    renumber();
}