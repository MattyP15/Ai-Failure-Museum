// ─── QUIZ EDITOR ────────────────────────────────────────────────────────────

function renumber(quizNum) {
    const boxes = document.querySelectorAll(`#questions-container-${quizNum} .question-box`);
    const countInput = document.getElementById(`question_count_${quizNum}`);
    if (!countInput) return;
    countInput.value = boxes.length;

    boxes.forEach((box, qi) => {
        const qNum = qi + 1;
        box.id = `quiz${quizNum}-question-${qNum}`;
        box.querySelector('h3').textContent = `Question ${qNum}`;
        box.querySelector('.question-prompt').name = `quiz_${quizNum}_question_${qNum}_prompt`;
        box.querySelector('.option-count').name = `quiz_${quizNum}_question_${qNum}_option_count`;

        const options = box.querySelectorAll('.options-container > div');
        box.querySelector('.option-count').value = options.length;

        options.forEach((opt, oi) => {
            const oNum = oi + 1;
            opt.querySelector('input[type="text"]').name = `quiz_${quizNum}_question_${qNum}_option_${oNum}`;
            const radio = opt.querySelector('input[type="radio"]');
            radio.name = `quiz_${quizNum}_question_${qNum}_correct`;
            radio.value = oNum;
        });
    });
}

function addQuestion(quizNum) {
    const container = document.getElementById(`questions-container-${quizNum}`);
    const div = document.createElement('div');
    div.className = 'question-box';
    div.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0;"></h3>
            <button type="button" onclick="removeQuestion(this, ${quizNum})" style="color:red;">✕ Remove</button>
        </div>
        <label>Question Text:</label>
        <textarea class="question-prompt" name="placeholder" rows="2" placeholder="Enter question..."></textarea>
        <div class="options-container"></div>
        <input type="hidden" name="placeholder" value="0" class="option-count" />
        <button type="button" onclick="addOption(this, ${quizNum})" style="margin-top:8px;">+ Add Option</button>
    `;
    container.appendChild(div);
    renumber(quizNum);
    addOption(div.querySelector(`button[onclick="addOption(this, ${quizNum})"]`), quizNum);
    addOption(div.querySelector(`button[onclick="addOption(this, ${quizNum})"]`), quizNum);
}

function removeQuestion(btn, quizNum) {
    btn.closest('.question-box').remove();
    renumber(quizNum);
}

function addOption(btn, quizNum) {
    const box = btn.closest('.question-box');
    const optionsContainer = box.querySelector('.options-container');
    const div = document.createElement('div');
    div.style = 'display:flex; align-items:center; gap:10px; margin-top:6px;';
    div.innerHTML = `
        <input type="text" name="placeholder" placeholder="Option text" style="flex:1;" />
        <label style="white-space:nowrap;">
            <input type="radio" name="placeholder_correct" value="0" /> Correct
        </label>
        <button type="button" onclick="removeOption(this, ${quizNum})" style="color:red;">✕</button>
    `;
    optionsContainer.appendChild(div);
    renumber(quizNum);
}

function removeOption(btn, quizNum) {
    btn.closest('div').remove();
    renumber(quizNum);
}

// ─── TIMELINE EDITOR ────────────────────────────────────────────────────────

function renumberEvents() {
    const boxes = document.querySelectorAll('.event-box');
    const countInput = document.getElementById('event_count');
    if (!countInput) return;
    countInput.value = boxes.length;

    boxes.forEach((box, i) => {
        const num = i + 1;
        box.querySelector('h3').textContent = `Event ${num}`;
        box.querySelector('.event-year').name = `event_${num}_year`;
        box.querySelector('.event-description').name = `event_${num}_description`;
    });
}

function addEvent() {
    const container = document.getElementById('events-container');
    const div = document.createElement('div');
    div.className = 'event-box';
    div.style = 'background: white; padding: 12px; margin: 10px 0; border-left: 4px solid #ED8936;';
    div.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; color:#666;"></h3>
            <button type="button" onclick="removeEvent(this)" style="color:red; background:none; border:none; cursor:pointer; padding:0;">✕ Remove</button>
        </div>
        <label>Year / Label:</label>
        <input type="text" class="event-year" name="placeholder" placeholder="e.g. 2017" />
        <label>Description:</label>
        <textarea class="event-description" name="placeholder" rows="2" placeholder="Describe what happened..."></textarea>
    `;
    container.appendChild(div);
    renumberEvents();
}

function removeEvent(btn) {
    btn.closest('.event-box').remove();
    renumberEvents();
}