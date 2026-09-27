const demoContent = document.querySelector(".demo-content")
let headerSpans = document.querySelectorAll(".demo-header span")


console.log(demoContent);

const scenes = [
    {
        type:'ai',
        question:'What is generator function in python?',
        response:`A generator function uses the <code>yield</code> keyword to produce values one at a time. It pauses after each value, making it memory-efficient for large data.`,
        leftTitle:'✦ Hirevance AI',
        rightTitle:'● Online'
    },

    {
        type:'test',
        title:'Java-Basics',
        questionNumber:1,
        question:'Which keyword is used to prevent a class from being inherited?',
        options:[
           {label:'A',text:'static'},
           {label:'B',text:'private'},
           {label:'C',text:'final'},
           {label:'D',text:'constant'}
        ],
        leftTitle:'MockTest',
        timer:'02:59'
    },

    {
        type:'progress',
        python:85,
        java:92,
        sql:90,
        tests:12,
    }
]

let currentScene = 0


function renderScene(sceneIndex)

{
    const scene = scenes[sceneIndex]

    switch (scene.type) {
        case 'ai':
                demoContent.innerHTML = `
            <div class="demo-scene active">
                        <div class="demo-question">
                        ${scene.question}
                        </div>
                    <div class="demo-response">
                        ${scene.response}
                    </div>
                    </div>
    
            `
            headerSpans[0].innerText = scene.leftTitle
            headerSpans[1].innerText = scene.rightTitle
            break;
        case 'test':
            demoContent.innerHTML = `
    <div class="demo-scene active test-scene">

        <div class="test-title">
            ${scene.title}
        </div>

        <div class="test-question-number">
            Question ${scene.questionNumber} of 10
        </div>

        <div class="test-question">
            ${scene.question}
        </div>

        <div class="test-options">
            <p>${scene.options[0].label}. ${scene.options[0].text}</p>
            <p>${scene.options[1].label}. ${scene.options[1].text}</p>
            <p>${scene.options[2].label}. ${scene.options[2].text}</p>
            <p>${scene.options[3].label}. ${scene.options[3].text}</p>
        </div>

    </div>`

            headerSpans[0].innerText = scene.leftTitle
            headerSpans[1].innerText = scene.timer
            break

        case 'progress':
            case 'progress':

    demoContent.innerHTML = `
        <div class="demo-scene active progress-scene">

            <div class="progress-title">
                Your Progress
            </div>

            <div class="progress-item">
                <div class="progress-label">
                    <span>Python</span>
                    <span>${scene.python}%</span>
                </div>

                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${scene.python}%"></div>
                </div>
            </div>

            <div class="progress-item">
                <div class="progress-label">
                    <span>Java</span>
                    <span>${scene.java}%</span>
                </div>

                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${scene.java}%"></div>
                </div>
            </div>

            <div class="progress-item">
                <div class="progress-label">
                    <span>SQL</span>
                    <span>${scene.sql}%</span>
                </div>

                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${scene.sql}%"></div>
                </div>
            </div>

            <div class="tests-completed">
                Tests completed: ${scene.tests}
            </div>

        </div>
    `;

    headerSpans[0].innerText = '✦ Hirevance';
    headerSpans[1].innerText = '';

    break;
    }


}

renderScene(currentScene)

setInterval(()=>{
    currentScene++;

if (currentScene >= scenes.length) {
    currentScene = 0;
}

renderScene(currentScene);


},4000)


function toggledPassword(inputID,button) {
    const input =  document.getElementById(inputID)
    const eye = button.querySelector('.eye-icon')
    const eye_off = button.querySelector('.eye-off-icon')

    if (input.type === 'password'){
        input.type = 'text'
        eye.style.display = 'none';
        eye_off.style.display = 'block';
    }
    else{
        input.type = 'password';
        eye.style.display = 'block';
        eye_off.style.display = 'none';
    }
    
}
